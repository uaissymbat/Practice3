def decode_number(s):
    mapping = {
        "ZER": 0, "ONE": 1, "TWO": 2, "THR": 3,
        "FOU": 4, "FIV": 5, "SIX": 6, "SEV": 7,
        "EIG": 8, "NIN": 9
    }
    digits = []
    for i in range(0, len(s), 3):
        triplet = s[i:i+3]
        digits.append(mapping[triplet])
    num = 0
    for d in digits:
        num = num * 10 + d
    return num

def encode_number(num):
    rev_map = {
        0: "ZER", 1: "ONE", 2: "TWO", 3: "THR",
        4: "FOU", 5: "FIV", 6: "SIX", 7: "SEV",
        8: "EIG", 9: "NIN"
    }
    if num == 0:
        return "ZER"
    s = str(num)
    result = ""
    for ch in s:
        result += rev_map[int(ch)]
    return result

def main():
    expr = input().strip()
    for i, ch in enumerate(expr):
        if ch in "+-*":
            op = ch
            left = expr[:i]
            right = expr[i+1:]
            break
    a = decode_number(left)
    b = decode_number(right)
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    else:  # '*'
        res = a * b
    print(encode_number(res))

if __name__ == "__main__":
    main()