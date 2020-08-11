import datetime

def getTime():
    currentDT=datetime.datetime.now()
    return str(currentDT)

if __name__=='__main__':
    print(getTime())