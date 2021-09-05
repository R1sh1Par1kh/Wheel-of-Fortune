# main.py

#change answer value to prefrence but meep it as a string. 
answer = "pepperoni"
letters = set()
guessNum = 15

def listToString(list):
  word = ""
  for item in list:
    word += item
  return word

print("Welcome to the Wheel of Fortune! You have " + str(guessNum) + " guesses to figure out the correct word. Good luck!")

currentState = []
currentStateStr = ""
for letter in answer:
  currentState.append("_ ")
  letters.add(letter)
  if letter == " ":
    currentState.append("  ")
currentStateStr = listToString(currentState)
print(currentStateStr)

while True:
  if guessNum == 0:
    print("Your'e out of guesses, meaning you lost the game!")
    break
  
  guess = input("Guess a letter! You have " + str(guessNum) + " guesses remaining. ")
  guessNum -= 1
    
  if guess in letters:
    for i in range(len(answer)):
      if guess == answer[i]:
        currentState[i] = guess
    currentStateStr = listToString(currentState)
  print(currentStateStr)
    
  if currentStateStr == answer:
    print("Congratulations, you win")
    break
