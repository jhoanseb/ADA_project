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

limit_hi = [0, 10**15, 44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 
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

def solve(m):
  ans = list()
  if 1 != m-1: ans.append((m,m-1))
  ans.append((m,1))
  k,ok = 2,True
  lo,hi = k*2,limit_hi[k]
  while k<(m>>1) and ok:
    ok = C(hi,k) >= m
    while lo+1!=hi and ok:
      mid = lo + ((hi-lo)>>1)
      if C(mid,k) <= m: lo = mid
      else: hi = mid
    if C(lo,k) == m:
      if k != lo-k: ans.append((lo,lo-k))
      ans.append((lo,k))
    k+=1
    lo,hi = k*2,min(limit_hi[k],lo+1)
    ok = lo<hi
  #print("k:",k-1)
  return ans

def main():
  T = int(stdin.readline())
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