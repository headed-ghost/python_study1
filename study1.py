#name='Ada Wang'
#name=name.upper()
#test='!@# qweasd QWE'
#test=test.upper()
#print(name)
#print(test)             upper用法 

#test=' pyth on '
#test=test.strip()
#print(test)            strip用法

#import this             Python之禅

#a=list(range(1,6,2))
#print(a)               range用法

#if 4 in range(1,6,2):
#    print('yes')
#else:
#    print('no')        输出的结果是'no'

#haoge=['牛b','帅','高','有钱']
#wode_ouxiang=['牛b','帅','聪明','高','有钱']
#for characteristic in wode_ouxiang:
#    if characteristic in haoge:
#        print('haoge has characteristics like this '+characteristic)
#    else:
#        print('辣鸡豪哥，一点也不'+characteristic)      
#for循环及元素是否在列表中

#添加字典
#alien_0={'color':'green','point':5}
#alien_0['x_position']=0
#alien_0['y_position']=25
#print(alien_0)

#遍历字典:键-值对
#user_0={'username':'haoge','first':'hao','last':'ge'}
#for v,k in user_0.items():
#    print(v)
#    print(k)

#字典的形式
#test1={10:'qwe','qwe':3}
#test2=test1.items()
#print(test2)

#sandwich_orders=['金枪鱼三明治','培根三明治','炸鸡腿三明治','牛肉三明治']
#finished_sandwich=[]
#while sandwich_orders:
#    mading_sandwich=sandwich_orders.pop()
#    finished_sandwich.append(mading_sandwich)
#    print("I'm mading your "+mading_sandwich)
#print("\nWell done!I have finished all the sandwich here are your sandwiches:\n")
#order=''
#for sandwich in finished_sandwich:
#    order+=sandwich+' '
#print(order)                               #熟食店

#def print_pet(animal_name,animal_type='dog'):
#    print(animal_type)
#    print(animal_name)
#print_pet('cat','miao')                    #有关函数的形参

#为什么没法打印名称出来？
#class_08=['myw','ly','bj','cyj','fyt']
#school_zbdx=['a','b','c','d',[class_08]]
#for student in school_zbdx:
#    if student in class_08:
#        print(student)
#如果没有给定参数，则构造函数将创建一个新的空列表。如果指定了参数，则该参数必须是可迭代的

#有关Python函数的return,感觉有点难搞懂
#def name(first,last):
#    print(first,last)
#    return "which run first?"
#print(name('haoge','niubi'),'\ntest')
#a=name('haoge','zhenshuai')
#print(a)

#二次函数求根
#from math import sqrt
#def quadratic(a,b,c):
#    delta=b*b-4*a*c
#    if delta<0:
#        return 'error','error'
#    elif delta==0:
#        return -b/2*a
#    else:
#        return (-b+sqrt(delta))/(2*a),(-b-sqrt(delta))/(2*a);
#a=input("输入a ")
#b=input("输入b ")
#c=input("输入c ")
#x1,x2=quadratic(float(a),float(b),float(c))
#print(x1,x2)
#print(quadratic(float(a),float(b),float(c))            #如果函数有多个返回值，返回元组

#用Python玩汉诺塔
#def hanoi(n,a,b,c):
#    if n==1:
#        print(a,'-->',c)
#    else:
#        hanoi(n-1,a,c,b)
#        print(a,'-->',c)
#        hanoi(n-1,b,a,c)
#hanoi(3,'A','B','C')

#from hgnb import *
#fun()
#grade(100)                 #读取函数

#class Restaurant:
#    def __init__(self,restaurant_name,cuisine_type):
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type

#    def sayhi(self):
#        print("welcome to %s !We have %s here!"%(self.restaurant_name,self.cuisine_type))

#    def serve(self,*order):
#        print("Hello sir!What do you need?\n")
#        for dish in order:
#            print("OK,%s will do %s for you!"%(self.restaurant_name,dish))

#restaurant_LongQuan=Restaurant('龙泉餐厅','大锅饭')
#restaurant_LongQuan.sayhi()
#restaurant_LongQuan.serve('rice','noodle','soop');print("\n")

#class IceCreamStation(Restaurant):
#    def __init__(self,restaurant_name,cuisine_type,flavor):
#        super(IceCreamStation,self).__init__(restaurant_name,cuisine_type)
#        #调用父类的构造方法的别的方式
#        #super().__init__(restaurant_name,cuisine_type)
#        #Restaurant.__init__(self,restaurant_name,cuisine_type)
#        self.flavor=flavor

#    def serve(self, *order):
#        for flavor in order:
#            print("OK! "+self.restaurant_name+' will do '+flavor+' icecream for you!')

#IceCreamStation1=IceCreamStation('蜜雪冰城','icecream','chocolate,vanila,strawberry')
#IceCreamStation1.sayhi()
#IceCreamStation1.serve('vanila','chocolate')

#另一个有趣的问题
#class Dog:
#    def __init__(self):
#        print("汪!")
#    def bar(self):
#        print("汪汪!")
#Dog1=Dog         #相当于给Dog改名字，也可以理解为地址传递，可以理解为Dog1就是Dog，d=Dog1()就是d=Dog()
#d=Dog1()           #相当于创建了名为d的Dog类或Dog1类
#d.bar()      
#Dog.bar(1)       #这样可以直接执行方法

#class Test:
#    def prt(self):
#        print(self)            #self表示实例的地址(实例)
#        print(self.__class__)
 
#t = Test()
#t.prt()

#class people:
#    name = ''
#    age = 0
#    __weight = 0
#    def __init__(self,n,a,w):
#        self.name = n
#        self.age = a
#        self.__weight = w
#    def speak(self):
#        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#class student(people):
#    grade = ''
#    def __init__(self,n,a,w,g):
#        people.__init__(self,n,a,w)
#        self.grade = g
#    def speak(self):
#        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
#s = student('ken',10,60,3)
#s.speak()

#file_name1=r'Faster than light.txt'     #相对路径
#with open(file_name1) as file1:
#    a=file1.read()
#    print(a)
#file_name2=r'D:\BaiduNetdiskDownload\test1.txt'         #绝对路径，最后引号前面加个r
#with open(file_name2) as file2:
#    b=file2.read()
#    print(b)
#with open(file_name1) as file1:
#    a=file1.readline()
#    print(a)
#    for line in a:
#        print(line)
#file1=open(file_name1,'a+')
#file1.write('\nSeen through my eyes\nTime slow down')
##a=file1.read()
##print(a)               #这样不能正常输出，因为指针指在文件末尾
#file1.seek(0)           #通过这样将指针回到开头，但还有一个flush没有搞懂
#a=file1.read()
#print(a)

#有关异常
#print('请输入数字，按q退出')
#while True:
#    a=input("first number: ")
#    b=input("second number: ")
#    if(a=='q'or b=='q'):
#        print("老子不陪你玩了")
#        break
#    try:
#     answer=int(a)+int(b)
#    except ValueError:
#     print("给老子输入数字")
#    else:
#     print(answer)