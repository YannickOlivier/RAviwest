from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\yannick.olivier\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\yannick.olivier\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

includes = []
include_files = [r"C:\\Users\\yannick.olivier\\AppData\\Local\\Programs\\Python\\Python36\DLLs\\tcl86t.dll",
                 r"C:\\Users\\yannick.olivier\\AppData\\Local\\Programs\\Python\\Python36\DLLs\\tk86t.dll",
                 r"C:\\appli_ftv\\_Yannick\\Github\\RAviwest\\logo.ico"]
packages = ['paramiko', 'cffi', 'cryptography']


setup(
    name = "RAviwest",
    options = {"build_exe": {"includes": includes, "include_files": include_files, "packages": packages}},
    version = "0.5",
    description = 'A simple app to reboot Aviwest StreamHub',
    executables = [Executable(script="raviwest.py", base='Win32GUI', icon="logo.ico")]
)