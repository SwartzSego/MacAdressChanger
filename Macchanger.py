import subprocess
import optparse
import re
def options():
    opt = optparse.OptionParser()
    opt.add_option("-m","--mac",dest="macadress",help="enter mac adress")
    opt.add_option("-i","--interface",dest = "interface",help="enter interface")
    (value,key) = opt.parse_args()
    return value
def changeHW(macadress,iface):
    subprocess.call(["ifconfig",iface,"down"])
    subprocess.call(["ifconfig",iface,"hw","ether",macadress])
    subprocess.call(["ifconfig",iface,"up"])

new = options()
changeHW(new.macadress,new.interface)
print("Start!")
def regex():
    t3mp = subprocess.check_output(["ifconfig"])
    temp = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",t3mp)
    return temp.group(0)
new2 = regex()
if new2 ==  new.macadress:
    print("Mac adress changed.")
else:
    print("Error!")