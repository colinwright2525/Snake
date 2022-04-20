from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.count = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())


    def create_board(self):
        self.penup()
        self.left(90)
        self.forward(270)
        self.color('white')
        self.write(f'SCORE: {self.count} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.count > self.high_score:
            with open('data.txt', mode='w') as data:
                data.write(str(self.count))
            self.high_score = self.count
            self.count = 0
            self.clear()
            self.write(f'SCORE: {self.count} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    #def game_over(self):
     #   self.right(180)
      #  self.forward(270)
       # self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.clear()
        self.count += 1
        self.write(f'SCORE: {self.count} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)




