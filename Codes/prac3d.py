# Program:
# Read a file line by line and print the word count of each line.
#--------------------------------------------------------------
import sys

def count_word(line):
    word = 1
    for i in line:
        if i==' ':
            word += 1
    return word

f = sys.argv[1]


if __name__=="__main__":
    l = 1
    with open(f) as fobj:
        for line in fobj:
            print(f"Line {l} => No of Words: {count_word(line)}")
            l += 1
