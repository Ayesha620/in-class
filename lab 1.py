def reverse_string(user_input):
    return user_input[::-1]

def remove_spaces(user_input):
    # defining a function so it can be called later
    return user_input.replace(" ",'')
#the return value is then assigned to the result variable and printed as an output.

def count_consonants_vowels(user_input):
    vowels = 0
    consonants = 0
    for char in user_input:
        if char.lower() in 'aeiou':
            vowels += 1
        elif char.isalpha():
            # isalpha return true if all the character in the string is alphabatic.
            consonants += 1

    return(vowels, consonants)

while True :
    # using while loop to create a menu
    print("1. reverse-string")
    print("2. remove_spaces")
    print("3. counting_vowels_consonants")
    print(" enter quit to exit")
    choice = input(" enter your choice:")
    if choice == "1":
        user_input = input(" enter a string:")
        print(reverse_string(user_input))
        # calling the first function.
    elif choice == "2":
        user_input = input(" enter a string:")
        print(remove_spaces(user_input))
    elif choice == "3":
        user_input = input("enter a string:")
        print(count_consonants_vowels(user_input))
    elif choice == "quit":

         print("thanks for  using this program")
         break
         # to exit the while loop use break.
    else:
        print("invalid choice")
        print(" try again")













