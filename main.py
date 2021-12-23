import art
import random

print(art.logo)
print("****************************  Welcome to guess the number game!  ****************************")
diff_lvl = input("\n-> Choose difficulty level! Type 'easy' or 'hard': ").lower()
random_num = random.randint(1, 100)

guess = 0
moves = 0

#executes only if player choses easy level
if diff_lvl == 'easy':
  moves = 10
  while guess != random_num and moves != 0:
    guess = int(input("\nType your guess here: "))
    if guess == random_num:
      print(f"\nWow! You guessed it correct! The random number is {random_num}")

    elif guess > random_num:
      print("\nToo high!")
      moves -= 1
      print(f"\nAttempts left {moves}")

    elif guess < random_num:
      print("\nToo low!")
      moves -= 1
      print(f"\nAttempts left {moves}")

    else:
      print("\nInvalid Input!")

    if moves == 0:
      print("\nOut of moves! You Lost!")


#executes only if player choses hard level
elif diff_lvl == 'hard':
  moves = 5
  while guess != random_num and moves != 0:
    guess = int(input("\nType your guess here: "))
    if guess == random_num:
      print(f"\nWow! You guessed it correct! The random number is {random_num}")

    elif guess > random_num:
      print("\nToo high!")
      moves -= 1
      print(f"\nAttempts left {moves}")

    
    elif guess < random_num:
      print("\nToo low!")
      moves -= 1
      print(f"\nAttempts left {moves}")

    
    else:
      print("\nInvalid Input!")

    if moves == 0:
      print("\nOut of moves! You Lost!")

else:
  print("\nInvalid Input!")