#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import init_db
from sqlalchemy.orm import sessionmaker,relationship

Session_class = sessionmaker(bind=init_db.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()

def User_Basic_Data():
    """初始化数据，这个手动添加"""
    u1 = init_db.User(name="Alex",password="123456")
    u2 = init_db.User(name="Jack",password="123456")
    u3 = init_db.User(name="Rain",password="123456")
    session.add_all([u1,u2,u3])
    session.commit()

User_Basic_Data()
session.close()