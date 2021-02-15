import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

dict = open("dictionary.txt")

dict_list = []
for line in dict:
    line = line.strip()
    dict_list.append(line)

dict.close()
print(len(dict_list))
print("--- Linear Search ---")

alice = open("AliceInWonderLand200.txt")


line_count = 1
for line in alice:

    words = split_line(line)
    for word in words:
        i = 0
        while i < len(dict_list) and word.upper() != dict_list[i]:
            i += 1
        if i >= len(dict_list):
            print("Possible misspelling on Line", line_count, ":", word)
    line_count += 1

alice.close()
alice = open("AliceInWonderLand200.txt")

print("--- Binary Search ---")
line_count = 1
for line in alice:
    words = split_line(line)
    for word in words:
        lower_bound = 0
        upper_bound = len(dict_list) - 1
        found = False

        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2

            if dict_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dict_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print("Possible misspelling on Line", line_count, ":", word)
    line_count += 1

alice.close()
