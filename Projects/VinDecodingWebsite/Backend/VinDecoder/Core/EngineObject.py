class EngineType:
    F12 =   "Flat-12"

    I3 =    "Inline-3"
    I4 =    "Inline-4"

    V6 =    "V6"
    V8 =    "V8"
    V12 =    "V12"


class FuelType:
    DIESEL =    "Diesel"
    PETROL =    "Petrol"
    ELECTRIC =  "Electric"


class AspirationType:
    NATURALLY_ASPIRATED =   "Naturally Aspirated"
    SUPERCHARGED =          "Supercharged"
    TURBO =                 "Turbocharged"
    TWIN_TURBO =            "Twin-Turbocharged"


class EngineObject(object):
    def __init__(self, name, manufacturer, uuid, fuel_type=None, engine_type=None, displacement_l=None, power_kw=None, torque_nm=None, aspiration=None):
        self.name = name
        self.manufacturer = manufacturer
        self.uuid = uuid
        self.fuel_type = fuel_type
        self.engine_type = engine_type
        self.displacement_l = displacement_l
        self.power_kw = power_kw
        self.torque_nm = torque_nm
        self.aspiration = aspiration
