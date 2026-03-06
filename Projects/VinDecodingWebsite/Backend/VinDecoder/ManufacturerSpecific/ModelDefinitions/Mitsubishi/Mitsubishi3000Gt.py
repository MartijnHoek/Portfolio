from VinDecoder.Core.ModelHandler import ModelHandler, VariantObject
from VinDecoder.Engines.MitsubishiEngines import MitsubishiEngines
from VinDecoder.ManufacturerSpecific.Variables.MitsubishiVariables import \
    MitsubishiProductionDateVariables, MitsubishiAssemblyPlantVariables


class Mitsubishi3000Gt(ModelHandler):
    def __init__(self, vin):
        super().__init__(vin)
        self.name = "3000GT"
        self.uuid = "866f0bdf-704b-46f7-97b6-337de2f363f0"
        self.vin = vin

    def _get_variant(self):
        # JA3X E 74C4NY028520
        variant_in_vin = self.vin[4]
        variant_dict = {
            # "D":        # FWD variant
            # "M":        # FWD variant
            "E":        VariantObject(name="VR-4", uuid="e97c0362-2534-4bfe-8b06-6b9a84a4c4f2"),
            "N":        VariantObject(name="VR-4", uuid="e97c0362-2534-4bfe-8b06-6b9a84a4c4f2"),

            # Note: Others are removed from portfolio
        }
        variant = variant_dict.get(variant_in_vin, None)
        return variant

    def set_production_date(self, manufacturer_production_date_dicts):
        # JA3XE74C4 N Y028520
        model_specific_production_date_dict = manufacturer_production_date_dicts[MitsubishiProductionDateVariables.MITSUBISHI_DEFAULT_1980_2009]
        self.production_date = model_specific_production_date_dict.get(self.vin[9], None)

    def set_assembly_plant(self, manufacturer_assembly_plant_dicts):
        # JA3XE74C4N Y 028520
        model_specific_assembly_plant_dict = manufacturer_assembly_plant_dicts[MitsubishiAssemblyPlantVariables.MITSUBISHI_DEFAULT]
        self.assembly_plant = model_specific_assembly_plant_dict.get(self.vin[10], None)

    def set_engine(self, engine_dict):
        # JA3XE74 C 4NY028520
        engine_dict = {
            "B":    MitsubishiEngines.MITSUBISHI_6G72_DOHC,
            "C":    MitsubishiEngines.MITSUBISHI_6G72_DOHC_TWIN_TURBO,
            # Note: Others are removed from portfolio
        }
        self.engine = engine_dict.get(self.vin[7], None)