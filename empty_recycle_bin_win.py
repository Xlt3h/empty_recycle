import winshell as ws
import ctypes


try:
    ws.recycle_bin().empty(sound=True)
    #ctypes.windll.user32.MessageBoxW(0,"Your recycle bin has been erased", "Successful", 0)
except:
    ctypes.windll.user32.MessageBoxW(0,"Cannot Erase your Recycle Bin please restart the application", "Error", 0)
