# phrase_repeater
# by brussels_sprout


def main():
    input_()


def input_():
    phrase = input("Input phrase to repeat: ")
    length = input("Input output string length: ")
    if length.isdigit():
        length = int(length)
        if length != 0:
            pass
        else:
            print("Please input a positive integer for the length.")
            input_()
    else:
        print("Please input a positive integer for the length.")
        input_()
    return phrase, length


main()
