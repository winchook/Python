#求1-2+3-4+5.....99的所有数的和

n = 1
oushu = 0
jishu = 0
while (n < 100):
    if n % 2 == 0:
        oushu = oushu + n
    else:
        jishu = jishu + n
    n = n + 1
sum = jishu - oushu
print (sum)
