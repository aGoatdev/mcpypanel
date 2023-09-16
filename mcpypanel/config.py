import os

from yaml import load, dump

class ConfFile:
    def __init__(self,parent):
        self.parent = parent
        self._datas = {}
        self._file = parent._DIR+"config.yaml"
        self.log = self.parent.log.get_child("config")
        self.load()
    
    def load(self):
        if not os.path.exists(self._file):
            self.log.fatal("Config file not found! Aborting startup.")
            self.parent._abort_startup = True
            return
        with open(self.file) as f:
            self._datas = load(f)
    def save(self):
        with open(self.file,'w') as f:
            f.write(dump(self._datas))
    
    def __getitem__(self, index):
        if not (type(index) in (str, bytes)):
            raise Exception("a str/bytes must be passed")
        return self.datas[index]
    def __setitem__(self, index, value):
        if not (type(index) in (str, bytes)):
            raise Exception("a str/bytes must be passed")
        self.datas[index] = value
        return self.data[index]
    def __delattr__(self, index):
        if not (type(index) in (str, bytes)):
            raise Exception("a str/bytes must be passed")
        del self.datas[index]
    def __delitem__(self, index):
        if not (type(index) in (str, bytes)):
            raise Exception("a str/bytes must be passed")
        del self.datas[index]
    def __iter__(self):
        for i in self.datas:
            yield i