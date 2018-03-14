#!/usr/bin/env python
#-*- coding=utf8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

############################################
username = "替换成自己的"
password = "替换成自己的"
############################################


driver = webdriver.Firefox()


driver.get("https://login.taobao.com/member/login.jhtml")

element = driver.find_element_by_link_text("密码登录")
element.click()
driver.find_element_by_id("TPL_username_1").clear()
driver.find_element_by_id("TPL_password_1").clear()
driver.find_element_by_id("TPL_username_1").send_keys(username)
sleep(1);
driver.find_element_by_id("TPL_password_1").send_keys(password)
sleep(1);


# 获取滑动条的size
span_background = driver.find_element_by_css_selector("#nc_1__scale_text > span")
span_background_size = span_background.size
print(span_background_size)

# 获取滑块的位置
button = driver.find_element_by_css_selector("#nc_1_n1z")
button_location = button.location
print(button_location)

# 拖动操作：drag_and_drop_by_offset
# 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
x_location = button_location["x"] + span_background_size["width"]
y_location = button_location["y"]
ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()
#driver.get_cookies()取得cookie


sleep(1)
driver.find_element_by_id("J_SubmitStatic").click()
cookie = "; ".join([item["name"] + "=" + item["value"] +"\n" for item in driver.get_cookies()])
print cookie