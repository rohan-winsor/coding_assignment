### Note : All programs are seperated in there own files and the unittest case for all the programs are present in test_code.py

## Question :

1. Write a program that prints the numbers from 1 to N. 
But, for multiples of three,  print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

Below is an example:

Input: N = 17
Output:
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17

********************************************************************************************************************

2.  Given an array print all the numbers that are repeating in it and the number of times they are repeating.

Below is an example:

Input: [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
Output:
1 - 4
2 - 2
5 - 3
8 - 2
4 - 2

Note: The final order of output need not be the same as above. The number after the dash(-) is the repeating count

********************************************************************************************************************


3. Given an object/dictionary, containing names as keys and amount_paid by each of them as
values, write a function that takes such an object as input and calculates the total sum paid by them together.

Below is an example:

Input: {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
Output: 275 

********************************************************************************************************************


4. Develop a program to calculate the total and individual player scores in a cricket match. 
Input would be an array with the index representing the ball number and the value representing the runs scored of that ball.

Assumptions/Tips:
1.	No Extras bowled
2.	Batsman has to be rotated after ever over
3.	Bowler can bowl any number of overs
4.	Assume Batsman 1 is on strike for the first ball.


Below is an example:

Input : [1,2,0,0,4,1,6,2,1,3];

Output:
Total Score: 20
Batsman 1 Score : 4 (1 + 3)
Batsman 2 Score : 16 (2 + 4 + 1 + 6 + 2 + 1)
