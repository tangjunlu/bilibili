#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：青竹红颜
@Date    ：2021/2/13 12:10 
"""
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


# 获取个人信息
def my_info(sess_data, bili_jct):
    url = 'http://api.bilibili.com/x/member/web/account'
    cookie = {
        'SESSDATA': sess_data,
        'bili_jct': bili_jct
    }
    response = requests.get(url=url, headers=HEADERS, cookies=cookie).json()
    if response['code'] == 0:
        return response['data']
    else:
        return response['code']
