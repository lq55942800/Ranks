#coding=utf-8

import os,time
import re

# 安装包路径
apk_path = '/Users/刘强/Downloads/Ksong.apk'
pkg_name = 'com.tencent.karaoke'
activity = 'com.tencent.karaoke.module.splash.ui.SplashBaseActivity'

def get_devices_info():
    devices_info = os.popen('adb devices').read()
    # 正则匹配设备号
    pattern = re.compile('List.*?attached(.*?)device',re.S)
    # 获取设备ID
    id = re.match(pattern,devices_info)
    # print(id.group(1))
    return id.group(1).split()[0]

def judge_whether_get_ID(ID):
    if ID == None:
        print("未获取到设备，请检查是否连接OK。")
    else:
        print('连接成功，设备号为：',ID)
        install_apk(apk_path)

def install_apk(apk_path):
    print('开始安装,apk路径为：',apk_path)
    install_cmd = os.popen('adb install -r %s'%apk_path)
    # print('安装信息：',install_cmd.read(),'安装结束。')
    pattern = re.compile('.*?pkg.*?apk(.*?)\[INSTALL_CANCELED_BY_USER\]', re.S)
    try:
        install_info = re.match(pattern, install_cmd.read()).group(1).split()[0]
        print('安装失败，请检查 "USB安装选项是否" 启用/请在手机上确认继续安装。')
    except:
        print('恭喜，安装成功')
        time.sleep(3)
        cold_start(pkg_name,activity)
        uninstall_apk(pkg_name)


def uninstall_apk(pkg_name):
    uinstall_cmd = os.popen('adb uninstall %s'%pkg_name)
    print('卸载结果：',uinstall_cmd.read())

def cold_start(pkg_name,activity):
    print('启动进程。')
    os.system('adb shell am start -n %s/%s'%(pkg_name,activity))
    time.sleep(5)
    os.system('adb shell  am force-stop %s'%pkg_name)
    print('结束进程。')

def main():
    ID = get_devices_info()
    judge_whether_get_ID(ID)


if __name__ == '__main__':
    main()
