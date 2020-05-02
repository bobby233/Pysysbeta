# 名称：Pyhak
# GitHub上的作者：bobby233
# 这是一个假冒的黑客程序

from random import choice
import json

import Pysys_str as s
import PSDK as p

def run():
    """运行"""
    p.wel('Pyhak')
    with open(s.ui) as u:
        s.user_info = json.load(u)
    try:
        _test = s.user_info['Pyhak']
    except KeyError:
        s.user_info['Pyhak'] = {'c': 0}
    else:
        s.user_info['Pyhak']['c'] += 1

    while True:
        s.mess = input('$ ')
        if s.mess == 'q':
            p.ext('Pyhak')
            break
        elif s.mess == 's':
            s.mess = input('### TYS: ')
            s.user_info['Pyhak']['s'] = s.mess
            with open(s.ui, 'w') as u:
                json.dump(s.user_info, u)
        elif s.mess == 'h':
            with open(s.ui) as u:
                s.user_info = json.load(u)
            s.user_info['Pyhak']['c'] += 1
            if s.user_info['Pyhak']['s']:
                if s.user_info['Pyhak']['c'] >= 20:
                    h = choice((True, False))
                    if h:
                        for i in range(1, 21):
                            print('Connecting to 20 hacking servers(' + str(i) + '/20)')
                        print('Connect success')
                    else:
                        print('Connect failed')
                    with open(s.ui, 'w') as u:
                            json.dump(s.user_info, u)
                else:
                    for i in range(1, 21):
                        print('Connecting to 20 hacking servers(' + str(i) + '/20)')
                    print('Connect success')
                    print('Your school has been hacked by you')
                    with open(s.ui, 'w') as u:
                        json.dump(s.user_info, u)
            else:
                pass