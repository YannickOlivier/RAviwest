## Simple application to reboot Aviwest Servers
## Sorry, it's my first app in Python

## Modules
from tkinter import Tk, Label, Button, Message, Canvas, Frame, Text, Scrollbar, StringVar, Entry, ttk, Place
import paramiko, socket, subprocess, json

## VAR
HOST_IP = ''
HOST_PORT = ''
HOST_LOGIN = ''
HOST_PASSWORD = ''

## Parameters for StringVar
#parametersIP = StringVar()


## Constructor
client = paramiko.SSHClient()
maFenetre = Tk()

## My functions 
def ping():
    response = subprocess.call(['ping', '-w', '1', '-n', '1', HOST_IP])
    if response == 0:
        pass
    else:
        pass

def connectSSH():
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD)

def closeSSH():
    client.close()

def commandSSH(command):
    client.exec_command(command)

def rebootServices():
    pass
    connectSSH()
    commandSSH("pwd; pwd")
    closeSSH()

def rebootServeur():
    pass

def configuration():
    conf = json.load(open('config.json', 'rb'))
    HOST_IP = conf['ip']
    HOST_PORT = conf['port']
    HOST_LOGIN = conf['login']
    HOST_PASSWORD = conf['password']
    return HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD

def sauvegarde(textIP):
    print("salu", textIP)
    data = {"ip": "192.168.1.4", "port": "22", "login": "toto", "password": "totoPS"}
    json.dump(data, open('config.json', 'wb') )

## Tkinter Général 
maFenetre.iconbitmap("logo.ico")
maFenetre.title('Raviwest 0.1')
maFenetre.geometry('220x300')
maFenetre.resizable(width='False', height='False')
#maFenetre.rowconfigure(0, weight='1')
#maFenetre.columnconfigure(0, weight='1')



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

## Tkinter Constructeur :
def tkinterConstructeur(textIP, textPORT, textLOGIN, textPASSWORD):
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
    entryPASSWORD = Entry(maFenetre, textvariable=textPASSWORD).grid(column='0', row='8', columnspan='2', rowspan='1', padx='0', pady='1', sticky='e')
    boutonConf = Button(maFenetre, text ='Valider', command=sauvegarde(textIP.get())).grid(column='0', row='9', padx='10', pady='5', sticky='nesw')

## Tkinter MainLoop
HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD = configuration()
textIP, textPORT, textLOGIN, textPASSWORD = tkinterText(HOST_IP, HOST_PORT, HOST_LOGIN, HOST_PASSWORD)
tkinterConstructeur(textIP, textPORT, textLOGIN, textPASSWORD)
maFenetre.mainloop()