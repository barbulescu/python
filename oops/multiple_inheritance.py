class LandAnimal:
    def walk(self):
        print("walk")


class WaterAnimal:
    def swim(self):
        print("swim")


class Amphibian(LandAnimal, WaterAnimal):
    pass
