"""
File: class_reviews.py
Name: Yi Lin Yang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = '-1'     # exit code for finishing key in score


def main():
    """
    This function will record each scores from SC001 and SC101,
    and judging the maximum, minimum and average score of both classes.
    """
    max_001 = 0
    max_101 = 0
    min_001 = 0
    min_101 = 0
    total_001 = 0
    total_101 = 0
    count_001 = 0
    count_101 = 0
    while True:
        classes = str(input("Which class? "))
        if classes == EXIT:
            break
        else:
            score = int(input("Score: "))
            if classes[2] == '0' and count_001 == 0:        # first data for class SC001
                max_001 = score
                min_001 = score
                total_001 = score
                count_001 += 1
            elif classes[2] == '1' and count_101 == 0:      # first data for class SC101
                max_101 = score
                min_101 = score
                total_101 = score
                count_101 += 1
            elif classes[2] == '0':                         # other data in SC001, compare
                if score > max_001:
                    max_001 = score
                if score < min_001:
                    min_001 = score
                total_001 += score
                count_001 += 1
            else:                                          # other data in SC101, compare
                if score > max_101:
                    max_001 = score
                if score < min_101:
                    min_101 = score
                total_101 += score
                count_101 += 1
    if count_001 == 0 and count_101 == 0:
        print("No class scores were entered")
    else:
        print("=============SC001=============")
        if count_001 == 0:
            print("No score for SC001")
        else:
            avg_001 = total_001 / count_001
            print("Max (001): " + str(max_001))
            print("Min (001): " + str(min_001))
            print("Avg(001): " + str(avg_001))
        print("=============SC101=============")
        if count_101 == 0:
            print("No score for SC101")
        else:
            avg_101 = total_101 / count_101
            print("Max (101): " + str(max_101))
            print("Min (101): " + str(min_101))
            print("Avg(101): " + str(avg_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
