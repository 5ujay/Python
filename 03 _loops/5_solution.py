word = "thisthisspthedon"

for char in word:
    print(char)
    if word.count(char) == 1:
        print("char with no repetition : " ,char)
        break