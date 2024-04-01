import random

# example picker class

# Layout of examples: list[tuple[int, list[int]]]
# list of tuples:  (answer, example(list of 7 ints))

def returnWhenDigMatch(exTup: tuple, dig: int) -> (tuple | None):
    if exTup[0] == dig:
        return exTup
    return

class ExPicker:
	__allExamples = []
	def __init__(self, examples) -> None:
		self.__allExamples = examples
		pass
	def pickDigit(self, digit: int):
		random.seed()
		# hope those list store only references
		self.correct = []
		self.incorrect = []
		for ex in self.__allExamples:
			if ex[0] != digit:
				self.incorrect.append(ex)
			else:
				self.correct.append(ex)
		pass

	def pickExample(self, chances: float) -> tuple[int, list[int]]:
		incIter = len(self.incorrect)
		cIter = len(self.correct)
		ifCorrect: bool = random.random() >= 1. - chances
		if ifCorrect:
			# TODO pick example from self.correct
			pass
		else:
			# TODO pick example from self.incorrect
			pass
		pass
	pass


if __name__ == '__main__':
	print('Run mainwindow.py or neuron-start.py to start program')
	# TEST
	ep = ExPicker([(1, 'elo1'), (2, 'elo2'), (2, 'elo2, 2'), (3, 'elo3')])
	ep.pickExample(2, 'xd')
	pass