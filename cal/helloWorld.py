'''
Author: CC-TSR
Date: 2021-01-05 12:38:16
LastEditTime: 2021-01-11 22:39:55
LastEditors: xiejiancheng1999@qq.com
Description: 
FilePath: \teach_for_noobXi\cal\helloWorld.py
可以输入预定的版权声明、个性签名、空行等
'''

def cal(numbers, method):
    """
   这是一个牛逼的计算器
   你可以通过第一个参数决定你要算啥
   第二个参数决定了运算的方法
    """
    count = 0
    for i in numbers:
        count += 1
        if(count == 1):
            res = i
        else:
            if method == '+':
                res += i
            elif method == '-':
                res -= i
            elif method == '*':
                res *= i
            elif method == '/':
                res /= i

            
    
    return res

if __name__ == '__main__':
    res =  cal([1,2,3],'-')
    print(res)
    