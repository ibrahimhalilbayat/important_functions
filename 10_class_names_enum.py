from enum import Enum

class MiddleEarthNation(Enum):
    elf = 0
    man = 1
    dwarf = 2
    orc = 3
    goblin = 4
    urukhai = 5

# An example of enum conveting 

example_class = 'goblin'

enum_converted_example_class = MiddleEarthNation[example_class]

print(f"""Example class of nation: {example_class} 
Enum converted version: {enum_converted_example_class} 
Value of converted version: {MiddleEarthNation(enum_converted_example_class).value}""")

# An example of list received by the sensors
example_list = ['goblin', 'dwarf', 'orc', 'urukhai', 'elf', 'elf', 'man', 'man']

enum_convered_list = []
enum_converted_value_list = []
string_converted_list = []
value_converted_list = []

for nation in example_list:
    enum_converted_nation = MiddleEarthNation[nation]
    enum_convered_list.append(enum_converted_nation)
    enum_converted_value_list.append(MiddleEarthNation(enum_converted_nation).value)

print(f"""
Enum Converted List: {enum_convered_list}
Enum Convrted Value List: {enum_converted_value_list}
""")

for enum_nation in enum_convered_list:
    string_converted_nation = MiddleEarthNation(enum_nation).name
    string_converted_list.append(string_converted_nation)

print(f"""
String Converted (received) List: {string_converted_list}
""")
    

for enum_value in enum_converted_value_list:
    converted_enum_value = MiddleEarthNation(enum_value).name
    value_converted_list.append(converted_enum_value)

print(f"""
From Value Converted List: {value_converted_list}
""")
