# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Reverse a sentence by word such as Hello World become olleH dlroW
def reverseByWord(sentence):
    words = ''
    reversedWord = ''

    for i in sentence:
        if (i != ' '):
            words += i
        else:
            reversedWord += words[::-1] + ' '
            words = ''
            
    reversedWord += words[::-1]

    return reversedWord

try:
    sentence = input("sentence: ")

    result = reverseByWord(sentence)
    print(result)
except:
    print("Error: Please make sure that 'sentence' is a string")