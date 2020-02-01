"""
4. Develop a program to calculate the total and individual player scores in a cricket match. 
Input would be an array with the index representing the ball number and the value representing the runs scored of that ball.

Assumptions/Tips:
1.	No Extras bowled
2.	Batsman has to be rotated after every over
3.	Bowler can bowl any number of overs
4.	Assume Batsman 1 is on strike for the first ball.


Below is an example:

Input : [1,2,0,0,4,1,6,2,1,3];

Output:
Total Score: 20
Batsman 1 Score : 4 (1 + 3)
Batsman 2 Score : 16 (2 + 4 + 1 + 6 + 2 + 1)
"""


def calculate_total(lst):
    batman1_score, batman2_score, current_batsman1 = [], [], True
    lst = [0] + lst
    for i in range(0, len(lst)):
        if current_batsman1 and lst[i] != 0:
            batman1_score.append(lst[i])
            current_batsman1 = False if lst[i] in [1, 3] else True
        elif not current_batsman1 and lst[i] != 0:
            batman2_score.append(lst[i])
            current_batsman1 = True if lst[i] in [1, 3] else False
        if not i % 6 and i != 0:
            current_batsman1 = not current_batsman1

    b1, b2 = list(map(str, batman1_score)), list(map(str, batman2_score))
    b1, b2 = f"{sum(batman1_score)} ({' + '.join(b1)})", f"{sum(batman2_score)} ({' + '.join(b2)})"
    str1 = f"Total Score {sum(batman1_score + batman2_score)} \nBatsman 1 Score : {b1} \nBatsman 2 Score : {b2}"
    return str1

