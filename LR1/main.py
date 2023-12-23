import math

def get_coefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Ошибка: Введите корректное значение.")

def solve_biquadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x,
    else:
        return None

def main():
    a = get_coefficient("Введите коэффициент A: ")
    b = get_coefficient("Введите коэффициент B: ")
    c = get_coefficient("Введите коэффициент C: ")

    roots = solve_biquadratic_equation(a, b, c)

    if roots is not None:
        print("Корни уравнения:", ", ".join(map(str, roots)))
    else:
        print("Уравнение не имеет действительных корней.")


main()
