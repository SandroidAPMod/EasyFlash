from tkinter import *
from tkinter import ttk 
import tkinter as tk
import os
import subprocess
import sys

# Pasta onde estão os cores
path = r"games/"
files = os.listdir(path)

# Lista de cores e games
flash_cores = []
games_list = []

# Pasta onde estão os games
flash_core_path = r"flash core/"

cores_exe = os.listdir(flash_core_path)

# Lista os cores na pasta "flash cores"
for core in cores_exe:
    # make sure file is an image
    if core.endswith(('.exe')):
        flash_cores_exe = flash_core_path + core
        flash_cores.append(core)




# Seta os executaveis e os games
def playgame():
    selected = str(lb_games.get(lb_games.curselection()))
    core_exe = str(cb_cores.get())
    core_exe_selected = ("flash core/" + core_exe)
    game_selected = ("games/" + selected)
    execute_flash = core_exe_selected , game_selected
    execute = subprocess.Popen(execute_flash)
    execute.communicate()




# Cria a tela
app = Tk()
app.title("Easy Flash")
app.geometry("440x300")
icon = PhotoImage(file="icon-32.png")
app.iconphoto(False, icon)
app.iconbitmap("icon.ico")

# Cria a mini lista de cores
bt_play = Button(app,text="PLAY!",width=25,command=playgame)
cb_cores = ttk.Combobox(app, values=flash_cores, state="readonly")
cb_cores.current(9)

cb_cores.pack()

# Criar a lista de games
lb_games = Listbox(app,
                   width=70
                   )


# Lista todos os arquivos .swf
for file in files:

    if file.endswith(('.swf')):
        games_path = path + file
        lb_games.insert(END,file)
        
# Adiciona os elemntos na tela        
bt_play.pack(side = BOTTOM, padx=45)
lb_games.pack(side = LEFT, fill = BOTH)
scrollbar = Scrollbar(app)
scrollbar.pack(side = RIGHT, fill = BOTH)
lb_games.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = lb_games.yview)





# Cria a janela e trava o redirecionamento.
app.resizable(False,False)
app.mainloop()