import nnstuff.perceptron
from nnstuff.network1 import *
from fileload import loadExamples
#import uistuff.uimanager

# Neural network use = neural network manager, mentioned in ui manager

# Uczenie z kieszonką - Podczas uczenia zapamiętujesz wagi i jak długo były wykorzystywane.
# Jeśli trenujesz kolejne wagi i okaże się, że ich czas życia jest krótszy to zastąp je tymi zapisanymi.



net1 = NeuralNetwork1()
examples = loadExamples()

# HERE SET PARAMETERS
# Overwrite 'learn_const'. Default is 0.2.
nnstuff.perceptron.learn_const = 0.1
neuron_count = 10
input_count = 35
learn_iterations = 200 # learning iterations per neuron
positive_ex_chance = 0.1 # chances for example with correct answer 'true'


NATURAL_CHANCE = 1 / neuron_count

# USAGE
def setNet1():
    net1.setupLayout(10, 35)

def trainNet1():
    print(u"Training network 🎓\n For now no learning reports. Check out TODO in netuse.py")
    net1.trainingSeason(examples, 200, 0.1) # natural chances would be 0.1
    testNet1()

def useNet1(input: list[int]) -> list[int]:
    print(u"Detecting 🔎...")
    out = net1.detectDigit(input) # or .digitChances() (this skipps comparsion to theta)
    print(out)
    return out

# TESTING
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
    exSorted = sortExamples()
    for d in range(10):
        print(f"#{d}:")
        for ex in exSorted[d]:
            print(net1.detectDigit(ex[1]))
            pass
        pass

def testNet1():
    print(u"Testing network 🧪...")
    exSorted = sortExamples()
    print('Score 0-10:')
    for d in range(10):
        testNet1For(d, exSorted)
        pass
    pass

def testNet1For(d: int, exSorted):
    score = 0
    count = 0
    for ex in exSorted[d]:
        out = net1.detectDigit(ex[1])
        if ex[0] in out:
            score += 1
        count += len(out)
        pass
    print(f"{d}:", (score * 1.0 / count * 10.0))
    pass


if __name__ == "__main__":
    print('This is terminal neural network test.\nRun mainwindow.py or neuron-start.py for GUI program.\n')
    setNet1()
    trainNet1()
    pass

#printExamples()