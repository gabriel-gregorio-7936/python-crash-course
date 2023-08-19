def solution(number):
    # Declaring the variables
    solutions = []
    counter = 0

    if number <= 3:
        # If limit minus or equal to 3 function returns 0 because there are no numbers to sum
        return 0
    else:
        # Else it tests if the numbers are multiples of 3 or 5 and store them in a list
        for value in range(1, number):
            if value % 3 == 0:
                solutions.append(value)
            elif value % 5 == 0:
                solutions.append(value)
        # Finally it runs a loop that sums everythin in the list
        for i in solutions:
            if counter == 0:
                result = i
                counter += 1
            else:
                result += i
                counter += 1

        return result

print(solution(10))