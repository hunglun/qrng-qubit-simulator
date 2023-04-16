import numpy as np 
from interface import Qubit, QuantumDevice

KET_0 = np.array([
[1],[0]
], dtype=complex)

H = np.array([
[1,1],[1,-1]
], dtype=complex) / np.sqrt(2)

class SingleQubitSimulator(Qubit, QuantumDevice):
    # Qubit Interface
    def __init__(self):
        self.reset()
    def reset(self):
        self.state = KET_0.copy()
    def h(self):
        self.state = H @ self.state
    def measure(self) -> bool:
        pr0 = np.abs(self.state[0,0] ** 2)
        sample = np.random.random() <= pr0
        return sample

    # Quantum Device Interface
    def allocate_qubit(self)-> Qubit:
        self.reset()
        return self

    def deallocate_qubit(self, qubit : Qubit):
        qubit.reset()