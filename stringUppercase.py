def stringUpperCase(string):
    string1 = ''
    a = ""
    c = ""
    b = ""
    for i in range(len(string)):
        if (string[i] >= 'a' and string[i] <= 'z'):
            string1 = string1 + chr((ord(string[i]) - 32))
        else:
            string1 = string1 + string[i]
    return string1

print(stringUpperCase("Satripleen"))