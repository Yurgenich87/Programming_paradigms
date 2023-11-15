def greet(name):
    print("Здравствуйте!")
    print(name)
    print("Как вы себя чувствуете сегодня?")


def rate_movie(score):
    if score > 8:
        return "Отличный фильм!"
    elif score > 6:
        return "Хороший фильм!"
    else:
        return "Средний или плохой фильм"


print(rate_movie(9))


def sum_to_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_to_n(100))








