""" Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up! """

words={
    "Kurshi" : "chair",
    "jutaa" : "Shoe",
    "Dabai" : "Medicine",
    "Billi" : "Cat"
}
word=input("Enter the word you want to know the meaning of: ")


if word:
    print(f"The meaning of '{word}' is: {words[word]}")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")