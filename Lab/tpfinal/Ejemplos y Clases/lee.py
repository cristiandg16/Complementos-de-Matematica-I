
def leer_grafo_archivo(file_path):
  
  with open(file_path, "r") as f:
    V=[]
    E=[]
    n=int(f.readline())
    for i in range(n):
      s=f.readline()
      s=s[:-1]
      V.append(s)
    for line in f:
      line=line.split()
      
      if line[0] in V and line[1] in V:
        q=(line[0],line[1])
        w=(line[1],line[0])
        if q in E or w in E:
          print("Error! Arista repetida")
        elif q!=w:
          E.append(q)
      else:
        print("Error al leer aristas")
    
    g=(V,E)
    return g
