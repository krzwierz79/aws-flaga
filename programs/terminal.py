import csv

def terminal():
    with open('/var/www/flaga/dane/terminal.csv', newline='\n') as csvfile:
        shortcuts = list(csv.reader(csvfile, delimiter=';'))#.encode('utf-8').decode()
    return shortcuts

print(terminal())