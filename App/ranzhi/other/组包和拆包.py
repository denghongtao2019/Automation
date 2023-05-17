#Auto:达实泽林
#Creat Time:2021/12/22 14:54
#Creat Function:组包和拆包
#Edit Auto:
#Edit Time:
#Edit Function:

#组包
#*args

# def f(a, *args):
#     print('a的值是：',a)
#     print('args的值是：',args)
# f(1,2,3,4,5,6)

#**kwargs
# def d(**kwargs):
#     print('kwargs的值是：',kwargs)
# d(a=1,b=2)

# def f(a,*args,**kwargs):
#     print(a,args,kwargs)
# f(1,2,3,b=1,c=2)

#拆包

# def func(a,b,c,d):
#     print(a,b,c,d)
# data = (1,2,3,4)
# func(*data)

# def person(name,age,**kwargs):
#     print('name:',name,'age:',age,'other:',kwargs)
# other = {'city':'BeiJing','job':'tesst'}
# person('xiaoming',18,**other)


