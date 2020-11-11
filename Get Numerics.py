def getNumerics(text):
    start = 0
    number = ""
    while text[start] == " ":
        start += 1
    if text[start].isalpha():
        return -1
    if text[start] in ["+", "-"]:
        number = number+text[start] if text[start] == "-" else number
        start += 1
    while text[start] != " " and text[start].isnumeric():
        number += text[start]
        start += 1
    return number


text = input("Enter the text: ")
print(getNumerics(text))
