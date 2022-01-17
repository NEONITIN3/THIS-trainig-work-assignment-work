from enum import Enum

class Country(Enum):


        # Enum is a predefined clas
        Iceland = 354
        India =91
        Indonesia = 62
        Iran =98
        Iraq =964
        Ireland =353

print('Member value: {}'.format(Country.India.value))

print()
for data in Country:
    print('{:15} = {}'.format(data.name, data.value))