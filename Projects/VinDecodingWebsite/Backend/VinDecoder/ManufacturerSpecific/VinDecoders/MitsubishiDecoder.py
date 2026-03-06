from VinDecoder.AssemblyPlants.AssemblyPlantsIndonesia import \
    AssemblyPlantsIndonesia
from VinDecoder.AssemblyPlants.AssemblyPlantsJapan import \
    AssemblyPlantsJapan
from VinDecoder.AssemblyPlants.AssemblyPlantsMalasyia import \
    AssemblyPlantsMalaysia
from VinDecoder.AssemblyPlants.AssemblyPlantsNetherlands import \
    AssemblyPlantsNetherlands
from VinDecoder.AssemblyPlants.AssemblyPlantsUnitedStates import \
    AssemblyPlantsUnitedStates
from VinDecoder.Core.Manufacturers import Manufacturers
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.Mitsubishi3000Gt import Mitsubishi3000Gt
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiCarisma import MitsubishiCarisma
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiColtZ30 import MitsubishiColtZ30
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiEclipseCross import MitsubishiEclipseCross
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiEclipseD31aD32aD33aD38aD39a import \
    MitsubishiEclipseD31aD32aD33aD38aD39a
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiEclipseDk2aDk4a import MitsubishiEclipseDk2aDk4a
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiGalantE30 import MitsubishiGalantE30
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiGalantE50E60E70E80 import MitsubishiGalantE50E60E70E80
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiGalantEaEc import MitsubishiGalantEaEc
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiIMiev import MitsubishiIMiev
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiStarion import MitsubishiStarion
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Mitsubishi.MitsubishiXpander import MitsubishiXpander
from VinDecoder.Core.VinDecoderBase import VinDecoderBase
from VinDecoder.ManufacturerSpecific.Variables.MitsubishiVariables import \
    MitsubishiProductionDateVariables, MitsubishiAssemblyPlantVariables


class MitsubishiDecoder(VinDecoderBase):

    def _get_defined_manufacturer_wmi_list(self):
        wmi_list = [
            "4A3",      # 4A3AC84LXYE******
            "JA3",      # JA3XD64B9MY******
            "JA4",      # JA4AS5AA8LZ009610
            "JMA",      # JMAA183AMHZ400115
            "JMB",      # JMBSNEA2AVZ002272
            "JMY",      # JMYXSZ23A5Z000381
            "MK2",      # MK2K6T1Y6MN******
            "PM7",      # PM7LRNC1WLC026441
            "XMC",      # XMCXJZ34A5F081122
            "XMD",
            "XNC",      # XNCBNZ36A7X******
            "XND"
        ]
        return wmi_list

    @staticmethod
    def _get_manufacturer_name():
        return {'name': Manufacturers.MITSUBISHI.name, 'uuid': Manufacturers.MITSUBISHI.uuid}

    def _get_model_decoding_positioning(self):
        if self.input_vin_wmi in ["JA3", "JA4", "4A3"]:
            return [3, 6]
        else:
            return [5, 9]

    @staticmethod
    def _get_production_date_dictionary():
        default_production_date_2001_2025 = {
            "1": "2001", "2": "2002", "3": "2003", "4": "2004", "5": "2005", "6": "2006",
            "7": "2007", "8": "2008", "9": "2009", "A": "2010", "B": "2011", "C": "2012",
            "D": "2013", "E": "2014", "F": "2015", "G": "2016", "H": "2017", "J": "2018",
            "K": "2019", "L": "2020", "M": "2021", "N": "2022", "P": "2023", "R": "2024",
            "S": "2025",
        }
        default_production_date_1980_2009 = {
            "A": "1980", "B": "1981", "C": "1982", "D": "1983", "E": "1984", "F": "1985",
            "G": "1986", "H": "1987", "J": "1988", "K": "1989", "L": "1990", "M": "1991",
            "N": "1992", "P": "1993", "R": "1994", "S": "1995", "T": "1996", "V": "1997",
            "W": "1998", "X": "1999", "Y": "2000", "1": "2001", "2": "2002", "3": "2003",
            "4": "2004", "5": "2005", "6": "2006", "7": "2007", "8": "2008", "9": "2009",
        }

        possible_production_date_dicts = {
            MitsubishiProductionDateVariables.MITSUBISHI_DEFAULT_1980_2009: default_production_date_1980_2009,
            MitsubishiProductionDateVariables.MITSUBISHI_DEFAULT_2001_2025: default_production_date_2001_2025,
        }
        return possible_production_date_dicts

    @staticmethod
    def _get_assembly_plant_dictionary():
        default_assembly_plant_dictionary = {
            "C": AssemblyPlantsMalaysia.HICOM_PLANT,                        # Xpander
            "E": AssemblyPlantsUnitedStates.DIAMOND_STAR_MOTORS_NORMAL,     # Eclipse (D31A/...)/Eclipse (DK2A/...)/Galant (E50/...)/
            # Note: Removed others for portfolio
        }

        possible_assembly_plant_dicts = {
            MitsubishiAssemblyPlantVariables.MITSUBISHI_DEFAULT:    default_assembly_plant_dictionary
        }
        return possible_assembly_plant_dicts

    def _get_model_dictionary(self):
        if self.input_vin_wmi in ["JA3", "JA4", "4A3"]:
            model_dict = {
                # 3000GT
                "AM4": Mitsubishi3000Gt,
                "XD6": Mitsubishi3000Gt,                    # JA3 XD6 4B0NY066749
                "XE7": Mitsubishi3000Gt,                    # JA3 XE7 4C4NY028520

                # Eclipse 2nd gen (D31A/D32A/D33A/D38A/D39A)
                "AX5":      MitsubishiEclipseD31aD32aD33aD38aD39a,          # 4A3 AX5 5F6XE072292
                # Note: Removed others for portfolio
            }
        else:
            model_dict = {
                # Carisma
                "DA1A":     MitsubishiCarisma,              # XMC SN DA1A 3F039726

                # Colt (Z30)
                "Z39A":     MitsubishiColtZ30,              # XMC XN Z39A 8F073477

                # Note: Removed others for portfolio
            }
        return model_dict