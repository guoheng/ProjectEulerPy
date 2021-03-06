
#Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
#Triangle           P3,n=n(n+1)/2           1, 3, 6, 10, 15, ...
#Square           P4,n=n^2           1, 4, 9, 16, 25, ...
#Pentagonal           P5,n=n(3n-1)/2           1, 5, 12, 22, 35, ...
#Hexagonal           P6,n=n(2n-1)           1, 6, 15, 28, 45, ...
#Heptagonal           P7,n=n(5n-3)/2           1, 7, 18, 34, 55, ...
#Octagonal           P8,n=n(3n-2)           1, 8, 21, 40, 65, ...
#
#The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
#
#   1. The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
#   2. Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
#   3. This is the only set of 4-digit numbers with this property.
#
#Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
import logging
import permute

def IsCyclic(a, b):
    return a%100 == b//100

def main(args):
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []

    n = 10
    temp = n*(n+1)//2
    while (temp < 10000):
        if (temp > 1000): p3.append(temp)
        temp = n*n
        if (temp > 1000 and temp < 10000): p4.append(temp)
        temp = n*(3*n-1)//2
        if (temp > 1000 and temp < 10000): p5.append(temp)
        temp = n*(2*n-1)
        if (temp > 1000 and temp < 10000): p6.append(temp)
        temp = n*(5*n-3)//2
        if (temp > 1000 and temp < 10000): p7.append(temp)
        temp = n*(3*n-2)
        if (temp > 1000 and temp < 10000): p8.append(temp)
        n += 1
        temp = n*(n+1)//2

    p = [p3, p4, p5, p6, p7, p8]

    for idx in permute.all_perms(list(range(1,6))):
        for n1 in p3:
            for n2 in p[idx[0]]:
                if (not IsCyclic(n1, n2)): continue
                for n3 in p[idx[1]]:
                    if (not IsCyclic(n2, n3)): continue
                    for n4 in p[idx[2]]:
                        if (not IsCyclic(n3, n4)): continue
                        for n5 in p[idx[3]]:
                            if (not IsCyclic(n4, n5)): continue
                            for n6 in p[idx[4]]:
                                if (not IsCyclic(n5, n6)): continue
                                if (IsCyclic(n6, n1)):
                                    logging.info((n1, n2, n3, n4, n5, n6))
                                    logging.info(idx)
                                    logging.info(sum([n1, n2, n3, n4, n5, n6]))
