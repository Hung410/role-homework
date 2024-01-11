# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:51:31 2024

@author: DELL-USER
"""

from role import swordsman,adviser,dancer

import random

if __name__=='__main__':
    ad=adviser('孔明',100,60)
    sm=swordsman('索龍',100,90)
    while ad.gethp() >0 and sm.gethp() >0:
        n=random.randint(1,100)
        if n%2==0:
            print(ad.getname(),'使出:',end='')
        
            if random.randint(1,10)==3:
                ad.skill()
                blood=random.randint(15,30)
            else:
                ad.fight()
                boold=random.randint(5,10)
          
            ad.fight() 
            boold=random.randint(5,10)
            sm.sethp(sm.gethp()-boold)
            print(sm.getname(),'的血量剩:',sm.gethp())
        else:
            print(sm.getname(),'使出:',end='')
            
            if random.randint(1,10)==5:
                ad.skill()
                blood=random.randint(15,30)
            else:
                ad.fight()
                boold=random.randint(5,10)
            
            
            
            sm.fight() 
            boold=random.randint(5,10)
            ad.sethp(ad.gethp()-boold)
            print(ad.getname(),'的血量剩:',ad.gethp())
            
if ad.gethp()>0:
  print(ad.getname(),'winner')  
else:
   print(sm.getname(),'winner')      
   
  
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    