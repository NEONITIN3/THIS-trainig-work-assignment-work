# Class to sort Country name by Country Code and sorted code List
import enum

class Country(enum.IntEnum):
    Afghanistan = 93
    Antarctica = 672
    Andorra = 376
    Albania = 355
    Algeria = 213
    Angola = 244

print('Country Name ordered by Country Code:')
print('\n'.join(' ' + c.name for c in sorted(Country)))

print("Original Code List : ", list(map(int, Country)))
print("Sorted Code List : ", list(map(int, sorted(Country))))