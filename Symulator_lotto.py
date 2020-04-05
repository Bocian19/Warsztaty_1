import random
START_NUMBER = 1
END_NUMBER = 49

def draw_lotto(n=6):
    numbers = [x for x in range(START_NUMBER, END_NUMBER + 1)]
    random.shuffle(numbers)
    return sorted(numbers[:n])

def get_user_numbers(n=6):
    numbers = []
    while len(numbers) < n:
        number = input("Podaj liczbę:")
        try:
            number = int(number)
        except ValueError:
            print("To nie jest liczba całkowita!")
            continue
        if START_NUMBER <= number <= END_NUMBER:
            if number in numbers:
                print("Liczba już wcześniej podana!")
            else:
                numbers.append(number)
        else:
            print(f"Liczba musi być z zakresu {START_NUMBER}-{END_NUMBER}!")
    return sorted(numbers)







numbers = get_user_numbers()
print(numbers)






