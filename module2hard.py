random_num = int(input('Enter the random number 3-20: '))
numbers_x = list(range(1, 21))
numbers_y = list(range(2, 21))
answer = []

for x in numbers_x:
    for y in numbers_y:
        if random_num % (x + y) == 0 and x != y:
            z = (str(x) + str(y))
            answer.append(z)
            if x in numbers_y:
                numbers_y.remove(x)

print(answer)
result = ''.join(answer)
print(result)
