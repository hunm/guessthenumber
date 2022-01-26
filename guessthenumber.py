import random


def get_random_number(a, b):
    return random.randint(a, b)


def game():
    print("You should guess random number in range 100-9999")
    n = get_random_number(100, 9999)
    x = 0

    while n != x:
        print("Input number:")
        x = int(input())
        if x < n:
            print("Your number is less than guessed number. Try again!")
        elif x > n:
            print("Your number is bigger than guessed number. Try again!")

    print("Congratulations!")


def main():
    game()


if __name__ == "__main__":
    game()
