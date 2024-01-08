import pyautogui
import time
import pandas
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

#Passo 2 - Fazer login
time.sleep(3)
pyautogui.click(x = 584, y = 379)

#diigitar o email
pyautogui.write('pythonimpressionador@gmail.com')

#passar pro campo de senha
pyautogui.press('tab')


#digitar a senha
pyautogui.write('minha senha')
#fazer login
pyautogui.press('tab')
pyautogui.press('enter')

#Passo 3 - Importar base de dados


tabela = pandas.read_csv('produtos.csv')


#Passo 4 - Cadastrar um produto
#Passo 5 - Repetir até acabar a base de dados
