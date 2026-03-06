from VinDecoder.Core.ModelHandler import VariantObject
from VinDecoder.ManufacturerSpecific.ManufacturerSpecificModelHandlers.FerrariModelHandler import FerrariModelHandler
from VinDecoder.ManufacturerSpecific.Variables.FerrariVariables import FerrariEngineVariables


class Ferrari458(FerrariModelHandler):
    def __init__(self, vin):
        super().__init__(vin)
        self.name = "458"
        self.uuid = "c78dcffc-011d-4429-a840-fb010dbe142a"
        self.vin = vin

    def _get_variant(self):
        variant_in_vin = self._get_model_code_in_vin()
        variant_dict = {
            "67":           VariantObject(name="Italia", uuid="c20c47e3-9d07-48ae-911a-7afae998697d"),          # ZFF 67 NFA7F0210687
            "68":           VariantObject(name="Spider", uuid="9fb3faa2-fb0b-4b41-a529-80a189633e6f"),          # ZFF 68 NHC000196445

            # Note: Others are removed from portfolio
        }
        variant = variant_dict.get(variant_in_vin, None)
        return variant

    def set_engine(self, engine_dict):
        model_specific_engine_dict = engine_dict[FerrariEngineVariables.FERRARI_ENGINE_CYCLE_3]

        if self._is_00aa_format():   # This model uses both model code formats so the position differs per used format
            self.engine = model_specific_engine_dict.get(self.vin[5], None)
        else:
            self.engine = model_specific_engine_dict.get(self.vin[3], None)
