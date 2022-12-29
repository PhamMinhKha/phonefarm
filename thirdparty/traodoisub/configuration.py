
class Configure():

    def __init__(self, api):
        self.nhanNV = "https://traodoisub.com/api/?fields={0}&access_token=" + api
        self.guiNVDaLam = "https://traodoisub.com/api/coin/?type={0}&id={1}&access_token=" + api
        self.nhanXu = "https://traodoisub.com/api/coin/?type={0}&id={1}&access_token="+api
