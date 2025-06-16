import random
def guess_the_number_game():

    max_attempts = 7
    secret_number = random.randint(1, 100)

    print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input("Введіть вашу припущення: "))

        except ValueError:
            print("Помилка: введіть тільки цілі числа. Спробуйте ще раз.")
            continue

        if guess < secret_number:
            print("Занадто маленьке!")
        elif guess > secret_number:
            print("Занадто велике!")
        else:
            print(f"Ви вгадали! Це число {secret_number}.")
            break
    else:
        print(f"Ви програли! Спроби закінчились. Це число {secret_number}.")

if __name__ == "__main__":
    guess_the_number_game()


