

class NeuronBase:
	""" This class is base for other types of neurons, perceptrons. It stores list with weights including bias."""
	_weights: list[float]
	def __init__(self, weights: list[float], biasWeight: float = 0.0):
		""" Construct perceptron object.
		weights - list of weights
		biasWeight (optional) - bias. to turn it off set it to 0
		"""
		self._weights = list([biasWeight] + weights)
		pass

	def multiplyInput(self, x: list[float]) -> float:
		"""Calculate sum of input and weights multiplication.
		Sum of x_i times w_i, x is input vector, w is weight vector."""
		if len(x) != len(self._weights) - 1:
			raise Exception(f"""Input array size does not match this perceptron's number of parameters!
				   You provided {len(x)} long array, while required input size is {len(self.__weights) - 1}""")
		#
		inSum: float = 1. * self._weights[0]
		for i in range(1, len(x)):
			inSum = inSum + (x[i - 1] * self._weights[i])
		return inSum