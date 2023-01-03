import math


def permutations2(str):
    if len(str) == 1:
        return str
    first = str[0]
    remainder = str[1:]
    result = set()
    for i in range(len(str)):
        for s in permutations2(remainder):
            tmp = s[:i] + first + s[i:]
            result.add(tmp)
    return result


def permutations3(str):
    if len(str) == 1:
        return str
    result = set()
    for i in range(len(str)):
        for s in permutations3(str[0:i] + str[i+1:]):
            result.add(str[i] + s)
    return result


def main():
    string = 'abcd'
    result = permutations3(string)
    print(result)
    print("result.len is " + str(len(result)))
    print("factorial result.len is " + str(math.factorial(len(string))))


if __name__ == "__main__":
    main()
