import random
def guess():
    number = random.randint(1, 100)
    n = 0
    print(number)
    while n != number:
        n = input("Wprowadź liczbę")
        try:
            if int(n) > number:
                print("Za dużo")
                continue
            if int(n) < number:
                print("Za mało")
                continue
        except ValueError:
            print("To nie jest liczba")
            continue
        else:
            return "Zgadłeś"

print(guess())