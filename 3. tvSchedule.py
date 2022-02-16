# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Create a string from list of integer. If values stick together (such as 1 2 3), group it together (such as 1 - 3). If not, separate with comma
def tvSchedule(arr):
    result = ''
    
    temp = 0
    for i in range(len(arr) - 1):
        if(arr[i] + 1 == arr[i + 1]):
            temp += 1
        elif(temp == 0):
            result += str(arr[i]) + ', '
        else:
            result += str(arr[i - temp]) + ' - ' + str(arr[i]) + ', '
            temp = 0
    if (temp == 0):
        result += str(arr[-1])
    else:
        result += str(arr[-1-temp]) + ' - ' + str(arr[-1])

    return result

# Check if 'char' is a digit (0 - 9)
def isDigit(char):
    # Check using ASCII code where 48 = 0 and 57 = 9
    if ord(char) >= 48 and ord(char) <= 57:
        return True
    else:
        return False

# Check if 'char' is a letter (a - z or A - Z)
def isLetter(char):
    # Check using ASCII code where 65 = A and 90 = Z and 97 = a and 122 = z
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        return True
    else:
        return False
# Convert string into list of Int
def listOfInt(string):
    listInt = []
    digitAmount = 0 # Count the amount of digit before go to

    for i in range(len(string)):
        if isDigit(string[i]):
            digitAmount += 1
        # If current char is not a digit and amount of digit is not 0. that's mean there is an integer, convert it and add to the list
        elif digitAmount != 0: 
            num = ''
            # Work with integer that isn't a digit e.g. 152, 34
            for j in range(i - digitAmount, i):
                num += string[j]
            listInt.append(int(num))
            digitAmount = 0
        # If there is a letter or '.', that's mean it is not a string of integer and raise an error
        elif isLetter(string[i]) or string[i] == '.':
            raise ValueError("'arr' contain letter or float")
        else:
            continue
    # If amount of digit is not 0, that's mean the last integer is left. Add that integer to the list
    if digitAmount != 0:
        num = ''
        for j in range(-digitAmount, 0):
            num += string[j]
        listInt.append(int(num))
        digitAmount = 0

    return listInt

try:
    arr = listOfInt(input("arr: "))

    result = tvSchedule(arr)
    print(result)
except:
    print("Error: Please make sure that arr is an array of integers")

