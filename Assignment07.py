# ------------------------------------------------- #
# Title: Assignment 07
# Description: A  program that pickles data into a binary file, with error handling.
# ChangeLog: <2020-08-04>, added error handling
# <DanielB>,<2020-08-04>,Created Script
# ------------------------------------------------- #
import pickle   # This imports code from another code file!

try:
    print("This program is a log of the drinks you consumed and the number of each drink.")
    name_of_drink = str(input("Please enter a type of drink you consumed: "))
    if name_of_drink.isnumeric():
        raise Exception("Please do not use numbers as a drink name.")
    number_of_drinks = int(input("Please enter the number of cups of " + name_of_drink + " that you consumed."))
    if number_of_drinks > 50:
        raise Exception("Are you made of liquid? Enter a reasonable number (under 50).")
    list_of_drinks = [name_of_drink, number_of_drinks]

    # Now we store the data with the pickle.dump method
    objFile = open("AppData.dat", "ab+")
    pickle.dump(list_of_drinks, objFile)
    objFile.close()

    # And, we read the data back with the pickle.load method
    objFile = open("AppData.dat", "rb")
    print("This is your complete log of drinks:")
    while True:
        try:
            objFileData = pickle.load(objFile) #load() only loads one row of data.
            print(objFileData)
        except EOFError:
            objFile.close()
            break

# Exception handling.
except ValueError as e:
    print("Error: You entered an incorrect value.")
    print("Please enter a numerical value for the number of drinks you had today.")
    print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
    print("Error: The AppData.dat file was not found.")
    print("Please create AppData.dat before continuing.")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was an error. Additional error info:")
    print(e, e.__doc__, type(e), sep='\n')
