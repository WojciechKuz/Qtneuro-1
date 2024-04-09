from nnstuff.neuronbase import NeuronBase
import random

learn_const = 0.2 # writable

def isZero(x: float) -> bool:
	"""There's no such thing in floats as == """
	ZEROVALUE = 1.0e-9
	if x > ZEROVALUE or x < -ZEROVALUE:
		return False
	return True

def bool2float(b: bool) -> float:
	"""Takes bool, outputs 1 if true, outputs -1 if false."""
	if b:
		return 1.0
	return -1.0

class Perceptron(NeuronBase):
	"""Represents single neuron"""
	pocket: list[float] = []
	pocketLife: int = 0
	lifeTime: int = 0
	__theta: float
	def __init__(self, weights: list[float], theta: float, biasWeight: float = 0.0):
		""" Construct perceptron object.
		weights - list of weights
		theta - sum of weights times input must be greater or equal theta
		biasWeight (optional) - bias. to turn it off set it to 0
		"""
		# super init or sth
		super(Perceptron, self).__init__(weights, biasWeight)
		self.__theta = theta

		# pocket learning
		self.pocket = weights
		self.lifeTime = 0
		pass
	#

	def perceptron(self, x: list[float]) -> bool:
		"""Do what perceptron does. multiply input by weights, and return if it's greater or equal to theta"""
		return self.multiplyInput(x) >= self.__theta
	
	def multiply(self, x):
		return self.multiplyInput(x)

	def SPLAsh(self, exInput: list[float], exAnswer: float):
		"""Teach perceptron. parameters: teaching example input, and answer for example (1.0 or -1.0)"""
		o = self.perceptron(exInput) # was: multiplyInput, which was wrong.
		err = exAnswer - bool2float(o)
		if err == 0.0: # comparing floats like that is not good idea, but here we add/substract only 1.0, -1.0, 0.0. Use isZero() in case of more complex float
			return
		self.__weightUpdate(exInput, err)
		pass

	def PLA(self, exInput: list[float], exAnswer: float):
		"""Teach perceptron. parameters: teaching example input, and answer for example (1.0 or -1.0)."""
		o = self.perceptron(exInput)
		err = exAnswer - bool2float(o) # That's why soft typed langs suck. Without bool2float it implicitly converted types. 🐛
		if isZero(err):
			# error is zero
			self.lifeTime += 1
			if self.lifeTime > self.pocketLife: # if lives longer update pocket
				self.pocket = list(self._weights)
				self.pocketLife = self.lifeTime
				pass
			pass
		else:
			# error is non-zero
			self.__weightUpdate(exInput, err)
			self.lifeTime = 0
			pass
		pass

	def endPLA(self):
		self._weights = self.pocket
		pass

	def __weightUpdate(self, e: list[float], err: float):
		"""Update perceptron's weights using formula in SPLA alghoritm.\n
		parameters: e - exInput, err - error"""
		for i in range(len(e)):
			self._weights[i+1] += learn_const * err * e[i]
			pass
		self.__theta -= learn_const * err
		pass

if __name__ == "__main__":
    print('Run mainwindow.py or neuron-start.py to start program')

def randomPerceptron(inputSize: int, useBias: bool = False) -> Perceptron:
	random.seed()
	randBiasWeight = 0.0
	if useBias:
		randBiasWeight: float = random.random()/2.0 # random number in 0-0.5 range
	randWeights: list[float] = [random.random()/2.0 for i in range(inputSize)]
	randTheta: float = random.random() / 2.0
	return Perceptron(randWeights, randTheta, randBiasWeight)