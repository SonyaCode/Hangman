import random
import os
from termcolor import colored
import time

# pick a secret randomize word function
def pick_secret_word():
  words = []
  file = open("words.txt", "r")
  for word in file:
    words.append(word.rstrip())
  r = random.randint(0, len(words) - 1)
  file.close()
  random_word = words[r]
  return random_word.upper()

  
# pick a secret easy word function
def pick_easy_secret_word():
  words = []
  file = open("easy_words.txt", "r")
  for word in file:
    words.append(word.rstrip())
  r = random.randint(0, len(words) - 1)
  file.close()
  random_word = words[r]
  return random_word.upper()


# pick a secret medium word function
def pick_medium_secret_word():
  words = []
  file = open("medium_words.txt", "r")
  for word in file:
    words.append(word.rstrip())
  r = random.randint(0, len(words) - 1)
  file.close()
  random_word = words[r]
  return random_word.upper()


# pick a secret hard word function
def pick_hard_secret_word():
  words = []
  file = open("hard_words.txt", "r")
  for word in file:
    words.append(word.rstrip())
  r = random.randint(0, len(words) - 1)
  file.close()
  random_word = words[r]
  return random_word.upper()


# put each letter of a secret word in a list
def create_secret_word_list(word):
  secret_word_list = []
  for letter in word:
    secret_word_list.append(letter)
  return secret_word_list


# the blank spaces of the secret word
def create_guessed_letter_list(secret_word_list):
  guessed_list = []
  # append blank spaces with the same len as the word
  for i in range(len(secret_word_list)):
    guessed_list.append("__")
  return guessed_list


# print out the guessed letter
def print_guessed_letters(guessed_letters):
  for letter in guessed_letters:
    print(letter, end=" ") 
  print()
  

# check if a letter is in the secret word list
def check_letter(secret_word_list, letter):
  if letter in secret_word_list:
    return True
  else:
    return False

    
# reveal the guessed letter function
def update_guessed_letters(secret_word_list, guessed_letters, letter):
  indx = 0
  # runs through each element in the secret_word_list
  for each_letter in secret_word_list:
    if each_letter == letter: # if a letter is same as the guessed letter
      guessed_letters[indx] = each_letter # reveals the letter
    indx += 1
  return guessed_letters


# check if all of the letters are guessed
def is_word_guessed(guessed_letters):
  if "__" in guessed_letters:
    return False
  else:
    return True


def zero_wrong():
  print("   _______")
  print(" |/      |")
  print(" |      (_)")
  print(" |      \|/")
  print(" |       |")
  print(" |      / \ ")
  print(" |")
  print("_|___")


def one_wrong():
  print("   _______")
  print(" |/      |")
  print(" |      (_)")
  print(" |      \|")
  print(" |       |")
  print(" |      / \ ")
  print(" |")
  print("_|___")


def two_wrong():
  print("   _______")
  print(" |/      |")
  print(" |      (_)")
  print(" |       |")
  print(" |       |")
  print(" |      / \ ")
  print(" |")
  print("_|___")


def three_wrong():
  print("   _______")
  print(" |/      |")
  print(" |      (_)")
  print(" |       |")
  print(" |       |")
  print(" |      / ")
  print(" |")
  print("_|___")


def four_wrong():
  print("   _______")
  print(" |/      |")
  print(" |      (_)")
  print(" |       |")
  print(" |       |")
  print(" |        ")
  print(" |")
  print("_|___")


def five_wrong():
  print("   _______")
  print(" |/      |")
  print(" |      (_)")
  print(" |        ")
  print(" |        ")
  print(" |        ")
  print(" |")
  print("_|___")


def six_wrong():
  print("   _______")
  print(" |/      |")
  print(" |        ")
  print(" |        ")
  print(" |        ")
  print(" |        ")
  print(" |")
  print("_|___")


def happy():
  print(" o   o  ")
  print("   ^    ")
  print("\______/")


def happy_blink():
  print(" -   -  ")
  print("   ^    ")
  print("\______/")


def sad():
  print(" O   O  ")
  print("   ^    ")
  print("/-----\ ")


def sad_cry():
  print(" -   -  ")
  print(" o ^ o  ")
  print("/-----\ ")


# main program: test code
guesses = 6
wrong_guess = []

# menu
print("Welcome to Hangman!")
print()
print("   _______")
print(" |/      |")
print(" |      (_)")
print(" |      \|/")
print(" |       |")
print(" |      / \ ")
print(" |")
print("_|___")
print()


print("Difficulty level:")
print("[1] Easy: 3-letters words")
print("[2] Medium: 4 or 5 letters words")
print("[3] Hard: 6 or more letters words")
print("[4] Randomized: Random amount of letters words")
print()
menu = input("Select your difficulty: ")

if menu.lower() == "easy" or menu == "1":
  word = pick_easy_secret_word()
elif menu.lower() == "medium" or menu == "2":
  word = pick_medium_secret_word()
elif menu.lower() == "hard" or menu == "3":
  word = pick_hard_secret_word()
elif menu.lower() == "randimized" or menu == "4":
  word = pick_secret_word()
else:
  print("Please enter the correct difficulty level.")

secret_word_list = create_secret_word_list(word)
guessed_list = create_guessed_letter_list(secret_word_list)

# loop until it runs out of guess or guess the word
while guesses > 0 and is_word_guessed(guessed_list) == False:
  os.system("clear")

  # if guess wrong, remove part of the hangman 
  if guesses == 6:
    zero_wrong()
  elif guesses == 5:
    one_wrong()
  elif guesses == 4:
    two_wrong()
  elif guesses == 3:
    three_wrong()
  elif guesses == 2:
    four_wrong()
  elif guesses == 1:
    five_wrong()

  print()
  
  print(colored(guessed_list, "green"))
  print()
  print("Wrong guesses:", colored(wrong_guess, "red"))
  print()
  print("Guesses Remaining:", colored(guesses, "yellow"))
  letter = input("Enter a letter: ")
  letter = letter.upper()

  # check to see if the letter is in the word
  if check_letter(secret_word_list, letter) == True:
    guessed_letters = update_guessed_letters(secret_word_list, guessed_list, letter)
    print(colored(guessed_letters, "green"))
    print()
  elif letter in wrong_guess:
    guesses = guesses
  else:
    guesses -= 1
    wrong_guess.append(letter)
    print()
    


if guesses == 0: # losing screen
  os.system("clear")
  six_wrong()
  print()
  print(colored(guessed_list, "green"))
  print()
  print("Wrong guesses:", colored(wrong_guess, "red"))
  print()
  print("Guesses Remaining:", colored(guesses, "yellow"))
  print(colored("You lost!", "red"), "The secret word was", colored(word, "blue"))
  time.sleep(10)
  print()
  
  for i in range(10):
    sad()
    time.sleep(0.5)
    os.system("clear")
    sad_cry()
    time.sleep(0.5)
    os.system("clear")
    
else: # winning screen
  print(colored("You won!", "green"))
  time.sleep(10)
  print()
  
  for i in range(10):
    happy()
    time.sleep(0.5)
    os.system("clear")
    happy_blink()
    time.sleep(0.5)
    os.system("clear")

print("Thanks for playing!")