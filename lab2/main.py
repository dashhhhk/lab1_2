def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    try:
        n = int(input("Введите количество чисел: "))
        numbers = []

        print(f"Введите {n} чисел:")
        for i in range(n):
            num = float(input(f"Число {i + 1}: "))
            numbers.append(num)

        bubble_sort(numbers)

        print("\nОтсортированный список:")
        for num in numbers:
            print(num, end=" ")
        print()

    except ValueError:
        print("Ошибка: введите корректные числа!")


if __name__ == "__main__":
    main()