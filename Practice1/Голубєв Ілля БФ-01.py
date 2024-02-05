import random

# 1. Створює перший текстовий файл, записує у нього алгебраїчний вираз для розрахунку, закриває файл;
with open("Practice1/file1.txt", "w") as f:
    f.write(str(random.randint(-1000, 1000)) + "+" + str(random.randint(-1000, 1000)) + "-" 
            + str(random.randint(-1000, 1000)) + "/" + str(str(random.randint(-1000, 1000))))

# 2. Зчитує із першого файлу рядок із алгебраїчним виразом, розраховує його та виводить результат;
with open("Practice1/file1.txt", "r") as f:
    result = f.read()

print(eval(result))

# 3. Створює другий файл та записує у нього квадратну матрицю цілих чисел розміром 4*4, закриває файл;

with open("Practice1/file2.txt", "w") as f:
    for i in range(4):
        for j in range(4):
            f.write(str(random.randint(0, 10)) + " ")
        f.write("\n")

# 4. Зчитує із другого файлу матрицю;
        
with open("Practice1/file2.txt", "r") as f:
    matrix = [[int(num) for num in line.split()] for line in f]

# 5. Розраховує суму елементів 2-го та 3-го рядочків та виводить результат.

print(f"Матриця:\n{matrix}")
print(f"Сума 2-го рядка: {sum(matrix[1])}, сума 3-го рядка: {sum(matrix[2])}")