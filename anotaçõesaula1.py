# Anotações primeira aula de python intensivo

# Primeira coisa para começar a fazer um projeto:
# 1- Escrever em portugues o passo a passo

# Biblioteca Python:  import pyautogui (automatizar o mouse, teclado e tela)
#                     import pyperclip (vem junto com o pyautogui) (ajuda com os problema do pyautogui que não reconhece caracteres especiais) (copia e cola links )
#                     import time (para o cod por algum tempo) (Comando time.sleep = 1 / quando cheagr nessa linha o cod vai para por 3 seg)
#                     import pandas as pd (trabalhar com base de dados) (as pd: muda o jeito que voce chama ele no cod)

# Comandos pyautogui: pyautogui.hotkey("ctrl","letra") (atalho de teclas)
#                     pyautogui.write ("o que voce quer escrever") (escrever)
#                     pyautogui.click (x = tanto, y = tanto, clicks = quant de clicks, button = "left/right") (clicar com o mouse)
#                     pyautogui.press (pressior apenas uma tecla)
#                     pyautogui.PAUSE = 1 (tempo que o pyautogui espera para realizar cada linha do cod)
#                     pyautogui.position() (É um código que fala pra voce onde a posição do mouse esta no momento que rodou o cod)
#

# Comandos pyperclip: pyperclip.copy("link") (copia algum texto) (utilizado quando der problema com o pyautogui.write)
#
#

# Comandos pandas:    variavel = pd.read_excel(r"passar o caminho inteiro do arquivo - nomedoarquivo.comextensao", sheets = "nome ou posicao da aba") (vai armazenar os dados do excel na variavel escolhida)
#                     variavel = tabela["Coluna desejada"].sum/med/count() (vai armazenar na variavel escolhida a coluna desejada, e de acordo com voce esolher vai somar ou fazer a media entre outros)
#                       
#


# Pyautogui
# - Para acessar site precisa de um delay, pois o pyautogui pode atropelar codigos (resolve com pyautogui.PAUSE)



# Dicas:
# Trabalhar com base de dados utilizar a bibliotecas pandas
# Sempre que estiver passando um caminho de um arquivo coloque um r antes das "", que mostra que é um string raw (leia o texto exatamente como escrevi)
# Texto em python com várias linhas começa com três aspas e fecha com  três aspas: """ aaaa  """