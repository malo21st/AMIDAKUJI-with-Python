#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:09:50 2018

@author: malo
"""

BOARD = [[0,0,0,0,0,0],
         [1,0,0,1,0,0],
         [1,0,1,0,1,0],
         [0,1,0,0,1,0],
         [0,1,0,1,0,0],
         [1,0,1,0,1,0],
         [1,0,0,1,0,0],
         [0,1,0,0,0,0],
         [0,0,0,0,0,0]]

class linkList:  
    # 初期化
    def __init__(self):
        self.symbol = "□　　"
        self.data = None
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
            self.setSymbol("■　　")
            if not YOKO:
                if self.right:
                    self.setSymbol("■▶◁")
                    self = self.right
                    YOKO = True
                elif self.left:
                    self = self.left
                    YOKO = True
                else:
                    self = self.next
                    YOKO = False
            else:
                if self.right:
                    self.setSymbol("■▷◀")
                self = self.next
                YOKO = False
        self.setSymbol("■　　")

    def backKuji(self):
        YOKO = False
        while self.prev:
#            print(self.data)
            self.setSymbol("■　　")
            if not YOKO:
                if self.right:
                    self.setSymbol("■▶◁")
                    self = self.right
                    YOKO = True
                elif self.left:
                    self = self.left
                    YOKO = True
                else:
                    self = self.prev
                    YOKO = False
            else:
                if self.right:
                    self.setSymbol("■▷◀")
                self = self.prev
                YOKO = False
        self.setSymbol("■　　")

def makeKuji():
    lst = []
    for line in BOARD:
        slt = []
        for obj in line:
            slt.append(linkList())
        lst.append(slt)
    setLink(lst)
    return lst

def setLink(lst):
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
                obj.symbol = "□▷◁"
            if BOARD[i][j-1] == 1:
                obj.left = lst[i][j-1]

def printKuji(lst):
    
    for line in lst:
        for obj in line:
            print(obj.symbol, end="")
        print()
    print()
           
def main():
    
    kuji0 = makeKuji()
    printKuji(kuji0)
    
    kuji0[0][4].goKuji()
    printKuji(kuji0)

    kuji1 = makeKuji()
    kuji1[8][2].backKuji()
    printKuji(kuji1)
    
if __name__ == '__main__':
    main()
