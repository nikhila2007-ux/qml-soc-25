from qiskit import QuantumCircuit,Aer,execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
qc=QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()
sim=Aer.get_backend('qasm_simulator')
job=execute(qc,sim,shots=1024)
res=job.result()
counts=res.get_counts()
plot_histogram(counts)
plt.show()
print(counts)

