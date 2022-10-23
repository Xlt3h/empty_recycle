import winshell as ws
import ctypes

style = 1 #ok and cancel
msgbox = ctypes.windll.user32.MessageBoxW(0,"Are you sure you want to clear your recycle bin", "Erase Recycle Bin", style)

if msgbox == 1:
    try:
        ws.recycle_bin().empty(sound=True)
        ctypes.windll.user32.MessageBoxW(0,"Your recycle bin has been erased", "Successful", 0)
    except:
        ctypes.windll.user32.MessageBoxW(0,"Cannot Erase your Recycle Bin please restart the application", "Error", 0)
