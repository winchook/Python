import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        v = self.get_argument('username')
        print(v)
        self.redirect('/index.html')

settings = {
    'template_path':'templates',
    'static_path':'static',
    'static_url_prefix':'/ppp/',
}

#application对象中封装了：路由信息，配置信息
application = tornado.web.Application([
    (r"/login.html",LoginHandler),
    (r"/index.html",MainHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8000)

    #开启r,w,e = select.select(inputs,)
    tornado.ioloop.IOLoop.instance().start()


#浏览器访问方式:
# http://127.0.0.1:8000/login.html