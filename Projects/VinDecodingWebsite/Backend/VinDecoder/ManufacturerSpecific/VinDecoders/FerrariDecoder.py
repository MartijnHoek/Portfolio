from VinDecoder.AssemblyPlants.AssemblyPlantsItaly import AssemblyPlantsItaly
from VinDecoder.Core.Manufacturers import Manufacturers
from VinDecoder.Core.VinDecoderBase import VinDecoderBase
from VinDecoder.Engines.FerrariEngines import FerrariEngines
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari208 import Ferrari208
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari308 import Ferrari308
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari328 import Ferrari328
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari348 import Ferrari348
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari355 import Ferrari355
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari360 import Ferrari360
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari400I import Ferrari400I
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari4084RM import Ferrari4084RM
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari412 import Ferrari412
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari456 import Ferrari456
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari512 import Ferrari512
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari550 import Ferrari550
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari575 import Ferrari575
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariF40 import FerrariF40
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariF50 import FerrariF50
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariGTBTurbo import FerrariGTBTurbo
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariGTO import FerrariGTO
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariGTSTurbo import FerrariGTSTurbo
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariMondial import FerrariMondial
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariPortofino import FerrariPortofino
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariF12 import FerrariF12
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariFF import FerrariFF
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariCaliforniaT import FerrariCaliforniaT
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari612 import Ferrari612
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariEnzo import FerrariEnzo
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari296 import Ferrari296
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari458 import Ferrari458
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari488 import Ferrari488
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari599 import Ferrari599
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.Ferrari812 import Ferrari812
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariCalifornia import FerrariCalifornia
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariDaytonaSP3 import FerrariDaytonaSP3
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariF430 import FerrariF430
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariF8 import FerrariF8
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariGTC4Lusso import FerrariGTC4Lusso
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariLaFerrari import FerrariLaFerrari
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariMonzaSP import FerrariMonzaSP
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariPurosangue import FerrariPurosangue
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariRoma import FerrariRoma
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariSF90 import FerrariSF90
from VinDecoder.ManufacturerSpecific.ModelDefinitions.Ferrari.FerrariTestarossa import FerrariTestarossa
from VinDecoder.ManufacturerSpecific.Variables.FerrariVariables import FerrariProductionDateVariables, \
    FerrariAssemblyPlants, FerrariEngineVariables


class FerrariDecoder(VinDecoderBase):

    def _get_defined_manufacturer_wmi_list(self):
        wmi_list = [
            "ZDF",
            "ZFF",      # ZFF CZ56B000126274
            "ZSG",
        ]
        return wmi_list

    @staticmethod
    def _get_manufacturer_name():
        return {'name': Manufacturers.FERRARI.name, 'uuid': Manufacturers.FERRARI.uuid}

    def _get_model_decoding_positioning(self):
        if self.vin[3:5].isnumeric():
            return [3, 5]
        else:
            return[5, 7]

    def _get_production_date_dictionary(self):
        production_date_aa00 = {
            "A": "1980", "B": "1981", "C": "1982", "D": "1983", "E": "1984", "F": "1985", "G": "1986",
            "H": "1987", "J": "1988", "K": "1989", "L": "1990", "M": "1991", "N": "1992", "P": "1993",
            "R": "1994", "S": "1995", "T": "1996", "V": "1997", "W": "1998", "Y": "2000", "1": "2001",
            "2": "2002", "3": "2003", "4": "2004", "5": "2005", "6": "2006", "7": "2007", "8": "2008",
            "9": "2009"
        }

        production_date_00aa = {
            "A": "2010", "B": "2011", "C": "2012", "D": "2013", "E": "2014", "F": "2015", "G": "2016",
            "H": "2017", "J": "2018", "K": "2019", "L": "2020", "M": "2021", "N": "2022", "P": "2023",
            "R": "2024", "S": "2025"
        }

        possible_production_date_dicts = {
            FerrariProductionDateVariables.FERRARI_AA00: production_date_aa00,
            FerrariProductionDateVariables.FERRARI_00AA: production_date_00aa,
            }
        return possible_production_date_dicts

    @staticmethod
    def _get_assembly_plant_dictionary():
        default_assembly_plant_dictionary = {
            "0":    AssemblyPlantsItaly.FERRARI_MARANELLO,
        }

        possible_assembly_plant_dicts = {
            FerrariAssemblyPlants.FERRARI_DEFAULT:    default_assembly_plant_dictionary
        }
        return possible_assembly_plant_dicts

    @staticmethod
    def _get_engine_dictionary():
        engine_cycle_1 = {
            'A': FerrariEngines.FERRARI_F106B040,
            'B': FerrariEngines.FERRARI_F106A021,
            # Note: Removed others for portfolio
        }

        engine_cycle_2 = {
            'A': FerrariEngines.FERRARI_F113B,
            'B': FerrariEngines.FERRARI_F117,
            # Note: Removed others for portfolio
        }

        engine_cycle_3 = {
            'A': FerrariEngines.FERRARI_F133F,
            'B': FerrariEngines.FERRARI_F133E,
            # Note: Removed others for portfolio
        }

        engine_cycle_4 = {
            "A": FerrariEngines.FERRARI_F154CB,
            "B": FerrariEngines.FERRARI_F140FG,
            # Note: Removed others for portfolio
        }

        possible_engine_dicts = {
            FerrariEngineVariables.FERRARI_ENGINE_CYCLE_1:      engine_cycle_1,
            FerrariEngineVariables.FERRARI_ENGINE_CYCLE_2:      engine_cycle_2,
            FerrariEngineVariables.FERRARI_ENGINE_CYCLE_3:      engine_cycle_3,
            FerrariEngineVariables.FERRARI_ENGINE_CYCLE_4:      engine_cycle_4,
        }
        return possible_engine_dicts

    def _get_model_dictionary(self):
        if self.vin[3:5].isnumeric():
            # 00AA Format
            model_dict = {
                "01": Ferrari296,           # ZFF 01 SMA9P0293307
                "02": FerrariPortofino,     # ZFF 02 RPA1P0292184
                "03": Ferrari812,           # ZFF 03 TMB000284643
                # Note: Removed others for portfolio
            }
        else:
            # AA00 Format
            model_dict = {
                "01": Ferrari308,           # ZFFAA 01 A3A0033487
                "02": Ferrari308,           # ZFFAA 02 A9C0038887
                # Note: Removed others for portfolio
            }
        return model_dict