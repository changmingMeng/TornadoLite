#! /usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import tornado.ioloop
import tornado.web
import hashlib
import Control



class MainHandler(tornado.web.RequestHandler):
  """主索引的处理"""
  def get(self):
      print "running MainHandler get()"
      self.redirect('/login', permanent=False, status=302)



class LoginHandler(tornado.web.RequestHandler):
  """登录界面的请求处理"""
  def get(self):
      print "running LoginHandler get()"
      self.render("login.html")

  def post(self):
    #debug版伪登入
    print "running LoginHandler post()"
    account = self.get_argument("account")
    password = self.get_argument("password")
    print account, password
    if account == password:
      self.redirect('/manage', permanent=False, status=302)
    else:
      self.add_header("userlogin", "fail")


class ManageHandler(tornado.web.RequestHandler):
  """处理管理界面的请求"""
  def get(self):
    print "running ManageHandler get()"
    self.render('manage.html')

class InsertHandler(tornado.web.RequestHandler):
  """向数据库存储信息"""
  def get(self):
    self.render("test.html")

  def post(self):
    province = self.get_argument('province')
    city = self.get_argument('city')
    carnum = self.get_argument('carnum')
    descript = self.get_argument('descript')
    print "view::InsertHandler", province, city, carnum, descript
    ctl = Control.Control()
    ctl.insert(province+city+carnum, descript, "E:/picture/")
    self.redirect('/manage')

class SelectHandler(tornado.web.RequestHandler):
    """从数据库取信息"""


    def get(self):
        self.render("select.html")

    def post(self):
        carNum = self.get_argument('carnum')
        ctl = Control.Control()
        descript, dateTime, carNum, imgUrl= ctl.select(carNum)
        self.render("selectResult.html",
                    descript=descript+imgUrl,
                    dateTime=dateTime,
                    carNum=carNum )

def make_app():
    return tornado.web.Application([(r'/', MainHandler),
                                    (r'/login', LoginHandler),
                                    (r'/manage', ManageHandler),
                                    (r'/select', SelectHandler),
                                    (r'/insert',InsertHandler)],
      cookie_secret='jf0239u0fr9n',
      template_path=os.path.join(os.path.dirname(__file__), "templates"),
      static_path=os.path.join(os.path.dirname(__file__), "static"),
      debug=True,
    )


if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.ioloop.IOLoop.current().start()
