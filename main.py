import math

def square_geom(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

def triangle_geom(a, b, c):
    pass

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
        
    elif choice == "3":
        radius = float(input("Введіть радіус кола: "))
        
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()