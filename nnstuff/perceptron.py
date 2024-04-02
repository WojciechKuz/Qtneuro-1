from nnstuff.neuronbase import NeuronBase
import random

LEARN_CONST = 0.2

class Perceptron(NeuronBase):
	"""Represents single neuron"""
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
		pass
	#

	def perceptron(self, x: list[float]) -> bool:
		"""Do what perceptron does. multiply input by weights, and return if it's greater or equal to theta"""
		return self.multiplyInput(x) >= self.__theta
	
	def probability(self, x):
		return self.multiplyInput(x)

	def SPLAsh(self, exInput: list[float], exAnswer: float):
		"""Teach perceptron. parameters: teaching example input, and answer for example"""
		o = self.multiplyInput(exInput)
		err = exAnswer - o
		if err == 0:
			return
		self.__weightUpdate(exInput, err)
		pass

	def __weightUpdate(self, e: list[float], err: float):
		"""Update perceptron's weights using formula in SPLA alghoritm.\n
		parameters: e - exInput, err - error"""
		for i in range(len(e)):
			self._weights[i+1] += LEARN_CONST * err * e[i]
			pass
		self.__theta -= LEARN_CONST * err
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