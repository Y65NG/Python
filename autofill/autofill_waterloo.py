import pyautogui as pg

data = []
with open('waterloo_12.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        name, level = line.strip().split(',')
        # print(line)
        data.append((name, level))

index =	3 
pg.moveTo(500, 200, 1)
pg.click()
inter = 0.01
while index < len(data):
    name, level = data[index]
    pg.write(name, interval=inter)
    pg.press('tab')
    pg.write(level, interval=inter)
    pg.press('tab')
    pg.write('Guangzhou Foreign Language Sch', interval=inter)
    pg.press('tab')
    pg.write('06/01/2022')
    pg.press('tab')
    pg.press('tab')
    index += 1
    