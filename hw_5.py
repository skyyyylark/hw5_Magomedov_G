import re
with open("./sf/data_corey.txt", "r") as text:
    num_nums = 0
    end7 = 0
    for line in text:
        find = re.compile(r"[\d]{3}-[\d]{3}-[\d]{4}")
        num7 = re.compile(r"[\d]{3}-[\d]{3}-[\d]{3}7$")
        found = re.search(find, line)
        found7 = re.search(num7, line)
        if found:
            num_nums += 1
        if found7:
            end7 += 1


print(num_nums)
print(end7)
text = text.close()