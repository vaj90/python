# Task 1
# -Create a function that
#       -takes two arguments
#   -creates a tuple of the two arguments
import os


def task1(args1, args2):
    tup1 = (args1, args2);
    print(tup1)


task1('allan', 'john')


# Task 2
# -Write a function that
#   -takes 1 parameter
#       -returns the first character and the last character (one return, two values)
# -Call and output the function above with STRING argument
def task2(str):
    return str[0] + str[-1]


msg = 'Hello World';
print(task2(msg))

# Task 3
# -Create a dictionary of 3 items
# -GET one of the keys
# -Remove one of the keys
# -output all values of the dictionary
# -output all keys of the dictionary
# -output all key-value pairs of the dictionary
Dict = dict({'Name': 'Allan John Valiente', 'Course': 'T127', 'Year': 2})
name = Dict['Name']
Dict.pop('Year', None)
print('\n')
for d in Dict:
    print(Dict[d])

print('\n')
for d in Dict:
    print(d)

print('\n')
for d in Dict:
    print('key:', d, 'value:', Dict[d])

# Task 4
# Create a dictionary of Countries that begin with any 5 letters of the alphabet
# Each letter should have a minimum of 3 countries
countries = {
    'D': ['Denmark', 'Dominica', 'Dominican Republic'],
    'A': ['Angola', 'Albania', 'Argentina'],
    'C': ['Chile', 'China', 'Colombia'],
    'B': ['Bahamas', 'Bahrain', 'Bolivia'],
    'E': ['Ecuador', 'Egypt', 'Estonia']
}


class CountryManager:
    def display_menu(self):
        menu = 'Country Manager Menu:\n' \
               ' ----------------\n' \
               ' View ...... [ 1] \n' \
               ' Add ....... [ 2] \n' \
               ' Delete .... [ 3] \n' \
               ' Shuffle ... [ 4] \n' \
               ' Exit ...... [ 5]'
        return menu

    def view(self, cParam):
        cParam = cParam.upper()
        output = ''
        if cParam in countries:
            output += 'Country: ';
            output += ', '.join(countries[cParam])
        else:
            for i in countries:
                output += '\nCountry names start with letter \'' + i + '\': '
                output += ', '.join(countries[i])
        print(output)

    def add(self, countryInput) -> bool:
        countryInput = countryInput.title()
        if len(countryInput) >= 4:
            key = countryInput[0]
            if key in countries:
                if countryInput in countries[key]:
                    return False
                else:
                    countries[key].append(countryInput)
                    return True
        return False

    def delete(self, countryInput) -> bool:
        countryInput = countryInput.title()
        key = countryInput[0]
        if key in countries:
            if countryInput in countries[key]:
                countries[key].remove(countryInput)
                return True
        return False

    def shuffle(self):
        newDict = {}
        for i in sorted(countries):
            newDict[i] = countries[i]
        print(newDict)

    def start(self):
        menu = self.display_menu();
        choice = 0
        while choice != 5:
            print(menu);
            choice = input('Please make an option: ')
            if choice.isnumeric():
                choice = int(choice)
                if choice == 1:
                    print('-----------------------------------------')
                    chr = input('Please enter letter to display - [A - E]:')
                    self.view(chr)
                    input('Press enter key to continue\n\n')
                if choice == 2:
                    print('----------------------------------------------')
                    countryInput = input('Please enter a country start with letter [A-E]'
                                         '\n and must be a least 4 characters:')
                    isSuccess = self.add(countryInput)
                    print('Country', ('successfully' if isSuccess else 'unsuccessfully'), 'added')
                    input('Press enter key to continue\n\n')
                if choice == 3:
                    print('------------------------------------------')
                    countryInput = input('Please enter a country you want to delete:')
                    isSuccess = self.delete(countryInput)
                    print('Country', ('successfully' if isSuccess else 'unsuccessfully'), 'deleted')
                    input('Press enter key to continue\n\n')
                if choice == 4:
                    self.shuffle();
                    input('Press enter key to continue\n\n')
        print('---End of program---')

    def main(self):
        self.start()

cManager = CountryManager()
cManager.main();

