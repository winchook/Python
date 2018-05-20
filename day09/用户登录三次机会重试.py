#用户登录，使其有三次机会重试
n = 1
while n < 4:
    print("第",n,"次请输入")
    user_name = input("请输入用户名：")
    user_pass = input("请输入密码：")
    if (user_name == "root") and (user_pass == "123.com"):
        print("登录成功")
        break
    else:
        print("登录失败")
        if n == 3:
            print("对不起，三次机会已用完，账号已被锁定，请联系客服。")
    n = n + 1