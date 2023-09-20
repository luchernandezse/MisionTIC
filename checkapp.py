import psutil
list = psutil.pids()
# Go though list and check each processes executeable name for 'putty.exe'
for i in range(0, len(list)):
    try:
        p = psutil.Process(list[i])
        if p.cmdline()[0].find("p2p.exe") != -1:
            # PuTTY found. Kill it
            p.kill()
            break
    except:
        pass
print (2+4)