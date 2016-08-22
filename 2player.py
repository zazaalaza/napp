##
## 2 Player Game
##
import random

#Setting the startegy.
colours = ['red', 'black']
Pick_of_Ava = random.choice(colours)
print("When setting the strategy Ava tells Bruce that she will write down '" + Pick_of_Ava + "' immediately if Bruce's card is also " + Pick_of_Ava + ".")
print("#")
print("#")

# Players draw cards.
Card_of_Bruce = random.choice(["red", "black"])
print("Bruce draws a " + Card_of_Bruce + " card.")
Card_of_Ava = random.choice(["red", "black"])
print("Ava draws a " + Card_of_Ava + " card.")
print("#")
print("#")

# The actual game.
def Game():
  if Card_of_Bruce == Pick_of_Ava:
    print("Ava looks at Bruce's card. Because Bruce has a " + Pick_of_Ava + " card, she immediately writes down '" + Card_of_Bruce + "'.")
    print("Bruce realises that Ava has seen a " + Pick_of_Ava + " card so he also writes down '" + Card_of_Bruce + "'.")
  else:
    print("Ava looks at Bruce's card. She sees that Bruce has a " + Card_of_Bruce + " card, so she will not write down anything.")
    print("Because Ava is not moving Bruce realizes that Ava did not see a " + Pick_of_Ava + " card.")
    print("Bruce writes down '" + Card_of_Bruce + "'.")
    
Game()
print("#")
print("#")
print("#")
# The win.
print("Because Bruce guessed his card, they win the game.")

