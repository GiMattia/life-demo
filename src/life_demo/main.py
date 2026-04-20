import time
from life_demo.life import GameOfLife


def main():
    game = GameOfLife(30, 12)
    game.randomize(0.28)

    steps = 100
    delay = 0.1

    for i in range(1, steps + 1):
        print("\x1b[2J\x1b[H", end="")
        print("Conway's Game of Life")
        print("step", i)
        print()
        print(game.as_text())
        time.sleep(delay)
        game.step()


if __name__ == "__main__":
    main()
