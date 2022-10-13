#program to sort the words in string in alphabetic order or sort the string in lexicographical order
str=input(" enter a string: ")
words=[i.lower for i in str.split()]
words.sort()
for i in words:
    print(i)