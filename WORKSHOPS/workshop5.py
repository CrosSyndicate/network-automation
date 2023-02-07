import random

def guess_random_number(tries, start, stop):
    num = random.randint(start, stop)
    while tries != 0:
        print("Tries remaining:", tries)
        guess = input(f"\nGuess a number between {start} and {stop}:")
        if int(guess) > num:
            print("Guess lower!")
            tries -= 1
        elif int(guess) < num:
            print("Guess higher!")
            tries -= 1
        else:
            print("Congratulations! You guessed correctly!")
            return
    print("You have run out of tries! Sorry!")
    return

def guess_random_num_linear(tries, start, stop):
    num = random.randint(start, stop)
    print(f"The number for the program to guess is: {num}")
    for x in range(start, stop):
        guess = int(x)
        while tries != 0:
            print(f"Tries remaining: {tries}")
            print(f"The computer is guessing... {guess}")
            if guess < num:
                guess += 1
                tries -= 1
            else:
                print("The computer has guessed correctly!")
                return
    print("The program has failed to guess the correct number!")
    return

def guess_random_num_binary(tries, start, stop):
    num = random.randint(start, stop)
    the_list = range(start, stop)
    print(f"The number to find: {num}")
    lower_bound = 0
    upper_bound = stop - 1

    while lower_bound <= upper_bound and tries != 0:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]
        
        if pivot_value == num:
            print(f"Found it! {pivot}")
            return pivot
        if pivot_value > num:
            print("Guessing lower!")
            upper_bound = pivot - 1
            tries -= 1
        else:
            print("Guessing higher!")
            lower_bound = pivot + 1
            tries -= 1
    print("The program has failed to guess the correct number!")
    return


#""" TEST TASK 1 DRIVER CODE"""

# guess_random_number(5, 0, 10)

#""" TEST TASK 2 DRIVER CODE"""

# guess_random_num_linear(5, 0, 10)

#""" TEST TASK 3 DRIVER CODE"""

# guess_random_num_binary(6, 0, 100)


#"""CODE GRAVE YARD"""

#""" TASK 2"""

    # for i in range(start, stop):
    #     guess = 0
    #     while tries != 0:
    #         print(f"The program is guessing!.....{guess}")
    #         if guess > num:
    #             guess += 1
    #             tries -= 1
    #             i -= 1
    #             return
    #         else:
    #             print("The computer guessed correctly!")
    #     print("The compute has failed to guess correctly.")