import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=765, y=320)

time.sleep(5)

pyautogui.click(x=284, y=66)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=417, y=407)
login = 'c.oliveiradev@gmai.com'
pyautogui.write(login)
pyautogui.press('tab')
senha = '12345678'
pyautogui.write(senha)
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(5)

tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.click(x=400, y=292)

    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)