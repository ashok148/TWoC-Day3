#Program to remove duplicate character from a given string:--

def duplicate(str):
    s = set(str)

    return "".join(s)
str = input("Enter a string : ")
a = duplicate(str)
print(a)