# 7- write a script that will take user's age and tell if there are eligible to vote or not.



age = input("Please enter your age ?  ")

# remove any space
_age = age.strip()

# the once condition to vote
if _age.isdigit() and int(_age) >= 18 :

    print("You are eligible to vote 😇")

# if the given value is not numeric number
elif  not _age.isdigit(): 

    print("Please enter a numeric value !!!!")

# otherwise 
else:

    print("Oupsss 🫣! You are not eligible to vote")