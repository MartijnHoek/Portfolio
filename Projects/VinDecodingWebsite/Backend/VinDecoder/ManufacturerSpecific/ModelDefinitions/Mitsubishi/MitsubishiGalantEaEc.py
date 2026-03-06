from VinDecoder.Core.ModelHandler import ModelHandler, VariantObject
from VinDecoder.Engines.MitsubishiEngines import MitsubishiEngines
from VinDecoder.ManufacturerSpecific.Variables.MitsubishiVariables import \
    MitsubishiProductionDateVariables, MitsubishiAssemblyPlantVariables


class MitsubishiGalantEaEc(ModelHandler):
    def __init__(self, vin):
        super().__init__(vin)
        self.name = "Galant (EA/EC)"
        self.uuid = "89774e6c-7dfd-41f6-943e-4662d128649e"
        self.vin = vin

    def _get_variant(self):
        if self.wmi in ["4A3", "JA3"]:
            # 4A3AA 4 6G1YE******
            variant_in_vin = self.vin[5]
            variant_dict = {
                "3":        VariantObject(name="DE", uuid="1ed96ddd-c58b-48b7-b73a-c46dcc70042c"),
                "4":        VariantObject(name="ES/GTZ",uuid= "21e2279f-2040-4a16-9120-b0e8b7a1a428"),
                "5":        VariantObject(name="LS",uuid= "ed85e3bd-8c94-4d69-9d18-cf000f6d8309"),
            }
        else:
            # JMBSNEA2 A VZ006842
            variant_in_vin = self.vin[8]
            variant_dict = {
                "A":        None,   # Sedan version, no other differences seen.
                "W":        VariantObject(name="Station Wagon", uuid="9a8b4b26-3db9-4484-ae95-fd9df40611b2")
            }
        variant = variant_dict.get(variant_in_vin, None)
        return variant

    def set_production_date(self, manufacturer_production_date_dicts):
        # 4A3AA46G1 Y E******
        model_specific_production_date_dict = manufacturer_production_date_dicts[MitsubishiProductionDateVariables.MITSUBISHI_DEFAULT_1980_2009]
        self.production_date = model_specific_production_date_dict.get(self.vin[9], None)

    def set_assembly_plant(self, manufacturer_assembly_plant_dicts):
        # 4A3AA46G1Y E ******
        model_specific_assembly_plant_dict = manufacturer_assembly_plant_dicts[MitsubishiAssemblyPlantVariables.MITSUBISHI_DEFAULT]
        self.assembly_plant = model_specific_assembly_plant_dict.get(self.vin[10], None)

    def set_engine(self, engine_dict):
        # 4A3AA46 G 1YE******
        engine_dict = {
            "C":    MitsubishiEngines.MITSUBISHI_4G93_SOHC,
            "G":    MitsubishiEngines.MITSUBISHI_4G64_SOHC,
            "H":    MitsubishiEngines.MITSUBISHI_6G72_SOHC_24V,
            "2":    MitsubishiEngines.MITSUBISHI_4G64_GDI,
            "5":    MitsubishiEngines.MITSUBISHI_6A13,
        }
        self.engine = engine_dict.get(self.vin[7], None)