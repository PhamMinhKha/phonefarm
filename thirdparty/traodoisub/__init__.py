from . import configuration
import requests
import json
class Traodoisub:
    def __init__(self):
        self.api = "TDSQfiATMyVmdlNnI6IiclZXZzJCLiUWbuwmcpdWYiojIyV2c1Jye"
        self.name = ""
        self.config = configuration.Configure(self.api)
    def getNV(self, tenNV):
        get = requests.get((self.config.nhanNV).format(tenNV)).json()
        data = get
        return data
    def postNV(self, tenNV, idNV):
        get = requests.get((self.config.guiNVDaLam).format(tenNV, idNV)).json()
        data = get
        print(data)
        return data
    def nhanXu(self, tenNV, id_job):
        get = requests.get((self.config.nhanXu).format(tenNV, id_job)).json()
        data = get
        print(data)
        return data