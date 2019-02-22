from configs.config_01 import mc_config

from selenium.webdriver.common.keys import Keys
from constant.constant_01 import *
from configs.config_01 import browser_config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
driver = browser_config['chrome']()
driver.maximize_window()
# rrr = 'http://www.sit-webgame.com/MainWeb.html?customerId=27894&customerName=zongdai0001&token=841b990e-2392-4d1c-bb0a-049422a40ebd&machineId=100&gameServerIp=10.8.90.201&gameServerPort=54011&gameId=ws01&roomType=ws_nn_room_1&roomName=无双牛牛1元场&customerNickName=null&serverId=100&acctType=1'
# game_url = "http://www.sit-webgame.com/MainWeb.html?customerId=27894&customerName=zongdai0001&token=841b990e-2392-4d1c-bb0a-049422a40ebd&machineId=100&gameServerIp=10.8.90.201&gameServerPort=54061&gameId=ws06&roomType=ws_gswz_room_1&roomName=无双港式五张1元场&customerNickName=null&serverId=100&acctType=1"
driver.get('http://www.sit-tcgdemo.com/#home')
sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').send_keys('zongdai0001')
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').send_keys('zongdai0001')
driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div').click()

sleep(5)
driver.find_element_by_xpath('//*[@id="bodyContent"]/div[2]/div/ul/li[4]/img').click()

sleep(5)
driver.switch_to.frame(0)
sleep(5)
ddd = ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="game_list"]/div[1]/div/img')).perform()
sleep(10)
driver.find_element_by_xpath('//*[@id="game_list"]/div[1]/div/div/div').click()
# driver.find_element_by_xpath('//*[@id="back_to_menu"]').send_keys(Keys.ENTER)
# ActionChains(driver).move_by_offset(1360,590).click().perform()
# driver.findElement(by.id)
# driver.find_element_by_xpath('//*[@id="back_to_menu"]').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="game_type_list"]/div[5]').click()
print(111)
# ActionChains(driver).move_by_offset(1345, 544).perform()
sleep(10)
driver.quit()
# sleep(10)
# driver = browser_config['chrome']()
# driver.maximize_window()
# game_url = "http://www.sit-webgame.com/MainWeb.html?customerId=27894&customerName=zongdai0001&token=841b990e-2392-4d1c-bb0a-049422a40ebd" \
#            "&machineId=100&gameServerIp=10.8.90.201&gameServerPort=54061&gameId=ws06&roomType=ws_gswz_room_1&roomName=无双港式五张1元场&customerNickName=null&serverId=100&acctType=1"
# driver.get(game_url)
#
# sleep(5)
# ActionChains(driver).move_by_offset(1360,690).click().perform()
#
# sleep(10)
# driver.quit()


# driver=webdriver.Chrome()
#
# driver.get("https://www.126.com/") #126邮箱登陆测试
# time.sleep(4)
# driver.switch_to.frame(0)
# e=driver.find_element_by_xpath("//input[@name='email']")
# e.clear()
# e.send_keys("********")
# driver.find_element_by_xpath("//input[@name='password']").send_keys('*****')
# driver.find_element_by_id("dologin").click()
# time.sleep(3)
# #fa=driver.find_element_by_class_name('cnt')
# #print(fa.id)
# #driver.switch_to_default_content()  #切出
# #e2=driver.find_element_by_id("normalLoginTab")
# #driver.switch_to_frame("x-URS-iframe")
# #driver.find_element_by_id('ismyphonebox').click()
# #driver.find_element_by_class_name('btnbox').find_element_by_link_text(u'登录').click()
#
# driver.switch_to.default_content() #进入一个iframe操作完成后，返回原来的页面需跳出iframe
# driver.find_element_by_id('_mail_tabitem_1_39').click()
