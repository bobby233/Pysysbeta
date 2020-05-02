# 名称：PSDK(Pysys Develop Kit)
# GitHub上的作者：bobby233
# 这是Pysys的开发包，有常用的开发功能
# v0.2.1

import json

import Pysys_str

# 这不能import
builtin_apps = ['settings', 'info', 'dev', 'Pyox', 'Pyrandcard', 'Pyrandom']
thirdparty_apps = []
commands = ["ck", "mkd", "dld", "mkf", "dlf"]

#################### app management ####################

def wel(string='Test'):
    """输出欢迎语句（每个应用必须添加），需要实参应用名称"""
    _welcome_str = 'Welcome to ' + string
    _welcome_str_all = _welcome_str + '-'*(60-len(_welcome_str))
    print(_welcome_str_all)

def ext(string='Test'):
    """输出退出语句（每个应用必须添加），需要实参应用名称"""
    _ext_str = 'Exit ' + string
    _ext_str_all = _ext_str + '-'*(60-len(_ext_str))
    print(_ext_str_all)

def info(name='Test', author='bobby233', version='0.0.1beta', info='This is a test.'):
    """输出应用信息（每个应用必须添加），需要实参应用名称、作者、版本和描述"""
    _info_dict = {'Name': name, 'Author': author, 'Version': version, 'Info': info}
    for k, v in _info_dict.items():
        print(k + ': ' + v)

#################### password security ####################

def check_psw(prompt='Please type your password: '):
    """检测是否密码正确，需要input语句实参"""
    _message = input(prompt)
    # 检测密码
    try:
        with open(Pysys_str.ui) as f:
            _ui_password = json.load(f)
    except FileNotFoundError:
        print('YOU CHEAT!!!')
    else:
        if _message == _ui_password['password']:
            return 1
        else:
            print('Password error!')
            return 0

def pswd_improve(prompt="Type to encode: "):
    """使用base64算法对密码加密"""
    import base64
    _msg = input(prompt)
    _passwd = base64.b64encode(_msg.encode())
    return _passwd.decode()

def iprved_pswd_check(iprved_pswd, prompt="Type to decode and check: "):
    """使用base64算法对密码解密，需要对比校验的加密密码"""
    import base64
    _msg = input(prompt)
    _passwd = base64.b64decode(str(iprved_pswd).encode())
    if _msg == _passwd.decode():
        return 1
    else:
        return 0

#################### file system ####################

def check():
    """查看所有当前目录中的文件和目录（类似ls）并列出绝对路径；"""
    # 找到当前位置：
    # 1.是DISK
    if Pysys_str.file_pos == "DISK":
        _read_from = Pysys_str.user_info["DISK"]
    # 2.是普通路径（以后更新）
    else:
        print("Do not have now...")
    # 列出指定位置下的所有文件和文件夹
    # 检测：
    _files = []
    _dirs = []
    for f_or_d in _read_from:
        # 1.如果是文件
        if f_or_d[0] == "^":
            _files.append(f_or_d[1:])
        # 2.如果是目录
        else:
            _dirs.append(f_or_d)
    # 输出
    print("Files:")
    for file in _files:
        print('\t' + file)
    print("="*20 + '\n' + "Directories:")
    for dirr in _dirs:
        print('\t' + dirr)
    # 输出绝对路径
    print("Absolute route:", Pysys_str.file_pos)

def make_dir(name=None):
    """在当前目录创建一个目录（类似mkdir）并列出当前绝对路径和创建的目录的绝对路径；
    需要要创建的目录名称"""
    # 找到当前位置
    # 1.是DISK
    if Pysys_str.file_pos == "DISK":
        _read_from = Pysys_str.user_info["DISK"]
    # 2.是普通路径（以后更新）
    else:
        print("Do not have now...")
    # 创建目录并写入：
    # 1.创建目录到信息字典
    _read_from.append(name)
    # 2.写入json文件
    with open(Pysys_str.ui, 'w') as u:
        json.dump(Pysys_str.user_info, u)
    # 输出当前绝对路径
    print("Current absolute route:", Pysys_str.file_pos)
    # 输出创建的目录的绝对路径
    print("Created absolute route:", Pysys_str.file_pos + "/" + name)

def del_dir(name=None):
    """在当前目录删除一个目录（类似rm -r）并列出当前绝对路径和删除的目录的绝对路径；
    需要要删除的目录名称"""
    # 找到当前位置
    # 1.是DISK
    if Pysys_str.file_pos == "DISK":
        _read_from = Pysys_str.user_info["DISK"]
    # 2.是普通路径（以后更新）
    else:
        print("Do not have now...")
    # 删除目录并写入：
    # 1.删除目录到信息字典
    # 检测是否有要删除的目录
    try:
        _read_from.remove(name)
    # 如果没有就告知
    except ValueError:
        print("This directory does not exist")
    # 2.写入json文件
    with open(Pysys_str.ui, 'w') as u:
        json.dump(Pysys_str.user_info, u)
    # 输出当前绝对路径
    print("Current absolute route:", Pysys_str.file_pos)
    # 输出删除的目录的绝对路径
    print("Deleted absolute route:", Pysys_str.file_pos + "/" + name)

def make_file(name=None):
    """在当前目录创建一个文件（类似touch）并列出当前绝对路径和创建的文件的绝对路径；
    需要要创建的文件名称"""
    # 找到当前位置
    # 1.是DISK
    if Pysys_str.file_pos == "DISK":
        _read_from = Pysys_str.user_info["DISK"]
    # 2.是普通路径（以后更新）
    else:
        print("Do not have now...")
    # 创建文件并写入：
    # 1.创建文件到信息字典
    _read_from.append("^" + name)
    # 2.写入json文件
    with open(Pysys_str.ui, 'w') as u:
        json.dump(Pysys_str.user_info, u)
    # 输出当前绝对路径
    print("Current absolute route:", Pysys_str.file_pos)
    # 输出创建的文件的绝对路径
    print("Created absolute route:", Pysys_str.file_pos + "/" + name)

def del_file(name=None):
    """在当前目录删除一个文件（类似rm）并列出当前绝对路径和删除的文件的绝对路径；
    需要要删除的文件名称"""
    # 找到当前位置
    # 1.是DISK
    if Pysys_str.file_pos == "DISK":
        _read_from = Pysys_str.user_info["DISK"]
    # 2.是普通路径（以后更新）
    else:
        print("Do not have now...")
    # 删除文件并写入：
    # 1.删除文件到信息字典
    # 检测是否有要删除的文件
    try:
        _read_from.remove("^" + name)
    # 如果没有就告知
    except ValueError:
        print("This file does not exist")
    # 2.写入json文件
    with open(Pysys_str.ui, 'w') as u:
        json.dump(Pysys_str.user_info, u)
    # 输出当前绝对路径
    print("Current absolute route:", Pysys_str.file_pos)
    # 输出删除的文件的绝对路径
    print("Deleted absolute route:", Pysys_str.file_pos + "/" + name)

#################### network ####################

import urllib.request

def check_network(url="https://github.com"):
    """通过连接一个网站来确定是否有到指定网站网络；
    需要网站链接"""
    print("Connecting to", url + "...")
    try:
        _net_checker = urllib.request.urlopen(url)
    except urllib.request.HTTPError:
        print("Connect failed")
    else:
        print("Connect succeed")
        Pysys_str.network = True

def get_web_code(url="https://github.com"):
    """获取一个网站的源码；
    需要网站链接"""
    if Pysys_str.network:
        _opener = urllib.request.urlopen(url)
        _code = _opener.readlines()
        print("These are the code:")
        print("=====CODE START HERE=====")
        for cd in _code:
            print(str(cd, 'utf-8'), end="")
        print("\n=====CODE END HERE=====")
    else:
        check_network(url)
        if Pysys_str.network:
            _opener = urllib.request.urlopen(url)
            _code = _opener.readlines()
            print("These are the code:")
            print("=====CODE START HERE=====")
            for cd in _code:
                print(str(cd, 'utf-8'), end="")
            print("\n=====CODE END HERE=====")

def Pysys_app_doc_reader(app=None):
    """阅读Pysys官方的app文档；
    需要app名称"""
    if app in (builtin_apps or thirdparty_apps):
        if Pysys_str.network:
            try:
                _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/appdoc" + "/" + app + ".txt")
            except urllib.request.HTTPError:
                print("Wait for us. We are writing quickly!")
            else:
                print("This is just a test and test secceed!")
        else:
            check_network("https://raw.githubusercontent.com")
            if Pysys_str.network:
                try:
                    _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/appdoc" + "/" + app + ".txt")
                except urllib.request.HTTPError:
                    print("Wait for us. We are writing quickly!")
                else:
                    print("This is just a test and test secceed!")
    elif app == None:
        if Pysys_str.network:
            print("Let's see the code of Pysys")
            get_web_code("https://raw.githubusercontent.com/bobby233/Pysys/master/Pysys.py")
        else:
            check_network("https://raw.githubusercontent.com")
            if Pysys_str.network:
                print("Let's see the code of Pysys")
                get_web_code("https://raw.githubusercontent.com/bobby233/Pysys/master/Pysys.py")
    else:
        print("No such app...")

def download_as_file(url, filename):
    """将网站上面的所有代码下载至指定的文件；
    需要指定域名和文件名"""
    if Pysys_str.network:
        print("Downloading page on", url, "to", filename)
        _opener = urllib.request.urlopen(url)
        _code = _opener.read().decode()
        with open(filename, "w") as f:
            f.write(_code)
        print("Download succeed")
    else:
        check_network(url)
        if Pysys_str.network:
            print("Downloading page on", url, "to", filename)
            _opener = urllib.request.urlopen(url)
            _code = _opener.read().decode()
            with open(filename, "w", newline="") as f:
                f.write(_code)
            print("Download succeed")

def check_system_update():
    """通过GitHub检查是否为最新版本，可以调节手动和自动（以后更新）"""
    if Pysys_str.beta:
        _msg = input("Do you want beta version or common version?(beta/comm) ")
        if _msg == "beta":
            if Pysys_str.network:
                _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                _info = eval(str(_opener.read(), encoding="utf-8"))
                if Pysys_str.version < _info["latest_beta"]:
                    print("You need update.\nGo to https://github.com/bobby233/Pysysbeta to download.")
                else:
                    print("Your version is the latest.")
            else:
                check_network("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                if Pysys_str.network:
                    _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                    _info = eval(str(_opener.read(), encoding="utf-8"))
                    if Pysys_str.version < _info["latest_beta"]:
                        print("You need to update.\nGo to https://github.com/bobby233/Pysysbeta to download.")
                    else:
                        print("Your version is the latest.")
        elif _msg == "comm":
            if Pysys_str.network:
                _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                _info = eval(str(_opener.read(), encoding="utf-8"))
                if Pysys_str.version < _info["latest_beta"]:
                    print("You need update.\nGo to https://github.com/bobby233/Pysys to download.")
                else:
                    print("Your version is the latest.")
            else:
                check_network("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                if Pysys_str.network:
                    _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                    _info = eval(str(_opener.read(), encoding="utf-8"))
                    if Pysys_str.version < _info["latest"]:
                        print("You need to update.\nGo to https://github.com/bobby233/Pysys to download.")
                    else:
                        print("Your version is the latest.")
        else:
            print("No this option!")
    else:
        if Pysys_str.network:
            _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
            _info = eval(str(_opener.read(), encoding="utf-8"))
            if Pysys_str.version < _info["latest_beta"]:
                print("You need update.\nGo to https://github.com/bobby233/Pysys to download.")
            else:
                print("Your version is the latest.")
        else:
            check_network("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
            if Pysys_str.network:
                _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/system.json")
                _info = eval(str(_opener.read(), encoding="utf-8"))
                if Pysys_str.version < _info["latest"]:
                    print("You need to update.\nGo to https://github.com/bobby233/Pysys to download.")
                else:
                    print("Your version is the latest.")

def download_app(app):
    """从GitHub下载app；
    需要app名称"""
    if Pysys_str.network:
        _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/app.json")
        _app_info = eval(str(_opener.read(), encoding="utf-8"))
        if app in _app_info["app_list"]:
            print("Downloading", app + "...")
            with open(app + ".py", "w") as a:
                a.write(_app_info["app"][app]["code"])
            print("Download succeed")
        else:
            print("No such app...")
    else:
        check_network("https://raw.githubusercontent.com/bobby233/Pysys/master/app.json")
        if Pysys_str.network:
            _opener = urllib.request.urlopen("https://raw.githubusercontent.com/bobby233/Pysys/master/app.json")
            _app_info = eval(str(_opener.read(), encoding="utf-8"))
            if app in _app_info["app_list"]:
                print("Downloading", app + "...")
                with open(app + ".py", "w") as a:
                    a.write(_app_info["app"][app]["code"])
                print("Download succeed")
            else:
                print("No such app...")