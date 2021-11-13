import pyautogui as pg

data = []
with open('data.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        name, g1, g2 = line.strip().split(',')
        data.append((name, g1, g2))

index = 1
pg.moveTo(500, 200, 1)
pg.click()
inter = 0.01
while index < len(data):
    name, g1, g2 = data[index]
    pg.write(name + ' Semester 1', interval=inter)
    pg.press('tab')
    pg.write('01', interval=inter)
    pg.press('tab')
    pg.write('22', interval=inter)
    pg.press('tab')
    pg.write(g1, interval=inter)
    pg.press('tab')
    pg.press('tab')
    
    pg.write(name + ' Semester 2', interval=inter)
    pg.press('tab')
    pg.write('07', interval=inter)
    pg.press('tab')
    pg.write('22', interval=inter)
    pg.press('tab')
    pg.write(g2, interval=inter)
    pg.press('tab')
    pg.press('tab')
    
    index += 1
    