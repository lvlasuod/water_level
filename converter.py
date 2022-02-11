
print("\n[===============| Unit Converter |===============]")
print("Press 'Q' to exit\n")

run = True

def convert():

    global run
    
    user_input = input("From what do you want to convert? ['C'/'F' | 'Q' to Exit]: ")
    
    if user_input == "q" or user_input == "Q":
        print("Goodbye, human.")
        run = False

    if user_input == 'C' or user_input == 'c':
        print ('To convert a temperature from Celsius to Fahrenheit:')
        cels = input('CELSIUS: ')
        to_fahrenheit(cels)

    elif user_input == 'F' or user_input == 'f':
        print ('To convert a temperature from Fahrenheit to Celsius:')
        fahr = input('FAHRENHEIT: ')
        to_celsius(fahr)


def to_fahrenheit(celsius):

    c = float(celsius)
    f = c * 9 / 5 + 32
    print ('%r Celsius, converted to Fahrenheit, is: %r Fahrenheit.' % (c, f))


def to_celsius(fahrenheit):

    f = float(fahrenheit)
    c = (f - 32) * 5 / 9
    print ('%r Fahrenheit, converted to Celsius, is: %r Celsius.' % (f, c))

while run:
    convert()
