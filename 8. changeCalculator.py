# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Calculate changes for item with prices lower than 1000 and the customer always pay with 1000THB bank note
def changesCalculator(price):
    changes = [500, 100, 50, 10, 5, 1]
    result = {}
    change = 1000 - price

    for i in changes:
        amount = change // i
        change -= i * amount

        result[i] = amount

    return result


try:
    price = int(input("price: "))
    if price >= 0 and price < 1000:
        result = changesCalculator(price)
        print(result)
    else:
        raise ValueError("'price' must be between 0 and 999")
except:
    print("Error: Please make sure that 'price' in an integer within 0 - 999")