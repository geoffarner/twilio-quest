import sys

input = sys.argv
input.pop(0)

for index, item in enumerate(input, start=1):
    string = f"{index}. {item}"
    print(string)
