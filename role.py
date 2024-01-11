# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:39:14 2024

@author: DELL-USER
"""

class swordsman:
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp
        
    def sethp(self,hp):
        self.__hp=hp
        
    def setmp(self,mp):
        self.__mp=mp
        
    def getname(self):
        return self.__name
    
    def gethp(self):
        return self.__hp
    
    def getmp(self):
        return self.__mp
    
    def fight(self):
        print('劍士攻擊')
        
    def skill(self):
         print('三十六煩惱鳳')

class adviser:
    
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp
        
    def sethp(self,hp):
        self.__hp=hp
        
    def setmp(self,mp):
        self.__mp=mp
        
    def getname(self):
        return self.__name
    
    def gethp(self):
        return self.__hp
    
    def getmp(self):
        return self.__mp
    
    def fight(self):
        print('突襲部隊')
        
    def skill(self):
         print('金窟棒')
         
    def smart(self):
        print('血滴子')
        
        
class dancer:
    def __init__(self,name,hp,mp):
        self.__name=name
        self.__hp=hp
        self.__mp=mp
        
    def sethp(self,hp):
        self.__hp=hp
        
    def setmp(self,mp):
        self.__mp=mp
        
    def getname(self):
        return self.__name
    
    def gethp(self):
        return self.__hp
    
    def getmp(self):
        return self.__mp
    
    def fight(self):
        print('風雲變色攻擊')
        
    def skill(self):
         print('分身乏術')
         
    def cure(self):
        print('守護者技能')
        
        
    
         
         
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        