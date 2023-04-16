from interface import QuantumDevice
from simulator import SingleQubitSimulator

def qrng(device : QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h() # apply Hadamard to rotate initial state 90 degree
        return q.measure()

if __name__ == "__main__":

    qsim = SingleQubitSimulator()
    random_sample = qrng(qsim)
    print(f"Our QRNG returned {random_sample}.")
