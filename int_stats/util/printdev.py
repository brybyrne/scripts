#====================================================================
def print_device_info(device):

    print '-------------------------------------------------------'
    print '    Device Name:      ',device.name
    print '    Device IP:        ',device.ip_address
    print '    Device username:  ',device.username
    print '    Device password:  ',device.password

    print ''
    print '    Interfaces'
    print ''

    print device.interfaces
    print '-------------------------------------------------------\n\n'