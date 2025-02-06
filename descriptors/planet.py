from positive_descriptor import PositiveDescriptor


class Planet:
    def __init__(self, name, radius_meters, mass_kilograms, orbital_period_seconds, surface_temprature_kelvin):
        self.name = name
        self.radius_meters = radius_meters
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temprature_kelvin = surface_temprature_kelvin

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Cannot set empty name')
        self._name = value

    radius_meters = PositiveDescriptor()
    mass_kilograms = PositiveDescriptor()
    orbital_period_seconds = PositiveDescriptor()
    surface_temprature_kelvin = PositiveDescriptor()

def main():
    mercury = Planet('Mercury', radius_meters=2439.7e3, mass_kilograms=3.3022e24, orbital_period_seconds=7.60052e6, surface_temprature_kelvin=340)
    venus = Planet('Venus', radius_meters=6051.8e3, mass_kilograms=4.8676e24, orbital_period_seconds=1.94142e7, surface_temprature_kelvin=737)
    earth = Planet('Earth', radius_meters=6371.0e3, mass_kilograms=5.972e24, orbital_period_seconds=3.15581e7, surface_temprature_kelvin=288)
    mars = Planet('Mars', radius_meters=3389.5e3, mass_kilograms=6.4185e23, orbital_period_seconds=5.93543e7, surface_temprature_kelvin=210)

    return mercury, venus, earth, mars

if __name__ == '__main__':
    main()
