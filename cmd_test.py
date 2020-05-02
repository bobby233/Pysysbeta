from cmd import Cmd
import Pysys_str as s
import PSDK as p
import json

# just test start
s.user = 'defult'
builtin_apps = ['settings', 'info', 'dev', 'Pyox', 'Pyrandcard', 'Pyrandom']
thirdparty_apps = []
# just test end

class Run(Cmd):
    """运行"""
    
    intro = s.wel
    if s.user == 'defult':
        prompt = s.defult_user_opr
    elif s.user == 'xuser':
        prompt = s.xuser_opr
    else:
        prompt = s.guest_opr

    # q退出
    def do_q(self, none):
        """exit or quit"""
        return True
    
    # 设置settings：设置系统
    def do_settings(self, none):
        """system settings"""
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
    def do_app(self, opt):
        """list apps"""
        if opt:
            if opt == 'list':
                print('These are built in apps:')
            for app in builtin_apps:
                print(app)
            print('These are third party apps:')
            for app in thirdparty_apps:
                print(app)
        else:
            print('These are built in apps:')
            for app in builtin_apps:
                print(app)
            print('These are third party apps:')
            for app in thirdparty_apps:
                print(app)

    # 系统信息info：查看系统信息
    def do_info(self, none):
        """see info of the system"""
        p.wel('info')
        print('These are the info of Pysys:')
        p.info(name='Pysys', info='A breakthrough system based on Python', version='v0')
        p.ext('info')

    # 开发者设置dev：在开发者的角度设置系统
    def do_dev(self, none):
        p.wel('dev')
        p.ext('dev')

    # 游戏Pyox：OX棋
    def do_Pyox(self, none):
        """DO NOT PLAY IT"""
        s.mess = input(s.fob)
        if s.mess == 'y':
            import Pyox
            pyox = Pyox.Pyox()
            pyox.run()
    
    # 抽牌Pyrandcard：抽牌器
    def do_Pyrandcard(self, none):
        """random cards"""
        import Pyrandcard
        pyrandcard = Pyrandcard.RandomCard()
        pyrandcard.run()
    
    # 随机抽取Pyrandom：抽奖
    def do_Pyrandom(self, none):
        """random"""
        import Pyrandom
    
    def emptyline(self):
        print("empty line!")

test = Run()
test.cmdloop()