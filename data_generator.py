import random

d_10_random = random.sample(range(1, 11), 10)
with open("d_10.txt", 'w') as txt_file:
    for value in d_10_random:
        txt_file.write(str(value) + '\n')

# d_40_random = random.sample(range(1, 41), 40)
# with open("d_40.txt", 'w') as txt_file:
#     for value in d_40_random:
#         txt_file.write(str(value) + '\n')

# d_80_random = random.sample(range(1, 200), 80)
# with open("d_80.txt", 'w') as txt_file:
#     for value in d_80_random:
#         txt_file.write(str(value) + '\n')


