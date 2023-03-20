import pyautogui
import time

#pyautogui.PAUSE(1,0)


#Acessar o navegador
pyautogui.press("win")
time.sleep(2)
pyautogui.click(x=874, y=340)
pyautogui.write("Chrome")
pyautogui.press("enter")

#Acessar o site
time.sleep(2)
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
123456
#Fazer Login no Site
time.sleep(2)
pyautogui.click(x=885, y=347)
pyautogui.write("lucas.lp")
time.sleep(2)
pyautogui.click(x=1006, y=408)
pyautogui.write("123456")
time.sleep(2)
pyautogui.click(x=965, y=493)

#selecionar e baixar o arquivo
time.sleep(2)
pyautogui.click(x=828, y=254)
time.sleep(2)
pyautogui.click(x=1715, y=165)
time.sleep(2)
pyautogui.click(x=1407, y=562)







