# Exercise 0: Example
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

print("-------------------------------------------------------")

# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()  
    
    if len(letter) != 1 or not letter.isalpha():  
        print("Invalid input! Please enter a single letter.")
    elif letter in 'aeiou':  
        print(f"The letter {letter} is a vowel.")
    else:  
        print(f"The letter {letter} is a consonant.")

# Call the function
check_letter()


print("-------------------------------------------------------")

# Exercise 2: Old enough to vote?

def check_voting_eligibility():
        
    age = int(input("Please enter your age: "))  
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:  
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not old enough to vote.")

# Call the function
check_voting_eligibility()

print("-------------------------------------------------------")
# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    dog_age = int(input("Input a dog's age: "))
        
    if dog_age < 0:
        print("Age cannot be negative.")
    elif dog_age <= 2:
        dog_years = dog_age * 10  
    else:
        dog_years = 2 * 10 + (dog_age - 2) * 7  
    print(f"The dog's age in dog years is {dog_years}.")

# Call the function
calculate_dog_years()

print("-------------------------------------------------------")

# Exercise 4: Weather Advice

def weather_advice():
    cold = input("Is it cold? (yes/no): ").lower() == 'yes'
    raining = input("Is it raining? (yes/no): ").lower() == 'yes'
    
    if cold and raining:
        print("Wear a waterproof coat.")
    elif cold and not raining:
        print("Wear a warm coat.")
    elif not cold and raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()

print("-------------------------------------------------------")

# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    day = int(input("Enter the day of the month: "))
    
    if month in ['Dec', 'Jan', 'Feb'] or (month == 'Mar' and day <= 19):
        season = "Winter"
    elif month in ['Mar', 'Apr', 'May'] or (month == 'Jun' and day <= 20):
        season = "Spring"
    elif month in ['Jun', 'Jul', 'Aug'] or (month == 'Sep' and day <= 21):
        season = "Summer"
    else: 
        season = "Fall"
    
    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()
