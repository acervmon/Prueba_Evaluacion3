import random

class TowerOfHanoi:
    def __init__(self, n):
        self.n = n

    def move_tower(self, source, target, auxiliary):
        if self.n % 2 == 0:
            auxiliary, target = target, auxiliary

        total_moves = 2**self.n - 1

        for move in range(1, total_moves + 1):
            if move % 3 == 1:
                self.move_piedra(source, target, "A", "grande")
            elif move % 3 == 2:
                self.move_piedra(source, auxiliary, "B", "pequeña")
            else:
                self.move_piedra(auxiliary, target, "C", "mediana")

            if self.n <= 0:
                break

    def move_piedra(self, from_tower, to_tower, stone_type, stone_size):
        if self.n <= 0:
            return

        print(f"Move {stone_type} {stone_size} from {from_tower} to {to_tower}")
        self.n -= 1

def main():
    n = random.randint(0, 74)
    tower = TowerOfHanoi(n)
    tower.move_tower("A", "B", "C")

if __name__ == "__main__":
    main()
