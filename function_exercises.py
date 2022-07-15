#create function named is_vowel that takes in one parameter
def is_vowel(x):
    #create list of vowels to compare off of later
    vowels = ['a', 'e', 'i', 'o', 'u']
    #check if x is in vowels, consider case
    if type(x) == str and x.lower() in vowels:
        #return function as True if x was in the vowels list
        return True
    #return function as False
    return False


#create function named calculate_tip that takes in two parameters
def calculate_tip(percent, total):
    #return the total times the percent, adjusted to be rounded to 2 decimals
    return round(float(total) * float(percent), 2)


#create function named get_letter_grade that takes in one parameter
def get_letter_grade(grade):
    #ensure it is an integer type
    grade = int(grade)
    #cycle through the grade scale options
    if grade >= 88:
        #return letter if in specific grade scale
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 67:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'