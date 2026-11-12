
import csv
import os



class Table:
    def __init__(self, data):
        self.data = data

    def filter_items(self, condition):
        filtered_data = list(filter(condition, self.data))
        return Table(filtered_data)

    def aggregate(self, aggregation_key, aggregation_function):
        values = [
            float(item[aggregation_key])
            for item in self.data
        ]

        return aggregation_function(values)


    def __iter__(self):
        return iter(self.data)


    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_csv(self):
        location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )

        cities = []

        with open(
            os.path.join(location, self.filename),
            newline='',
            encoding='utf-8'
        ) as f:
            rows = csv.DictReader(f)

            for row in rows:
                cities.append(dict(row))

        return Table(cities)


loader = DataLoader('Cities.csv')
cities = loader.load_csv()


print("First 5 cities:")

for city in cities[:5]:
    print(city)

print()


print("The average temperature of all the cities:")

average_temperature = cities.aggregate(
    'temperature',
    lambda temps: sum(temps) / len(temps)
)

print(average_temperature)
print()



print("All cities in Germany:")

germany_cities = cities.filter_items(
    lambda city: city['country'] == 'Germany'
)

for city in germany_cities:
    print(city)

print()


print("Cities in Spain with temperature above 12°C:")

spain_cities = cities.filter_items(
    lambda city: city['country'] == 'Spain'
    and float(city['temperature']) > 12
)

for city in spain_cities:
    print(city)

print()


print("The number of unique countries:")

unique_countries = set(
    city['country'] for city in cities
)

print(len(unique_countries))
print()



print("The average temperature of cities in Germany:")

germany_average = germany_cities.aggregate(
    'temperature',
    lambda temps: sum(temps) / len(temps)
)

print(germany_average)
print()


print("The maximum temperature of cities in Italy:")

italy_cities = cities.filter_items(
    lambda city: city['country'] == 'Italy'
)

italy_max_temperature = italy_cities.aggregate(
    'temperature',
    lambda temps: max(temps)
)

print(italy_max_temperature)
