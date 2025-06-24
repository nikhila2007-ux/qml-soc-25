from qiskit import QuantumCircuit,Aer,execute
import numpy as np
def cU(qc,t,c,tgt):qc.crz(t,c,tgt)
def phase_est(t,n=3):
 qc=QuantumCircuit(n+1,n)
 qc.h(range(n))
 qc.x(n)
 for j in range(n):
  for _ in range(2**j):cU(qc,t,j,n)
 for q in range(n//2):qc.swap(q,n-q-1)
 for j in range(n):
  qc.h(j)
  for k in range(j+1,n):qc.cp(-np.pi/(2**(k-j)),k,j)
 qc.measure(range(n),range(n))
 return qc
theta=np.pi/4
qc=phase_est(theta)
sim=Aer.get_backend('qasm_simulator')
res=execute(qc,sim,shots=1024).result()
print(res.get_counts())
