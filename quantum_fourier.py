import numpy as np
from qiskit import QuantumCircuit, Aer, execute
def notsurewhatthisdoes(qc, num):
 for i in range(num):
  qc.h(i)
  for j in range(i+1,num):
   val = np.pi / (2 ** (j - i))
   qc.cp(val,j,i)
  # hmm maybe needed?
def flip_them(qc, total):
 for a in range(0,int(total/2)):
  qc.swap(a,total-a-1)
def finalCircuit():
 c=QuantumCircuit(3,3)
 temp = [0,2]
 for x in temp:
  c.x(x)
 notsurewhatthisdoes(c,3)
 flip_them(c,3)
 for m in [0,1,2]:
  c.measure(m,m)
 return c
qc = finalCircuit()
b = Aer.get_backend("qasm_simulator")
r = execute(qc,b,shots=432).result().get_counts()
print(r)

