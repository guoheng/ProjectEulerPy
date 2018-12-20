
#Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#Triangle           Tn=n(n+1)/2           1, 3, 6, 10, 15, ...
#Pentagonal           Pn=n(3n-1)/2           1, 5, 12, 22, 35, ...
#Hexagonal           Hn=n(2n-1)           1, 6, 15, 28, 45, ...
#
#It can be verified that T285 = P165 = H143 = 40755.
#
#Find the next triangle number that is also pentagonal and hexagonal.

import logging

def Triangle(n):
    return n*(n+1)//2

def Pentagonal(n):
    return n*(3*n-1)//2

def Hexagonal(n):
    return n*(2*n-1)

def main(args):
    t = 286
    p = 165
    h = 143

    done = 0
    while (done == 0):
        tri = Triangle(t)
        pen = Pentagonal(p)
        while(pen < tri):
            p += 1
            pen = Pentagonal(p)
        if (pen != tri):
            t += 1
            continue
        hexa = Hexagonal(h)
        while (hexa < tri):
            h += 1
            hexa = Hexagonal(h)
        if (hexa == tri):
            logging.info((t, p, h, tri))
            done = 1
        else:
            t += 1
