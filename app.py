import random

word_list = [
    "java",
    "python",
    "swift",
]

word = word_list[random.randint(0, 2)]
answer = []
for char in range(len(word)):
    answer.append("_")

while True:
    for i in answer:
        print(i, end="")
    print("\n")
    char = input("Enter one letter (a ~ z): ")
    
    if char in word:
        print("Correct")
        for i in range(len(word)):
            if char == word[i]:
                answer[i] = char
    else:
        print("Wrong")
    
    if "_" not in answer:
        print('Answer is "{}"'.format(word))
        print("Program exit! bye bye")
        break