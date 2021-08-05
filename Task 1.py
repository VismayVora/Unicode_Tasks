n = int(input("\nEnter the number of words\n"))
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
#print(words_dict)

print("\nOutput")
print(len(words_dict))


for key,value in words_dict.items():
    print(value, end = " ")

key_list = list(words_dict.keys())
val_list = list(words_dict.values())


n1 = 1
n2 = 1
for value in val_list:
    if n1 < value:
        n1 = value
    if n2 > value:
        n2 = value

position_highest = val_list.index(n1)
position_lowest = val_list.index(n2)

print("\n")
print("\nThe most repeated word is '{}'.".format(key_list[position_highest]))
print("The least repeated word is '{}'.".format(key_list[position_lowest]))