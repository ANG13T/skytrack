class Airport:
    def __init__(self,
                 ident = None,
                 type = None,
                 name = None,
                 elevation_ft = None,
                 continent = None,
                 iso_country = None,
                 iso_region = None,
                 municipality = None,
                 gps_code = None,
                 iata_code = None,
                 local_code = None,
                 coordinates = None,):
        self.ident = ident
        self.type = type
        self.name = name
        self.elevation_ft = elevation_ft
        self.continent = continent
        self.iso_country = iso_country
        self.iso_region = iso_region
        self.municipality = municipality
        self.gps_code = gps_code
        self.iata_code = iata_code
        self.local_code = local_code
        self.coordinates = coordinates