from sys import stdin
import time

"""
Nombre: Jhoan Sebastian Lozano
Código: 8931869
Código de honor del curso:
Como miembro de la comunidad académica de la 
Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""

"""
C(n,k) = ((n)(n-1)...(n-k+1)/((k)(k-1)...(1))
"""

LIMIT_HI = [0, 10**15, 44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 
  100, 87, 78, 72, 67, 63, 61, 59, 57, 56, 55, 54, 54, 54, 54, 54, 54, 
  54, 54, 54, 55, 55, 56, 56, 57, 57, 58, 59, 59, 60, 
  61, 61, 62, 63, 63, 64, 65, 66, 67, 67, 68, 69, 70]

def C(n,k):
  ans = 1
  k = min(k,n-k)
  if k!=0:
    if k==1: ans = n
    else:
      n_i,k_i = n,k
      for i in range(1,k):
        n_i *= (n-i)
        k_i *= (k-i)
        ans = n_i//k_i
  return ans

def init_pascal():
  pascal = [ [1 for _ in range(31) ] for _ in range(LIMIT_HI[4]+1) ]
  n,k = 1,1
  while k!=31:
    if n == LIMIT_HI[4]+1: k,n = k+1,1
    else:
      pascal[n][k] = pascal[n-1][k] + pascal[n][k-1]
      # if pascal[n][m] == M: ans.append((m+n,n))
      k+=1
  return pascal

def solve(m):
  ans = list()
  limits = [0,10**15]
  k,ok = 2,True
  lo,hi = k*2,LIMIT_HI[k]
  if 1 != m-1: ans.append((m,m-1))
  ans.append((m,1))
  while k<(m>>1) and ok:
    ok = C(hi,k) >= m
    while lo+1!=hi and ok:
      mid = lo + ((hi-lo)>>1)
      if C(mid,k) <= m: limits[0] = lo = mid
      else: limits[1] = hi = mid
    if C(lo,k) == m:
      if k != lo-k: ans.append((lo,lo-k))
      ans.append((lo,k))
    k+=1
    lo,hi = k*2,min(LIMIT_HI[k],limits[1],lo+1)
    ok = lo<hi
  return ans

def main():
  T = int(stdin.readline())
  pascal = init_pascal()
  #t = time.time()
  for _ in range(T):
    m = int(stdin.readline())
    ans = solve(m)
    print(len(ans))
    print("("+str(ans[-1][0])+","+str(ans[-1][1])+")",end="")
    for i in range(len(ans)-2,-1,-1):
      print("","("+str(ans[i][0])+","+str(ans[i][1])+")",end="")
    print()
  #print(time.time() - t)
  return

main()