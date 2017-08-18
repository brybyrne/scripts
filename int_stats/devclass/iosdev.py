import pexpect
from devclass.basedev import NetworkDevice

#========================================================================================
#--- Class to hold information about an IOS network device -------------
class NetworkDeviceIOS(NetworkDevice):

    def __init__(self, name, ip, user='python', pw='python'):
        NetworkDevice.__init__(self, name, ip, user, pw)

    def connect(self):
        print '--- connecting IOS: ssh '+self.username+'@'+self.ip_address

        self.session = pexpect.spawn('ssh '+self.username+'@'
                                     +self.ip_address, timeout=5)
        result = self.session.expect(['Password:', pexpect.TIMEOUT])

        # Check for failure
        if result != 0:
            print '--- Timeout or unexpected reply from device'
            return 0

        print '--- password:',self.password
        self.session.sendline(self.password)
        self.session.expect('#')

    def get_interfaces(self):

        self.session.sendline('term len 0')
        result = self.session.expect('#')

        self.session.sendline('show interface | include is up | error')
        result = self.session.expect('#')

        self.interfaces = self.session.before