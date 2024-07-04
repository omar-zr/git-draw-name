import json
from datetime import datetime, timedelta
import random
import subprocess

with open('char_patterns.json', 'r') as f:
    char_patterns = json.load(f)

cols, rows = 50, 7
array = [[0 for _ in range(cols)] for _ in range(rows)]

def draw_char(array, char_pattern, start_row, start_col):
    for i, row in enumerate(char_pattern):
        for j, val in enumerate(row):
            array[start_row + i][start_col + j] = val

def draw_string(array, input_string, start_row=0, start_col=0, spacing=1):
    current_col = start_col
    for char in input_string:
        if char in char_patterns:
            draw_char(array, char_patterns[char], start_row, current_col)
            current_col += len(char_patterns[char][0]) + spacing

def addCommit(date):
    try:
        commit_date = datetime.strptime(date, "%Y/%m/%d")
        
        git_date = commit_date.strftime("%a %b %d %H:%M:%S %Y %z")
        salt = random.randint(1000, 9999)
        subprocess.run(f'echo "{date} Salt : {salt}" > foo.txt', shell=True, check=True)
        subprocess.run('git add .', shell=True, check=True)
        subprocess.run(f'git commit --quiet --date "{git_date}" -m "Commit To Draw My Name"', shell=True, check=True)

        print(f"Commit added on {date}")
    except Exception as e:
        print(f"Error adding commit: {e}")    

def execute_commits(array, start_date):
    current_date = datetime.strptime(start_date, "%Y/%m/%d")
    for col in range(cols):
        for row in range(rows):
            if array[row][col] == 1:
                addCommit(current_date.strftime("%Y/%m/%d"))
            current_date += timedelta(days=1)

input_string = "OMAR-ZR"
draw_string(array, input_string)

for row in array:
    print(' '.join(map(str, row)))
# First Sunday of the year
start_date = "2022/01/02"

execute_commits(array, start_date)
