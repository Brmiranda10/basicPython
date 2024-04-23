def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


try:
    user_input = int(input("Enter a number: "))

    for x in range(user_input):
        user_input = collatz(user_input)
except ValueError:
    print("Error")
