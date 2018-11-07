#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

#初始化数据库，需要手动单独运行

from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#create database mphost CHARACTER SET utf8;
engine = create_engine("mysql+pymysql://root:123456@10.63.64.147/mphost?charset=utf8",  #要写入中文必须加上?charset=utf8
                       encoding='utf-8') #echo=True #echo的作用就是打印出执行的过程，所有的信息都打印出来

Base = declarative_base()

class Host(Base):
    """初始化创建的主机表，8个字段"""
    __tablename__ = 'hosts'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),nullable=False)
    hostid = Column(Integer,default=0)
    ip = Column(String(64),nullable=False)
    port = Column(String(64),nullable=False)
    operation = Column(String(64),nullable=False)
    status = Column(String(64),nullable=False)
    hostaddr = Column(String(64),nullable=False)
    hosttype = Column(String(64),nullable=False)

    def __repr__(self):
        return  "%s,%s,%s,%s,%s,%s,%s,%s" %(self.hostname,self.hostid,self.ip,self.port,self.operation,self.status,self.hostaddr,self.hosttype)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    password = Column(String(32), nullable=False)

    def __repr__(self):
        return self.password


Base.metadata.create_all(engine)