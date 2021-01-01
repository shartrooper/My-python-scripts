# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
>>> from collections import namedtuple
>>> Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
>>> my_car = Car('red', 3812.4)
>>> my_car.color
'red'
>>> my_car.mileage
3812.4

# We get a nice string repr for free:
>>> my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
>>> my_car.color = 'blue'
AttributeError: "can't set attribute"

subclassing.py

# Since namedtuples are classes. These can be added as subclasses

class Point(namedtuple('Point', 'x y')):

    __slots__ = ()

    @property
    def hypot(self):
        return sqrt((self.x ** 2 + self.y ** 2))

    def __str__(self):
        return f'Point: x={self.x}  y={self.y}  hypot={self.hypot}'


p = Point(5, 5)
print(p.hypot)
print(p)

#The defaults parameter can be used to provide default values to fields. 

class Point(namedtuple('Point', 'x y', defaults=[1, 1])):

    __slots__ = ()

    @property
    def hypot(self):
        return sqrt((self.x ** 2 + self.y ** 2))

    def __str__(self):
        return f'Point: x={self.x}  y={self.y}  hypot={self.hypot}'


p1 = Point(5, 5)
print(p1)

p2 = Point()
print(p2)

#Since Python 3.6, we can use the typing.NamedTuple to create a namedtuple. 

from typing import NamedTuple


class City(NamedTuple):
    name: str
    population: int


c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)

print(c1)
print(c2)

# Python provides several helper methods for a namedtuple. 

class Point(NamedTuple):

    x: int = 1
    y: int = 1


p = Point(5, 5)

print(p._fields)
print(p._field_defaults)
print(p._asdict())

'''
The _fields is a tuple of strings listing the field names. 
The _field_defaults is a dictionary mapping field names to default values. 
The _asdict method returns a new ordered dictionary, which maps field names to their corresponding values. 
'''

#output
'''
$ ./helpers.py 
('x', 'y')
{'x': 1, 'y': 1}
OrderedDict([('x', 5), ('y', 5)])
'''

#The _asdict() method can be used to serialize namedtuples into JSON format. 


class City(NamedTuple):
    name: str
    population: int


c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)
c3 = City('Prague', 1280000)
c4 = City('Warsaw', 1748000)

cities = [c1, c2, c3, c4]

print(json.dumps(c1._asdict()))

json_string = json.dumps([city._asdict() for city in cities])
print(json_string)
'''
{"name": "Bratislava", "population": 432000}
[{"name": "Bratislava", "population": 432000}, {"name": "Budapest", "population": 1759000}, 
{"name": "Prague", "population": 1280000}, {"name": "Warsaw", "population": 1748000}]
'''


#In the following example, we sort a list of namedtuples. 

class City(NamedTuple):
    id: int
    name: str
    population: int


c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Berlin', 3671000)

cities = [c1, c2, c3, c4, c5, c6, c7]

cities.sort(key=lambda e: e.name)

for city in cities:
    print(city)


'''
City(id=7, name='Berlin', population=3671000)
City(id=1, name='Bratislava', population=432000)
City(id=2, name='Budapest', population=1759000)
City(id=6, name='Edinburgh', population=464000)
City(id=5, name='Los Angeles', population=3971000)
City(id=3, name='Prague', population=1280000)
City(id=4, name='Warsaw', population=1748000)
'''

#Python namedtuples are helpful when we read CSV data. 

#cities.csv
'''
Bratislava, 432000
Budapest, 1759000
Prague, 1280000
Warsaw, 1748000
Los Angeles, 3971000
New York, 8550000
Edinburgh, 464000
Berlin, 3671000
'''

import csv

City = namedtuple('City' , 'name population')

f = open('cities.csv', 'r')

with f:

    reader = csv.reader(f)
    
    for city in map(City._make, reader):
        print(city)

# this is the output
'''
City(name='Bratislava', population=' 432000')
City(name='Budapest', population=' 1759000')
City(name='Prague', population=' 1280000')
City(name='Warsaw', population=' 1748000')
City(name='Los Angeles', population=' 3971000')
City(name='New York', population=' 8550000')
City(name='Edinburgh', population=' 464000')
City(name='Berlin', population=' 3671000')
'''

#In the following example, we use a namedtuple to read data from SQLite database. 

#cities.sql
'''
DROP TABLE IF EXISTS cities;
CREATE TABLE cities(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, 
  population INTEGER);

INSERT INTO cities(name, population) VALUES('Bratislava', 432000);
INSERT INTO cities(name, population) VALUES('Budapest', 1759000);
INSERT INTO cities(name, population) VALUES('Prague', 1280000);
INSERT INTO cities(name, population) VALUES('Warsaw', 1748000);
INSERT INTO cities(name, population) VALUES('Los Angeles', 3971000);
INSERT INTO cities(name, population) VALUES('New York', 8550000);
INSERT INTO cities(name, population) VALUES('Edinburgh', 464000);
INSERT INTO cities(name, population) VALUES('Berlin', 3671000);
'''

#These are SQL statements to create the cities table.
'''
    $ sqlite3 ydb.db
    SQLite version 3.31.1 2020-01-27 19:55:54
    Enter ".help" for usage hints.
    sqlite> .read cities.sql
'''

#With the sqlite3 command line tool, we generate the SQLite database and the cities table. 

import sqlite3 as sqlite


class City(NamedTuple):
    
    id: int
    name: str
    population: int


con = sqlite.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute('SELECT * FROM cities')
    
    for city in map(City._make, cur.fetchall()):
        print(city)       
#We read all data from the cities table and transform each table row into a City namedtuple. 