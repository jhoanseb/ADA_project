from sys import stdin

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
  cnt = 0
  for k in range(2,m-1):
    lo = 1
    hi = limit_hi[k] if k<55 else 10**15
    #print(lo,hi)
    find = False
    while lo+1!=hi and not find:
      cnt+=1
      mid = lo + ((hi-lo)>>1)
      C_mid = C(mid,k)
      #print("lo",lo,"hi",hi,"mid:",mid,"k:",k,C_mid)
      if C_mid <= m:
        lo = mid
        if C_mid == m: find = True
      else: hi = mid
    #print("---------->",find)
    if find: ans.append((lo,k))
    #if C(lo,k) == m: ans.append((lo,k))
  print(cnt)
  ans.append((m,1)) ; ans.append((m,m-1))
  return ans

def main():
  T = int(stdin.readline())
  for _ in range(T):
    m = int(stdin.readline())
    ans = solve(m)
    ans.sort()
    print(len(ans))
    for a in ans: print("("+str(a[0])+","+str(a[1])+")",end=" ")
    print()
  return

main()