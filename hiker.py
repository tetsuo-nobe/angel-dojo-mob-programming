'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''
# 1
def global_answer():
    return 6 * 7

# 2
def add_one(num):
    return str(num + 1)

# 3
def check_even_odd(num):
    result = num % 2
    if result == 0:
        return "even"
    return "odd"

# 4
def fizz(num):
    result = num % 3
    if result == 0:
        return "Fizz"
    return str(num)

# 5
def buzz(num):
    result = num % 3
    if result == 0:
        return "Fizz"
    result = num % 5
    if result == 0:
        return "Buzz"
    return str(num)

# 6
def fizzbuzz(num):
    result = num % 15
    if result == 0:
        return "FizzBuzz"
    result = num % 3
    if result == 0:
        return "Fizz"
    result = num % 5
    if result == 0:
        return "Buzz"
    return str(num)

# 7
def fizzbuzz_with_numcheck(num):
    if isinstance(num, int) == False:
        raise ValueError
    if num <=0:
        raise ValueError
    result = num % 15
    if result == 0:
        return "FizzBuzz"
    result = num % 3
    if result == 0:
        return "Fizz"
    result = num % 5
    if result == 0:
        return "Buzz"
    return str(num)

# 8
def fizzbuzzplus(num):
    result = ''
    if num % 3 == 0 or '3' in str(num):
       result += 'Fizz'
    if num % 5 == 0 or '5' in str(num):
       result += 'Buzz'
    if result:
       return result
    return str(num)


