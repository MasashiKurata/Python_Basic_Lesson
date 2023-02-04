import tkinter
import time

import winsound as ws

w=400
h=300

root1=tkinter.Tk()
root1.title("timer")
root1.geometry("400x300")
canvas=tkinter.Canvas(root1,width=w,heigh=h)
canvas.pack()

timer_cnt = 10 # 秒で指定する
min_cnt = timer_cnt // 60
sec_cnt = timer_cnt - 60 * min_cnt

while True:
    timer_str = str(timer_cnt)
    min_cnt = timer_cnt // 60
    sec_cnt = timer_cnt - 60*min_cnt
    min_str = str(min_cnt)
    sec_str = str(sec_cnt)
    if len(sec_str)==1:
        sec_str = "0"+sec_str       
    if len(min_str)==1:
        min_str = "0"+min_str
    canvas.create_text(w/2,h/2,text=min_str+":"+sec_str,font=("",50,"italic"),tag='Y') 
    canvas.update()
    canvas.delete('Y')
    time.sleep(1)
    timer_cnt -=1
    if timer_cnt ==0:
        break

timer_cnt = 0
while True:
    timer_str = str(timer_cnt)
    min_cnt = timer_cnt // 60
    sec_cnt = timer_cnt - 60*min_cnt
    min_str = str(min_cnt)
    sec_str = str(sec_cnt)
    if len(sec_str)==1:
        sec_str = "0"+sec_str
    if len(min_str)==1:
        min_str = "0"+min_str
    canvas.create_text(w/2,h/2,text=min_str+":"+sec_str,fill='red',font=("",50,"italic"),tag='Y') 
    canvas.update()
    canvas.delete('Y')
    time.sleep(1)
    timer_cnt +=1
    ws.Beep(800, 150)
    ws.Beep(800, 150)

