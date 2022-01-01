import time
import serial
import telepot
from telepot.loop import MessageLoop
r1='0'
r2='0'
r3='0'
def action(msg):
    global ctrl1,ctrl2,ctrl3,r1,r2,r3
    chat_id = msg['chat']['id']
    command = msg['text']
    print(command)
    if chat_id==1372914804:
        if command=='r1n':
            ctrl1=1
            r1='1'
        if command=='r1f':
            ctrl1=1
            r1='0'
        if command=='r1cf':
            ctrl1=0
        if command=='r2n':
            ctrl2=1
            r2='1' 
        if command=='r2f':
            ctrl2=1
            r2='0'
        if command=='r2cf':
            ctrl2=0
        if command=='r3n':
            ctrl3=1
            r3='1'
        if command=='r3f':
            ctrl3=1
            r3='0'
        if command=='r3cf':
            ctrl3=0
        
telegram_bot = telepot.Bot('2022052147:AAF9LnDZasxhdJPExpYGzck3H44dORJUZNM')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
ctrl1=0
ctrl2=0
ctrl3=0

s= serial.Serial('COM17',9600)
#time.sleep(0.5)
while(1): 
    x=s.readline().decode()
    print(x)
    x=x[8:]
    try:
        x=int(x)
        print(x)
        

        if x>50:
            x=list('000')
            if ctrl1:
                x[0]=r1
            if ctrl2:
                x[1]=r2
            if ctrl3:
                x[2]=r3
            x=''.join(x)
            #x+='\0\n'
            print(x)
            s.write(x.encode())
        #   time.sleep(1)
        else:
            x=list('111')
            if ctrl1:
                x[0]=r1
            if ctrl2:
                x[1]=r2
            if ctrl3:
                x[2]=r3
            x=''.join(x)
            #x+='\0\n'
            print(x)
            s.write(x.encode())
    finally:
        pass
