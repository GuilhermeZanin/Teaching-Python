# If its any of the values below, returns true, else returns false
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 

# Counts vowels
def countVowels(word):
    """
    Parameters:
    word: str
     value in str
    """
    count = 0
    for i in range(len(word)):
        if(isVowel(word[i])):
            count+=1
    return count

# wordTest = "abcde_fgh a i o aaa "
# print(countVowels(wordTest))

#Note in lists in python
# [1:5] is equivalent to "from 1 to 5" (5 not included)
# [1:] is equivalent to "1 to end"
# [len(a):] is equivalent to "from length of a to end"

# Hide card number
def hideCardNumber(ccNumber):
    # Gets length of numbers to mask (entire lenght-4)
    strLength=len(ccNumber)
    masked = strLength-4

    # last 4 digits are equal to last position of masked until end
    lastNumber = ccNumber[masked:]
    # Prints "*"" times the length of masked, and concatenates the last 4 digits
    print(("*" * masked) + lastNumber)

# hideCardNumber("123456789")
    