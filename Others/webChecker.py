import urllib.request
import ssl
from datetime import datetime
from socket import timeout 

urlList = {
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx",
    "https://some_URL/xxxxx"
}

class checkList: 
    errorMessage = ""
    url = ""
    isAvailable = False

    def __init__(self, errorMessage, url, isAvailable):
        self.errorMessage = errorMessage
        self.url = url
        self.isAvailable = isAvailable

#Bypass SSL cert verification 
gcontext = ssl.SSLContext()  # Only for gangstars

def webCheck(vm):
    try:
        contents = str(urllib.request.urlopen(vm,context=gcontext,timeout=10).read())
        if "password" in contents and "Something" in contents:
            return True
        return False
    except Exception as ex:
        return False

print("Make sure you are connected to VPN before running this script, otherwise, you won't be reaching the URL's listed.")
print(f"Start time: {datetime.now()}")

for vm in urlList:
    if webCheck(vm):
        print(vm + " it's web loaded correctly")
    else:
        print(vm + " it's web couln't be loaded")


#Content to be evaluated
print("Exceution completed")
print(f"End time: {datetime.now()}")