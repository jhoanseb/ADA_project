from sys import stdin
import time
import math

"""
Nombre: Jhoan Sebastian Lozano
Código: 8931869
Código de honor del curso:
Como miembro de la comunidad académica de la 
Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""

m = None
LIMIT_HI = [0, 10**15, 44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 
  100, 87, 78, 72, 67, 63, 61, 59, 57, 56, 55, 54, 54, 54, 54, 54, 54, 
  54, 54, 54, 55, 55, 56, 56, 57, 57, 58, 59, 59, 60, 
  61, 61, 62, 63, 63, 64, 65, 66, 67, 67, 68, 69, 70]

def C(n,k):
  if  k == 2: return (n*(n-1))>>1
  elif k == 3: return (n*(n-1)*(n-2))//6

def init_pascal(ans):
  pascal = [ [1 for _ in range(31) ] for _ in range(LIMIT_HI[4]+1) ]
  n,k = 2,1
  tmp = min(LIMIT_HI[k]+1,LIMIT_HI[4]+1)
  while k!=31:
    if n == tmp: k,n = k+1,k+2 ; tmp = min(LIMIT_HI[k]+1,LIMIT_HI[4]+1)
    else:
      pascal[n][k] = pascal[n-1][k] + pascal[n-1][k-1]
      if ans.get(pascal[n][k]) != None:
        ans[pascal[n][k]].add(((n,k)))
        ans[pascal[n][k]].add(((n,n-k)))
      n+=1

def solve(ans_dict):
  ans_dict.add((m,m-1)) ; ans_dict.add((m,1))
  n = int(1+math.sqrt(1+8*m)//2)
  if C(n,2) == m: ans_dict.add((n,n-2)) ; ans_dict.add((n,2))
  lo,hi = 6,n+1
  while lo+1<hi:
    mid = lo + ((hi-lo)>>1)
    if C(mid,3) <= m: lo = mid
    else: hi = mid
  if C(lo,3) == m:
    ans_dict.add((lo,lo-3)) ; ans_dict.add((lo,3))

def main():
  global m
  T = int(stdin.readline())
  #t = time.time()
  ans_dict,order = dict(),list()
  for _ in range(T):
    m = int(stdin.readline())
    order.append(m)
    ans_dict[m] = set()
  init_pascal(ans_dict)
  for m in order:
    solve(ans_dict[m])
    ans = list(ans_dict[m])
    ans.sort() 
    print(len(ans))
    print("("+str(ans[0][0])+","+str(ans[0][1])+")",end="")
    for i in range(1,len(ans)):
      print("","("+str(ans[i][0])+","+str(ans[i][1])+")",end="")
    print()
  #print(time.time() - t)
  return

main()