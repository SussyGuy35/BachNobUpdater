from requests import get
from shutil import unpack_archive
from os import remove
from configparser import ConfigParser

from tkinter import Tk
from tkinter.filedialog import askdirectory

config = ConfigParser()
url_prefix = "https://github.com/SussyGuy35/BachNobServer"
url = "/raw/main/bachplatformer.zip"
gamename='bachplatformer'

config.read('BachNobUpdater.ini')

try:
    path = config.get('Setting', 'path')
except:
    path = askdirectory(title='Chọn thư mục game')
    config.add_section('Setting')
    config.set('Setting','path',str(path))
    with open('BachNobUpdater.ini', 'w') as configfile:
        config.write(configfile)

try:
    print(f'Cảm ơn bạn đã sử dụng BachNobUpdater v1.1! {gamename} đang được cập nhật!')
    file = get(url_prefix + url)
    print('Đã tải gói!')
    open('package.zip','wb').write(file.content)
    unpack_archive('package.zip',path)
    print('Đã giải nén gói!')
    remove("package.zip")
    print('Đã xóa gói!')
    print('Cập nhật thành công!')
    input('Nhấn Enter để thoát...')
except:
    print('Đã có lỗi xảy ra!')
    input('Nhấn Enter để thoát...')