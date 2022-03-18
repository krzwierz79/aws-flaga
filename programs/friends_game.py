import random
import csv

def read_riddle():
    with open('/var/www/flaga/programs/ffriends.csv', newline='\n') as csvfile:
        entries = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
        return random.choice(entries)

# entry, mean_1, mean_2, correct = read_riddle() 
# print(entry)
# print(mean_1)
# print(mean_2)
# print(correct)


# def read_lines():
#     text_lines = open('friends.csv', encoding='utf-8').readlines()

#     poem_lines = []
#     for line in text_lines:
#         line = line.strip()
#         poem_lines.append(line)
    
#     return poem_lines

# print(friends_game())