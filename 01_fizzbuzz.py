"""Problem: FizzBuzz
Print numbers from 1 to n. For multiples of 3 print "Fizz", for multiples
of 5 print "Buzz", for multiples of both print "FizzBuzz".
"""

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    print(fizzbuzz(20))
