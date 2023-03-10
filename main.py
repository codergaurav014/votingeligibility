# Ask the user if they have a voter ID card
has_voter_id = input("Do you have a voter ID card? (yes/no) ")

# Convert the user's answer to a lowercase string
has_voter_id = has_voter_id.lower()

# Use a try-except block to catch any errors that occur when the user inputs their age
try:
    # Ask the user for their age
    user_age = int(input("Enter your age: "))
except ValueError:
    # If the user inputs an invalid age, print an error message and exit the program
    print("Error: please enter a valid age.")
    exit()

# Check if the user is 18 or older and has a voter ID card
if has_voter_id == "yes" and user_age >= 18:
    print("You are an adult and can vote.")

# Check if the user is between 4 and 17 years old
elif 3 < user_age < 18:
    print("You are in school.")

# Check if the user is 0 to 3 years old
elif user_age <= 3:
    print("You are too young to vote.")

# If the user doesn't have a voter ID card and is 18 or older, print a message telling them to get one
elif has_voter_id == "no" and user_age >= 18:
    print(
        "Voter ID card is important to vote. You have to get a voter ID card.")

# If none of the above conditions are met, the user is not able to vote
else:
    print("You are not able to vote.")
