# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:58:19 2024

@author: DELL-USER
"""

from role import swordsman,adviser,dancer

import random

if __name__=='__main__':
    player=list()
    com=list()
    
    for i in range(3):
        p=int(input('劍士按1,軍師按2,舞者按3:'))
        name=input('輸入角色姓名:')
        
        if p==1:
            player.append(swordsman(name,100,80))
            
        elif p==2:
            player.append(adviser(name,100,180))
        
        else:
            player.append(dancer(name,100,100))
            
    print(player)    
    
    for i in range(3):
         c=random.randint(1,3)
         name=['茂野','千尋','彌豆子','白龍','佐藤','湯婆婆']
         
         
         if c==1:
             com.append(swordsman(random.choice(name),100,80))
             
         elif c==2:
             com.append(adviser(random.choice(name),100,180))
         
         else:
             com.append(dancer(random.choice(name),100,100))
             
    print(com)
             
    while len(player) > 0 and len(com) > 0:
        
        
        name=['茂野','千尋','彌豆子','白龍','佐藤','湯婆婆']
        p=name.pop()
        print(p)
        
             
         
             
    
         
    
            
        
    
   
    
   
    
   
    
   
    
   
    
   
    