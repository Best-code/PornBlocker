j="good"
import os
directory=os.path.abspath('')
    
lines = ""
def addLink(link):
	hosts=open("C:\Windows\System32\drivers\etc\hosts","a")
	hosts.write("\n0.0.0.0 " + link)
	hosts.close()
	os.system("del " + directory +"\\hostsCopy.txt")
	os.system("more C:\\Windows\\System32\\Drivers\\etc\\hosts >> "+directory+"\\hostsCopy.txt")
	
import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    addLink(link=j)

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

