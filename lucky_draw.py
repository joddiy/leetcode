import csv
import random as r
import time as t


def print_title(text):
    length = len(text) + 4
    print("-" * length)
    print("|", text, "|")
    print("-" * length)


def print_content(text, bottom_line=False):
    length = len(text) + 4
    print("=" * length)
    print(text)
    if bottom_line:
        print("=" * length)
    t.sleep(0.6)


ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) *
                                            (n % 10 < 4) * n % 10::4])


def lucky_draw():
    print_title("Welcome to Lucky Draw !")

    with open("name_list.csv", 'r') as csv_file:
        print("Loading the guests list...")

        csv_reader = csv.reader(csv_file)
        name_list = list(csv_reader)
        n_candidate = len(name_list)

        print_content("Loaded %d guests" % n_candidate, bottom_line=True)

        n_winner = None
        while not n_winner or n_winner > n_candidate:
            n_winner = int(input("Please enter the number of winner: "))
            print_content("Starting to draw %d winner from %d guests..." %
                          (n_winner, n_candidate))
            if n_winner > n_candidate:
                print_content(
                    "The number of winner cannot be larger than guests, please re-enter it...",
                    bottom_line=True)

        for i in range(n_winner):
            print_content("Drawing the %s winner, press ctrl+c to stop..." %
                          ordinal(i + 1),
                          bottom_line=True)
            r.seed(t.time())
            while True:
                try:
                    _idx = r.randint(0, len(name_list) - 1)
                    _candidate = name_list[_idx]
                    print("\r%s" % _candidate[1], end="")
                    t.sleep(0.01)
                except KeyboardInterrupt:
                    print("\r%s" % _candidate[1], end="")
                    print()
                    print_content("Guest %s, %s won! Congrats!" %
                                  (_candidate[0], _candidate[1]))
                    del name_list[_idx]
                    break
        print_content("All winners have been drawn. Congrats!",
                      bottom_line=True)


if __name__ == '__main__':
    lucky_draw()
