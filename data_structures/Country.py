from operator import attrgetter


class Country:
    def __init__(self, name, population, area):
        self.population = population
        self.name = name
        self.area = area

    def __repr__(self):
        return repr((self.name, self.area, self.population))


countries = [
    Country('India', 1200, 100),
    Country('China', 1400, 200),
    Country('USA', 120, 300)
]

countries.append(Country('Russia', 80, 900))

countries.sort(key=attrgetter('population'), reverse=True)
print(countries)

print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))
print(max(countries, key=attrgetter('area')))
print(min(countries, key=attrgetter('area')))

country_length = [ len(c.name) for c in countries ]
print(country_length)

country_length_3 = [ len(c.name) for c in countries if len(c.name) == 3]
print(country_length_3)