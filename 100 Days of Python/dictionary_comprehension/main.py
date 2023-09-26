#Take a word as an input and for each letter in the word, output the nato phonetic alphabet word
#For example: if the user enters "amazon", the output should be ['Alfa', 'Mike', 'Alfa', 'Zulu', 'Oscar', 'November']

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {value.letter: value.code for (key, value) in df.iterrows()}

word = input("Enter a word: ").upper()

code_word = [nato_alphabet[letter] for letter in word]
print(code_word)
