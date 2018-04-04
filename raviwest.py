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
from tkinter import Tk, Label, Button, Message, Canvas, Frame, Text, Scrollbar, StringVar, Entry, ttk, Place
import paramiko, socket, subprocess, json, os

## VAR
HOST_IP = ''
HOST_PORT = ''
HOST_LOGIN = ''
HOST_PASSWORD = ''
COMMAND_SERVICES = 'pwd'
COMMAND_REBOOT = 'pwd'

## Constructor
client = paramiko.SSHClient()
maFenetre = Tk()

## My functions 
def jsonCreation():
    if os.path.isfile('config.json'):
        print("Fichier OK : pas de création")
    else:
        print("Fichier NOK : création")
        data = {'ip': '', 'port': '', 'login': '', 'password': '', 'services': COMMAND_SERVICES, 'reboot': COMMAND_REBOOT}
        json.dump(data, open('config.json', 'w'), indent=4)

def ping():
    response = subprocess.call(['ping', '-w', '1', '-n', '1', HOST_IP])
    if response == 0:
        pass
    else:
        pass

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
    return HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD

def sauvegarde():
    print("Sauvegarde")    
    data = {'ip': textIP.get(), 'port': textPORT.get(), 'login': textLOGIN.get(), 'password': textPASSWORD.get(), 'services': COMMAND_SERVICES, 'reboot': COMMAND_REBOOT}
    json.dump(data, open('config.json', 'w'), indent=4)

## Tkinter Général 
maFenetre.iconbitmap("logo.ico")
maFenetre.title('Raviwest 0.2')
maFenetre.geometry('200x280+600+300')
maFenetre.resizable(width='False', height='False')

## Tkinter Text : 
def tkinterText(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD):
    textIP = StringVar()
    textIP.set(HOST_IP)
    print(textIP.get())
    textPORT = StringVar()
    textPORT.set(HOST_PORT)
    textLOGIN = StringVar()
    textLOGIN.set(HOST_LOGIN)
    textPASSWORD = StringVar()
    textPASSWORD.set(HOST_PASSWORD)
    return textIP, textPORT, textLOGIN, textPASSWORD

def action():
    print("action")

## Tkinter Constructeur :
def tkinterConstructeur():
    text1Label = Label(maFenetre, text='Choisir le type de reboot désiré :', anchor='center').grid(column='0', row='0', padx='10', pady='5')
    boutonServices = Button(maFenetre, text ='Redémarrer les services', command=rebootServices).grid(column='0', row='1', padx='10', pady='5', sticky='nesw')
    boutonServeur = Button(maFenetre, text ='Redémarrer le serveur', command=rebootServeur).grid(column='0', row='2', padx='10', pady='5', sticky='nesw')
    text2Label = Label(maFenetre, text='--------------------------', anchor='center').grid(column='0', row='3', padx='0', pady='0')
    text3Label = Label(maFenetre, text='Configuration du serveur :', anchor='center').grid(column='0', row='4', padx='10', pady='0')
    textIPLabel = Label(maFenetre, text='IP :').grid(column='0', row='5', padx='0', pady='1', sticky='w')
    entryIP = Entry(maFenetre, textvariable=textIP).grid(column='0', row='5', columnspan='1', padx='0', pady='1', sticky='e')
    textPORTLabel = Label(maFenetre, text='PORT :').grid(column='0', row='6', padx='0', pady='1', sticky='w')
    entryPORT = Entry(maFenetre, textvariable=textPORT).grid(column='0', row='6', columnspan='2', rowspan='1', padx='0', pady='2', sticky='e')
    textLOGINLabel = Label(maFenetre, text='LOGIN :').grid(column='0', row='7', padx='0', pady='1', sticky='w')
    entryLOGIN = Entry(maFenetre, textvariable=textLOGIN).grid(column='0', row='7', columnspan='2', rowspan='1', padx='0', pady='1', sticky='e')
    textPASSWORDLabel = Label(maFenetre, text='PASSWORD :').grid(column='0', row='8', padx='0', pady='1', sticky='w')
    entryPASSWORD = Entry(maFenetre, textvariable=textPASSWORD, show="*").grid(column='0', row='8', columnspan='2', rowspan='1', padx='0', pady='1', sticky='e')
    boutonConf = Button(maFenetre, text ='Valider', command=sauvegarde).grid(column='0', row='9', padx='10', pady='5', sticky='nesw')

## Tkinter MainLoop
jsonCreation()
HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD = configuration()
textIP, textPORT, textLOGIN, textPASSWORD = tkinterText(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD)
tkinterConstructeur()
maFenetre.mainloop()