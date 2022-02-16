# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Draw a triangle using * symbol
def triangleUp(row):
    for i in range(1, row + 1):
        print(' ' * ((row - i) * 2) + '* ' * (i + i - 1))

try:
    row = int(input("row: "))
    triangleUp(row)
except:
    print("Error: Please make sure that row is an integer")