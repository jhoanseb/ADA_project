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

def C(n,k):
  ans = n
  k = min(k,n-k)
  n_i,k_i = n,k
  if k!=0:
    for i in range(1,k):
      n_i *= (n-i)
      k_i *= (k-i)
      ans = n_i//k_i
  return ans

def solve(m):
  ans = list()
  for k in range(1,m):
    lo,hi = 1,10**15
    find = False
    while lo+1!=hi and not find:
      mid = lo + ((hi-lo)>>1)
      C_mid = C(mid,k)
      if C_mid <= m:
        lo = mid
        if C_mid == m: find = True
      else: hi = mid
    if find: ans.append((lo,k))
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