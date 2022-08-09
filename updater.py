import requests
import shutil
import os

url_prefix = "https://github.com/SussyGuy35/BachNobServer"
url = "/raw/main/bachplatformer.zip"
gamename='bachplatformer'

try:
    print(f'Welcome to BachNobUpdater. {gamename} is being updated!')
    file = requests.get(url_prefix + url)
    print('File downloaded!')
    open('package.zip','wb').write(file.content)
    shutil.unpack_archive('package.zip')
    print('File extracted!')
    os.remove("package.zip")
    print('Package file deleted!')
    print('Update successful!')
    input('Press Enter to quit...')
except:
    print('Error lmao. Maybe u r not connected to the internet.')    