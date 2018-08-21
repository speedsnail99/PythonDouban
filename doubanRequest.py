#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : doubanRequest.py
# @Author: G
# @Date  : 2018/8/5

import requests

url = 'https://movie.douban.com'





doubanText = requests.get(url).text

print(doubanText)
