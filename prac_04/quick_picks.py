import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_PER_PICK = 6

def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        print_quick_pick()

def print_quick_pick():
    numbers = []
    while len(numbers) < NUMBER_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
        numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))

main()

