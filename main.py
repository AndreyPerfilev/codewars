# Если мы перечислим все натуральные числа ниже 10, кратные 3 или 5, мы получим 3, 5, 6 и 9.
# Сумма этих кратных равна 23. Завершите решение так,
# чтобы оно возвращало сумму всех кратных 3. или 5 ниже переданного числа.
# Кроме того, если число отрицательное, верните 0. Примечание.
# Если число кратно 3 и 5, считайте его только один раз. С разрешения projecteuler.net (Проблема 1)
numbers = int(input())
d = numbers // 3
b = numbers / 3
c = numbers % 3
print(d)
print(b)
print(c)
numbers_list = []
b = 0
if numbers < 0:
    print(b)
elif numbers > 0:
    while numbers > 0:
        if numbers > 0 and (numbers % 3 == 0 or numbers % 5 == 0):
            numbers_list.append(numbers)
        numbers -= 1
print(numbers)
print(sum(numbers_list))

numbers = int(input())


def ccl(number):
    a = 0
    lists = []
    if number > 0:
        for i in reversed(range(1, number, )):
            if i % 3 == 0 or i % 5 == 0:
                a += i
                lists.append(i)
        return a, lists
    else:
        return 0


print(ccl(numbers))
