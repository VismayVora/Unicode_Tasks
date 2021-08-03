n = int(input("Enter the number of words\n"))
sequence = ""

for i in range(n):

    sequence = sequence + input() + "\n"

sequence_list = sequence.split("\n")

words_dict = {}