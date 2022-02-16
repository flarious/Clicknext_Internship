# Nattawut Klinsawas from Clicknext Camp Online Workshop @Kmutt

# Format second into hh:mm:ss format
def secondFormatter(second):
    time = ''

    if(second >= 60 * 60):
        hour = second // 3600
        second -= 3600 * hour

        time += ('0' if hour < 10 else '') + str(hour)
    else:
        time += '00'
    
    time += ':'

    if(second >= 60):
        minute = second // 60
        second -= 60 * minute

        time += ('0' if minute < 10 else '') + str(minute)
    else:
        time += '00'

    time += (':0' if second < 10 else ':') + str(second)

    return time

try:
    second = int(input("second: "))
    if second >= 0:
        result = secondFormatter(second)
    else:
        raise ValueError("'second' can't be negative")

    print(result)
except:
    print("Error: Please make sure that 'second' is a positive integer")