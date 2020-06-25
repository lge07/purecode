from win32 import win32api, win32file

hStdIn = win32api.GetStdHandle(win32api.STD_INPUT_HANDLE)
hStdOut = win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE)

rc, data = win32file.WriteFile(hStdOut,512)
print(data)