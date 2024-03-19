class TowerOfHanoi:
    def __init__(self, n):
        self.n = n

    def move_tower(self, source, target, auxiliary):
        if self.n % 2 == 0:
            auxiliary, target = target, auxiliary

        total_moves = 2**self.n - 1

        for move in range(1, total_moves + 1):
            if move % 3 == 1:
                self.move_disk(source, target)
            elif move % 3 == 2:
                self.move_disk(source, auxiliary)
            else:
                self.move_disk(auxiliary, target)

            if self.n <= 0:
                break

    def move_disk(self, from_tower, to_tower):
        if self.n <= 0:
            return

        print(f"Move disk from {from_tower} to {to_tower}")
        self.n -= 1

def main():
    n = 74
    tower = TowerOfHanoi(n)
    tower.move_tower("A", "B", "C")

if __name__ == "__main__":
    main()
