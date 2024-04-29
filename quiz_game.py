print("Welcome to the computer Quiz!")

name = input("Enter your name: ")
print("Hi, ", name)

playing = input("Are you ready to play? ")
if playing.lower() != "yes":
    quit()

print("Ok! lets play!!")
score = 0

answer = input("What does the C in CPU stand for?: ")
if answer.lower() == "central":
    print("correct, CPU stands for Central Processing Unit!")
    score += 1
else:
    print(answer, "is not correct, the correct answer is central!")

answer = input("What is the capital city of Canada?: ")
if answer.lower() == "ottawa":
    print("correct, the capital of Canada is ottawa!")
    score += 1
else:
    print(answer, "is not correct, the correct answer is ottawa!")

answer = input("What is 2 x 2 = ?: ")
if answer.lower() == "4":
    print("correct, 2 x 2 = 4!")
    score += 1
else:
    print(answer, "is not correct, the correct answer is 4!")

answer = input("What ocean is south of Greenland?: ")
if answer.lower() == "atlantic":
    print("correct, atlantic ocean is south of Greenland!")
    score += 1
else:
    print(answer, "is not correct, the correct answer is central!")

print('You scored ', score, " out of 4!")

