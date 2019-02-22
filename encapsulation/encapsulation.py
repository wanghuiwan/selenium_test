# -*- coding: utf-8 -*-
# @Time    : 2018-05-14 13:42
# encapsulation/encapsulation.py

# 封装部分维护在此

from configs.config_01 import mc_config
from log.log import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class UIHandle():
    logger = Logger()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()




    # element对象
    @classmethod
    def element(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入显性等待
        # 此处便可以传入config_o1中的dict定位参数
        el = WebDriverWait(cls.driver, 10, 0.5).until(EC.presence_of_element_located(mc_config[page][element]))
        # 加入日志
        cls.logger.loginfo(page+'OK')
        return el

    # select
    @classmethod
    def select(cls, page, element):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入显性等待
        # 此处便可以传入config_o1中的dict定位参数
        el = WebDriverWait(cls.driver, 10, 0.5).until(EC.presence_of_element_located(mc_config[page][element]))
        # 加入日志
        cls.logger.loginfo(page + 'OK')
        return el

    # element对象
    @classmethod
    def elements(cls, page, element,lottery):
        # 加入日志
        cls.logger.loginfo(page)
        # 加入显性等待
        # 此处便可以传入config_o1中的dict定位参数
        el = WebDriverWait(cls.driver, 10, 0.5).until(EC.presence_of_element_located([mc_config[page][element][0], mc_config[page][element][1] % lottery]))
        # 加入日志
        cls.logger.loginfo(page+'OK')
        return el


    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        el.send_keys(msg)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        el.click()

    # click方法循环进入彩票
    @classmethod
    def Clicks(cls, page, element, lottery):
        el = cls.elements(page, element, lottery)
        el.click()

    # ActionChains
    @classmethod
    def ActionChains(cls, page, element):
        el = cls.element(page, element)
        ActionChains(cls.driver).move_to_element(el).perform()

    # 清理输入框
    @classmethod
    def clears(cls, page, element):
        el = cls.element(page, element)
        el.clear()

    # 获取确认信息
    @classmethod
    def texts(cls, page, element):
        el = cls.element(page, element)
        return el.text

    @classmethod
    def finds(cls):
        el = cls.driver.find_element_by_xpath("//*[@id=\"content:lottery_submit\"]")
        return el.text