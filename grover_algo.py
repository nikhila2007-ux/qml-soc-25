from qiskit import QuantumCircuit,Aer,execute
def grover_circuit():
 qc=QuantumCircuit(2,2)
 qc.h([0,1])
 qc.cz(0,1)
 qc.h([0,1])
 qc.x([0,1])
 qc.cz(0,1)
 qc.x([0,1])
 qc.h([0,1])
 qc.measure([0,1],[0,1])
 return qc
qc=grover_circuit()
sim=Aer.get_backend('qasm_simulator')
res=execute(qc,sim,shots=1024).result()
print(res.get_counts())
