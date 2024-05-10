import re
import subprocess

devices_ids = {
    "046d:c092": "G203 Lightsync Mouse",
    "046d:c084": "G203 Prodigy Mouse"
}

def lsusb():
    device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb")
    global devices
    devices = []
    for i in df.split(b'\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = str(dinfo.pop('bus')) + ":" + str(dinfo.pop('device'))
                devices.append(dinfo)
                
def devices():
    lsusb()
    ind = 0
    device_names = []
    for item in devices:
        if "Logitech" in str(devices[ind]["tag"]):
            device_names.append(str(devices[ind]["tag"])[2:-1] + "," + str(devices[ind]["id"])[2:-1])
            
        ind += 1
    return device_names
        
def raw_device_codes():
    lsusb()
    ind = 0
    raw_codes = []
    for item in devices:
        if "Logitech" in str(devices[ind]["tag"]):
            raw_codes.append(str(devices[ind]["id"])[2:-1])
            
        ind += 1
        
    return raw_codes

def identify_connected_devices(device_ids):
    ind = 0
    device_info = []
    
    for i in range(len(device_ids)):
        if device_ids[ind] in devices_ids:
            device_info.append(devices_ids[device_ids[ind]])
        ind += 1
        
    return device_info