from abc import ABC, abstractmethod


class GamingConsole(ABC):

    @abstractmethod
    def up(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def left(self): pass

    @abstractmethod
    def right(self): pass


class MarioGame(GamingConsole):

    def up(self): print("up")

    def down(self): print("down")

    def left(self): print("left")

    def right(self): print("right")


game = MarioGame()

game.up()
game.down()
game.left()
game.righ()
