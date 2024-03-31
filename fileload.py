

# fileload, loadExamples and map-reduce functions



# reads file into list of lines
def __loadText(filename: str) -> list[str]:
    file = open(filename, mode="r")
    return [line for line in file]

# takes list of lists and merges them into one list
def flatten(listoflist: list[list|tuple]) -> list:
    megalist = list()
    for sublist in listoflist:
        megalist += list(sublist)
    return megalist

# does 'map' in 'map reduce'
def collectionMap(mylist: list, fun) -> list:
    collMap = list() # list of tuples
    for elem in mylist:
        collMap.append(fun(elem))
    return collMap

def loadExamples(filename: str = 'training.txt') -> list[tuple[int, list[int]]]:
    # load it to tuple (answer, exInput)
    lines = __loadText(filename)
    digit = -1
    examples = []
    for ln in lines:
        if '#' in ln:
            digit = int(ln.rstrip()[-1])
            row = 0
        else:
            examples.append((
                digit,
                collectionMap(ln.rstrip().split(), lambda s: int(s.strip()))
            )) # each example is tuple of (digit and list of (7 ints))
            pass
        pass
    return examples

if __name__ == '__main__':
    print('Run mainwindow.py or neuron-start.py to start program')
    flattenedMap = flatten(collectionMap(__loadText('training.txt'), str.split)) # list of list of words
    pass