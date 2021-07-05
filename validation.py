#function to check the number is in ta range of 0 to 255 or not
def validation(character):
    while character<0 or character >255:
        print("\n")
        print("Invalid input!!!" )
        print("The number that you have entered is out of range.")  
        character=int(input("Please Re-enter decimal number between the range 0 to 255:"))
    return character
