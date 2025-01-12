#first panda
import pandas as pd
import numpy as np
a=np.array([11,99,303,44,55,6])
b=np.array([1,2,3,4,5,6])
c=a+b
d=np.array(["Abi","Bala","Coulins","Dinesh","Elger","Ganesh"])
frame={"Name":d, "A":a, "B":b, "C":c}
g=pd.DataFrame(frame)
print(g)