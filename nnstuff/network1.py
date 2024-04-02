from nnstuff.perceptron import Perceptron, randomPerceptron
import nnstuff.perceptron
from nnstuff.expicker import ExPicker
from fileload import loadExamples, flatten, collectionMap

VARIABLE_LEARN_CONST = False
lc_max = 0.2
lc_min = 0.01

def linearLearnConst(i: int, i_max: int, printing: bool = False):
	if not VARIABLE_LEARN_CONST:
		return
	if i % (i_max // 20) == 0 and printing:
		print(nnstuff.learn_const)
	dist = lc_max - lc_min
	perStep = dist / i_max
	lc = lc_max - perStep * i
	if lc < lc_min:
		print('Warning! learn_const > lc_max:', lc)
	if lc > lc_max:
		print('Warning! learn_const < lc_min:', lc)
	if lc < 0:
		print('Warning! learn_const < 0:', lc)
	nnstuff.learn_const = lc
	return lc

# functions to convert representations of 'digit grid'. (7ints to 35 floats)
def list7toList35(seven: list[int]) -> list[float]:
    """Convert list of 7 integers (where each contain 5 values stored as bits) to list of 35 floats containing 1. or 0."""
    return flatten([__numToByteList(n) for n in seven])

def __numToByteList(n: int) -> list[float]:
    """In n there's saved 5 numbers (0s or 1s) as bits. Get list of them as floats."""
    row = []
    access: int = 1
    for i in range(5):
        if (n & access) > 0: # n & access gives 0 or other integer. then integer to 1.0, 0 to 0.0
            row.append(1.0) 
        else:
            row.append(0.0)
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

def convert(seven: list[int]) -> list[float]: # FIXME should I convert [0, 1] to [-1, 1] here??? Or convert only output???
	return list7toList35(seven)

class NeuralNetwork1:
	__net: list[Perceptron] = []
	"""Class representing set of perceptrons for assignment 1.
	set of 10 perceptrons, each with 35 inputs.
	This class only allows for parallel neurons, it's not possible
	to feed one with other's output."""

	def load(self):
		"""Load perceptrons (weights and thetas) if it's already prepared."""
		# load list[tuple[weights: list[float], theta: float]]
		pass

	def setupLayout(self, nofPerceptr: int, inputSize: int):
		"""Sets up and initializes perceptrons layout according to provided size.
		It does not set correct weights, uses randomized weights."""
		self.__net = [randomPerceptron(inputSize) for i in range(nofPerceptr)]
		pass

	def trainingSeason(self, examples, iterations, chances):
		"""Train network. Provide array of examples.
		Teaches each perceptron 'iterations' number of times.
		For teaching chooses random example. Parameter 'chances' should be in range 0 to 1,
		this are chances for positive example (where perceptron should output true)."""
		# teach & update with .SPLAsh(), check with .perceptron()
		exPick = ExPicker(examples)
		for d in range(len(self.__net)): # 10 digits
			exPick.pickDigit(d)
			for i in range(iterations): # iterations
				linearLearnConst(i, iterations, d == 1)
				ex = exPick.pickExample(chances)
				self.__net[d].SPLAsh(convert(ex[1]), ifDigMatch(ex[0], d))
				pass
			pass
		pass

	def detectDigit(self, input: list[int]) -> list[int]:
		"""Detects digit, returns list of possible digits. Parameter 'input' is list of 7 ints (encoded grid)."""
		possible_digits = []
		for d in range(len(self.__net)):
			if self.__net[d].perceptron(convert(input)):
				possible_digits.append(d)
		return possible_digits

	def digitChances(self, input: list[int]):
		"""returns list of posibilities for each of 10 digits."""
		probabil = []
		for perceptr in self.__net:
			probabil.append(perceptr.probability(convert(input)))
		return probabil

if __name__ == '__main__':
	print('Run mainwindow.py or neuron-start.py to start program')
	pass

# def NET1TEST():
# 	# TEST
# 	decoded = convert([31, 17, 17, 17, 17, 17, 31])
# 	print('length of decoded:', len(decoded))
# 	print(decoded)

# def NET1TEST_BYTES():
# 	for x in range(31+1):
# 		print(f"{x}:", __numToByteList(x))