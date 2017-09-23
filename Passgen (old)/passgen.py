__author__ = 'Sander'

"""
Importing the required library's:

string for the character lists (used in: password_generator)

os to check or the file/path exists (used in: multi_password)

errno to help with error handling with the making sure the directory exists (used in: multi_password)

random to get random numbers from character lists provided by the string library (used in: password_generator)

datetime just to look cool and see how long it takes to generate a password or write them to a file
(used in: password_generator, multi_password)
"""
import string
import os
import errno
from random import *
from datetime import datetime

"""
Generated passwords are stored into this array
Later to be converted into a string
So it can be written to the generated passwords file
"""
generated_passwords = []


def main():
    # Just keeping this method might add some more stuff to it
    # Currently only calls the pre_password method
    print("Launching password generator...")
    pre_password()


def pre_password():
    """
    pre_password()
    This method gets some basic info like:
    The requested password level
    The requested password length
    The requested amount of passwords to generate
    -
    The while True loop is to make sure the user enters a number smaller or equal to 3 and bigger then 0
    If the user does not fills in a number within that range the user will receive a message
    saying that they need to try again and choose one off the given numbers
    the exception "ValueError" occurs when the user enters a string/text instead off a number/int
    -
    if the user requests more then 1 password it continue's to the multi_password method
    else if the user requests only a single password it continue's to the generator
    with the required params
    """

    print("Password levels: ")
    print("Level 1: Simple letters")
    print("Level 2: Letters and numbers")
    print("Level 3: Letters, numbers and symbols")
    print("")

    while True:
        try:
            password_level = int(input("Password level: "))
            if 3 >= password_level > 0:
                break
            if password_level > 3:
                print("Please try again and enter one off these numbers: 1, 2, 3")
                pass
        except ValueError:
            print("Value error caught!")
            print("Please enter one off the given password levels (1, 2, 3)")

    print("")
    print("Password length recommended over 8 characters")

    password_length = int(input("Password length: "))

    print("")
    password_count = int(input("How many passwords?: "))

    if password_count > 1:
        multi_password(password_length, password_level, password_count)
    if password_count == 1:
        password_generator(password_length, password_level)


def multi_password(pass_length, pass_level, pass_count):
    """
    multi_password()
    :param pass_length:
    :param pass_level:
    :param pass_count:
    :return:
    -
    If the user requested more then 1 password in pre_password()
    multi_password creates a loop:
    While the requested password count is bigger then X
    it adds a password to the array defined at the imports (generated_passwords)
    and gives X + 1
    this repeats itself until the requested password count is no longer bigger then X
    after the loop it lists all the generated passwords
    -
    Within the first try statement it checks or the folder "Generated" exists
    if it does not exist it will be made
    if it does exist it will continue to the next statement
    -
    within the try statement it first checks or the file exists
    if it exists it asks or the user wishes to continue and overwrite the currently stored passwords in the file
    if the user says no the program closes
    if the user says yes it passes on into writing the new passwords to the file
    it also only writes 1 password each line
    -
    The part where it says: "\n".join(generated_passwords)
    is required to make a new line for each password
    it also converts the array (generated_passwords) into a string writeable to a file
    -
    the part where it says: file.close()
    should not be necessary but just incase something goes wrong it makes sure the file is closed
    """

    x = 0
    directory = "Generated"
    t4 = datetime.now()

    while pass_count > x:
        password_generator(pass_length, pass_level)
        x += 1

    print("")
    print("Generated passwords: ")
    print("\n".join(generated_passwords))

    t5 = datetime.now()
    t6 = t5 - t4

    print("")
    print("Please enter a filename to store your generated passwords in")
    filename = input("Filename: ")

    t1 = datetime.now()

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    dir_filename = directory + "\\" + filename

    try:
        if os.path.exists(dir_filename):
            print("This will override the currently stored passwords in the file:", dir_filename)
            print("Are you sure you wish to continue?")
            yes_no = input("Y/N? ").lower()
            if yes_no == "y":
                pass
            elif yes_no == "n":
                exit(0)

        with open(dir_filename, mode='w+', encoding='utf-8') as file:
            file.write("\n".join(generated_passwords))
            file.close()

    except IOError:
        print("Caught IOError")
        print("Passwords could not be written to the file")

    t2 = datetime.now()
    t3 = t2 - t1
    t3 += t6

    print("Passwords written to file")
    print("File name:", dir_filename)
    print("Time:", t3)


def password_generator(pass_length, pass_level):
    """
    password_generator()
    :param pass_length:
    :param pass_level:
    :return:
    -
    Variables:
    letters: contains all the possible ascii letters lower and capitalized (abcABC)
    numbers: contains all the possible numbers (0123456789)
    punctations: contains all the possible symbols ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    password: is an empty string used later to store the generated password in
    -
    depending on the requested password level it will go trough the if statements
    if the requested level is 1 it will execute the code within the if pass_level == 1
    which will generate a password existing only out of ascii letters
    the while loop is to get the password the requested length
    it keeps repeating itself until X is no longer smaller then pass_length
    after it generated the password it adds it to the generated_passwords array
    that array is used for writing the passwords to a file if the user requested multiple passwords
    -
    The password levels are:
    Level 1: the ascii letters
    Level 2: the ascii letters and numbers
    Level 3: the ascii letters, numbers and punctuations
    """

    letters = string.ascii_letters
    numbers = string.digits
    punctations = string.punctuation

    password = ""
    t1 = datetime.now()

    if pass_level == 1:
        x = 0
        z = len(letters) - 1
        while pass_length > x:
            y = randint(0, z)
            password += letters[y]
            x += 1

    elif pass_level == 2:
        x = 0
        letters_and_numbers = letters + numbers
        z = len(letters_and_numbers) - 1
        while pass_length > x:
            y = randint(0, z)
            password += letters_and_numbers[y]
            x += 1

    elif pass_level == 3:
        x = 0
        all3 = letters + numbers + punctations
        z = len(all3) - 1
        while pass_length > x:
            y = randint(0, z)
            password += all3[y]
            x += 1

    else:
        print("Something went wrong returning to main menu")
        main()

    t2 = datetime.now()
    t3 = t2 - t1

    generated_passwords.append(password)

    print("")
    print("Generated password:", password)
    print("")
    print("Password size:", len(password))
    print("Password level:", pass_level)
    print("Total time:", t3)

    input("Press any key to close...")


if __name__ == '__main__':
    main()
