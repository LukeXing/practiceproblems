def myAtoi(s):
    list_of_values = s.split(" ")
    for i in list_of_values:
        #three cases - either i is a string, null, or a numeric string which can easily get convereted
        if i == "":
            continue
        elif i.isnumeric():
            i = int(i)
            if i > (2 ** 31 - 1):
                i = 2 ** 31 - 1
                return i
            elif i < -2 ** (-31):
                i = 2 ** (-31)
                return i
            return i
        elif i[0] == "+" or i[0] == "-":
            if i[0] == "+":
                i = i[1: len(i)]
                try:
                    i = int(i)
                except ValueError:
                    return 2 ** 31 - 1
            elif i[0] == "-":
                i = i[1: len(i)]
                try:
                    i = int(i)
                except ValueError:
                    return -2 ** 31
                i *= (-1)

            if i > (2 ** 31 - 1):
                i = 2 ** 31 - 1
            elif i < -2 ** 31:
                i = -2 ** 31

            return i

    # if nothing was read
    return 0

print(myAtoi("5 is a number"))
print(myAtoi("-10000000000"))
print(myAtoi("this number is really large + " + str(2**(31))))
print(myAtoi("   -42"))
print(myAtoi("+12313"))
print(myAtoi("words and 987"))
