from random import choice


def funny_names(first, last):
    for item in first:
        n = choice(last)
        last.remove(n)
        print(f"{item} {n}")


if __name__ == '__main__':
    size = int(input("Enter the number of your friends: "))
    friends = [input(f"Enter the full name of friend {i}: ") for i in range(1, size + 1)]
    first_names = [name.split(" ")[0] for name in friends]
    last_names = [name.split(" ")[1] for name in friends]
    funny_names(first_names, last_names)
