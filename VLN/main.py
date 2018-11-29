from ui.SalesmanUI import SalesmanUI
import time


def pixelArt():
    art = open('pixelart.txt', 'r')

    for line in art:
        line = line[0:-1]
        print(line)
        time.sleep(0.050)


def assemblePassword():
    H1 = chr(97)
    H2 = chr(100)
    H3 = chr(109)
    H4 = chr(105)
    H5 = chr(110)
    thepass = str(H1 + H2 + H3 + H4 + H5)
    return thepass


def main():
    THEPASS = assemblePassword()
    invalidCount = 0
    correctPass = False
    while correctPass == False:
        enteredPassword = input("Enter very well encoded password: ")
        if enteredPassword == THEPASS:
            correctPass = True
        else:
            invalidCount += 1
            if invalidCount == 3:
                print(
                    "Since you have tried so hard we will reward you by printing out the password..")
                print("admin")
            else:
                print("Invalid password!")

    if correctPass == True:
        # pixelArt()
        ui = SalesmanUI()
        ui.main_menu()


main()
