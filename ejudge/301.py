def is_valid(number):
    for ch in str(abs(number)):
        if int(ch) % 2 != 0:
            return False
    return True


n = int(input())
if is_valid(n):
    print("Valid")
else:
    print("Not valid")