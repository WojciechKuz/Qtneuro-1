import nnstuff.perceptron
from nnstuff.network1 import NeuralNetwork1
import nnstuff.network1
from fileload import loadExamples
#import uistuff.uimanager

# Neural network use = neural network manager, mentioned in ui manager

# Uczenie z kieszonką - Podczas uczenia zapamiętujesz wagi i jak długo były wykorzystywane.
# Jeśli trenujesz kolejne wagi i okaże się, że ich czas życia jest krótszy to zastąp je tymi zapisanymi.



net1 = NeuralNetwork1()
examples = loadExamples()

# HERE SET PARAMETERS
nnstuff.perceptron.learn_const = 0.01    # Overwrite 'learn_const'. Default is 0.2.
nnstuff.network1.lc_max = 0.2
nnstuff.network1.lc_min = 0.05
neuron_count = 10
input_count = 35
learn_iterations = 8000          # learning iterations per neuron
positive_ex_chance = 0.1        # chances for example with correct answer 'true'


unique_elem_count = neuron_count
NATURAL_CHANCE = 1 / neuron_count
PRINT_ARR = False

# USAGE
def setNet1():
    net1.setupLayout(neuron_count, input_count)

def trainNet1():
    print(u"Training network 🎓\n For now no learning reports. Check out TODO in netuse.py")
    net1.trainingSeason(examples, learn_iterations, positive_ex_chance)
    testNet1()

def useNet1(input: list[int]) -> list[int]:
    print(u"Detecting 🔎...")
    out = net1.detectDigit(input) # or .digitChances() (this skipps comparsion to theta)
    print(out)
    return out

# TESTING
def sortExamples() -> list:
    """Digits are indexes. Each list element is list containing example tuples."""
    exSorted = [[] for i in range(neuron_count)]
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
    for d in range(unique_elem_count):
        testNet1For(d, exSorted)
        pass
    pass

def testNet1For(d: int, exSorted):
    score = 0
    count = 0 # out length sum
    outs = 0 # out count
    result = []
    for ex in exSorted[d]:
        out = net1.detectDigit(ex[1])
        result.append(out)
        if ex[0] in out:
            score += 1
        count += len(out)
        outs += 1
        pass
    if count == 0:
        score = 0
        count = 1
    print(f"#{d} score:", (score * 1.0 / count * 10.0), 'avgOutLen:', (count / outs))
    if PRINT_ARR:
        print('arr:', result)
    pass


if __name__ == "__main__":
    print('This is terminal neural network test.\nRun mainwindow.py or neuron-start.py for GUI program.\n')
    setNet1()
    trainNet1()
    pass

#printExamples()