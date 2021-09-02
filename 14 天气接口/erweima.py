# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/28 17:04
# @Author    :   Chasion
# Description:
from MyQR import myqr
import os

version, level, qr_name = myqr.run(
    words='xiao wang, ni neng bu neng bu yao zai ban zhe lian le',
    version=1,
    level='H',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name='pp.png',
    save_dir=os.getcwd()
)
