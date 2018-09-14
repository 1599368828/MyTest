#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
#定义初始值,sum指的是总和，start指的是1-100的整数
sum=0
start=1
while True:
   if start==101:
     break  
#%运算是取余数，判断是奇数还是偶数
   if start%2 ==1:
     sum=sum+start
   if start%2 ==0:
     sum=sum-start
   start +=1
print(sum)
test
test1
test pull
