from VinDecoder.ManufacturerSpecific.VinDecoders.FerrariDecoder import FerrariDecoder
from VinDecoder.ManufacturerSpecific.VinDecoders.KiaDecoder import KiaDecoder
from VinDecoder.ManufacturerSpecific.VinDecoders.MitsubishiDecoder import MitsubishiDecoder
from VinDecoder.ManufacturerSpecific.VinDecoders.ZeekrDecoder import ZeekrDecoder

def get_defined_vin_decoders():
    """
    Funtion handling all the defined VIN decoders
    :return: List containing all the defined VIN decoders
    """
    vin_decoders = [
        FerrariDecoder,
        KiaDecoder,
        MitsubishiDecoder,
        ZeekrDecoder
    ]

    return vin_decoders