from os import listdir
from os.path import join
import os, errno

def getImageNum(rootDir):
    return len(listdir(join(rootDir)))


def safeMkdir(path:str):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise