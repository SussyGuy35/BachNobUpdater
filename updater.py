print('Chào mừng đến với BachNobUpdater!')
from requests import get
from os import remove, system
from configparser import ConfigParser

config = ConfigParser()
url_prefix = "https://raw.githubusercontent.com/sussyguy35/BachNobServer/main/"
fname = "BachNobUpdater.ini"
pw = 'tlcktdchlcslotc'
config.read('BachNobUpdaterConfig.ini')
# get current_version
try:
    current_version_str = config.get('Setting', 'current_version')
    current_version = current_version_str.split(".")
    current_main, current_minor,current_patch = int(current_version[0]), int(current_version[1]), int(current_version[2])
except:
    current_main, current_minor,current_patch = 0,0,0
    current_version_str = f'{current_main}.{current_minor}.{current_patch}'
    config.add_section('Setting')
    config.set('Setting','current_version',current_version_str)
    with open('BachNobUpdaterConfig.ini', 'w') as configfile:
        config.write(configfile)
print('Vui lòng tắt game nếu game đang chạy! Điều này là cần thiết để trình cập nhật hoạt động đúng!')
input('Nhấn Enter để xác nhận...')
# get newest ver
print('Đang tìm bản cập nhật...')
try:
    newest_ver_get = get(url_prefix+fname)
    open(fname,'wb').write(newest_ver_get.content)
    config.read(fname)
    newest_ver_str = config.get('Setting','version')
    newest_ver = newest_ver_str.split('.')
    newest_main, newest_minor,newest_patch = int(newest_ver[0]), int(newest_ver[1]), int(newest_ver[2])
    remove(fname)
    print(f'Phiên bản hiện tại: {current_version_str}, phiên bản trên máy chủ: {newest_ver_str}')
except:
    print('Đã có lỗi xảy ra!')  
try:
    if newest_main > current_main:
        state = 'greater'
    elif newest_main == current_main and newest_minor> current_minor:
        state = 'greater'
    elif newest_main == current_main and newest_minor == current_minor and newest_patch > current_patch:
        state = 'greater' 
    elif newest_main == current_main and newest_minor == current_minor and newest_patch == current_patch:
        state = 'equal'
    elif newest_main < current_main:
        state = 'lower'
    elif newest_main == current_main and newest_minor< current_minor:
        state = 'lower'
    elif newest_main == current_main and newest_minor == current_minor and newest_patch < current_patch:
        state = 'lower'     
    else :
        state = 'error'
except:
    state = 'error'
try:
    if state == 'greater':
        print('Đang tải xuống...')
        file = get('https://github.com/SussyGuy35/BachNobServer/raw/main/MyPlatformer-engine.npk')
        open('MyPlatformer-engine.npk','wb').write(file.content)
        print('Tải xuống thành công!')
        print('Đang cài đặt...')
        system(f'cmd /c "7z.exe x MyPlatformer-engine.npk -p{pw} -y"')
        remove('MyPlatformer-engine.npk')
        config.read('BachNobUpdaterConfig.ini')
        config.set('Setting','current_version',newest_ver_str)
        with open('BachNobUpdaterConfig.ini', 'w') as configfile:
            config.write(configfile)
        print(f'Cài đặt phiên bản {newest_ver_str} thành công!')
            
    elif state == 'equal':
        print('Phiên bản của bạn bằng với phiên bản trên máy chủ.')
    elif state == 'lower':
        print('Phiên bản của bạn cao hơn phiên bản trên máy chủ. How?')
    elif state == 'error':
        print('python suck')
except:
    print('Đã có lỗi xảy ra')
input('Nhấn Enter để thoát...')    
