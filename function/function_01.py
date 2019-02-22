# -*- coding: utf-8 -*-
# @Time    : 2018-05-14 13:42
# function/function_01.py
# 业务功能脚本（用例脚本可调用此处的功能脚本）

from encapsulation.encapsulation import UIHandle
from constant.constant_01 import *
from datas.data_01 import *
from configs.config_01 import browser_config
from time import sleep
import time
# 打开首页，进行登陆功能
def logins(names,pwds):
    print(time.time())
    # 打开浏览器
    driver = browser_config['chrome']()
    driver.maximize_window()
    # 传入driver对象
    uihandle = UIHandle(driver)
    #输入url地址
    uihandle.get(reg)
    # 调用二次封装后的方法，此处可见操作了哪个页面，哪个元素，msg是要插入的值，插入值得操作在另外一个用例文件中传入
    uihandle.Click('登陆', '语言')
    uihandle.Click('登陆', '中文')
    sleep(10)
    uihandle.Input('登陆', '用户名', names)
    uihandle.Input('登陆', '密码', pwds)
    uihandle.Click('登陆', '登陆按钮')

def register(name,password,passwords):
    driver = browser_config['chrome']()
    driver.maximize_window()
    # 传入driver对象
    uihandle = UIHandle(driver)
    # 输入url地址
    uihandle.get(reg)
    uihandle.Input('注册', '用户名', name)
    uihandle.Input('注册', '密码', password)
    uihandle.Input('注册', '确认密码',passwords)
    uihandle.Click('注册', '注册按钮')

def enter_lottery():
    print(time.time())
    uihandle = UIHandle
    for caizhong in game_ssc:
        uihandle.ActionChains('悬浮', '窗口')
        uihandle.Clicks('悬浮', '彩种', caizhong['cz'])
        sleep(2)
        if caizhong['cx'] =='ssc':
            add_order_ssc(uihandle)


def add_order_ssc(uihandle):
    print(time.time())
    for shuju in (sscwf2,sscwf3):
        if shuju[0] == sscwf3[0]:
            attempts = 0
            success = False
            while attempts < 5 and not success:
                try:
                    uihandle.Click('玩法', '进入任选')
                    success = True
                except:
                    sleep(1)
                    attempts += 1
            if attempts == 4:
                print('没有任选')
        for wanfa in shuju:
            attempts = 0
            success = False
            while attempts < 5 and not success:
                try:
                    if int(wanfa['type']) ==1:
                        lottery_add_changgui111(uihandle,wanfa)
                    else:
                        lottery_add_danshi111(uihandle,wanfa)
                    success = True
                except :
                    sleep(1)
                    attempts += 1
            if not success:
                print(wanfa['wfname'] + '~~~~~~~~~~~' + str(attempts) + '次下单全部失败')


def lottery_add_changgui111(uihandle,wanfa):
    uihandle.Clicks('玩法', '大玩法', wanfa['wfcname'])
    uihandle.Clicks('玩法', '子玩法', wanfa['zwf'])
    xunhuan = 0
    sleep(1)
    while xunhuan < wanfa['xhcs']:
        uihandle.Clicks('玩法', '复式', (wanfa['haoma'][xunhuan][0], wanfa['haoma'][xunhuan][1]))
        xunhuan += 1
    sleep(0.5)
    uihandle.Click('玩法', '快速下单2')
    xinxi = 0
    ssss = False
    while xinxi < 5 and not ssss:
        try:
            sleep(1)
            try:
                uihandle.Click('玩法', '确认下单')  # 确认下单
                ssss = True
                xx1 = False
            except:
                print("空1")
                # d = uihandle.finds()
                d = uihandle.texts('玩法', '获取信息')  # 弹出信息
                if d == '':
                    raise RuntimeError('信息没获取到')
                ssss = True
                xx1 = True
        except:
            xinxi +=1
            print(xinxi)
    xx = 0
    print("空2")
    while xx < 2 and not xx1:
        try:

            print("空3")
            # d = uihandle.finds()
            d = uihandle.texts('玩法', '获取信息')  # 弹出信息
            print("空4")
            print(d)
            if d == '':
                print("空5")
                sleep(1)
                continue
            else:
                print("空6")
                xx1 = True

        except Exception as asdfg:
            print("获取信息。。。"+asdfg)
            xx += 1
    print(wanfa['wfname'] + str(d))


def lottery_add_danshi111(uihandle,wanfa):
    uihandle.Clicks('玩法', '大玩法', wanfa['wfcname'])
    uihandle.Clicks('玩法', '子玩法', wanfa['zwf'])
    uihandle.clears('玩法', '单式')
    uihandle.Input('玩法', '单式', (str(wanfa['haoma'][0]) + ' '))
    sleep(1)
    uihandle.Click('玩法', '快速下单')
    xinxi = 0
    ssss = False
    while xinxi < 5 and not ssss:
        try:
            sleep(1)
            try:
                uihandle.Click('玩法', '确认下单')  # 确认下单
                ssss = True
                succ = True
            except:
                d = uihandle.finds()  # 弹出信息
                if d == '':
                    raise RuntimeError('信息没获取到')
                ssss = True
                succ = True
        except:
            xinxi += 1
    xinxi = 0
    while xinxi < 5 and not succ:
        try:
            sleep(1)
            d = uihandle.finds()  # 弹出信息
            if d == '':
                continue
            else:
                succ = True
        except:
            print('shibai')
            xinxi += 1
    print(wanfa['wfname']+d)
