from nnstuff.perceptron import *
from nnstuff.network1 import *
from fileload import loadExamples, flatten

# Neural network use = neural network manager, mentioned in ui manager

# Uczenie z kieszonką - Podczas uczenia zapamiętujesz wagi i jak długo były wykorzystywane.
# Jeśli trenujesz kolejne wagi i okaże się, że ich czas życia jest krótszy to zastąp je tymi zapisanymi.

# functions to convert representations of 'digit grid'. (7ints to 35 floats)
def list7toList35(seven: list[int]) -> list[float]:
    """Convert list of 7 integers (where each contain 5 values stored as bits) to list of 35 floats containing 1. or 0."""
    return flatten([__numToByteList(n) for n in seven])
def __numToByteList(n: int) -> list[float]:
    """In n there's saved 5 numbers (0s or 1s) as bits. Get list of them as floats."""
    row = []
    access = 1
    for i in range(5):
        row.append(float((n & access)**0)) # n & access gives 0 or other_int. then exponent to 0 is 1 or 0. And finally to float
        access = access << 1
    return row

# helper functions
def mapTo1m1(x):
    """Convert numbers from range 0, 1 to -1, 1."""
    return 2. * x - 1.
def ifDigMatch(a, b) -> float:
    if a == b:
        return 1.
    else:
        return -1.


# TODO netuse.py

net1 = NeuralNetwork1()

def setNet1():
    net1.setupLayout(10, 35)


if __name__ == "__main__":
    print('Run mainwindow.py or neuron-start.py to start program')