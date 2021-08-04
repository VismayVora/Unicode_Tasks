n = int(input("Enter the number of words\n"))
sequence = ""

for i in range(n):

    sequence = sequence + input() + "\n"

sequence_list = sequence.split("\n")

words_dict = {}

for word in sequence_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

words_dict.pop("")
print(words_dict)

distinct_words = len(words_dict)
print(distinct_words)

for key,value in words_dict.items():
    print(value, end = " ")