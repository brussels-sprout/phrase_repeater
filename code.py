# phrase_repeater
# by brussels_sprout


def main():
    title()
    phrase, length = input_()
    actual_length, num_phrase_in_length = actual_length_fun(phrase, length)
    string = operation(phrase, num_phrase_in_length)
    print(f"\nResultant string:\n{string}\nResultant string length: {actual_length}")
    end()


def title():
    print("\033[1m" + "String repeater" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def input_():
    phrase = input("Input phrase to repeat: ")
    length = input("Input resultant string length: ")
    if length.isdigit():
        length = int(length)
        if length != 0:
            pass
        else:
            print("Please input a positive integer for the length.\n")
            input_()
    else:
        print("Please input a positive integer for the length.\n")
        input_()
    return phrase, length


def actual_length_fun(phrase, length):
    phrase_length = len(phrase)
    num_phrase_in_length = (length + 1) // (phrase_length + 1)  # number of times phrase and a following space fits in length
    num_spaces = num_phrase_in_length - 1
    actual_length = num_phrase_in_length * phrase_length + num_spaces
    return actual_length, num_phrase_in_length


def operation(phrase, num_phrase_in_length):
    phrases = [phrase for _ in range(num_phrase_in_length)]
    string = " ".join(phrases)
    return string


def end():
    if input("\nInput any character(s) to run again or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()


main()
