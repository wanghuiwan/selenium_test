# -*- coding: utf-8 -*-
# @Time    : 2018-05-14 13:42
# configs/config_01.py
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import *


# config配置部分

# 浏览器种类维护在此处
browser_config = {
    'ie': webdriver.Ie,
    'chrome': webdriver.Chrome
}

# 定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
mc_config = {
    '登陆': {
        '语言': ['xpath', '//*[@id="loginSelect"]/div/div'],

        '中文': ['xpath', '//*[@id="react-select-2--value-0"]'],
        '用户名': ['xpath', '//*[@id="container"]/div/div[2]/div/div[2]/div/input'],
        '密码': ['xpath', '//*[@id="container"]/div/div[2]/div/div[3]/div/input'],
        '登陆按钮': ['xpath', '//*[@id="container"]/div/div[2]/div/div[4]/div[2]/button']
    },
    '注册':{
        '用户名': ['xpath', '//*[@class="br_login_input"][1]/input'],
        '密码': ['xpath', '//*[@class="br_login_input"][2]/input'],
        '确认密码': ['xpath', '//*[@class="br_login_input"][3]/input'],
        '注册按钮': ['xpath', '//*[@class="br_login_bright"]/button']
                  },
    '弹窗':{
        '弹窗a':['xpath','.//*[@class="br_imodal_cmclose"]']
    },
    '悬浮':{
        '窗口':['xpath','//*[@id=\"mc_header\"]/header/div[2]'],
        '彩种':['xpath','//*[@id=\"mc_header\"]/header/div[2]/div/div//div[@data-lt=\'%s\']']

    },
    '玩法':{
        '大玩法':['xpath', '//*[@id=\"lottery\"]/div[3]//span[text()=\'%s\']'],
        '子玩法':['xpath', '//*[@id=\"lottery\"]/div[4]//dd[@data-type=\'%s\']'],
        '进入任选':['xpath', '//*[@id=\"lottery\"]/div[3]//button[@data-type=\'rx\']'],
        '复式': ['xpath', '//*[@id=\"lottery\"]/div[contains(@class,\'number\')]//descendant::dl[@rel=\'selectNum\'][%s]/dd/i[%s]'],
        '单式': ['xpath', '//*[@id=\"lottery\"]//div[contains(@class,\'number\')]//div[contains(@class,\'box\')]//textarea'],
        '快速下单': ['CLASS_NAME', 'quickSubmit'],
        '快速下单2': ['xpath', '//*[@id="lottery"]//a[contains(@class,\'quickSubmit\')]'],
        '确认下单': ['xpath', '/html/body/div[@role=\'alertdialog\']/div/table/tbody/tr[3]/td/div[2]/button[1]'],
        '获取信息': ['xpath', '//*[@id=\"content:lottery_submit\"]'],
    }

}
