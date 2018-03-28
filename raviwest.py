## Simple application to reboot Aviwest Servers
## Sorry, it's my first app in Python

## Modules
from tkinter import Tk, Label, Button, Message, Canvas, Frame, Text, Scrollbar, StringVar, Entry
import paramiko, socket, subprocess

## VAR
HOST_IP = ''
HOST_PORT = ''
HOST_LOGIN = ''
HOST_PASSWORD = ''


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

## Tkinter Général 
maFenetre.iconbitmap("logo.ico")
maFenetre.title('Raviwest 0.1')
maFenetre.geometry('300x300')
maFenetre.resizable(width='False', height='False')
maFenetre.rowconfigure(0, weight='1')
maFenetre.columnconfigure(0, weight='1')


## Tkinter Constructeur
text1Label = Label(maFenetre, text='Choisir le type de reboot désiré :', pady='5').grid(column='0', row='0')
boutonServices = Button(maFenetre, text ='Redémarrer les services', command=rebootServices).grid(column='0', row='1')

# sticky='n'

## Tkinter MainLoop
maFenetre.mainloop()