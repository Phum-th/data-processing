
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

cities = []

with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


for city in cities[:5]:
    print(city)

print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps) / len(temps))
print()


print("All cities in Germany:")
germany = [city for city in cities if city['country'] == 'Germany']

for city in germany:
    print(city)
print()

print("Cities in Spain with temperature above 12°C:")
spain = [
    city for city in cities
    if city['country'] == 'Spain'
    and float(city['temperature']) > 12
]

for city in spain:
    print(city)
print()


print("Number of unique countries:")
countries = set(city['country'] for city in cities)
print(len(countries))
print()


print("The average temperature for all the cities in Germany:")
germany_temps = [
    float(city['temperature']) for city in germany
]
print(sum(germany_temps) / len(germany_temps))
print()


print("The max temperature for all the cities in Italy:")
italy_temps = [
    float(city['temperature'])
    for city in cities
    if city['country'] == 'Italy'
]
print(max(italy_temps))
