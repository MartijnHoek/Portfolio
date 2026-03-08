from CountryDefinitions.GeographicObjects import Country
from CountryDefinitions.Regions import Regions


class Countries:
    """ Class that houses the different defined Countries.
    The variables inside this class are used for the Player Objects to define nationality
    """
    # Europe
    ALBANIA =           Country("Albania", Regions.EUROPE, "962a8c65-8638-4ccc-b26e-fa5619306164")
    ARMENIA =           Country("Armenia", Regions.EUROPE, "fc0d430e-e265-4f9f-8f8c-e30db2f75eb5")
    AUSTRIA =           Country("Austria", Regions.EUROPE, "b2ee98fa-5dd4-460a-a64f-938273bd0e77")
    BELGIUM =           Country("Belgium", Regions.EUROPE, "3babc6f3-bde1-4ddc-a7e3-b8b0498750fd")
    BOSNIA_HERZEGOVINA= Country("Bosnia-Herzegovina", Regions.EUROPE, "fc65670c-e83c-40d8-a225-daf514e33af4")
    BULGARIA =          Country("Bulgaria", Regions.EUROPE, "66dbe0be-98a1-4d3a-bd90-1870fd8fb4e8")
    CROATIA =           Country("Croatia", Regions.EUROPE, "e7d6713d-2a2a-427c-8fef-23f69d08e222")
    CZECH_REPUBLIC =    Country("Czech Republic", Regions.EUROPE, "7467f411-c872-44f4-8114-5e3a9ce0a422")
    DENMARK =           Country("Denmark", Regions.EUROPE, "9f9aeda6-9310-4274-8d66-0371f76c31c8")
    ENGLAND =           Country("England", Regions.EUROPE, "d320a4c3-c292-40fe-9bc7-f842a969cfea")
    ESTONIA =           Country("Estonia", Regions.EUROPE, "e76e0494-7fd9-4551-83c1-5801cceadf27")
    FINLAND =           Country("Finland", Regions.EUROPE, "7cd95feb-be12-4639-bbff-34932ad5e755")
    FRANCE =            Country("France", Regions.EUROPE, "aa02d251-59e9-4938-b686-a78186340d28")
    GERMANY =           Country("Germany", Regions.EUROPE, "13d22354-ff0e-40ff-b17a-1a66a3d002c8")
    GREECE =            Country("Greece", Regions.EUROPE, "a9a3de01-7411-490c-9684-72a9c3459b56")
    HUNGARY =           Country("Hungary", Regions.EUROPE, "d9430fab-f473-4898-9856-8e7b4a5e5621")
    ICELAND =           Country("Iceland", Regions.EUROPE, "9dc6462a-f4e1-4108-933a-4d1d494dff61")
    IRELAND =           Country("Ireland", Regions.EUROPE, "47c08da0-89de-449b-914c-762c934f4f13")
    ITALY =             Country("Italy", Regions.EUROPE, "c9329fb8-6473-4b98-99a9-8eeac26f7ec7")
    KOSOVO =            Country("Kosovo", Regions.EUROPE, "44421a9c-5ae4-4e74-ac47-3db48bdb28c0")
    LITHUANIA =         Country("Lithuania", Regions.EUROPE, "b4976fa7-36f3-4d57-a59c-cc0d59e4f7d2")
    LUXEMBOURG =        Country("Luxembourg", Regions.EUROPE, "773a9c83-1ead-406d-9885-767621989338")
    MONTENEGRO =        Country("Montenegro", Regions.EUROPE, "8fe0a8ff-8904-4648-95be-ba391c17d544")
    NETHERLANDS =       Country("Netherlands", Regions.EUROPE, "23bc8dc7-5eb9-444e-8583-55fea484d8b0")
    NORTHERN_IRELAND =  Country("Northern Ireland", Regions.EUROPE, "b28931c7-5dc7-4e2a-ad58-5cdc56de070f")
    NORWAY =            Country("Norway", Regions.EUROPE, "f20602e5-2b59-46ca-8567-022151d094c4")
    POLAND =            Country("Poland", Regions.EUROPE, "056644d1-8e6e-4e27-9cc0-93e2b99bd2e4")
    PORTUGAL =          Country("Portugal", Regions.EUROPE, "80c02bce-3dbd-4253-8bde-2b0a690ab741")
    ROMANIA =           Country("Romania", Regions.EUROPE, "730609b5-4601-4d0f-9b96-72a4e484f98f")
    RUSSIA =            Country("Russia", Regions.EUROPE, "b2fc4056-7060-468f-b9a9-4565bf9e5a09")
    SCOTLAND =          Country("Scotland", Regions.EUROPE, "c54b4431-c67b-4a53-ae9c-e27d402cb269")
    SERBIA =            Country("Serbia", Regions.EUROPE, "2926a03b-05cd-4930-9a9f-d19d36e18e4a")
    SLOVAKIA =          Country("Slovakia", Regions.EUROPE, "2ef713cc-0cbc-47df-9f9e-677f9a5c2f2a")
    SLOVENIA =          Country("Slovenia", Regions.EUROPE, "d033dc04-a51f-4220-a35e-3cd91e120665")
    SPAIN =             Country("Spain", Regions.EUROPE, "0af58981-b7f4-405e-b6b1-a9b543533953")
    SWEDEN =            Country("Sweden", Regions.EUROPE, "0f2a8ce0-cb35-42e6-a5cf-2928f188dee5")
    SWITZERLAND =       Country("Switzerland", Regions.EUROPE, "8e0ca660-665f-4f34-9ec4-1438cb952faf")
    TURKEY =            Country("Turkey", Regions.EUROPE, "b198df34-4c65-40a9-929f-14c55bf62eb2")
    UKRAINE =           Country("Ukraine", Regions.EUROPE, "bd666a04-2736-4826-b562-6e4cca8a62c5")
    WALES =             Country("Wales", Regions.EUROPE, "e15eed4a-b7dd-4633-ab4f-01b30dcfa706")

    # North America
    CANADA =            Country("Canada", Regions.NORTH_AMERICA, "a9764a2f-0f72-416d-81f4-bb962568faaf")
    COSTA_RICA =        Country("Costa Rica", Regions.NORTH_AMERICA, "7e87c7b1-d80a-4e94-a854-50d0af2a143e")
    MEXICO =            Country("Mexico", Regions.NORTH_AMERICA, "eeb43609-a477-49f5-bf6e-de62a8f7ff4f")
    UNITED_STATES =     Country("United States", Regions.NORTH_AMERICA, "d0281762-ad40-4614-9127-0fd402585042")
    US_VIRGIN_ISLANDS = Country("US Virgin Islands", Regions.NORTH_AMERICA, "71decd50-99af-46e2-84b8-5a5a17a16859")

    # South America
    ARGENTINA =         Country("Argentina", Regions.SOUTH_AMERICA, "ec1bd7f9-453e-4693-a2d1-db9a8b07fa7c")
    BOLIVIA =           Country("Bolivia", Regions.SOUTH_AMERICA, "65acf52b-d871-442a-897d-3ecb18d6c148")
    BRAZIL =            Country("Brazil", Regions.SOUTH_AMERICA, "12f26104-9ff3-488f-8262-75b59f8a0520")
    CHILE =             Country("Chile", Regions.SOUTH_AMERICA, "bd08a6f4-07a2-4815-901a-59d1d9d94c29")
    COLOMBIA =          Country("Colombia", Regions.SOUTH_AMERICA, "ee97af8e-e9d4-4c9c-b54f-4d636841b922")
    PARAGUAY =          Country("Paraguay", Regions.SOUTH_AMERICA, "14561674-80a9-4ada-9dbb-8dd16d59b7d3")
    VENEZUELA =         Country("Venezuela", Regions.SOUTH_AMERICA, "d1a22824-a4b3-4033-8a57-32f25b7b5f00")
    URUGUAY =           Country("Uruguay", Regions.SOUTH_AMERICA, "e7ae386f-2118-4ffb-9ff1-94e0c5cb0821")

    # Africa
    ALGERIA =           Country("Algeria", Regions.AFRICA, "8f19938e-3c84-490a-bf65-a8f4552140fa")
    ANGOLA =            Country("Angola", Regions.AFRICA, "7d95e930-616e-431d-aac3-eaf36f9de6ae")
    BENIN =             Country("Benin", Regions.AFRICA, "7fdc045d-b6f5-4bae-8c4e-b92eedb99f7d")
    CAMEROON =          Country("Cameroon", Regions.AFRICA, "e41d6416-62b7-424b-831f-549976bff477")
    EGYPT =             Country("Egypt", Regions.AFRICA, "47ac1d5f-af8c-4cd7-be05-130fbfddd5ae")
    GABON =             Country("Gabon", Regions.AFRICA, "2675ba24-2b07-4a67-ab9e-1df101dd317a")
    GHANA =             Country("Ghana", Regions.AFRICA, "c5322868-6776-493c-91bf-3f4c747d7360")
    IVORY_COAST =       Country("Ivory Coast", Regions.AFRICA, "1623da91-ceba-488d-b6ba-32beaff3226c")
    MOROCCO =           Country("Morocco", Regions.AFRICA, "33285c35-1a3d-4a91-974e-13305a1e7223")
    NIGERIA =           Country("Nigeria", Regions.AFRICA, "b6e965a3-82aa-450f-b326-4546f87a1bb8")
    SENEGAL =           Country("Senegal", Regions.AFRICA, "956b8c8e-5e95-44ef-8947-2e1c61e1b842")
    SOUTH_AFRICA =      Country("South Africa", Regions.AFRICA, "c08e5165-21d3-4964-a9f5-4c327298ea8d")

    # Asia
    CHINA =             Country("China", Regions.ASIA, "469e3700-f090-428a-8246-114a5c7cc9f7")
    JAPAN =             Country("Japan", Regions.ASIA, "ec7fed55-d70b-49b9-b0f7-302300140def")
    SAUDI_ARABIA =      Country("Saudi Arabia", Regions.ASIA, "59245803-6b44-4308-a994-46324595d4f0")
    SOUTH_KOREA =       Country("South Korea", Regions.ASIA, "a738065a-6ebb-442d-9838-2a8a81d73f9b")

    # Oceania
    AUSTRALIA =         Country("Australia", Regions.OCEANIA, "e4fa45c6-6f2c-4728-9340-0c2a2ff88194")
    NEW_ZEALAND =       Country("New Zealand", Regions.OCEANIA, "0fee1651-6b88-4bc4-8a0d-96472933c1a7")