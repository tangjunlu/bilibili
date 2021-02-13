#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：青竹红颜
@Date    ：2021/2/13 12:44 
"""
from api import bilibiliApi


def get_my_info(sess_data,bili_jct):
    info = bilibiliApi.my_info(sess_data,bili_jct)
    if info == -101:
        return '账号未登录'
    uid = info['mid']
    user_name = info['uname']
    user_id = info['userid']
    sign = info['sign']
    birthday = info['birthday']
    sex = info['sex']
    rank = info['rank']
    data = f'''UID:{uid}
昵称:{user_name}
用户名:{user_id}
签名:{sign}
性别:{sex}
生日:{birthday}
会员等级:{rank}
'''
    return data