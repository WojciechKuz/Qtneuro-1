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
    net1.trainingSeason(examples, 80, 0.2) # natural chances would be 0.1

def useNet1(input: list[int]) -> list[int]:
    print(u"Detecting 🔎...")
    return net1.detectDigit(input) # or .digitChances() (this skipps comparsion to theta)

 # TODO funkcja testująca. sprawdza, czy poprawnie rozpozna każdy przykład. I raporty z uczenia by się przydały.