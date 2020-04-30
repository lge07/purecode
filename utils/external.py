# Subprocess based external component
from subprocess import Popen, PIPE, STDOUT
import msvcrt
from win32 import win32file, win32event
import pywintypes

class ExternalCommand:
    def __init__(self, command: str, name: str):
        self.command = [command]
        self.name = name
        self.proc = None
        self.outpipe = None
    
    def initRun(self, args: list = []):
        cmd = self.command
        cmd.extend(args)
        self.proc = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=False)

    def get(self):
        self.outpipe = msvcrt.get_osfhandle(self.proc.stdout.fileno())
        self.overlapread = pywintypes.OVERLAPPED()
        self.overlapread.hEvent = win32event.CreateEvent(None, 0, 0, None)
        r, d = win32file.ReadFile(self.outpipe, 4096, self.overlapread)
        rc = win32event.WaitForSingleObject(self.overlapread.hEvent, 10)
        if rc == win32event.WAIT_OBJECT_0:
            n = win32file.GetOverlappedResult(self.outpipe, self.overlapread, True)
            return [chr(x) for x in d[:n]]

    def doOther(self, cmd):
        self.proc.stdin.write(cmd)
    

x = ExternalCommand("powershell.exe", "test")

x.initRun()
print(x.get())

print(x.get())
print(x.get())
x.doOther("cd scratch \r".encode())
x.doOther("mkdir test \r".encode())

#print(x.get())