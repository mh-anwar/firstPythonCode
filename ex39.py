#create a mapping of states to abreviation
states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan':'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'* 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is: ", states["Florida]"])

#do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abreviation
print('-' * 10)
for state, abbrev in list(cities.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)

