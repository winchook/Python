from wsgiref.simple_server import make_server


def f1(req):
    print(req)
    print(req["QUERY_STRING"])

    f1=open("index1.html","rb")
    data1=f1.read()
    return [data1]

def f2(req):

    f2=open("index2.html","rb")
    data2=f2.read()
    return [data2]

import time

def f3(req):        #模版以及数据库

    f3=open("index3.html","rb")
    data3=f3.read()
    times=time.strftime("%Y-%m-%d %X", time.localtime())
    data3=str(data3,"utf8").replace("!time!",str(times))#这里的格式是自己定义的!time!，和html里面一致即可

    return [data3.encode("utf8")]


def routers():

    urlpatterns = (
        ('/winchoo',f1),
        ('/chason',f2),
        ("/cur_time",f3)
    )
    return urlpatterns


def application(environ, start_response):

    print(environ['PATH_INFO'])
    path=environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])


    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode("utf8")]

httpd = make_server('', 8000, application)

print('Serving HTTP on port 8000...')

# 开始监听HTTP请求:

httpd.serve_forever()