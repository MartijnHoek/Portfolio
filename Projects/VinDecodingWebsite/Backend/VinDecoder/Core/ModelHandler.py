from dataclasses import dataclass


class ModelHandler:
    def __init__(self, vin):
        self.name= None
        self.uuid= None
        self.vin = vin
        self.wmi = vin[:3]
        self.variant = self._variant_handling()
        self.production_date = None
        self.assembly_plant = None
        self.engine = None

    def _variant_handling(self):
        """
        Handling the _get_variant function
        :return: a VariantObject
        """
        variant = self._get_variant()
        if not variant:
            variant = VariantObject()
        return variant

    def _get_variant(self):
        """
        Get the specific variant of a model (i.e. convertable, wagon or trim levels like GTI for instance).
        :return: variant information
        """
        return None

    def set_production_date(self, manufacturer_production_date_dicts):
        """
        Set the production date from the VIN as the self.production_date variable
        For this in each xDecoder file are defined which mappings are possible for this manufacturer
        :param manufacturer_production_date_dicts: dictionary containing all the mappings (defined in another dictionary) of the manufacturer
                                     i.e:    { 'default_mitsubishi_2001_2025': {1: 2001, 2: 2002, etc.}
        """

    def set_assembly_plant(self, manufacturer_assembly_plant_dicts):
        """
        Set the assembly location from the VIN as the self.assembly_plant variable
        :param manufacturer_assembly_plant_dicts: dictionary containing manufacturer specific mappings
                                                i.e:    'default_assembly_plant':  {  "C": AssemblyPlantsMalaysia.HICOM_PLANT, etc...}
        """

    def set_engine(self, engine_dict):
        """
        Set the engine from the VIN as the self.engine variable
        Per defined model the decoding mapping is defined.
        :param engine_dict: dictionary containing mapping for engines
                            i.e:    { 'engine_cycle_4': {R: FerrariEngineXxxxX, etc.}
        """

class VariantObject:
    def __init__(self, name=None, uuid=None):
        self.name=  name
        self.uuid=  uuid
