print("Welcome to my fun quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    exit()
print("Okay! Let's play :)")
score = 0
answer = input("What does ICA stand for? ")
if answer.lower() == "independent component analysis":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does RFE stand for? ")
if answer.lower() == "recursive feature analysis":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does xAI stand for? ")
if answer.lower() == "explainable artificial intelligence":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does PCA stand for? ")
if answer.lower() == "principal component analysis":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does ML stand for? ")
if answer.lower() == "machine learning":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("What does ANN stand for? ")
if answer.lower() == "artificial neural network":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

print("You got",score,"questions correct!")
print("You got "+ str((score/6) * 100)+"%.")