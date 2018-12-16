#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:09:50 2018
@author: malo
"""
import random
import copy

def makeKujiMap(num):
    LIST0 = [0, 0, 1]
    LIST1 = [0, 1]
    LIST2 = [0, 1]
    init = []
    for i in range(num):
        init.append(0)

    FLAG = True   
    while FLAG:
        MAP = [init]
        for i in range(8):
            line = [random.choice(LIST0)]
            for j in range(num-2):
                if line[-1] == 1:
                    line.append(0)
                else:
                    line.append(random.choice(LIST1))
            line.append(0)
            MAP.append(line)
            line = [random.choice(LIST2)]
        MAP.append(init)
       
        chk1 = 1
        for i in range(num-1):
            chk0 = 0
            for v in MAP:
                chk0 += v[i]
#            print(chk0, end=" ")
            if (chk0 > 2) and (chk0 < 6):
                pass
            else:
                chk0 = 0
#            print(chk0)
            chk1 = chk1 * chk0
        if chk1:
            return MAP
        else:
            continue
   
class linkList: 
    # 初期化
    def __init__(self):
        self.symbol = "| "
#        self.data = None
        self.next = None
        self.prev = None
        self.right= None
        self.left = None

    def setSymbol(self, s):
        self.symbol = s

    def goKuji(self):
        YOKO = False
        while self.next:
#            print(self.data)
            self.setSymbol("v ")
            if not YOKO:
                if self.right:
                    self.setSymbol(">>")
                    self = self.right
                    YOKO = True
                elif self.left:
                    self.setSymbol("< ")
                    self = self.left
                    YOKO = True
                else:
                    self = self.next
                    YOKO = False
            else:
                if self.right:
                    self.setSymbol("v<")
                self = self.next
                YOKO = False
        self.setSymbol("# ")

    def backKuji(self):
        YOKO = False
        while self.prev:
#            print(self.data)
            self.setSymbol("^ ")
            if not YOKO:
                if self.right:
                    self.setSymbol(">>")
                    self = self.right
                    YOKO = True
                elif self.left:
                    self.setSymbol("< ")
                    self = self.left
                    YOKO = True
                else:
                    self = self.prev
                    YOKO = False
            else:
                if self.right:
                    self.setSymbol("^<")
                self = self.prev
                YOKO = False
        self.setSymbol("# ")

def makeKuji(BOARD):
    lst = []
    for line in BOARD:
        slt = []
        for obj in line:
            slt.append(linkList())
        lst.append(slt)
    setLink(lst, BOARD)
    return lst

def setLink(lst, BOARD):
    for (i, line) in enumerate(lst):
        for (j, obj) in enumerate(line):
            obj.data = [i,j]
            try:
                obj.next = lst[i+1][j]
            except:
                pass
          
            if i == 0:
                pass
            else:
                obj.prev = lst[i-1][j]

            if BOARD[i][j] == 1:
                obj.right = lst[i][j+1]
                obj.symbol = "|-"
            if BOARD[i][j-1] == 1:
                obj.left = lst[i][j-1]

def printKuji(lst):
    for line in lst:
        for obj in line:
            print(obj.symbol, end="")
        print()
    print()
    
def print2Kuji(lst1, lst2):
    for lin1,lin2 in zip(lst1, lst2):
        for obj1 in lin1:
            print(obj1.symbol, end="")
        print("　", end="")
        for obj2 in lin2:
            print(obj2.symbol, end="")
        print()
    print()
          
def print3Kuji(lst0, lst1, lst2):
    for lin0,lin1,lin2 in zip(lst0, lst1, lst2):
        for obj0 in lin0:
            print(obj0.symbol, end="")
        print("　", end="")
        for obj1 in lin1:
            print(obj1.symbol, end="")
        print("　", end="")
        for obj2 in lin2:
            print(obj2.symbol, end="")
        print()
    print()

def main():
    kuji_map = makeKujiMap(8)
   
    kuji0 = makeKuji(kuji_map)
    kuji1 = copy.deepcopy(kuji0)
    kuji2 = copy.deepcopy(kuji0)
    kuji3 = copy.deepcopy(kuji0)

    kuji1[0][4].goKuji()
    kuji2[9][2].backKuji()
    kuji3[3][2].goKuji()

    print3Kuji(kuji0, kuji1, kuji2)
#    print2Kuji(kuji0, kuji3)
  
if __name__ == '__main__':
    main()
    