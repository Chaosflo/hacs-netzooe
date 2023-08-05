from typing import Any, Optional, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Address:
    street: str
    housenumber: int
    postcode: int
    city: str
    country: str

    def __init__(
        self, street: str, housenumber: int, postcode: int, city: str, country: str
    ) -> None:
        self.street = street
        self.housenumber = housenumber
        self.postcode = postcode
        self.city = city
        self.country = country

    @staticmethod
    def from_dict(obj: Any) -> "Address":
        assert isinstance(obj, dict)
        street = from_str(obj.get("street"))
        housenumber = int(from_str(obj.get("housenumber")))
        postcode = int(from_str(obj.get("postcode")))
        city = from_str(obj.get("city"))
        country = from_str(obj.get("country"))
        return Address(street, housenumber, postcode, city, country)

    def to_dict(self) -> dict:
        result: dict = {}
        result["street"] = from_str(self.street)
        result["housenumber"] = from_str(str(self.housenumber))
        result["postcode"] = from_str(str(self.postcode))
        result["city"] = from_str(self.city)
        result["country"] = from_str(self.country)
        return result


class BankAccountIn:
    pass

    def __init__(
        self,
    ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> "BankAccountIn":
        assert isinstance(obj, dict)
        return BankAccountIn()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class Consumptions:
    total_consumption: int

    def __init__(self, total_consumption: int) -> None:
        self.total_consumption = total_consumption

    @staticmethod
    def from_dict(obj: Any) -> "Consumptions":
        assert isinstance(obj, dict)
        total_consumption = from_int(obj.get("totalConsumption"))
        return Consumptions(total_consumption)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalConsumption"] = from_int(self.total_consumption)
        return result


class EditableReadings:
    new_reading_possible: bool

    def __init__(self, new_reading_possible: bool) -> None:
        self.new_reading_possible = new_reading_possible

    @staticmethod
    def from_dict(obj: Any) -> "EditableReadings":
        assert isinstance(obj, dict)
        new_reading_possible = from_bool(obj.get("newReadingPossible"))
        return EditableReadings(new_reading_possible)

    def to_dict(self) -> dict:
        result: dict = {}
        result["newReadingPossible"] = from_bool(self.new_reading_possible)
        return result


class AvailableTimeRange:
    available_time_range_from: datetime
    to: datetime

    def __init__(self, available_time_range_from: datetime, to: datetime) -> None:
        self.available_time_range_from = available_time_range_from
        self.to = to

    @staticmethod
    def from_dict(obj: Any) -> "AvailableTimeRange":
        assert isinstance(obj, dict)
        available_time_range_from = from_datetime(obj.get("from"))
        to = from_datetime(obj.get("to"))
        return AvailableTimeRange(available_time_range_from, to)

    def to_dict(self) -> dict:
        result: dict = {}
        result["from"] = self.available_time_range_from.isoformat()
        result["to"] = self.to.isoformat()
        return result


class Result:
    timestamp: Optional[datetime]
    integer_places: int
    decimal_places: float
    plausible: bool
    reading_value: float

    def __init__(
        self,
        timestamp: Optional[datetime],
        integer_places: int,
        decimal_places: float,
        plausible: bool,
        reading_value: float,
    ) -> None:
        self.timestamp = timestamp
        self.integer_places = integer_places
        self.decimal_places = decimal_places
        self.plausible = plausible
        self.reading_value = reading_value

    @staticmethod
    def from_dict(obj: Any) -> "Result":
        assert isinstance(obj, dict)
        timestamp = from_union([from_datetime, from_none], obj.get("timestamp"))
        integer_places = from_int(obj.get("integerPlaces"))
        decimal_places = from_float(obj.get("decimalPlaces"))
        plausible = from_bool(obj.get("plausible"))
        reading_value = from_float(obj.get("readingValue"))
        return Result(
            timestamp, integer_places, decimal_places, plausible, reading_value
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["timestamp"] = from_union(
            [lambda x: x.isoformat(), from_none], self.timestamp
        )
        result["integerPlaces"] = from_int(self.integer_places)
        result["decimalPlaces"] = to_float(self.decimal_places)
        result["plausible"] = from_bool(self.plausible)
        result["readingValue"] = to_float(self.reading_value)
        return result


class Value:
    meternumber: int
    equipmentnumber: str
    registernumber: str
    integer_places: int
    decimal_places: int
    reference_number: str
    caloric_value: float
    additional_value: float
    old_result: Result
    new_result: Result
    calculated_consumption: float
    unit_for_calculated_consumption: str
    relevant_consumption: float

    def __init__(
        self,
        meternumber: int,
        equipmentnumber: str,
        registernumber: str,
        integer_places: int,
        decimal_places: int,
        reference_number: str,
        caloric_value: float,
        additional_value: float,
        old_result: Result,
        new_result: Result,
        calculated_consumption: float,
        unit_for_calculated_consumption: str,
        relevant_consumption: float,
    ) -> None:
        self.meternumber = meternumber
        self.equipmentnumber = equipmentnumber
        self.registernumber = registernumber
        self.integer_places = integer_places
        self.decimal_places = decimal_places
        self.reference_number = reference_number
        self.caloric_value = caloric_value
        self.additional_value = additional_value
        self.old_result = old_result
        self.new_result = new_result
        self.calculated_consumption = calculated_consumption
        self.unit_for_calculated_consumption = unit_for_calculated_consumption
        self.relevant_consumption = relevant_consumption

    @staticmethod
    def from_dict(obj: Any) -> "Value":
        assert isinstance(obj, dict)
        meternumber = int(from_str(obj.get("meternumber")))
        equipmentnumber = from_str(obj.get("equipmentnumber"))
        registernumber = from_str(obj.get("registernumber"))
        integer_places = from_int(obj.get("integerPlaces"))
        decimal_places = from_int(obj.get("decimalPlaces"))
        reference_number = from_str(obj.get("referenceNumber"))
        caloric_value = from_float(obj.get("caloricValue"))
        additional_value = from_float(obj.get("additionalValue"))
        old_result = Result.from_dict(obj.get("oldResult"))
        new_result = Result.from_dict(obj.get("newResult"))
        calculated_consumption = from_float(obj.get("calculatedConsumption"))
        unit_for_calculated_consumption = from_str(
            obj.get("unitForCalculatedConsumption")
        )
        relevant_consumption = from_float(obj.get("relevantConsumption"))
        return Value(
            meternumber,
            equipmentnumber,
            registernumber,
            integer_places,
            decimal_places,
            reference_number,
            caloric_value,
            additional_value,
            old_result,
            new_result,
            calculated_consumption,
            unit_for_calculated_consumption,
            relevant_consumption,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["meternumber"] = from_str(str(self.meternumber))
        result["equipmentnumber"] = from_str(self.equipmentnumber)
        result["registernumber"] = from_str(self.registernumber)
        result["integerPlaces"] = from_int(self.integer_places)
        result["decimalPlaces"] = from_int(self.decimal_places)
        result["referenceNumber"] = from_str(self.reference_number)
        result["caloricValue"] = to_float(self.caloric_value)
        result["additionalValue"] = to_float(self.additional_value)
        result["oldResult"] = to_class(Result, self.old_result)
        result["newResult"] = to_class(Result, self.new_result)
        result["calculatedConsumption"] = to_float(self.calculated_consumption)
        result["unitForCalculatedConsumption"] = from_str(
            self.unit_for_calculated_consumption
        )
        result["relevantConsumption"] = to_float(self.relevant_consumption)
        return result


class LastReadings:
    values: List[Value]
    new_reading_possible: bool

    def __init__(self, values: List[Value], new_reading_possible: bool) -> None:
        self.values = values
        self.new_reading_possible = new_reading_possible

    @staticmethod
    def from_dict(obj: Any) -> "LastReadings":
        assert isinstance(obj, dict)
        values = from_list(Value.from_dict, obj.get("values"))
        new_reading_possible = from_bool(obj.get("newReadingPossible"))
        return LastReadings(values, new_reading_possible)

    def to_dict(self) -> dict:
        result: dict = {}
        result["values"] = from_list(lambda x: to_class(Value, x), self.values)
        result["newReadingPossible"] = from_bool(self.new_reading_possible)
        return result


class Meter:
    meter_number: int

    def __init__(self, meter_number: int) -> None:
        self.meter_number = meter_number

    @staticmethod
    def from_dict(obj: Any) -> "Meter":
        assert isinstance(obj, dict)
        meter_number = int(from_str(obj.get("meterNumber")))
        return Meter(meter_number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["meterNumber"] = from_str(str(self.meter_number))
        return result


class Consumption:
    sum: float
    per_day: float
    days: int

    def __init__(self, sum: float, per_day: float, days: int) -> None:
        self.sum = sum
        self.per_day = per_day
        self.days = days

    @staticmethod
    def from_dict(obj: Any) -> "Consumption":
        assert isinstance(obj, dict)
        sum = from_float(obj.get("sum"))
        per_day = from_float(obj.get("perDay"))
        days = from_int(obj.get("days"))
        return Consumption(sum, per_day, days)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sum"] = to_float(self.sum)
        result["perDay"] = to_float(self.per_day)
        result["days"] = from_int(self.days)
        return result


class LyTrend:
    consumption_old: Consumption
    consumption_new: Consumption
    timerange_old: AvailableTimeRange
    timerange_new: AvailableTimeRange

    def __init__(
        self,
        consumption_old: Consumption,
        consumption_new: Consumption,
        timerange_old: AvailableTimeRange,
        timerange_new: AvailableTimeRange,
    ) -> None:
        self.consumption_old = consumption_old
        self.consumption_new = consumption_new
        self.timerange_old = timerange_old
        self.timerange_new = timerange_new

    @staticmethod
    def from_dict(obj: Any) -> "LyTrend":
        assert isinstance(obj, dict)
        consumption_old = Consumption.from_dict(obj.get("consumptionOld"))
        consumption_new = Consumption.from_dict(obj.get("consumptionNew"))
        timerange_old = AvailableTimeRange.from_dict(obj.get("timerangeOld"))
        timerange_new = AvailableTimeRange.from_dict(obj.get("timerangeNew"))
        return LyTrend(consumption_old, consumption_new, timerange_old, timerange_new)

    def to_dict(self) -> dict:
        result: dict = {}
        result["consumptionOld"] = to_class(Consumption, self.consumption_old)
        result["consumptionNew"] = to_class(Consumption, self.consumption_new)
        result["timerangeOld"] = to_class(AvailableTimeRange, self.timerange_old)
        result["timerangeNew"] = to_class(AvailableTimeRange, self.timerange_new)
        return result


class Profile:
    meter_point_administration_number: str
    profile_from: datetime
    to: datetime
    granularity: str
    profile_type: str
    smart_meter_type: str
    smart_meter: bool
    load_profile: bool
    reactive_current_profile: bool

    def __init__(
        self,
        meter_point_administration_number: str,
        profile_from: datetime,
        to: datetime,
        granularity: str,
        profile_type: str,
        smart_meter_type: str,
        smart_meter: bool,
        load_profile: bool,
        reactive_current_profile: bool,
    ) -> None:
        self.meter_point_administration_number = meter_point_administration_number
        self.profile_from = profile_from
        self.to = to
        self.granularity = granularity
        self.profile_type = profile_type
        self.smart_meter_type = smart_meter_type
        self.smart_meter = smart_meter
        self.load_profile = load_profile
        self.reactive_current_profile = reactive_current_profile

    @staticmethod
    def from_dict(obj: Any) -> "Profile":
        assert isinstance(obj, dict)
        meter_point_administration_number = from_str(
            obj.get("meterPointAdministrationNumber")
        )
        profile_from = from_datetime(obj.get("from"))
        to = from_datetime(obj.get("to"))
        granularity = from_str(obj.get("granularity"))
        profile_type = from_str(obj.get("profileType"))
        smart_meter_type = from_str(obj.get("smartMeterType"))
        smart_meter = from_bool(obj.get("smartMeter"))
        load_profile = from_bool(obj.get("loadProfile"))
        reactive_current_profile = from_bool(obj.get("reactiveCurrentProfile"))
        return Profile(
            meter_point_administration_number,
            profile_from,
            to,
            granularity,
            profile_type,
            smart_meter_type,
            smart_meter,
            load_profile,
            reactive_current_profile,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["meterPointAdministrationNumber"] = from_str(
            self.meter_point_administration_number
        )
        result["from"] = self.profile_from.isoformat()
        result["to"] = self.to.isoformat()
        result["granularity"] = from_str(self.granularity)
        result["profileType"] = from_str(self.profile_type)
        result["smartMeterType"] = from_str(self.smart_meter_type)
        result["smartMeter"] = from_bool(self.smart_meter)
        result["loadProfile"] = from_bool(self.load_profile)
        result["reactiveCurrentProfile"] = from_bool(self.reactive_current_profile)
        return result


class PointOfDelivery:
    meter_point_administration_number: str
    meter: Meter
    profiles: List[Profile]
    activation_status: str
    daily_dispatch_status: str
    monthly_dispatch_status: str
    retroactive_activation_date: datetime
    device_key_status: str
    monthly_trend: LyTrend
    yearly_trend: LyTrend
    last_readings: LastReadings
    available_profile_types: List[str]
    smart_meter_active: bool
    load_profile_active: bool
    available_time_range: AvailableTimeRange
    minimum_date: datetime
    maximum_date: datetime

    def __init__(
        self,
        meter_point_administration_number: str,
        meter: Meter,
        profiles: List[Profile],
        activation_status: str,
        daily_dispatch_status: str,
        monthly_dispatch_status: str,
        retroactive_activation_date: datetime,
        device_key_status: str,
        monthly_trend: LyTrend,
        yearly_trend: LyTrend,
        last_readings: LastReadings,
        available_profile_types: List[str],
        smart_meter_active: bool,
        load_profile_active: bool,
        available_time_range: AvailableTimeRange,
        minimum_date: datetime,
        maximum_date: datetime,
    ) -> None:
        self.meter_point_administration_number = meter_point_administration_number
        self.meter = meter
        self.profiles = profiles
        self.activation_status = activation_status
        self.daily_dispatch_status = daily_dispatch_status
        self.monthly_dispatch_status = monthly_dispatch_status
        self.retroactive_activation_date = retroactive_activation_date
        self.device_key_status = device_key_status
        self.monthly_trend = monthly_trend
        self.yearly_trend = yearly_trend
        self.last_readings = last_readings
        self.available_profile_types = available_profile_types
        self.smart_meter_active = smart_meter_active
        self.load_profile_active = load_profile_active
        self.available_time_range = available_time_range
        self.minimum_date = minimum_date
        self.maximum_date = maximum_date

    @staticmethod
    def from_dict(obj: Any) -> "PointOfDelivery":
        assert isinstance(obj, dict)
        meter_point_administration_number = from_str(
            obj.get("meterPointAdministrationNumber")
        )
        meter = Meter.from_dict(obj.get("meter"))
        profiles = from_list(Profile.from_dict, obj.get("profiles"))
        activation_status = from_str(obj.get("activationStatus"))
        daily_dispatch_status = from_str(obj.get("dailyDispatchStatus"))
        monthly_dispatch_status = from_str(obj.get("monthlyDispatchStatus"))
        retroactive_activation_date = from_datetime(
            obj.get("retroactiveActivationDate")
        )
        device_key_status = from_str(obj.get("deviceKeyStatus"))
        monthly_trend = LyTrend.from_dict(obj.get("monthlyTrend"))
        yearly_trend = LyTrend.from_dict(obj.get("yearlyTrend"))
        last_readings = LastReadings.from_dict(obj.get("lastReadings"))
        available_profile_types = from_list(from_str, obj.get("availableProfileTypes"))
        smart_meter_active = from_bool(obj.get("smartMeterActive"))
        load_profile_active = from_bool(obj.get("loadProfileActive"))
        available_time_range = AvailableTimeRange.from_dict(
            obj.get("availableTimeRange")
        )
        minimum_date = from_datetime(obj.get("minimumDate"))
        maximum_date = from_datetime(obj.get("maximumDate"))
        return PointOfDelivery(
            meter_point_administration_number,
            meter,
            profiles,
            activation_status,
            daily_dispatch_status,
            monthly_dispatch_status,
            retroactive_activation_date,
            device_key_status,
            monthly_trend,
            yearly_trend,
            last_readings,
            available_profile_types,
            smart_meter_active,
            load_profile_active,
            available_time_range,
            minimum_date,
            maximum_date,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["meterPointAdministrationNumber"] = from_str(
            self.meter_point_administration_number
        )
        result["meter"] = to_class(Meter, self.meter)
        result["profiles"] = from_list(lambda x: to_class(Profile, x), self.profiles)
        result["activationStatus"] = from_str(self.activation_status)
        result["dailyDispatchStatus"] = from_str(self.daily_dispatch_status)
        result["monthlyDispatchStatus"] = from_str(self.monthly_dispatch_status)
        result[
            "retroactiveActivationDate"
        ] = self.retroactive_activation_date.isoformat()
        result["deviceKeyStatus"] = from_str(self.device_key_status)
        result["monthlyTrend"] = to_class(LyTrend, self.monthly_trend)
        result["yearlyTrend"] = to_class(LyTrend, self.yearly_trend)
        result["lastReadings"] = to_class(LastReadings, self.last_readings)
        result["availableProfileTypes"] = from_list(
            from_str, self.available_profile_types
        )
        result["smartMeterActive"] = from_bool(self.smart_meter_active)
        result["loadProfileActive"] = from_bool(self.load_profile_active)
        result["availableTimeRange"] = to_class(
            AvailableTimeRange, self.available_time_range
        )
        result["minimumDate"] = self.minimum_date.isoformat()
        result["maximumDate"] = self.maximum_date.isoformat()
        return result


class ReadingsHistory:
    calculated_consumption_sum: int
    relevant_consumption_sum: int
    relevant_consumption_unit: None
    max_consumption_per_day: int
    readings_per_meter: BankAccountIn

    def __init__(
        self,
        calculated_consumption_sum: int,
        relevant_consumption_sum: int,
        relevant_consumption_unit: None,
        max_consumption_per_day: int,
        readings_per_meter: BankAccountIn,
    ) -> None:
        self.calculated_consumption_sum = calculated_consumption_sum
        self.relevant_consumption_sum = relevant_consumption_sum
        self.relevant_consumption_unit = relevant_consumption_unit
        self.max_consumption_per_day = max_consumption_per_day
        self.readings_per_meter = readings_per_meter

    @staticmethod
    def from_dict(obj: Any) -> "ReadingsHistory":
        assert isinstance(obj, dict)
        calculated_consumption_sum = from_int(obj.get("calculatedConsumptionSum"))
        relevant_consumption_sum = from_int(obj.get("relevantConsumptionSum"))
        relevant_consumption_unit = from_none(obj.get("relevantConsumptionUnit"))
        max_consumption_per_day = from_int(obj.get("maxConsumptionPerDay"))
        readings_per_meter = BankAccountIn.from_dict(obj.get("readingsPerMeter"))
        return ReadingsHistory(
            calculated_consumption_sum,
            relevant_consumption_sum,
            relevant_consumption_unit,
            max_consumption_per_day,
            readings_per_meter,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["calculatedConsumptionSum"] = from_int(self.calculated_consumption_sum)
        result["relevantConsumptionSum"] = from_int(self.relevant_consumption_sum)
        result["relevantConsumptionUnit"] = from_none(self.relevant_consumption_unit)
        result["maxConsumptionPerDay"] = from_int(self.max_consumption_per_day)
        result["readingsPerMeter"] = to_class(BankAccountIn, self.readings_per_meter)
        return result


class Supplier:
    id: str
    name: str

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> "Supplier":
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        return Supplier(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        return result


class Contract:
    contract_number: str
    branch: str
    scale_type: str
    active: bool
    move_in_date: datetime
    move_out_date: datetime
    consumptions: Consumptions
    readings_history: ReadingsHistory
    editable_readings: EditableReadings
    point_of_delivery: PointOfDelivery
    smart_meter_type: str
    smart_meter_type_name: str
    smart_meter_type_help: str
    power_generation_unit: bool
    station: int
    sub_station: int
    supplier: Supplier
    synth_profile: str
    smart_meter_activation_possible: bool
    load_profile_activation_possible: bool
    daily_profile_dispatch_active: bool
    monthly_profile_dispatch_active: bool
    daily_profile_dispatch_inactive: bool
    monthly_profile_dispatch_inactive: bool
    amis_meter: bool
    amis_active: bool
    load_curve_active: bool
    profile_active: bool
    device_key_status: str
    available_profile_types: List[str]
    device_key_available: bool
    daily_profile_dispatch_status: str
    monthly_profile_dispatch_status: str
    reactive_current_profile_present: bool
    new_reading_possible: bool

    def __init__(
        self,
        contract_number: str,
        branch: str,
        scale_type: str,
        active: bool,
        move_in_date: datetime,
        move_out_date: datetime,
        consumptions: Consumptions,
        readings_history: ReadingsHistory,
        editable_readings: EditableReadings,
        point_of_delivery: PointOfDelivery,
        smart_meter_type: str,
        smart_meter_type_name: str,
        smart_meter_type_help: str,
        power_generation_unit: bool,
        station: int,
        sub_station: int,
        supplier: Supplier,
        synth_profile: str,
        smart_meter_activation_possible: bool,
        load_profile_activation_possible: bool,
        daily_profile_dispatch_active: bool,
        monthly_profile_dispatch_active: bool,
        daily_profile_dispatch_inactive: bool,
        monthly_profile_dispatch_inactive: bool,
        amis_meter: bool,
        amis_active: bool,
        load_curve_active: bool,
        profile_active: bool,
        device_key_status: str,
        available_profile_types: List[str],
        device_key_available: bool,
        daily_profile_dispatch_status: str,
        monthly_profile_dispatch_status: str,
        reactive_current_profile_present: bool,
        new_reading_possible: bool,
    ) -> None:
        self.contract_number = contract_number
        self.branch = branch
        self.scale_type = scale_type
        self.active = active
        self.move_in_date = move_in_date
        self.move_out_date = move_out_date
        self.consumptions = consumptions
        self.readings_history = readings_history
        self.editable_readings = editable_readings
        self.point_of_delivery = point_of_delivery
        self.smart_meter_type = smart_meter_type
        self.smart_meter_type_name = smart_meter_type_name
        self.smart_meter_type_help = smart_meter_type_help
        self.power_generation_unit = power_generation_unit
        self.station = station
        self.sub_station = sub_station
        self.supplier = supplier
        self.synth_profile = synth_profile
        self.smart_meter_activation_possible = smart_meter_activation_possible
        self.load_profile_activation_possible = load_profile_activation_possible
        self.daily_profile_dispatch_active = daily_profile_dispatch_active
        self.monthly_profile_dispatch_active = monthly_profile_dispatch_active
        self.daily_profile_dispatch_inactive = daily_profile_dispatch_inactive
        self.monthly_profile_dispatch_inactive = monthly_profile_dispatch_inactive
        self.amis_meter = amis_meter
        self.amis_active = amis_active
        self.load_curve_active = load_curve_active
        self.profile_active = profile_active
        self.device_key_status = device_key_status
        self.available_profile_types = available_profile_types
        self.device_key_available = device_key_available
        self.daily_profile_dispatch_status = daily_profile_dispatch_status
        self.monthly_profile_dispatch_status = monthly_profile_dispatch_status
        self.reactive_current_profile_present = reactive_current_profile_present
        self.new_reading_possible = new_reading_possible

    @staticmethod
    def from_dict(obj: Any) -> "Contract":
        assert isinstance(obj, dict)
        contract_number = from_str(obj.get("contractNumber"))
        branch = from_str(obj.get("branch"))
        scale_type = from_str(obj.get("scaleType"))
        active = from_bool(obj.get("active"))
        move_in_date = from_datetime(obj.get("moveInDate"))
        move_out_date = from_datetime(obj.get("moveOutDate"))
        consumptions = Consumptions.from_dict(obj.get("consumptions"))
        readings_history = ReadingsHistory.from_dict(obj.get("readingsHistory"))
        editable_readings = EditableReadings.from_dict(obj.get("editableReadings"))
        point_of_delivery = PointOfDelivery.from_dict(obj.get("pointOfDelivery"))
        smart_meter_type = from_str(obj.get("smartMeterType"))
        smart_meter_type_name = from_str(obj.get("smartMeterTypeName"))
        smart_meter_type_help = from_str(obj.get("smartMeterTypeHelp"))
        power_generation_unit = from_bool(obj.get("powerGenerationUnit"))
        station = int(from_str(obj.get("station")))
        sub_station = int(from_str(obj.get("subStation")))
        supplier = Supplier.from_dict(obj.get("supplier"))
        synth_profile = from_str(obj.get("synthProfile"))
        smart_meter_activation_possible = from_bool(
            obj.get("smartMeterActivationPossible")
        )
        load_profile_activation_possible = from_bool(
            obj.get("loadProfileActivationPossible")
        )
        daily_profile_dispatch_active = from_bool(obj.get("dailyProfileDispatchActive"))
        monthly_profile_dispatch_active = from_bool(
            obj.get("monthlyProfileDispatchActive")
        )
        daily_profile_dispatch_inactive = from_bool(
            obj.get("dailyProfileDispatchInactive")
        )
        monthly_profile_dispatch_inactive = from_bool(
            obj.get("monthlyProfileDispatchInactive")
        )
        amis_meter = from_bool(obj.get("amisMeter"))
        amis_active = from_bool(obj.get("amisActive"))
        load_curve_active = from_bool(obj.get("loadCurveActive"))
        profile_active = from_bool(obj.get("profileActive"))
        device_key_status = from_str(obj.get("deviceKeyStatus"))
        available_profile_types = from_list(from_str, obj.get("availableProfileTypes"))
        device_key_available = from_bool(obj.get("deviceKeyAvailable"))
        daily_profile_dispatch_status = from_str(obj.get("dailyProfileDispatchStatus"))
        monthly_profile_dispatch_status = from_str(
            obj.get("monthlyProfileDispatchStatus")
        )
        reactive_current_profile_present = from_bool(
            obj.get("reactiveCurrentProfilePresent")
        )
        new_reading_possible = from_bool(obj.get("newReadingPossible"))
        return Contract(
            contract_number,
            branch,
            scale_type,
            active,
            move_in_date,
            move_out_date,
            consumptions,
            readings_history,
            editable_readings,
            point_of_delivery,
            smart_meter_type,
            smart_meter_type_name,
            smart_meter_type_help,
            power_generation_unit,
            station,
            sub_station,
            supplier,
            synth_profile,
            smart_meter_activation_possible,
            load_profile_activation_possible,
            daily_profile_dispatch_active,
            monthly_profile_dispatch_active,
            daily_profile_dispatch_inactive,
            monthly_profile_dispatch_inactive,
            amis_meter,
            amis_active,
            load_curve_active,
            profile_active,
            device_key_status,
            available_profile_types,
            device_key_available,
            daily_profile_dispatch_status,
            monthly_profile_dispatch_status,
            reactive_current_profile_present,
            new_reading_possible,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["contractNumber"] = from_str(self.contract_number)
        result["branch"] = from_str(self.branch)
        result["scaleType"] = from_str(self.scale_type)
        result["active"] = from_bool(self.active)
        result["moveInDate"] = self.move_in_date.isoformat()
        result["moveOutDate"] = self.move_out_date.isoformat()
        result["consumptions"] = to_class(Consumptions, self.consumptions)
        result["readingsHistory"] = to_class(ReadingsHistory, self.readings_history)
        result["editableReadings"] = to_class(EditableReadings, self.editable_readings)
        result["pointOfDelivery"] = to_class(PointOfDelivery, self.point_of_delivery)
        result["smartMeterType"] = from_str(self.smart_meter_type)
        result["smartMeterTypeName"] = from_str(self.smart_meter_type_name)
        result["smartMeterTypeHelp"] = from_str(self.smart_meter_type_help)
        result["powerGenerationUnit"] = from_bool(self.power_generation_unit)
        result["station"] = from_str(str(self.station))
        result["subStation"] = from_str(str(self.sub_station))
        result["supplier"] = to_class(Supplier, self.supplier)
        result["synthProfile"] = from_str(self.synth_profile)
        result["smartMeterActivationPossible"] = from_bool(
            self.smart_meter_activation_possible
        )
        result["loadProfileActivationPossible"] = from_bool(
            self.load_profile_activation_possible
        )
        result["dailyProfileDispatchActive"] = from_bool(
            self.daily_profile_dispatch_active
        )
        result["monthlyProfileDispatchActive"] = from_bool(
            self.monthly_profile_dispatch_active
        )
        result["dailyProfileDispatchInactive"] = from_bool(
            self.daily_profile_dispatch_inactive
        )
        result["monthlyProfileDispatchInactive"] = from_bool(
            self.monthly_profile_dispatch_inactive
        )
        result["amisMeter"] = from_bool(self.amis_meter)
        result["amisActive"] = from_bool(self.amis_active)
        result["loadCurveActive"] = from_bool(self.load_curve_active)
        result["profileActive"] = from_bool(self.profile_active)
        result["deviceKeyStatus"] = from_str(self.device_key_status)
        result["availableProfileTypes"] = from_list(
            from_str, self.available_profile_types
        )
        result["deviceKeyAvailable"] = from_bool(self.device_key_available)
        result["dailyProfileDispatchStatus"] = from_str(
            self.daily_profile_dispatch_status
        )
        result["monthlyProfileDispatchStatus"] = from_str(
            self.monthly_profile_dispatch_status
        )
        result["reactiveCurrentProfilePresent"] = from_bool(
            self.reactive_current_profile_present
        )
        result["newReadingPossible"] = from_bool(self.new_reading_possible)
        return result


class Welcome9:
    contract_account_number: str
    business_partner_number: int
    description: str
    active: bool
    branch: str
    address: Address
    billed_by_provider: bool
    bank_account_in: BankAccountIn
    bank_account_out: BankAccountIn
    invoice_settings: BankAccountIn
    contracts: List[Contract]
    product_change_available: bool
    disconnection_notification: BankAccountIn
    editable: bool

    def __init__(
        self,
        contract_account_number: str,
        business_partner_number: int,
        description: str,
        active: bool,
        branch: str,
        address: Address,
        billed_by_provider: bool,
        bank_account_in: BankAccountIn,
        bank_account_out: BankAccountIn,
        invoice_settings: BankAccountIn,
        contracts: List[Contract],
        product_change_available: bool,
        disconnection_notification: BankAccountIn,
        editable: bool,
    ) -> None:
        self.contract_account_number = contract_account_number
        self.business_partner_number = business_partner_number
        self.description = description
        self.active = active
        self.branch = branch
        self.address = address
        self.billed_by_provider = billed_by_provider
        self.bank_account_in = bank_account_in
        self.bank_account_out = bank_account_out
        self.invoice_settings = invoice_settings
        self.contracts = contracts
        self.product_change_available = product_change_available
        self.disconnection_notification = disconnection_notification
        self.editable = editable

    @staticmethod
    def from_dict(obj: Any) -> "Welcome9":
        assert isinstance(obj, dict)
        contract_account_number = from_str(obj.get("contractAccountNumber"))
        business_partner_number = int(from_str(obj.get("businessPartnerNumber")))
        description = from_str(obj.get("description"))
        active = from_bool(obj.get("active"))
        branch = from_str(obj.get("branch"))
        address = Address.from_dict(obj.get("address"))
        billed_by_provider = from_bool(obj.get("billedByProvider"))
        bank_account_in = BankAccountIn.from_dict(obj.get("bankAccountIn"))
        bank_account_out = BankAccountIn.from_dict(obj.get("bankAccountOut"))
        invoice_settings = BankAccountIn.from_dict(obj.get("invoiceSettings"))
        contracts = from_list(Contract.from_dict, obj.get("contracts"))
        product_change_available = from_bool(obj.get("productChangeAvailable"))
        disconnection_notification = BankAccountIn.from_dict(
            obj.get("disconnectionNotification")
        )
        editable = from_bool(obj.get("editable"))
        return Welcome9(
            contract_account_number,
            business_partner_number,
            description,
            active,
            branch,
            address,
            billed_by_provider,
            bank_account_in,
            bank_account_out,
            invoice_settings,
            contracts,
            product_change_available,
            disconnection_notification,
            editable,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["contractAccountNumber"] = from_str(self.contract_account_number)
        result["businessPartnerNumber"] = from_str(str(self.business_partner_number))
        result["description"] = from_str(self.description)
        result["active"] = from_bool(self.active)
        result["branch"] = from_str(self.branch)
        result["address"] = to_class(Address, self.address)
        result["billedByProvider"] = from_bool(self.billed_by_provider)
        result["bankAccountIn"] = to_class(BankAccountIn, self.bank_account_in)
        result["bankAccountOut"] = to_class(BankAccountIn, self.bank_account_out)
        result["invoiceSettings"] = to_class(BankAccountIn, self.invoice_settings)
        result["contracts"] = from_list(lambda x: to_class(Contract, x), self.contracts)
        result["productChangeAvailable"] = from_bool(self.product_change_available)
        result["disconnectionNotification"] = to_class(
            BankAccountIn, self.disconnection_notification
        )
        result["editable"] = from_bool(self.editable)
        return result


def welcome9_from_dict(s: Any) -> Welcome9:
    return Welcome9.from_dict(s)


def welcome9_to_dict(x: Welcome9) -> Any:
    return to_class(Welcome9, x)
