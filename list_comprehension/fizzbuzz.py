fizzbuzz = ["Fizz"*(not i%3) + "Buzz"*(not i%5) or i for i in range(1, 100)]

for el in fizzbuzz:
    print(el)