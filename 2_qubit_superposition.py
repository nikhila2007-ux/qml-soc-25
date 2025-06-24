from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(2,2)
qc.h(0)
qc.h(1)
qc.measure([0,1], [0,1])
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()
print(counts)
