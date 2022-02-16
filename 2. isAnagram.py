# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Compare 2 strings if it is anagram. Anagram is a word that can be formed by rearrange other word such as cinema and iceman
def isAnagram(s1, s2):
    s1 = toLower(s1)
    s2 = toLower(s2)

    countS1 = {}
    countS2 = {}

    if len(s1) == len(s2):
        for i in s1:
            if i in countS1:
                countS1[i] += 1
            else:
                countS1[i] = 0
        
        for i in s2:
            if i in countS2:
                countS2[i] += 1
            else:
                countS2[i] = 0
        
        if countS1 == countS2:
            return True
        
        else:
            return False
    else:
        return False

# Convert every uppercase letter in a string to a lowercase one
def toLower(str):
    lowered = ''
    for i in str:
        ch = ord(i)
        if ch >= 65 and ch <= 90:
            lowered += chr(ch + 32)
        else:
            lowered += chr(ch)
    
    return lowered

try:
    string1 = input("string1: ")
    string2 = input("string2: ")

    result = isAnagram(string1, string2)
    print(result)
except:
    print("Error: Please make sure that both 'string1' and 'string2' are string")