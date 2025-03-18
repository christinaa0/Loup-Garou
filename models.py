from abc import ABC, abstractmethod
import random

class Game:

    def __init__(self, nb_max_turn):
        self.__nb_max_turn = nb_max_turn # dunder => double underscore ?
        self.__current_turn = 0

    @property
    def nb_max_turn(self):
        return self.__nb_max_turn


class Player(ABC):

    # pseudo only 1 letter length
    def __init__(self, pseudo : str, field_distance):
        if len(pseudo) != 1:
            raise ValueError('Max length of pseudo is 1')
        self.__pseudo = pseudo
        self.__field_distance = field_distance

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def field_distance(self):
        return self.__field_distance

    def __str__(self):
        return self.__pseudo


class Wolf(Player):

    def __init__(self, pseudo):
        super().__init__(pseudo, 2)



class Villager(Player):
    def __init__(self, pseudo):
        super().__init__(pseudo, 1)


class GameBoard:

    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.__content = [['x'] * width for _ in range(height)]

    def subscribe_player(self, player : Player):
        player_height = random.randrange(0, self.__height)
        player_width = random.randrange(0, self.__width)
        self.__content[player_height][player_width] = player

    def __repr__(self):
        result = ''
        for row in self.__content:
            result += ' '.join(map(str, row)) + '\n'
        return result


if __name__ == '__main__':
    g = GameBoard(10, 5)
    print(g)
    p1 = Wolf('A')
    p2 = Wolf('B')
    p3 = Villager('V')
    g.subscribe_player(p1)
    g.subscribe_player(p2)
    g.subscribe_player(p3)
    print(g)