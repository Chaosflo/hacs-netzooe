"""Platform for sensor integration."""
from __future__ import annotations
from datetime import timedelta
import voluptuous as vol

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
import homeassistant.helpers.config_validation as cv
from homeassistant.const import UnitOfEnergy, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.util import Throttle

import requests
from .dashboard_response import welcome9_from_dict

MIN_TIME_BETWEEN_HOURLY_UPDATES = timedelta(hours=1)

# Configuration of netzooe
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_USERNAME): cv.string,
        vol.Optional(CONF_PASSWORD): cv.string,
    }
)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    add_entities([TotalEnergySensor(config[CONF_USERNAME], config[CONF_PASSWORD])])


class TotalEnergySensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Total energy sensor"
    _attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password

    @Throttle(MIN_TIME_BETWEEN_HOURLY_UPDATES)
    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        s = requests.session()

        # login into netzooe
        loginData = {"j_username": self._username, "j_password": self._password}

        loginResponse = s.post(
            "https://eservice.netzooe.at/service/j_security_check",
            json=loginData,
            headers={
                "Client-Id": "netzonline",
            },
        )

        sessionResponse = s.get("https://eservice.netzooe.at/service/v1.0/session")

        # Fetch dashboards
        dashboardResponse = s.get(
            "https://eservice.netzooe.at/service/v1.0/contract-accounts/1000214124/200100954422"
        )

        dashboard = welcome9_from_dict(dashboardResponse.json())

        self._attr_native_value = (
            dashboard.contracts[0]
            .point_of_delivery.last_readings.values[0]
            .new_result.reading_value
        )

        s.get("https://eservice.netzooe.at/service/logout")
