import pyautogui as pg
import pandas as pd
import pynput as pn

loc = ('data.xlsx')
sheet = pd.read_excel(loc)

types = [i for i in sheet['Type'][:]]
names = [i for i in sheet['Name'][:]]
g1 = [i for i in sheet['Grade1'][:]]
g2 = [i for i in sheet['Grade2'][:]]
time = [i for i in sheet['Time'][:]]
school = [i for i in sheet['School'][:]]

print(types)

choices = [types, names, g1, g2, time, school]
choice = input('Type: 1, Name: 2, Grade1: 3, Grade2: 4, Time: 5, School: 6\n')
tabs = int(input('Number of tabs in the end of each line:\n'))

start = int(input('Start from?\n'))

print('Click the place you want to start from')

with pn.mouse.Events() as event:
    for i in event:
        # print(i)
        if isinstance(i, pn.mouse.Events.Click):
            # pos = pg.position()
            break
            

inter = 0.01
while start < len(types):
    print()
    items = [choices[j-1] for j in [int(i) for i in choice]]
    for item in items:
        content = str(item[start])
        pg.write(content, interval=inter)
        pg.press('tab')
    start += 1
    
    for _ in range(tabs): pg.press('tab')