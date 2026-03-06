from VinDecoder.Core.ModelHandler import ModelHandler
from VinDecoder.ManufacturerSpecific.Variables.FerrariVariables import FerrariMarketVariables, \
    FerrariProductionDateVariables, FerrariAssemblyPlants


class FerrariModelHandler(ModelHandler):
    def __init__(self, vin):
        super().__init__(vin)

    def _is_00aa_format(self):
        """
        Helper function to quickly determine what decoding style to use (00AA or AA00)
        :return: Boolean if VIN is 00AA format
        """
        if self.vin[3:5].isnumeric():
            return True
        else:
            return False

    def _get_model_code_in_vin(self):
        """
        Helper function to quickly get model code characters from the VIN without having duplicate code (used to determine variant by Ferrari)
        :return: the model codes
        """
        if self._is_00aa_format():
            variant_in_vin = self.vin[3:5]
        else:
            variant_in_vin = self.vin[5:7]
        return variant_in_vin

    def _get_market(self):
        """
        Ferrari specific function to decode the market that the car is designed for.
        :return: market as string
        """""
        market_dict = {
            "A": FerrariMarketVariables.NORTH_AMERICA,
            "B": FerrariMarketVariables.EUROPE,

            # Note: rest of decoding is removed for portfolio

        }
        return market_dict.get(self.vin[7], None)

    def set_production_date(self, manufacturer_production_date_dicts):
        """
        Ferrari production date is determined based on the market and which cycle of model codes is used.
        :return:
        """
        market = self._get_market()
        if market not in [FerrariMarketVariables.NORTH_AMERICA, FerrariMarketVariables.MIDDLE_EAST,
                          FerrariMarketVariables.CENTRAL_AMERICA, FerrariMarketVariables.CHINA]:
            # Only vehicles for above market support production year decoding
            return

        if self.vin[3:5].isnumeric():
            model_specific_production_date_dict = manufacturer_production_date_dicts[FerrariProductionDateVariables.FERRARI_00AA]
        else:
            model_specific_production_date_dict = manufacturer_production_date_dicts[FerrariProductionDateVariables.FERRARI_AA00]
        self.production_date = model_specific_production_date_dict.get(self.vin[9], None)

    def set_assembly_plant(self, manufacturer_assembly_plant_dicts):
        model_specific_assembly_plant_dict = manufacturer_assembly_plant_dicts[FerrariAssemblyPlants.FERRARI_DEFAULT]
        self.assembly_plant = model_specific_assembly_plant_dict.get(self.vin[10], None)