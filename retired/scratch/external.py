# Subprocess based external component: will try to use pty
from subprocess import Popen, PIPE, STDOUT, run
class ExternalCommand:
    def __init__(self, command: str, name: str):
        self.command = [command]
        self.name = name
        self.proc = None
    
    def initRun(self, args: list = []):
        cmd = self.command
        cmd.extend(args)
        #self.proc = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True, encoding="utf-8", bufsize=0)
        self.proc = run(cmd, capture_output=True)
        

    def get(self):
        return iter(self.proc.stdout.readline, "")
        #return self.proc

    def doOther(self, cmd: str):
        self.proc.stdin.write(cmd)
    

x = ExternalCommand("powershell.exe", "test")

x.initRun()
print(x.get())
#for y in x.get():
#    print(y)

#x.doOther("cd scratch")
#x.doOther("mkdir test")
#print(x.get().read())