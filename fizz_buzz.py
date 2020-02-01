"""
1. Write a program that prints the numbers from 1 to N. 
But, for multiples of three,  print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

Below is an example:

Input: N = 17
Output:
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17
"""


def fizz_buzz(num):
    output = []
    for i in range(1, num+1):
        if not i % 3 and not i % 5:
            output.append("FizzBuzz")
        elif not i % 3:
            output.append("Fizz")
        elif not i % 5:
            output.append("Buzz")
        else:
            output.append(str(i))
    return f"{','.join(output)}"
