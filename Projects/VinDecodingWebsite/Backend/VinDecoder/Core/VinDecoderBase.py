from VinDecoder.Core.AssemblyPlantObject import AssemblyPlantObject
from VinDecoder.Core.EngineObject import EngineObject
from VinDecoder.Core.ModelHandler import ModelHandler


class VinDecoderBase:
    def __init__(self, vin):
        # Variables based on input
        self.vin = vin
        self.input_vin_wmi = self.vin[:3]

        # Manufacturer specific variables
        self.manufacturer_wmi_list = self._get_defined_manufacturer_wmi_list()
        self.manufacturer_name = self._get_manufacturer_name()

        # Values to be overwritten
        self.model = ModelHandler(self.vin)

    @staticmethod
    def _get_defined_manufacturer_wmi_list():
        """
        Function inherited by subclasses to be used to define all the WMI's of that manufacturer.
        :return: Empty List
        """
        return []

    @staticmethod
    def _get_manufacturer_name():
        return {'name': '', 'uuid': ''}

    def _is_wmi_for_this_manufacturer(self):
        """
        Internal function to compare the inputted VIN's WMI against the defined manufacturer WMI's for a match.
        :return: Return Boolean if a match is found.
        """
        for manufacturer_wmi in self.manufacturer_wmi_list:
            if manufacturer_wmi == self.input_vin_wmi:
                return True
        return False

    @staticmethod
    def _get_model_decoding_positioning():
        """
        Get the position of the characters in the VIN used to decode the model description
        :return: List [first position, last position]
        """
        return [None, None]

    @staticmethod
    def _get_model_dictionary():
        """
        Get a dictionary containing the encoded model definition from the VIN and the corresponding decoded model:
        :return: dictionary containing mapping of encoded VIN model and the decoded model:\
                i.e: { 'AA3':  ModelList.GALANT_EA_EC}
        """
        return {}

    @staticmethod
    def _get_production_date_dictionary():
        """
        Get a dictionary containing the encoded production date from the VIN, for some manufacturers this may differ per
        model/region/WMI. Per model is defined which dictionary they should use.
        :return: dictionary containing all the mappings (defined in another dictionary) of the manufacturer
                i.e:    { 'default_mitsubishi_2001_2025': {1: 2001, 2: 2002, etc.}
        """
        return {}

    @staticmethod
    def _get_assembly_plant_dictionary():
        """
        Get a dictionary containing the mapping for the assembly plant location.
        """
        return {}

    @staticmethod
    def _get_engine_dictionary():
        """
        Get a dictionary containing the mapping of engines
        :return:
        """
        return{}

    def is_vin_for_this_decoder(self):
        """
        External function that returns if the inputted VIN can be decoded with this decoder
        :return: Boolean if decoding is possible using this decoder.
        """
        if self._is_wmi_for_this_manufacturer():
            return True
        else:
            return False

    def get_model(self):
        """
        External function that returns the model if it is found in the manufacturer specific VIN decoder
        :return: ModelHandler Object of the matched model
        """
        first_character_position, last_character_position = self._get_model_decoding_positioning()
        model_dict = self._get_model_dictionary()

        model_code_in_vin = self.vin[first_character_position:last_character_position]
        model_class = model_dict.get(model_code_in_vin, None)
        if model_class is None:
            return ModelHandler(self.vin)

        self.model = model_class(self.vin)

        return self.model

    def get_production_date(self):
        """
        External function that returns the production date of the provided VIN.
        :return: production date as string
        """
        if not self.model:
            return None

        production_date_dict = self._get_production_date_dictionary()
        if not production_date_dict:
            return None

        self.model.set_production_date(production_date_dict)
        return self.model.production_date

    def get_assembly_plant(self):
        """
        External function that returns the assembly plant of the provided VIN.
        :return: assembly plant as AssemblyPlantObject
        """
        if not self.model:
            return AssemblyPlantObject()
        assembly_plant_dict = self._get_assembly_plant_dictionary()

        self.model.set_assembly_plant(assembly_plant_dict)
        if self.model.assembly_plant is None:
            return AssemblyPlantObject()

        return self.model.assembly_plant

    def get_engine(self):
        """
        External function that returns the engine of the provided VIN.
        :return: Engine as EngineObject
        """
        if not self.model:
            return EngineObject(name=None, manufacturer=None, uuid=None)
        engine_dict = self._get_engine_dictionary()

        self.model.set_engine(engine_dict)
        if self.model.engine is None:
            return EngineObject(name=None, manufacturer=None, uuid=None)
        return self.model.engine