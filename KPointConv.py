# Python 3.4

# Step 1. user inputs to set the lower and upper limit of kpoint grid dimension
# Note that ONLY the cubic grid is considered for the moment

print('Please enter an integer number:')
print('For example: 1')
userInputLower = input('Enter the lower limit of kpoint grid dimension:')
#print(userInput)

print('Please enter an integer number:')
print('For example: 10')
userInputUpper = input('Enter the upper limit of kpoint grid dimension:')
# print(userInput)

userinput=[userInputLower,userInputUpper]
print(userinput)

# Step 2. automatically create directories and input files for the kpoint convergence study
# based on the user input kpoint grid dimensions

