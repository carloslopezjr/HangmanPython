# GLOBAL VARIABLES #


# FUNCTIONS #
def start():

    # we need a user to give the mystery word
    global hangmanPrompt
    hangmanPrompt = input("Enter the hangman word: ")
    print("")

    # when we have the mystery word, we need to mask it with underlines
    lenPrompt = len(hangmanPrompt)  # this gets the total length of the word

    x = 0  # acts as a counter
    global hiddenList
    hiddenList = []  # this is where the list of underscores will go

    while x <= lenPrompt - 1:  # runs through the length of lenPrompt minus 1
        # each loop, it adds a underscore to the hiddenList
        hiddenList.append("_")
        x += 1  # adds to the counter, stops when x is greater than lenPrompt - 1

    # takes the hiddenList and joins them together
    global hiddenString
    hiddenString = " ".join(hiddenList)


def prompt():
    # prompt that showcases the size of the hidden word
    print(f"Guess a letter: {hiddenString}\n")


def selection():

    letter = input("Enter letter: ")  # enter the guess letter
    print(" ")

    count = 0
    for x in hangmanPrompt:  # find a new way to see if a letter is in a word more than 1 times

        if x == letter:
            count += 1

    if count > 1:

        # make copy of hangmanPrompt
        hangmanPromptCopy = []  # new list that acts as an copy to mutate

        for x in hangmanPrompt:  # loops through letters and adds them in list
            hangmanPromptCopy.append(x)

        increment = 0

        while count > 0:

            # get first index of letter that is > 1 indexes
            index = hangmanPromptCopy.index(letter)

            # update _ list
            hiddenList[index + increment] = letter

            # remove first index from hangmanPrompt
            hangmanPromptCopy.pop(index)

            increment += 1
            count -= 1

        print(" ".join(hiddenList))
        print(" ")

        # if there's more letters, keep it going till no more letters

    elif letter in hangmanPrompt:  # if letter is in the word the user gave

        # gets index of letter from original word
        index = hangmanPrompt.index(letter)

        # uses the hiddenlist (underscores) and updates it with the letter
        hiddenList[index] = letter

        print(" ".join(hiddenList))  # joins the new hidden list
        print(" ")

    else:
        print(f"Letter is not in the word.")


start()


prompt()

num = 0  # acts as a value that will keep the while loop running until changed
while num == 0:  # loop will run as long as num == 0

    selection()

    if "_" not in hiddenList:
        print("You guessed the word!")
        print("")

        num = 1


# Next Updates

    # Add lives:
        # give 6 lives to the player

    # Add different modes: Unlimited - Classic

        # Unlimited: The player gets unlimited tries to guess the word

        # Classic: The player only gets 6 tries

    # Add word display even when they guess a letter wrong
