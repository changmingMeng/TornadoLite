#! /usr/bin/python
# -*- coding:utf-8 -*-

import datetime
import dbManip


class Control(object):

    def __init__(self):
        self.dbm = dbManip.dbManipulate("mydb")

    def insert(self, carNum, descript, imgUrl):
        print "Control::insert", carNum, descript, imgUrl
        dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert = "insert into car(dateTime, carNum, descript, imgUrl) values('"+dateTime+"', '"+carNum+"', '"+descript+"', '"+imgUrl+"')"
        print insert
        self.dbm.insert(insert)
        self.dbm.Commit()

    def select(self, carNum):
        print "Countrol::select", carNum
        select = "select * from car where carNum='"+carNum+"'"
        print select
        return self.dbm.select(select)
        #self.dbm.Commit()

if __name__ == "__main__":
    ct = Control()
    print ct.select("赣L123")