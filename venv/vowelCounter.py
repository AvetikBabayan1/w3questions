#To count number of vowels and consonants in the string

def vowelCount(word):
    vowels="aeiouAEIOU"
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowCount=0
    conCount=0
    nonLetter=0
    for w in word:
        if w in vowels:
            vowCount+=1
        elif w in consonant:
            conCount+=1
        else:
            nonLetter+=1
    print("Vowels Count is: ", vowCount)
    print("Consonant Count is: ", conCount)
    print("Non Letter Symbol Count is: ", nonLetter)
word = input("Please enter the word to count letters: ")
vowelCount(word)

