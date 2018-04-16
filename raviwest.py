#  This file is part of Raviwest.
#  Simple application to reboot Aviwest Streamhub services and server.
#
#  Raviwest is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Raviwest is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Raviwest.  If not, see <http://www.gnu.org/licenses/>.
#
#  Created by Yannick Olivier in 2018. France 3 Centre Val de Loire.
#
#  Sorry, it's my first app in Python

## Modules
from tkinter import Tk, Label, Button, Message, Canvas, Frame, Text, Scrollbar, StringVar, Entry, ttk, Place, Menu, messagebox, Toplevel
import paramiko, socket, subprocess, json, os

## VAR
HOST_IP = ''
HOST_PORT = ''
HOST_LOGIN = ''
HOST_PASSWORD = ''
COMMAND_SERVICES = 'pwd'
COMMAND_REBOOT = 'reboot'

## Constructor
client = paramiko.SSHClient()
maFenetre = Tk()

## My functions 
def jsonCreation():
    if os.path.isfile('config.json'):
        print("Fichier Config OK : pas de création")
    else:
        print("Fichier NOK : création")
        data = {'ip': '', 'port': '', 'login': '', 'password': ''}
        json.dump(data, open('config.json', 'w'), indent=4)
    if os.path.isfile('commandes.json'):
        print("Fichier Commandes OK : pas de création")
    else:
        print("Fichier NOK : création")
        data = {'services': COMMAND_SERVICES, 'reboot': COMMAND_REBOOT}
        json.dump(data, open('commandes.json', 'w'), indent=4)

def connectSSH(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD):
    try:
        print("ConnectSSH")
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD)
    except:
        print("Le serveur ne répond pas")

def closeSSH():
    client.close()

def commandSSH(command):
    print("commandSSH")
    client.exec_command(command)

def rebootServices():
    pass
    connectSSH(textIP.get(), textPORT.get(), textLOGIN.get(), textPASSWORD.get())
    commandSSH("pwd; pwd")
    closeSSH()

def rebootServeur():
    print("Reboot demandé")
    print(textIP.get())
    connectSSH(textIP.get(), textPORT.get(), textLOGIN.get(), textPASSWORD.get())
    commandSSH(COMMAND_REBOOT)
    closeSSH()

def configuration():
    conf = json.load(open('config.json', 'rb'))
    HOST_IP = conf['ip']
    HOST_PORT = conf['port']
    HOST_LOGIN = conf['login']
    HOST_PASSWORD = conf['password']
    print("HOST_IP", HOST_IP)
    return HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD

def sauvegarde():
    print("Sauvegarde")
    print("SAUV_IP", textIP.get())
    data = {'ip': textIP.get(), 'port': textPORT.get(), 'login': textLOGIN.get(), 'password': textPASSWORD.get()}
    json.dump(data, open('config.json', 'w'), indent=4)

def ping():
    conf = json.load(open('config.json', 'rb'))
    HOST_IP = conf['ip']
    result = subprocess.Popen(["ping", "-n", "1", "-w", "5", "-4", HOST_IP],shell=True, bufsize=-1).wait()
    if result == 0:
        canvasPing('chartreuse3')
    else:
        canvasPing('red2') 
    maFenetre.after(1000, ping)

def canvasPing(color):
    canvas = Canvas(width=20, height=20, bg=color).grid(column='0', row='4', columnspan='1', padx='0', pady='0', sticky='e')

## Tkinter Général 
maFenetre.iconbitmap("logo.ico")
maFenetre.title('Raviwest 0.5')
maFenetre.geometry('200x175+600+300') #180
maFenetre.resizable(width='False', height='False')

## Tkinter Text : 
def tkinterText(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD):
    textIP = StringVar()
    textIP.set(HOST_IP)
    textPORT = StringVar()
    textPORT.set(HOST_PORT)
    textLOGIN = StringVar()
    textLOGIN.set(HOST_LOGIN)
    textPASSWORD = StringVar()
    textPASSWORD.set(HOST_PASSWORD)
    return textIP, textPORT, textLOGIN, textPASSWORD

def menu1():
    maFenetreConfig = Toplevel()
    maFenetreConfig.iconbitmap("logo.ico")
    maFenetreConfig.title('Configuration :')
    maFenetreConfig.geometry('200x158+600+350')
    maFenetreConfig.resizable(width='False', height='False')
    #monIP = StringVar()
    #monIP = HOST_IP
    #print("Après StringVar", monIP)
    text5Label = Label(maFenetreConfig, text='Configuration du serveur :').grid(column='0', row='0', padx='5', pady='3', columnspan='2')
    textIPLabel = Label(maFenetreConfig, text='IP :').grid(column='0', row='1', padx='0', pady='1', sticky='w')
    entryIP = Entry(maFenetreConfig, textvariable=textIP).grid(column='1', row='1', columnspan='1', padx='0', pady='1', sticky='e')
    textPORTLabel = Label(maFenetreConfig, text='PORT :').grid(column='0', row='2', padx='0', pady='1', sticky='w')
    entryPORT = Entry(maFenetreConfig, textvariable=textPORT).grid(column='1', row='2', columnspan='1', rowspan='1', padx='0', pady='2', sticky='e')
    textLOGINLabel = Label(maFenetreConfig, text='LOGIN :').grid(column='0', row='3', padx='0', pady='1', sticky='w')
    entryLOGIN = Entry(maFenetreConfig, textvariable=textLOGIN).grid(column='1', row='3', columnspan='1', rowspan='1', padx='0', pady='1', sticky='e')
    textPASSWORDLabel = Label(maFenetreConfig, text='PASSWORD :').grid(column='0', row='4', padx='0', pady='1', sticky='w')
    entryPASSWORD = Entry(maFenetreConfig, textvariable=textPASSWORD, show="*").grid(column='1', row='4', rowspan='1', padx='0', pady='1', sticky='e')
    boutonConf = Button(maFenetreConfig, text ='           Valider         ', command=sauvegarde).grid(column='0', row='5', padx='5', pady='10', columnspan='2')
   # maFenetreConfig.mainloop()

def menu2():
    messagebox.showinfo("Informations :", "Programme développé par Yannick Olivier\nFrance 3 Centre-Val de Loire\nAvril 2018\nhttp://github.com/YannickOlivier")

## Tkinter Constructeur :
def tkinterConstructeur():
    menubar = Menu(maFenetre)
    menubar.add_cascade(label="Configuration", command=menu1)
    menubar.add_cascade(label="?", command=menu2)
    maFenetre.config(menu=menubar)
    text1Label = Label(maFenetre, text='Choisir le type de reboot désiré :', anchor='center').grid(column='0', row='0', padx='10', pady='5')
    boutonServices = Button(maFenetre, text ='Redémarrer les services', command=rebootServices).grid(column='0', row='1', padx='10', pady='5', sticky='nesw')
    boutonServeur = Button(maFenetre, text ='Redémarrer le serveur', command=rebootServeur).grid(column='0', row='2', padx='10', pady='5', sticky='nesw')
    text2Label = Label(maFenetre, text='--------------------------', anchor='center').grid(column='0', row='3', padx='0', pady='0')
    text3Label = Label(maFenetre, text='Etat du serveur (ping) :', anchor='center').grid(column='0', row='4', padx='5', pady='0', sticky='w')
    maFenetre.mainloop()

## Tkinter MainLoop
jsonCreation()
HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD = configuration()
textIP, textPORT, textLOGIN, textPASSWORD = tkinterText(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD)
ping()
tkinterConstructeur()


