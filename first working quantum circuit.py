from qiskit import Aer, QuantumCircuit, execute

# basic 1-qubit test
c = QuantumCircuit(1, 1)
c.h(0)
c.measure(0, 0)

# sim
sim = Aer.get_backend("qasm_simulator")
res = execute(c, sim, shots=1000).result()
counts = res.get_counts()

print("outcomes ->", counts)

