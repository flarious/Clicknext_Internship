# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Draw a triangle using number which goes up by 1 and only show last digit if number is exceed 10
def triangleInt(row):
    number = 1

    for i in range(1, row + 1):
        print(' ' * ((row - i) * 2), end = ' ')
        for j in range(0, i):
            print(number % 10, ' ', end = ' ')
            number += 1 
        print()

try:
    row = int(input("row: "))
    if(row >= 1 and row <= 4):
        triangleInt(row)
    else:
        raise ValueError("Row must be between 1 and 4")
except:
    print("Error: Please make sure that 'row' is an integer within range of 1 - 4")