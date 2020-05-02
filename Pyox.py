# 名称：Pyox游戏
# GitHub上的作者：bobby233
# 一款OX棋游戏，内置于Pysys
# 版本：0.0.1beta

import random

import Pysys_str as s
import PSDK as p

class Pyox():
    """游戏主体"""

    def ask_diff(self):
        """询问难度"""
        while True:
            if s.oxout:
                break
            print('These are the difficulties:')
            print('1. test')
            print('Type "q" to quit')
            s.mess = input('Choose a difficulty above(type number): ')
            if s.mess == '1':
                self.test()
            elif s.mess == 'q':
                break
            else:
                print('Difficulty not found...')
                continue

    def test(self):
        """test难度"""
        s.oxout = False
        while True:
            if s.oxout == True:
                break
            print('Let us play test difficulty.')
            print('The computer does not want to win, just random.')
            print('You go first. You are "o", computer is "x", empty is "e".')
            hor = '  1 2 3'
            li1 = '1 e e e'
            li2 = '2 e e e'
            li3 = '3 e e e'
            print(hor)
            print(li1)
            print(li2)
            print(li3)
            ho = list(hor)
            l1 = list(li1)
            l2 = list(li2)
            l3 = list(li3)
            while True:
                s.mess = input('Please type a position(like 11): ')
                # 绘制
                if s.mess[0] == '1':
                    if s.mess[1] == '1':
                        l1[2] = 'o'
                    elif s.mess[1] == '2':
                        l2[2] = 'o'
                    elif s.mess[1] == '3':
                        l3[2] = 'o'
                elif s.mess[0] == '2':
                    if s.mess[1] == '1':
                        l1[4] = 'o'
                    elif s.mess[1] == '2':
                        l2[4] = 'o'
                    elif s.mess[1] == '3':
                        l3[4] = 'o'
                elif s.mess[0] == '3':
                    if s.mess[1] == '1':
                        l1[6] = 'o'
                    elif s.mess[1] == '2':
                        l2[6] = 'o'
                    elif s.mess[1] == '3':
                        l3[6] = 'o'
                else:
                    s.oxout = True
                    break

                # 处理
                while True:
                    c_l = str(random.randint(1, 4))
                    c_h = str(random.randint(1, 4))
                    c_a = c_l + c_h
                    if c_a == s.mess:
                        continue
                    elif c_l == '1':
                        if c_h == '1':
                            l1[2] = 'x'
                        elif c_h == '2':
                            l2[2] = 'x'
                        elif c_h == '3':
                            l3[2] = 'x'
                        break
                    elif c_l == '2':
                        if c_h == '1':
                            l1[4] = 'x'
                        elif c_h == '2':
                            l2[4] = 'x'
                        elif c_h == '3':
                            l3[4] = 'x'
                        break
                    elif c_l == '3':
                        if c_h == '1':
                            l1[6] = 'x'
                        elif c_h == '2':
                            l2[6] = 'x'
                        elif c_h == '3':
                            l3[6] = 'x'
                        break

                # 判断谁赢了
                if (l1[2] == 'o' and l1[4] == 'o' and l1[6] == 'o') or (l2[2] == 'o' and l2[4] == 'o' and l2[6] == 'o') or (l3[2] == 'o' and l3[4] == 'o' and l3[6] == 'o') or (l1[2] == 'o' and l2[2] == 'o' and l3[2] == 'o') or (l1[4] == 'o' and l2[4] == 'o' and l3[4] == 'o') or (l1[6] == 'o' and l2[6] == 'o' and l3[6] == 'o'):
                    win = True
                elif (l1[2] == 'x' and l1[4] == 'x' and l1[6] == 'x') or (l2[2] == 'x' and l2[4] == 'x' and l2[6] == 'x') or (l3[2] == 'x' and l3[4] == 'x' and l3[6] == 'x') or (l1[2] == 'x' and l2[2] == 'x' and l3[2] == 'x') or (l1[4] == 'x' and l2[4] == 'x' and l3[4] == 'x') or (l1[6] == 'x' and l2[6] == 'x' and l3[6] == 'x'):
                    lose = True
                else:
                    win, lose = False, False

                # 处理列表到字符串
                hor = ''.join(ho)
                li1 = ''.join(l1)
                li2 = ''.join(l2)
                li3 = ''.join(l3)
                
                # 输出
                print(hor)
                print(li1)
                print(li2)
                print(li3)
                if win:
                    print('You win!')
                    break
                elif lose:
                    print('Computer wins!')
                    break
                else:
                    continue

    def info(self):
        """信息或玩"""
        print('Type "q" to quit')
        while True:
            s.mess = input('Welcome to Pyox.\nDo you want to see info or play(info/play)? ')
            if s.mess == 'info':
                p.info(name='Pyox', info='This is a OX chess game.')
                continue
            elif s.mess == 'play':
                self.ask_diff()
            elif s.mess == 'q':
                s.oxout = True
                break
            else:
                print('We do not have this option...')
                continue

    def run(self):
        """运行"""
        p.wel('Pyox')
        self.info()
        self.ask_diff()
        p.ext('Pyox')