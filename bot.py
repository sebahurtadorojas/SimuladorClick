import Movimiento
import pyautogui
import pyperclip
from PIL import Image
import time



mover=Movimiento.mover
def midPoint(imagen):
    img=Image.open(imagen)
    ancho,alto=img.size
    anc,alt=ancho/2,alto/2
    return anc,alt

def moveToImage(imgSRC,confid=0.9,click=True,ale0=5,ale1=10,varx=0,vary=0):
    anc,alt=midPoint(imgSRC)
    #print("funciona1")
    try:
        ubicacion=pyautogui.locateOnScreen(imgSRC,confidence=confid)
        if ubicacion:
            vx,vy=ubicacion.left+anc,ubicacion.top+alt
            mover(vx,vy,ale0,ale1)
            if click:
                pyautogui.click(vx,vy)
        else:
            print("Imagen no encontrada")
    except:
            print("Imagen no encontrada")

def inPage(key,all=0):
    pyautogui.click(688,53)#Buscador
    pyautogui.hotkey('ctrl','c')
    textCopy=pyperclip.paste()
    if all==1:
        if key==textCopy:
            return True
        else:return False
    else:
        if key in textCopy:
            return True
        else:return False




imagen="imgBoton/edge2.png"
roller="imgBoton/rollercoin.png"
play="imgBoton/play.png"


moveToImage(imagen,confid=0.9,click=True)#edge
moveToImage(roller,confid=0.9,click=True)#roller
moveToImage(play)#play
if inPage("choose_game"):
    print("En pantalla juegos")
