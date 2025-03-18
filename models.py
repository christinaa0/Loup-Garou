from abc import ABC, abstractmethod
import random

class Game:

    def __init__(self, nb_max_turn, width, height):
        self.__nb_max_turn = nb_max_turn # dunder => double underscore ?
        self.__current_turn = 0
        self.__gameboard = GameBoard(height, width)
        self.__actions = {} #c'est un dictionnaire


    @property
    def nb_max_turn(self):
        return self.__nb_max_turn
    #action :(witdh,height) > indique de combien on se deplace de hauteur et de largeur (-1,0) , (1,0) , (0,1), (0,-1) {c'est un tuple}
    def register_action(self, player, action):
        self.__actions[player] = action

    def process_action(self):
        new_positions = {}  # Pour éviter des conflits de déplacement

        for player, action in self.__actions.items():
            current_x, current_y = self.find_player_position(player)  # Trouver la position actuelle
            new_x = current_x + action[0]
            new_y = current_y + action[1]

            # Vérifier si la nouvelle position est valide et libre
            if 0 <= new_x < self.__gameboard._GameBoard__height and 0 <= new_y < self.__gameboard._GameBoard__width:
                if self.__gameboard._GameBoard__content[new_x][new_y] == 'x':  # Vérifier si la case est vide
                    new_positions[player] = (new_x, new_y)

        # Appliquer les déplacements après avoir tout vérifié
        for player, (new_x, new_y) in new_positions.items():
            current_x, current_y = self.find_player_position(player)
            self.__gameboard._GameBoard__content[current_x][current_y] = 'x'  # Effacer l'ancienne position
            self.__gameboard._GameBoard__content[new_x][new_y] = player  # Mettre à jour la nouvelle position

    def find_player_position(self, player):
        """ Trouve la position actuelle d'un joueur sur le plateau """
        for x in range(self.__gameboard._GameBoard__height):
            for y in range(self.__gameboard._GameBoard__width):
                if self.__gameboard._GameBoard__content[x][y] == player:
                    return x, y
        return None, None  # Si jamais on ne trouve pas le joueur (erreur)


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
    def __str__(self):
        return 'W'


class Villager(Player):
    def __init__(self, pseudo):
        super().__init__(pseudo, 1)
    def __str__(self):
        return 'O'


class GameBoard:

    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.__content = [['x'] * width for _ in range(height)]

    def subscribe_player(self, player: Player):
        while True:
            player_height = random.randrange(0, self.__height)
            player_width = random.randrange(0, self.__width)

            # Vérifier que la case est vide
            if self.__content[player_height][player_width] == 'x':
                self.__content[player_height][player_width] = player
                break  # Sortir de la boucle une fois que le joueur est bien placé

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