# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 02:15:18 2021

@author:Satyam
"""


while True:  
    try: 
        budget = float(input("Enter your budget : ")) 
        # budget can be float or int 
        bud = budget
    except ValueError: 
        print("digits only") 
        continue
    else: 
        break
  
# dictionary to store
dic ={"Product Name":[], "Quantity":[], "Price":[]} 
  
# converting dictionary to list for further updation 
lis = list(dic.values()) 
  
 
pro = lis[0] 
  
 
quan = lis[1] 
  

pri = lis[2] 
  
while True: 
    try: 
        ch = int(input("1.ADD an item\n2.EXIT\nEnter your choice : ")) 
    except ValueError: 
        print("\nERROR: Only 1 or 2 can be chosen") 
        continue
    else: 
        # check the budget
        
        if ch == 1 and bud>0:        
   
            # input products name                 
            pn = input("Enter Product  : ")  
            # input quantity of product 
            q = input("Enter quantity : ") 
            # input price of the product 
            p = float(input("Enter price : "))   
  
            if p>bud: 
                # checks if price is less than budget 
                print("\nCAN, T BUT THE PRODUCT")  
                continue
  
            else: 
                # checks if product name exists earlier
                if pn in pro:   
                    # index of that product 
                    ind = pro.index(pn)   

                    quan.remove(quan[ind])  
  
                    pri.remove(pri[ind])   
                    quan.insert(ind, q)    
                    pri.insert(ind, p)    
  
                    #calulating budget
                    bud = budget-sum(pri*q)    
  
                    print("\nAmount left  : ", bud) 
                else: 
                    
                    pro.append(pn)   
   
    
                    quan.append(q)    
  
                    
                    pri.append(p)     
  
                    
                    bud = budget-sum(pri)    
  
                    print("\Amount left  :", bud) 
  
        
        elif bud<= 0:  
            print("\nNO BUDGET")  
            break
        else: 
            break 
  

print("\nAmount left : Rs.", bud)  
  

if bud in pri:  
    #  printing the name of the product which can buy 
    print("\nAmount left can buy you a", pro[pri.index(bud)])   
  
print("\n\n\nGROCERY LIST") 
  
# GRocery list
for i in range(len(pro)):  
    print(pro[i], quan[i], pri[i])