import random

# example picker class

# Layout of examples: list[tuple[int, list[int]]]
# list of tuples:  (answer, example(list of 7 ints))

random.seed()

def returnWhenDigMatch(exTup: tuple, dig: int) -> (tuple | None):
    if exTup[0] == dig:
        return exTup
    return

class ExPicker:
	__allExamples = []
	def __init__(self, examples) -> None:
		self.__allExamples = examples
		# seed
		pass
	def pickDigit(self, digit: int):
		# hope those list store only references
		self.correct = []
		self.incorrect = []
		for ex in self.__allExamples:
			if ex[0] != digit:
				self.incorrect.append(ex)
			else:
				self.correct.append(ex)
		return self

	def pickExample(self, chances: float) -> tuple[int, list[int]]:
		incLen = len(self.incorrect)
		cLen = len(self.correct)
		ifCorrect: bool = random.random() >= 1. - chances
		if ifCorrect:
			#print('good ', end='')
			return self.correct[random.randint(0, cLen-1)]
		else:
			#print('bad  ', end='')
			return self.incorrect[random.randint(0, incLen-1)]
	pass

def flip(elem: float, chances):
	if random.random() >= chances:
		return (elem + 1) % 2
	return elem # random < chances

def randomFlip(array: list[float], chances: float):
	"""Flip random elements in the list of floats. 0->1, 1->0"""
	for i in range(len(array)):
		array[i] = flip(array[i], chances)
	return array


if __name__ == '__main__':
	print('Run mainwindow.py or neuron-start.py to start program')
	# TEST
	ep = ExPicker([(1, 'elo1'), (2, 'elo2'), (2, 'elo2, 2'), (3, 'elo3')])
	ep.pickDigit(2)
	for i in range(10):
		print(ep.pickExample(0.5))
		pass
	pass