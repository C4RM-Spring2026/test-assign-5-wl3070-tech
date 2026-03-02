import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    # per-period rate and number of periods
    r = y / ppy
    N = int(m * ppy)

    C = face * couponRate / ppy

    t = np.arange(1, N + 1)

    df = 1.0 / (1.0 + r) ** t

    price = np.sum(C * df) + face * df[-1]

    return price
