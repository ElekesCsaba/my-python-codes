import random

min_number = 1
max_number = 10
max_tries = 3
try_nums = []

magic_number = random.randint(min_number, max_number)

print("="*50, "MAGIC NUMBER", "="*50)
print(f"Find out my number between {min_number} and {max_number}.")
print(f"You have {max_tries} tries.")

user_guess = input("Your guess: ")

try_nums.append(user_guess)

while user_guess != str(magic_number):
    max_tries -= 1

    if max_tries == 0:
        print("Sorry. No more tries.")
        break

    print(f"Wrong answer. Nr of trie(s) left: {max_tries}.")
    user_guess = input("Your guess: ")
    try_nums.append(user_guess)

if user_guess == str(magic_number):
    print("You won.")
else:
    print("Game over.")

print(f"My number was {magic_number}.")

print("Your tries:")
for i, t in enumerate(try_nums):
    print(f"{i + 1}. {t}")
