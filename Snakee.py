class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        def take_step(position):
            self.body = self.body[1:] + [position]

    
class Apple:
    ...
class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        matrix = [["." for i in range(self.width)] for j in range(self.height)]
        return matrix
    '''TODO: return a matrix'''

    def render(self):
        matrix = self.board_matrix()
        print(Snake)
        print("+","-"*self.width,"+", sep=' ')
        #TODO: print matrix
        for row in matrix:
            cleanrow = "".join(row)
            print("|", cleanrow, "|")
        #For row in matrix
        self.snake
        print("+", "-" * self.width, "+", sep=' ')
        # ...

game = Game(10, 20)
game.render()
# =>
# Height: 10
# Width: 20