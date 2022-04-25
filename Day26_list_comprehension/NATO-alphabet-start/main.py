import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}
print(alphabet_dict)


def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        word_code = [alphabet_dict[keyname] for keyname in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(word_code)


generate_phonetic()
