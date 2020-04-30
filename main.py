import shutil
import msvcrt

def createSession():
    tsize = shutil.get_terminal_size()
    sessionlines = []
    for x in range (1,tsize[1]):
        line = ""
        # Prepare numbers for printing
        if len(str(x))==1:
            num = "0"+str(x)
        else:
            num = str(x)
        line+=num
        # Prepare the rest
        spaces = tsize[0]-len(num)
        line+=spaces*("")
        sessionlines.append(line)
    sessionlines.append("v.0.0 | l:%d v:%d s:%d")
    return (sessionlines)

def editSession(lines):
    lines.reverse()
    for x in lines:
        print(str(x), end = "\033[F", flush = True)
def __main__():
    x = createSession()
    for y in range (0,len(x)):
        if y!= len(x)-1:
            print (x[y])
        else:
            print(x[y] %(2,3,1))
    while True:
        print(msvcrt.getch())
        

if __name__=="__main__":
    __main__()