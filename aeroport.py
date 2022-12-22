class Airport:
    def __init__(self, name, code, lat, long):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

    def __new__(cls, name, code):
        airport = super().__new__(cls)

        airport.name = name
        airport.last_name = code

        airport.full_name = f'{name} {code}'
        return airport