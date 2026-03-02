import numpy as np

def FizzBuzz(start, finish):

    numvec = np.arange(start, finish)

    objvec = np.array(numvec, dtype=object)

    fizz = (numvec % 3 == 0)
    buzz = (numvec % 5 == 0)

    objvec[fizz & buzz] = "fizzbuzz"
    objvec[fizz & ~buzz] = "fizz"
    objvec[buzz & ~fizz] = "buzz"

    return list(objvec)
