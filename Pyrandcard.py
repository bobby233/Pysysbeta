# 名称：Pyrandcard
# GitHub上的作者：bobby233
# 特殊方法和collections的简单练习

import collections
from random import choice

# namedtumple创建简单的没有方法的只有属性的类
Card = collections.namedtuple('Card', ['rank', 'suit'])
# 第一个实参是类的名称
# 第二个实参是列表，这里包括两个将被放到类里的属性

# 类名称后不需要括号也可以
class FrenchDeck:
    """一打牌"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 这是序数，有for的简写；后面list是将字符串转换成列表，结果应该是['J', 'Q', 'K', 'A']
    suits = 'spades diamonds clubs hearts'.split()
    # 这是花色，字符串.split()可以将字符串转换成列表
    # 和list不同的是它是按照空格进行辨别的，list是按照字母
    # 如果换成list，会输出这个['s', 'p', ...]（后面省略）

    def __init__(self):
        """初始化"""
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        # 这里包含两个for简写，这样的排版应该可以理解
        # 前面的_cards有一个下划线（单前导下划线），是在内部使用的变量

    def __len__(self):
        """测量长度"""
        return len(self._cards)
        # 这里执行时可以转化成len(class)

    def __getitem__(self, position):
        """查看特定序列的card"""
        return self._cards[position]
        # 这里和上面的性质相同，可以转换成class[pos]
    # 在上面所有的方法命名中，这些叫做魔术方法，原理是这样的：
    # 在Python解释器中，调用len(obj)会先把它转换成obj.__len__()
    # 然后就可以输出长度了，这里可以告诉Python这个方法行得通
    # obj[pos]也是这个原理

# 通过上面的实践，可以制作一个简单的交互式抽牌器（将会应用到Pysys）
import Pysys_str as s
import PSDK as p

class RandomCard:
    """抽牌器"""
    # 先做一打牌
    deck = FrenchDeck()

    def ask(self):
        """询问抽牌数"""
        while True:
            s.mess = input('How many cards do you want to choose? ')
            # 退出
            if s.mess == 'q':
                s.rcout = True
                break
            # 抽
            else:
                try:
                    self._num = int(s.mess)
                except ValueError:
                    print('Type a number!')
                else:
                    break
                
    def choose(self):
        """开始抽"""
        result = []
        for i in range(self._num):
            result.append(choice(self.deck))
        print('You have chosen', self._num, 'cards, they are:')
        for i in result:
            print(i)
    
    def run(self):
        """运行"""
        p.wel('Pyrandcard')
        print('Type "q" to quit.')
        while True:
            s.rcout = False
            self.ask()
            if s.rcout:
                p.ext('Pyrandcard')
                break
            else:
                self.choose()