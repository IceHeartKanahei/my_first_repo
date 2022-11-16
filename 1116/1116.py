with open("input.txt") as file:
    content = file.read().splitlines()

my_sum = 0
for item in content:
    my_sum = my_sum + int(item)

for index, item in enumerate(content):
    content[index] = int(item)

for i in range(len(content)):
    content[i] = int(content[i])


print(content)
