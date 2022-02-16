# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Draw an upside down triangle with * symbol
def triangleDown(row):
    for i in range(row, 0, -1):
        print(' ' * ((row - i) * 2) + '* ' * (i + i - 1))

try:
    row = int(input("row: "))
    triangleDown(row)
except:
    print("Error: Please make sure that row is an integer")
