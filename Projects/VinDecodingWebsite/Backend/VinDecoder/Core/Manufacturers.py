from dataclasses import dataclass


@dataclass
class ManufacturerObject:
    name:   str
    uuid:   str

class Manufacturers:
    FERRARI =       ManufacturerObject("Ferrari", "52de1ce7-813b-48dc-8a2f-c561effa7fe2")
    KIA =           ManufacturerObject("Kia", "12e38086-1a68-44b1-b0b7-4c3883e06ca8")
    MITSUBISHI =    ManufacturerObject("Mitsubishi", "c7ea1379-10c5-426b-8a43-b24dc1c8cb38")
    ZEEKR =         ManufacturerObject("Zeekr", "4cdc5cfc-963b-4f1f-8436-6fb657856236")