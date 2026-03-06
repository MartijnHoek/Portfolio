from VinDecoder.Core.DefinedVinDecoders import get_defined_vin_decoders
from VinDecoder.Core.VinDecoderBase import VinDecoderBase


class VinDecodingHandler:
    def __init__(self, vin):
        self.vin = vin
        self.decoder = VinDecoderBase(self.vin)     # Just a placeholder for the IDE to recognize the functions

    def get_vin_decoder(self):
        """
        Loop through all the possible VIN decoders from DefinedVinDecoders and check if a match is made on the WMI.
        :return: VIN decoder to be used for decoding the VIN or None of nothing was found.
        """
        for vin_decoder in get_defined_vin_decoders():
            decoder = vin_decoder(self.vin)
            result = decoder.is_vin_for_this_decoder()
            if result:
                self.decoder = decoder
                return decoder
        return None

    def get_vin_decoding_result(self, vin_decoder):
        """
        Use the selected VIN decoder to request the values of:
        - Model
        - Variant
        - Production Date
        - Assembly Plant
        - Engine
        And combine them into a dictionary to be returned
        :param vin_decoder: VIN decoder used to decoded values from the VIN
        :return: dictionary containing decoded values from the VIN
        """
        manufacturer_info = vin_decoder.manufacturer_name
        model_info = vin_decoder.get_model()
        variant_info = model_info.variant
        production_date = vin_decoder.get_production_date()
        assembly_plant = vin_decoder.get_assembly_plant()
        engine = vin_decoder.get_engine()

        result_dict = {
            "vin":      self.vin,                                           # Inputted VIN
            "make":     {
                        'name': manufacturer_info['name'],                  # Name of the manufacturer (defined in the Manufacturer specific Decoder)
                        'uuid': manufacturer_info['uuid']},                 # Uuid of the manufacturer (defined in the Manufacturer specific Decoder)
            "model":    {
                        'name': model_info.name,                            # Name of the model (defined in the specific ModelObject)
                        'uuid': model_info.uuid,                            # Uuid of the model (defined in the specific ModelObject)
                        'variant': {                                        # Information about a variant of the model
                            'name': variant_info.name,                      # Name of the variant (defined in a specific VariantObject of the ModelObject)
                            'uuid': variant_info.uuid,                      # Uuid of the variant (defined in a specific VariantObject of the ModelObject)
                        },
                        'production_date': production_date,                 # Production date of the vehicle (Defined in the specific Manufacturer specific Decoder and ModelObjects)
                        'assembly_plant': {                                 # Information about the assembly plant that the vehicle is made at
                            'name': assembly_plant.name,                    # Name of the assembly plant
                            'city': assembly_plant.city,                    # City that the plant is based in
                            'region': assembly_plant.region,                # Region that the assembly plant is based in
                            'country': {                                    # Information about the country of the assembly plant (using pycountry.db.Country)
                                'alpha_2':  assembly_plant.country.alpha_2, # alpha 2 code of the country (ISO 3166-1)
                                'name':     assembly_plant.country.name,    # Name of the country (ISO 3166-1)
                            },
                        },
                        'engine': {                                         # Information about the engine
                            'name':             engine.name,                # Name of the engine
                            'manufacturer':     engine.manufacturer,        # Manufacturer of the engine
                            'uuid':             engine.uuid,                # Uuid of the engine
                            'fuel_type':        engine.fuel_type,           # Fuel type of the engine
                            'engine_type':      engine.engine_type,         # Form factor of the engine (i.e. Inline-4, V6)
                            'displacement_l':   engine.displacement_l,      # Displacement of the engine in Liters
                            'power_kw':         engine.power_kw,            # Power of the engine in kW
                            'torque_nm':        engine.torque_nm,           # Torque of the engine in Nm
                            'aspiration':       engine.aspiration,          # Aspiration type of the engine (i.e. Turbo, Supercharged)
                            }
                        }
        }
        return result_dict