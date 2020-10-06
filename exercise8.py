# Ask the user to enter an age, and print on the screen which phase of life the age belongs to. Up to 11 years old - childhood stage, from 12 to 20 years old - adolescence, from 21 to 74 years old - adult, and from 75 years old - old age.


age = int(input("Please enter your age "))

if age >0 and age <= 11:
    phase = "childhood"
elif age >11 and age <20:
    phase = "adolescene"
elif age > 20 and age <74:
    phase = "adult"
elif age > 74:
    phase = "old age"
else:
    phase = "out of range"


print(F"Your phase is {phase}")
