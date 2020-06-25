from subprocess import Popen, PIPE, STDOUT
import msvcrt
from win32 import win32file, win32event
import pywintypes

p = Popen("powershell.exe", stdout=PIPE, stderr=STDOUT, stdin = PIPE, shell=False)


def getText(process):
    outpipe = msvcrt.get_osfhandle(process.stdout.fileno())
    overlapread = pywintypes.OVERLAPPED()
    overlapread.hEvent = win32event.CreateEvent(None,0,0,None)
    r,d = win32file.ReadFile(outpipe,4096,overlapread)

    rc = win32event.WaitForSingleObject(overlapread.hEvent, 10)
    if rc == win32event.WAIT_OBJECT_0:
        n = win32file.GetOverlappedResult(outpipe, overlapread, True)
        x = d[:n]

    finalstr = ""
    for c in x:
        finalstr += chr(c)

    return finalstr

print(getText(p))
print("2nd")
print(getText(p))
print("3")
print(getText(p))
p.stdin.write("echo test".encode())
print(getText(p))
p.stdin.write("exit".encode())
