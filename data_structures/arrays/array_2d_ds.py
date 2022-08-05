# print("Hola Mundo")

#En este ejemplo renovado, se estará trabajando en un ambiente Linux virtualizado para no contaminar el ambiente local del equipo

# print("Hola Mundo desde Ubuntu 22.04")

# print("Segunda prueba del Hola Mundo en Ubuntu")

import math
import os
import random
import re
import sys

"""arr = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0],
]"""

arr = [
    [-1,-1,0,-9,-2,-2],
    [-2,-1,-6,-8,-2,-5],
    [-1,-1,-1,-2,-3,-4],
    [-1,-9,-2,-4,-4,-5],
    [-7,-3,-3,-2,-9,-9],
    [-1,-3,-1,-2,-4,-5],
]

def hourglassSum(arr):
    result, range_n, size = None, 4, 3
    for pos_i in range(range_n):
        for pos_j in range(range_n):
            print("---")
            print("[%s,%s]: %s" %(pos_i, pos_j, arr[pos_i][pos_j]))
            hg_result = 0
            for pos_h in range(size):
                row = ""
                for pos_k in range(size):
                    if not (pos_h == 1 and pos_k == 0) and not (pos_h == 1 and pos_k == 2):
                        row += "%s " %(arr[pos_i+pos_h][pos_j+pos_k])
                        hg_result += arr[pos_i+pos_h][pos_j+pos_k]
                    else:
                        row += "  "
                    
                print(row)
            print ("Hourglass total sum: %s" %hg_result)
            result = hg_result if result == None else hg_result if hg_result > result else result


    return result

if __name__ == '__main__':
    print("\nThe largest HourGlass sums: %s" %hourglassSum(arr)) 
