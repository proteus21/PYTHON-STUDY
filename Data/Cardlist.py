#------------------------------
# Write the programme, which will be shuffle cards between 5 players
#----------------------------------
import random
cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Jo"
            ""
            "ker", "Joker"]
random.shuffle(cardList)
print(cardList)

conteinerAll =[]
conteiner1 =[]
conteiner2 =[]
conteiner3 =[]
conteiner4 =[]
conteiner5 =[]
n = 7
a = [[0] * n for i in range(n)]
for x  in range(5):
  z = cardList.pop()
  for i in range(n):
      for j in range(n):

              a[i][j]=z

  for row in a:
      print(' '.join([str(elem) for elem in row]))
