import requests
import shutil
import os

url_prefix = "https://github.com/SussyGuy35/BachNobServer"
url = "/raw/main/bachplatformer.zip"

try:
    file = requests.get(url_prefix + url)
    print('file downloaded!')
    open('package.zip','wb').write(file.content)
    shutil.unpack_archive('package.zip')
    print('file extracted!')
    os.remove("package.zip")
    print('package file deleted!')
    print('update success!')
except:
    print('Error lmao. Maybe u r not connected to the internet.')    