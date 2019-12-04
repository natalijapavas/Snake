import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class SnakeGame:
    def __init__(self, snake, last_move, food, eaten):
        self.snake = snake
        self.last_move = last_move
        self.food = food
        self.eaten = eaten

    def update_snake(self, move):
        self.last_move = move
        head = self.snake[-1]

        if self.eaten > 0:
            self.eaten -= 1
        else:
            self.snake.pop(0)

        if self.last_move == 'r':
            self.snake_append((head[0] + 1, head[1]))
        elif self.last_move == 'l':
            self.snake_append((head[0] - 1, head[1]))
        elif self.last_move == 'u':
            self.snake_append((head[0], head[1] - 1))
        elif self.last_move == 'd':
            self.snake_append((head[0], head[1] + 1))
        if head in self.snake[:-1]:
            raise Exception('ur bad')

    def move(nns, i=0):
        if i == len(nns) - 1:
            k = nns[i].feed_forward(sg.make_tset())
            if k.index(max(k)) == 0:
                sg.update_snake('r')
            elif k.index(max(k)) == 1:
                sg.update_snake('l')
            elif k.index(max(k)) == 2:
                sg.update_snake('d')
