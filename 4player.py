##
## 4 Player Game
##
import random


#Setting the startegy.
colours = ['clubs', 'hearts', 'diamonds', 'spades']
Pick_of_Emily, Pick_of_Charles, Pick_of_Doug = random.sample(colours, 3)

print("When setting the strategy Emily tells Fran that she will write down '" + Pick_of_Emily + "' immediately if Fran's card is also " + Pick_of_Emily + ".")
print("#")
print("Charles tells Fran that he will write down '" + Pick_of_Charles + "' immediately if Fran's card is also " + Pick_of_Charles + ".")
print("#")
print("Doug tells Fran that he will write down '" + Pick_of_Emily + "' immediately if Fran's card is also " + Pick_of_Emily + ".")
print("#")
print("#")

# Players draw cards.
Card_of_Emily = random.choice(colours)
print("Emily draws " + Card_of_Emily + ".")
Card_of_Charles = random.choice(colours)
print("Charles draws " + Card_of_Charles + ".")
Card_of_Doug = random.choice(colours)
print("Doug draws " + Card_of_Doug + ".")
Card_of_Fran = random.choice(colours)
print("Fran draws " + Card_of_Fran + ".")
print("#")
print("#")

# The actual game.
def Game():
  if Card_of_Fran == Pick_of_Emily:
    print("The players looks at Fran's card.")
    print("Because Fran has " + Pick_of_Emily + ", Emily immediately writes down '" + Card_of_Fran + "'.")
    print("Fran realises that Emily has seen " + Pick_of_Emily + " so she also writes down '" + Card_of_Fran + "'.")
  elif Card_of_Fran == Pick_of_Charles:
    print("The players looks at Fran's card.")
    print("Because Fran has " + Pick_of_Charles + ", Charles immediately writes down '" + Card_of_Fran + "'.")
    print("Fran realises that Charles has seen " + Pick_of_Charles + " so she also writes down '" + Card_of_Fran + "'.")
  elif Card_of_Fran == Pick_of_Doug:
    print("The players looks at Fran's card.")
    print("Because Fran has " + Pick_of_Doug + ", Doug immediately writes down '" + Card_of_Fran + "'.")
    print("Fran realises that Doug has seen " + Pick_of_Doug + " so she also writes down '" + Card_of_Fran + "'.")
  else:
    print("The players looks at Fran's card. Because Fran has " + Card_of_Fran + " they will not write down anything.")
    print("Because no one is writing down anything Fran realizes that they do not see " + Pick_of_Emily + ", " + Pick_of_Charles + " or a " + Pick_of_Doug + " in her hand.")
    print("Fran writes down '" + Card_of_Fran + "'.")
    
Game()
print("#")
print("#")
print("#")
# The win.
print("Because Fran guessed her card, they win the game.")
