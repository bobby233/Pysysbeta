# 名称：Pysys_appbox应用集
# GitHub上的作者：bobby233
# 配合Pysys使用的应用集
# 版本：0.2.1

import json

import Pysys_str as s
import PSDK as p

builtin_apps = ['settings', 'info', 'dev', 'Pyox', 'Pyrandcard', 'Pyrandom']
thirdparty_apps = []
commands = ["ck", "mkd", "dld", "mkf", "dlf",
            "ckn", "gwc", "adr", "daf", "csu", "doa"]
s.version = 20

def sign_log():
    """登录和注册"""
    while True:
        # 检测是否注册
        try:
            with open(s.ui) as u:
                s.user_info = json.load(u)
        # 如果没有就提示注册
        except FileNotFoundError:
            usrn = p.pswd_improve(s.sign)
            s.user_info['username'] = usrn
            pswd = p.pswd_improve(s.sign_psw)
            s.user_info['password'] = pswd
            with open(s.ui, 'w') as u:
                json.dump(s.user_info, u)
            print('Sign in successfully')
            continue
        # 如果有就提示登录
        else:
            usrn = p.iprved_pswd_check(s.user_info["username"], s.log)
            pswd = p.iprved_pswd_check(s.user_info["password"], s.log_psw)
            if usrn and pswd:
                break
            if usrn == 0:
                print("Username error")
            if pswd == 0:
                print("Password error")
            
def run():
    """运行"""
    
    print(s.wel)
    while True:
        s.mess = input(s.defult_user_opr)

        # q退出
        if s.mess == 'q':
            break
        
        # 设置settings：设置系统
        elif s.mess == 'settings':
            p.wel('settings')
            while True:
                settings_do = 'What do you want to do(type "q" to quit)? '
                new_psw = 'Type your new password: '
                print('Type "cpsw" to change your password.')
                print('Type "info" to see the info.')
                s.mess = input(settings_do)
                if s.mess == 'cpsw':
                    cpsw = p.check_psw()
                    if cpsw:
                        s.mess = input(new_psw)
                        with open(s.ui) as f:
                            s.user_info = json.load(f)
                            s.user_info['password'] = s.mess
                        with open(s.ui, 'w') as f:
                            json.dump(s.user_info, f)
                        print('Change succefully')
                elif s.mess == 'info':
                    p.info(name='settings', info='System settings')
                elif s.mess == 'q':
                    p.ext('settings')
                    break
                else:
                    print('We do not have this option.')

        # 应用列表app list：查看所有拥有的应用
        elif s.mess == 'app list':
            print('These are built in apps:')
            for app in builtin_apps:
                print(app)
            print('These are third party apps:')
            for app in thirdparty_apps:
                print(app)
        
        # 命令列表cmd list：查看所有命令
        elif s.mess == "cmd list":
            print("These are the commands:")
            for cmd in commands:
                print(cmd)

        # 系统信息info：查看系统信息
        elif s.mess == 'info':
            p.wel('info')
            print('These are the info of Pysys:')
            p.info(name='Pysys', info='A breakthrough system based on Python', version='v0.2.0')
            p.ext('info')

        # 开发者设置dev：在开发者的角度设置系统
        elif s.mess == 'dev':
            p.wel('dev')
            p.ext('dev')

        # 游戏Pyox：OX棋
        elif s.mess == 'Pyox':
            s.mess = input(s.fob)
            if s.mess == 'y':
                import Pyox
                pyox = Pyox.Pyox()
                pyox.run()
            else:
                continue
        
        # 抽牌Pyrandcard：抽牌器
        elif s.mess == 'Pyrandcard':
            import Pyrandcard
            pyrandcard = Pyrandcard.RandomCard()
            pyrandcard.run()
        
        # 随机抽取Pyrandom：抽奖
        elif s.mess == 'Pyrandom':
            import Pyrandom
        
        # 文件系统ck：查看当前目录中的所有文件和目录
        elif s.mess == "ck":
            p.check()
        
        # 文件系统mkd：在当前目录下新建一个目录
        elif s.mess[:3] == "mkd":
            _args = s.mess.split()
            if len(_args) == 2:
                p.make_dir(_args[1])
            else:
                print("This command takes a command and an argument!")
        
        # 文件系统dld：在当前目录下删除一个目录
        elif s.mess[:3] == "dld":
            _args = s.mess.split()
            if len(_args) == 2:
                p.del_dir(_args[1])
            else:
                print("This command takes a command and an argument!")
        
        # 文件系统mkf：在当前目录下新建一个文件
        elif s.mess[:3] == "mkf":
            _args = s.mess.split()
            if len(_args) == 2:
                p.make_file(_args[1])
            else:
                print("This command takes a command and an argument!")
        
        # 文件系统dlf：在当前目录下删除一个文件
        elif s.mess[:3] == "dlf":
            _args = s.mess.split()
            if len(_args) == 2:
                p.del_file(_args[1])
            else:
                print("This command takes a command and an argument!")
        
        # 网络ckn：检查网络是否可以连接（可选连接的域名）
        elif s.mess[:3] == "ckn":
            if len(s.mess.split()) == 1:
                p.check_network()
            elif len(s.mess.split()) == 2:
                p.check_network(s.mess.split()[1])
            else:
                print("This command takes a command(and an argument)!")
        
        # 网络gwc：抓取网站源码
        elif s.mess[:3] == "gwc":
            if len(s.mess.split()) == 2:
                p.get_web_code(s.mess.split()[1])
            else:
                print("This command takes a command and an argument!")
        
        # 网络adr：阅读官方的线上app文档
        elif s.mess[:3] == "adr":
            if len(s.mess.split()) == 2:
                p.Pysys_app_doc_reader(s.mess.split()[1])
            elif len(s.mess.split()) == 1:
                p.Pysys_app_doc_reader()
            else:
                print("This command takes a command(and an argument)!")
        
        # 网络daf：把网页下载为一个页面
        elif s.mess[:3] == "daf":
            if len(s.mess.split()) == 3:
                p.download_as_file(s.mess.split()[1], s.mess.split()[2])
            else:
                print("This command takes a command and two arguments!")
        
        # 网络csu：检查系统更新
        elif s.mess[:3] == "csu":
            if len(s.mess.split()) == 1:
                p.check_system_update()
            else:
                print("This command takes a command!")
        
        # 网络doa：联网下载app
        elif s.mess[:3] == "doa":
            if len(s.mess.split()) == 2:
                p.download_app(s.mess.split()[1])
            else:
                print("This command takes a command and an argument!")
        
        # 下载的app：test
        elif s.mess == "test":
            try:
                import test
            except ImportError:
                print("App not found...")
        
        else:
            print('Command or app not found...')