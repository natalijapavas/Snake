import numpy as np
def sigmoid(X):
    return 1/(1+np.exp(-x))

class SnakeGame:
    def __init__(self, snake, last_move, food, eaten):
        self.snake = snake
        self.last_move = last_move
        self.food = food
        self.eaten = eaten

    def update_snake:
        self.last_move = move
        head = self.snake[-1]

        if self.eaten > 0:
            self.eaten -= 1
        else:
            self.snake.pop(0)

        if self last_move == 'r':
            self.snake_append((head[0]+1,head[1]))
        elif self.last_move == 'l':
            self.snake_append((head[0]-1,head[1]))
        elif self.last_move == 'u':
            self.snake_append((head[0],head[1]-1))
        elif self.last_move == 'd':
            self.snake_append((head[0],head[1]+1))
