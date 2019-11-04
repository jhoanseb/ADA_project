from sys import stdin

"""
Nombre: Jhoan Sebastian Lozano
Código: 8931869
Código de honor del curso:
Como miembro de la comunidad académica de la 
Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""

def solve(M):
  pascal = [ [1 for _ in range(M+1) ] for _ in range(M+1) ]
  n,m = 1,1
  ans = list()
  while n!=M+1:
    if m == M+1: n,m = n+1,1
    else:
      pascal[n][m] = pascal[n-1][m] + pascal[n][m-1]
      if pascal[n][m] == M: ans.append((m+n,n))
      m+=1
  return ans

def main():
  T = int(stdin.readline())
  for _ in range(T):
    m = int(stdin.readline())
    ans = solve(m)
    # for p in pascal: print(p)
    ans.sort()
    print(len(ans))
    for a in ans: print("("+str(a[0])+","+str(a[1])+")",end=" ")
    print()

  return

main()