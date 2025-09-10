def bubble_sort(arr, direction):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if direction == 1:  # по возрастанию
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:  # по убыванию
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    try:
        n = int(input("Введите количество чисел "))
        numbers = []

        print(f"Введите {n} чисел:")
        for i in range(n):
            num = float(input(f"Число {i + 1}: "))
            numbers.append(num)

        print("1 - по возрастанию")
        print("2 - по убыванию")
        choice = int(input("Введите 1 или 2: "))

        if choice == 1:
            bubble_sort(numbers, 1)
            print("\nОтсортировано по возрастанию:")
        elif choice == 2:
            bubble_sort(numbers, 2)
            print("\nОтсортировано по убыванию:")
        else:
            print("Не понял, сортирую по возрастанию")
            bubble_sort(numbers, 1)
            print("\nОтсортировано по возрастанию:")

        for num in numbers:
            print(num, end=" ")
        print()

    except ValueError:
        print("Ой! Нужно вводить только числа!")


if __name__ == "__main__":
    main()