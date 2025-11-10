import random

class WumbusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.place_entities()

    def place_entities(self):
        # Place Wumbus at a random cell
        wx, wy = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
        self.grid[wx][wy] = 'W'

        # Place pit at a random cell not occupied by Wumbus
        while True:
            px, py = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (px, py) != (wx, wy):
                break
        self.grid[px][py] = 'P'

    def show_grid(self):
        for row in self.grid:
            print(row)

if __name__ == "__main__":
    game = WumbusWorld()
    game.show_grid()