#========================================================================================
class NetworkDevice():

    def __init__(self, name, ip, user='python', pw='python'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_itnerfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'