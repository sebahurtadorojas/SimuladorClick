import numpy as np
import pyautogui,random


def ruido(t,escala=1.0):
    return np.random.normal(0,escala)*t

def movimiento(t,x0,y0,xf,yf,escala=1.0):
    sigm=t**3/(t**3+(1-t)**3)
    x=x0+(xf-x0)*sigm+ruido(t,escala)
    y=y0+(yf-y0)*sigm+ruido(t,escala)
    return x,y

def mover(xf,yf,ale0=5,ale1=10):
    posx,posy=pyautogui.position()
    aleatorio=random.randint(ale0,ale1)
    t_values=np.linspace(0,1,aleatorio)
    x_values,y_values=[],[]
    for t in t_values:
        x,y=movimiento(t,posx,posy,xf,yf)
        x_values.append(x)
        y_values.append(y)
        
    c=0
    while True:
        try:
            pyautogui.moveTo(x_values[c],y_values[c])
        except:
            break
        c=c+1

