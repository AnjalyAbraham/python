x=[[61,62,63],[71,72,73],[81,82,83]]
y=[[91,92,93],[94,95,96],[95,96,97]]
result=[[43,44,45],[46,47,48],[51,52,53]]
   for i in range (len(x)):
      for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
   for r in result:
       print(r)