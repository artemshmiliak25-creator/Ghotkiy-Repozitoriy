import math

def square_geom(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

def triangle_geom(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return None, None
    perimeter = a + b + c
    p_half = perimeter / 2
    area = math.sqrt(p_half * (p_half - a) * (p_half - b) * (p_half - c))
    return perimeter, area

def circle_geom(radius):
    pass

def main():
    print("--- Геометричний калькулятор ---")
    print("1. Квадрат\n2. Трикутник\n3. Коло")
    choice = input("Оберіть фігуру (1-3): ")

    if choice == "1":
        side = float(input("Введіть сторону квадрата: "))
        p, s = square_geom(side)
        print(f"Периметр квадрата: {p}, Площа: {s}")
        
    elif choice == "2":
        print("Введіть три сторони трикутника:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        p, s = triangle_geom(a, b, c)
        if p is None:
            print("Трикутник із такими сторонами не існує!")
        else:
            print(f"Периметр трикутника: {p}, Площа: {s:.2f}")
        
    elif choice == "3":
        radius = float(input("Введіть радіус кола: "))
        
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()
