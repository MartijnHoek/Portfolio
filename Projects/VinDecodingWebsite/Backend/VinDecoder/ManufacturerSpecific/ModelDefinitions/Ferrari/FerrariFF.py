from VinDecoder.Core.ModelHandler import VariantObject
from VinDecoder.ManufacturerSpecific.ManufacturerSpecificModelHandlers.FerrariModelHandler import FerrariModelHandler
from VinDecoder.ManufacturerSpecific.Variables.FerrariVariables import FerrariEngineVariables


class FerrariFF(FerrariModelHandler):
    def __init__(self, vin):
        super().__init__(vin)
        self.name = "FF"
        self.uuid = "444e0faf-d2db-40b1-b5c1-02ad8aa137be"
        self.vin = vin

    def set_engine(self, engine_dict):
        model_specific_engine_dict = engine_dict[FerrariEngineVariables.FERRARI_ENGINE_CYCLE_3]
        self.engine = model_specific_engine_dict.get(self.vin[5], None)
