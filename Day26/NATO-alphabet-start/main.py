import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(alphabet_data)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}
print(alphabet_dict)

word = input("Enter a word:").upper()

word_code = [alphabet_dict[keyname] for keyname in word]
print(word_code)

# word_code_2 = []
# for keyname in word:
#     word_code_2.append(alphabet_dict[keyname])
# print(word_code_2)

# if word in alphabet_dict:
#     print(alphabet_dict[word])
# else:
#     print("no")