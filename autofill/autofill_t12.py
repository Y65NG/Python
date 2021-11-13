import pyautogui as pg

data = []
with open('toronto_12.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        cha, name = line.strip().split(',')
        data.append((cha, name))
   			    					 
index = 1
pg.moveTo(500, 200, 1)
pg.click()
inter = 0.01
while index < len(data):
    if index >= 4:
        pg.press(' ')
        pg.press('tab')
    cha, name = data[index]
    pg.write(cha, interval=inter)
    pg.press('tab')

    pg.write(name, interval=inter)
    pg.press('tab')
    
    pg.press(' ')
    pg.press('tab')
    
    pg.write('June', interval=inter)
    pg.press('tab')
    pg.write('2022', interval=inter) 
    pg.press('tab')
    index += 1

    