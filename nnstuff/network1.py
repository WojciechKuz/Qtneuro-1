# TODO network.py
from perceptron import *

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

	def trainingSeason():
		"""Train network. Provide array of examples."""
		# teach & update with .SPLAsh(), check with .perceptron()
		pass

if __name__ == '__main__':
	print('Run mainwindow.py or neuron-start.py to start program')
	pass
