from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
simulator = Aer.get_backend("qasm_simulator")
job = execute(qc, simulator, shots=1000)
result = job.result()
print(result.get_counts(qc))
