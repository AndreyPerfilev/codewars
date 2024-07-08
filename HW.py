def solution(number):
    numbers_list = []
    if number > 0:
        while number > 0:
            if (number % 3 == 0 or number % 5 == 0):

                numbers_list.append(number)
            number -= 1


        return sum(numbers_list)
    else:
        return 0


a = solution(7)
print(a)
