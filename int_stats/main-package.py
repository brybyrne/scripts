from util.readdev import read_devices_info
from util.printdev import print_device_info

# Main program - The script will log into the device with SSH and run 'show interface' and output the error counts on
# interfaces that are in an up state. The script will use the module read_device_info to read in the device file 'term-serv.txt'
# to run the commands against. The module print_device_info will use to send the output to terminal.

devices_list = read_devices_info('term_serv.txt')

for device in devices_list:

  print '==== Devices ==================================================================='

  device.connect()
  device.get_interfaces()
  print_device_info(device)