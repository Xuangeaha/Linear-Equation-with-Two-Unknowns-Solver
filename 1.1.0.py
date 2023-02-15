print("--------------------------------------------------")
print("  解一元二次方程计算器   1.1.0")
print("  copyright:轩哥啊哈OvO   版权所有，侵犯必究")
print("  Optifine版本：0.0020.1938   有新版本Optifine可供下载……")
print("--------------------------------------------------")
print("  解方程：ax²+bx+c=0")
print("--------------------------------------------------")
import time
import math
time.sleep(0.3)
a = input("  请设置二次项系数a的值：")
b = input("  请设置一次项系数b的值：")
c = input("  请设置常数项c的值：")
print("--------------------------------------------------")
print("  解方程：" + str(a) + "x²+" + str(b) + "x+" + str(c) + "=0")
print("--------------------------------------------------")
print("  正在检查a的值……")
time.sleep(0.4)
print("  a的值检测完毕！")
print("  a的值为：" + str(a))
time.sleep(0.1)
print("  a值已成功带入函数……")
time.sleep(0.1)
print("  正在检查b的值……")
time.sleep(0.4)
print("  b的值检测完毕！")
print("  b的值为：" + str(b))
time.sleep(0.1)
print("  b值已成功带入函数……")
time.sleep(0.1)
print("  正在检查c的值……")
time.sleep(0.4)
print("  c的值检测完毕！")
print("  c的值为：" + str(c))
time.sleep(0.1)
print("  c值已成功带入函数……")
time.sleep(0.1)
print("  正在准备计算delta……")
time.sleep(0.05)
print("  开始计算delta……")
print("  引入公式：delta=b²-4ac")
time.sleep(0.05)
print("  正在计算……")
time.sleep(2)
deltab2 = int(b)**2
print("  delta第一部分计算完成！")
print("  delta第一部分的值为：" + str(deltab2))
time.sleep(0.1)
delta4ac = 4*int(a)*int(c)
print("  delta第二部分计算完成！")
print("  delta第二部分的值为：" + str(delta4ac))
time.sleep(0.1)
delta = deltab2 - delta4ac
print("  delta已计算完成！")
print("  delta的值为：" + str(delta))
time.sleep(0.05)
print("  正在准备计算x……")
time.sleep(0.05)
print("  开始计算x……")
print("  引入公式：x=(-b±√delta)/2a")
time.sleep(0.05)
print("  正在计算……")
time.sleep(2)
x1 = int(b)*-1
print("  x第一部分计算完成！")
print("  x第一部分的值为：" + str(x1))
time.sleep(0.05)
print("  x第一部分已代入函数……")
time.sleep(0.2)
x2 = math.sqrt(delta)
print("  x第二部分计算完成！")
print("  x第二部分的值为：" + str(x2))
time.sleep(0.05)
print("  x第二部分已代入函数……")
time.sleep(0.2)
x3 = int(a)*2
print("  x第三部分计算完成！")
print("  x第三部分的值为：" + str(x3))
time.sleep(0.05)
print("  x第三部分已代入函数……")
time.sleep(0.2)
print("  正在计算第一种情况：+delta……")
time.sleep(1)
xs1top = x1 + x2
print("  x第一种情况分子的值为：" + str(xs1top))
xdown = x3
print("  x第一种情况分母的值为：" + str(xdown))
x1s = xs1top / xdown
time.sleep(0.2)
print("  x第一种情况计算完成！")
print("  x第一种情况的值为：" + str(x1s))
print("  正在计算第二种情况：-delta……")
time.sleep(0.7)
xs2top = x1 - x2
print("  x第二种情况分子的值为：" + str(xs2top))
print("  x第二种情况分母的值已设置为第一种情况分母：" + str(xdown))
x2s = xs2top / xdown
time.sleep(0.2)
print("  x第二种情况计算完成！")
print("  x第二种情况的值为：" + str(x2s))
time.sleep(0.1)
print("  所有函数进程已结束！")
print("  正在得出结论……")
time.sleep(0.1)
print("  即将得出结论……")
time.sleep(2)
print("--------------------------------------------------")
if x1s == x2s:
    xts1 = "  解得：x1=x2="
    xts2 = str(x1s)
    print(xts1 + xts2)
else:
    xys1 = "  解得：x1="
    xys2 = str(x1s)
    xys3 = ",x2="
    xys4 = str(x2s)
    print(xys1 + xys2 + xys3 + xys4)
print("--------------------------------------------------")
Stop = input()


print("""
感谢您使用本计算器！
制作者：轩哥啊哈OvO
历史版本：
1.0.0 正式版发布
1.0.1 新增输入a、b、c的值后的原方程显示
1.0.2 新增解方程过程中a、b、c带入函数前的显示
1.0.3 新增解方程过程中delta第一部分、第二部分和结果的显示
1.0.4 新增末尾历史版本提示
1.0.5 新增解方程过程中x第一部分、第二部分、第三部分结果的显示
1.0.6 新增解方程过程中x第一种情况及过程和第二种情况及过程结果的显示
1.0.7 更改方程结果显示函数名
1.0.8 新增解方程过程中x第一种情况和第二种情况带入函数显示
1.0.9 优化并缩短部分计算时间
1.0.10 字符缩进
1.1.0 正式版发布
1.1.1 新增Optifine多进程函数 Optifine版本：0.0020.1938



""")


































