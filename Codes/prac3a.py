# Print a name 'n' times, where name and n are read from standard input,
# using for and while loops.
import argparse

def name_in_while_loop(name, num):
    i = 0
    while i < num:
        print(f"{name}")
        i += 1

def name_in_for_loop(name, num):
    for i in range(num):
        print(f"{name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Demontrating for and while loop of python")
    parser.add_argument('name')
    parser.add_argument('number')
    args = parser.parse_args()
    print("\nPrinting using While loop:")
    name_in_while_loop(args.name, int(args.number))
    print("\nPrinting using for loop:")
    name_in_for_loop(args.name, int(args.number))

