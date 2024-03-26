from neuronbase import NeuronBase

class Perceptron(NeuronBase):
	__theta: float
	def __init__(self, weights: list[float], theta: float, biasWeight: float = 0.0):
		""" Construct perceptron object.
		weights - list of weights
		theta - sum of weights times input must be greater or equal theta
		biasWeight (optional) - bias. to turn it off set it to 0
		"""
		# super init or sth
		NeuronBase(self, weights, biasWeight)
		self.__theta = theta
		pass
	#

	def perceptron(self, x: list[float]) -> bool:
		"""Do what perceptron does. multiply input by weights, and return if it's greater or equal to theta"""
		return self.multiplyInput(x) >= self.__theta

if __name__ == "__main__":
    print('Run mainwindow.py or neuron-start.py to start program')