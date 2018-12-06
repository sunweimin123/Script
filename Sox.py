import os
import re


class Sock:
    def __init__(self,filename):
        self.filename = filename

    def soxCommand(self,remix,reshape):
        os.system(remix)
        os.system(reshape)

    def takeCommand(self):
        pathDir = os.listdir(self.filename)
        for allDir in pathDir:
            child = os.path.join('%s/%s' % (self.filename, allDir))
            child_child = os.listdir(child)
            for childDir in child_child:
                in_wav = os.path.join('%s/%s' % (child, childDir))
                if in_wav.split(".")[1]=="wav":
                    remix_wav =  in_wav.split(".")[0] + "_remix.wav"
                    reshape_wav = in_wav.split(".")[0] + "_shape.wav"
                    remix = "sox "+in_wav+" "+remix_wav+" remix 2 1 4  3 5 6"
                    reshape = "sox "+remix_wav+" -r 16k -b 16 -e signed-integer "+reshape_wav
                    self.soxCommand(remix,reshape)


fileName = "radio"
soc = Sock(fileName)
soc.takeCommand()