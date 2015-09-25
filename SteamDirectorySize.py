import os
import sys

#"D:\Steam\SteamApps\common"
dirs = {}

def getDirs(path):
    for item in os.listdir(path):
        dirs[item] = 0

def byteToMB(num):
    return round(num / 1000000.0,2)

def getAll(path):
    pLength = len(path)+1
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            x = os.path.join(dirpath, f)
            y = pLength + os.path.join(dirpath, f)[pLength:].find("\\")
            folderName = x[pLength:y]
            if folderName in dirs:
                try:
                    dirs[folderName] += os.path.getsize(x)
                except:
                    e = sys.exc_info()[0]
                    print "Error: %s" % e

def writeToFile():
    f = open("SteamDirectorySize.txt", 'w')
    f.write("Summary of " + path + "\n------\n")
    for i in dirs:
        tmp = i + ' : ' + str(byteToMB(dirs[i])) + "MB"
        f.write(tmp + "\n")
        print tmp
    f.close()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        path = raw_input("Path to \Steam\SteamApps\common \n Example: D:\Steam\SteamApps\common : ")
    else:
        path = sys.argv[1] 
    print "This will take a bit, and you might see some errors."

    getDirs(path)
    getAll(path)
    writeToFile()
