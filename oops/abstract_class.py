from abc import ABC, abstractmethod


class AbstractRecipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Recipe1(AbstractRecipe):
    def get_ready(self):
        print("get_ready")

    def do_the_dish(self):
        print("do_the_dish")

    def cleanup(self):
        print("cleanup")


recipe = Recipe1()
recipe.execute()
