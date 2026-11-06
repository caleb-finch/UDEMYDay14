from game_data import data
from art import *
import random

def main()
    #Define some needed variables for later
    isCorrect = True
    number_correct = 0
    #use a general random function to get 2 separate items (people)
    itemA = get_random_item()
    itemB = get_random_item()
    print(logo)
    #major while loop where we have set isCorrect so we can enter loop. Later we have a function that either keeps the isCorrect to True or change it to False
    while isCorrect:
        ##TESTING PRINTS SO I CAN GET IT RIGHT CAN BE DELETED
        # print(f"itemA: {itemA}")
        # print(f"itemB: {itemB}\n")
        #I wanted a general output so I'm not printing so much in main()
        compare_output(itemA, itemB)
        #As mentioned earlier this changes the isCorrect variable. This passes the follower accounts ONLY because that is all we need. So we're just passing 2 numbers into the function.
        isCorrect = compare(itemA["follower_count"], itemB["follower_count"])
        #okay now isCorrect MIGHT have changed. We need to see if user was correct based on above function
        if isCorrect:
            number_correct += 1
            correct_output()
            print(f"Current Streak: {number_correct}")
            itemA = itemB
            itemB = get_random_item()
        else:
            incorrect_output()

def incorrect_output():
    print(logo)
    print("Sorry that's wrong. ")


def correct_output():
    print(logo)
    print("That's correct!")

def compare_output(itemA, itemB):
    #print("\n" * 100)
    print(f"Compare A: {itemA["name"]}, {itemA['description']}, from {itemA['country']}")
    print(vs)
    print(f"Compare B: {itemB["name"]}, {itemB['description']}, from {itemB['country']}")


def get_random_item():
    return random.choice(data)

#this function is the meat and potatoes. We're passing 2 numbers and checking if user chose the correct account. If user thinks follower A's is larger then A should be greater than B. If user thinks follower B's is larger then B > A should be correct. if it isn't then return False!
def compare(followerA, followerB):
    user_choice = input("Who has more followers? Type ""A"" or ""B"": ")
    if user_choice == "A" and followerA > followerB:
        return True

    elif user_choice == "B" and followerB > followerA:
        return True

    else:
        return False

main()