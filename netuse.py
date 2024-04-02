from nnstuff.perceptron import *
from nnstuff.network1 import *
from fileload import loadExamples
#import uistuff.uimanager

# Neural network use = neural network manager, mentioned in ui manager

# Uczenie z kieszonką - Podczas uczenia zapamiętujesz wagi i jak długo były wykorzystywane.
# Jeśli trenujesz kolejne wagi i okaże się, że ich czas życia jest krótszy to zastąp je tymi zapisanymi.

if __name__ == "__main__":
    print('Run mainwindow.py or neuron-start.py to start program')
    exit(1)

net1 = NeuralNetwork1()
examples = loadExamples()



def setNet1():
    net1.setupLayout(10, 35)

def trainNet1():
    print(u"Training network 🎓\n For now no learning reports. Check out TODO in netuse.py")
    net1.trainingSeason(examples, 200, 0.2) # natural chances would be 0.1
    testNet1print()

def useNet1(input: list[int]) -> list[int]:
    print(u"Detecting 🔎...")
    out = net1.detectDigit(input) # or .digitChances() (this skipps comparsion to theta)
    print(out)
    return out

 # TODO funkcja testująca. sprawdza, czy poprawnie rozpozna każdy przykład. I raporty z uczenia by się przydały.
def sortExamples() -> list:
    """digits are indexes"""
    exSorted = [[] for i in range(10)]
    for ex in examples:
        d = ex[0]
        exSorted[d].append(ex)
    return exSorted

def printExamples():
    exSorted = sortExamples()
    for d in range(10):
        print(f"#{d}:")
        for ex in exSorted[d]:
            print(ex)
            pass
        print('\n')
        pass
    pass

def testNet1print():
    print(u"Testing network 🧪...")
    #results = []
    exSorted = sortExamples()
    for d in range(10):
        print(f"#{d}:")
        for ex in exSorted[d]:
            print(net1.detectDigit(ex[1]))
            pass
        pass

def testNet1():
    print(u"Testing network 🧪...")
    #results = []
    exSorted = sortExamples()
    testNet1For(0, exSorted)
    testNet1For(1, exSorted)
    testNet1For(3, exSorted)
    pass

def testNet1For(d: int, exSorted):
    print(f"#{d}:")
    for ex in exSorted[d]:
        print(net1.detectDigit(ex[1]))
        pass

#printExamples()