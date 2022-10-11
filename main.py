# ******************************
# Make your Code
# ******************************
numbers = list(map(int, input().split()))
while True:
    for i in range(len(numbers)):
        if numbers[i] < numbers[i-1]:
            (numbers[i-1], numbers[i]) = (numbers[i], numbers[i-1])
    if numbers[0] < numbers[1] < numbers[2] < numbers[3] < numbers[4]:
        break
a = int(input())
for i in range(5):
    if a < numbers[i]:
        numbers.insert(i, a)
        break
print(numbers)