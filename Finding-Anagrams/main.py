# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(stra, strb):

    stra = sorted(stra.lower())
    strb = sorted(strb.lower())

    return stra == strb

stra = input("Enter first string:  ")
strb = input("Enter second string: ")

print (find_anagrams(stra, strb))


