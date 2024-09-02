from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
        # with open("data.txt") as data:
        #     self.high_score = int(data.read())         
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"Score: {self.score} HighScore: {self.high_score}", False, align="center", font=('Arial', 16, 'bold'))

    def increase_score(self):
        self.score += 1
        # if self.score > self.high_score:
        #     with open("data.txt", mode = "w") as data:
        #         data.write(str(self.score))   
        self.update_scoreboard()

    def reset_score(self):        
        if self.score > self.high_score:
            with open("data.txt", mode = "w") as data:
                data.write(str(self.score))  
            # self.high_score = self.score
            
        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.clear()
    #     self.setpos(0, 0)
    #     self.write(f"GAME OVER", False, align="center", font=('Arial', 18, 'bold'))
    #     self.setpos(0, -25)
    #     self.write(f"Score: {self.score}", False, align="center", font=('Arial', 18, 'bold'))

    # def reset_scoreborad():
        
