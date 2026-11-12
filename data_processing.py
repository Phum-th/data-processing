
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


def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries
    that satisfy the given condition.
    """
    return list(filter(condition, dict_list))


def aggregate(aggregation_key, aggregation_function, dict_list):
    
    values = [
        float(item[aggregation_key])
        if aggregation_key == "temperature"
        else item[aggregation_key]
        for item in dict_list
    ]

    return aggregation_function(values)



for city in cities[:5]:
    print(city)

print("The average temperature of all the cities:")
print(
    aggregate(
        "temperature",
        lambda x: sum(x) / len(x),
        cities
    )
)
print()


print("All cities in Germany:")
germany = filter_items(
    lambda city: city['country'] == 'Germany',
    cities
)

for city in germany:
    print(city)
print()


print("Cities in Spain with temperature above 12°C:")
spain = filter_items(
    lambda city: city['country'] == 'Spain'
    and float(city['temperature']) > 12,
    cities
)

for city in spain:
    print(city)
print()

print("Number of unique countries:")
countries = set(
    city['country'] for city in cities
)
print(len(countries))
print()


print("The average temperature for all the cities in Germany:")
print(
    aggregate(
        "temperature",
        lambda x: sum(x) / len(x),
        germany
    )
)
print()

print("The max temperature for all the cities in Italy:")
italy = filter_items(
    lambda city: city['country'] == 'Italy',
    cities
)

print(
    aggregate(
        "temperature",
        max,
        italy
    )
)
