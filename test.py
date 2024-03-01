num=int(input("輸入0~255之間的數字:"))

if(0<=num<=255):
 
 a=num-2**7
 if(a>=0):
     x7=1
 else:
     x7=0
     a=num
     
 b=a-2**6
 if(b>=0):
     x6=1
 else:
     x6=0
     b=a
     
 c=b-2**5
 if(c>=0):
     x5=1
 else:
     x5=0
     c=b
     
 d=c-2**4
 if(d>=0):
     x4=1
 else:
     x4=0
     d=c
    
 e=d-2**3
 if(e>=0):
     x3=1
 else:
     x3=0
     e=d
     
 f=e-2**2
 if(f>=0):
     x2=1
 else:
     x2=0
     f=e
     
 g=f-2**1
 if(g>=0):
     x1=1
 else:
     x1=0
     g=f
    
 h=g-2**0
 if(h>=0):
     x0=1
 else:
     x0=0
     
 print("二進位:",x7,x6,x5,x4,x3,x2,x1,x0)
 
else:print("不可輸入0~255以外的數字")

y2=x7*2**3+x6*2**2+x5*2**1+x4*2**0
if(y2>=10):
    y2=y2-10
    y2=chr(65+y2)
else:
    y2=y2
    
y1=x3*2**3+x2*2**2+x1*2**1+x0*2**0
if(y1>=10):
    y1=y1-10
    y1=chr(65+y1)
else:
    y1=y1
    
print("十六進位:",y2,y1)
