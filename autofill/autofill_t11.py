import pyautogui as pg

data = []
with open('toronto_11.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        cha, name, grade = line.strip().split(',')
        data.append((cha, name, grade))
        
index = 6
pg.moveTo(500, 200, 1)
pg.click()
inter = 0.01
while index < len(data):
    if index >= 4:
        pg.press(' ')
        pg.press('tab')
    cha, name, grade = data[index]
    pg.write(cha, interval=inter)
    pg.press('tab')

    pg.write(name, interval=inter)
    pg.press('tab')
    
    pg.write(grade, interval=inter)
    pg.press('tab')
    
    pg.write('100', interval=inter)
    pg.press('tab')
    
    pg.write('July', interval=inter)
    pg.press('tab')
    
    pg.write('2020', interval=inter)
    pg.press('tab')
    
    index += 1