import pyautogui
import time
import pandas
#pyautogui.PAUSE = 0.2

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
time.sleep(2)
#Passo 3 - Importar base de dados


tabela = pandas.read_csv('produtos.csv')
#print(tabela)

#Passo 5 - Repetir até acabar a base de dados
for linha in tabela.index:
    #Passo 4 - Cadastrar um produto
    pyautogui.click(x=576, y=255)
    #codigo

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    #tipo

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    #categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    #preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    #custo

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    #obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    
    #enviar o produto
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)


