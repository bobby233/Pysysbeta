# 作品名称：Pyrandom随机抽奖器
# 版本：0.0.1beta

import PSDK as p

mess = ''
do = '''Type "random" to random sth.
Type "start" to start random.
Type "random -r" to random some numbers.
Type "start -r" to start random.
What do you want to do(type "q" to quit)? '''
random_do = 'How many things do you want to add into random? '
random_add = 'Type things you want to random: '
random_add_success = 'Random list is successfully added!'
random_r_do = 'Type the start number you want to random: '
random_r_stop_num = 'Type the stop number: '

p.wel('Pyrandom')

while True:   # 主循环
    mess = input(do)

    # 基本功能random：进入随机交互
    if mess == 'random':
        mess = input(random_do)
        r_num = int(mess)
        r_list = []
        # 将随机物品加入列表
        for r in range(1, r_num+1):
            mess = input(random_add)
            r_list.append(mess)
        print(random_add_success)

    # 基本功能start：开始随机抽取
    elif mess == 'start':
        from random import choice
        result = choice(r_list)
        print(result)

    # 退出q：按"q"退出
    elif mess == 'q':
        p.ext('Pyrandom')
        break

    # 功能random -r：随机一系列整数
    elif mess == 'random -r':
        mess = input(random_r_do)
        r_r_start_num = int(mess)
        mess = input(random_r_stop_num)
        r_r_stop_num = int(mess)
        r_r_list = list(range(r_r_start_num, r_r_stop_num+1))

    # 功能start -r：运行随机一系列整数
    elif mess == 'start -r':
        from random import choice
        result_r = choice(r_r_list)
        print(result_r)

    elif mess == 'info':
        p.info(name='Pyrandom', info='Random numbers or strings.')