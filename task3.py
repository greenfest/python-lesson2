# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

for symbol1 in str1:
    count = 0
    for symbol2 in str2:
        if symbol1 == symbol2:
            count += 1
    print(f"{symbol1} - {count}")        
