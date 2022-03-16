# 注册函数
def register():
    print("我是注册函数")
    pass


# 登录函数
def login():
    print("我是登录函数")
    pass


# 余额函数
def check_money():
    print("我是余额函数")
    pass


# 存钱函数
def save_money():
    print("我是存钱函数")
    pass


# 取钱函数
def get_money():
    print("我是取钱函数")
    pass


# 账单函数
def account():
    print("我是账单函数")
    pass


# 功能选择的字典
fun_select = {
    0: ['退出', exit],
    1: ['注册', register],
    2: ['登录', login],
    3: ['余额', check_money],
    4: ['存款', save_money],
    5: ['取款', get_money],
    6: ['账单', account],
}


def run():
    while 1:
        print("欢迎来到ATM操作系统".center(70))
        for i in fun_select:
            print(i,fun_select[i][0])
        select =int(input("请选择你要做的操作>>>"))
        if select in fun_select:
            print("你选择的功能存在")
            fun_select[select][1]()
        else:
            print("输入错误，请重新输入")
run()
