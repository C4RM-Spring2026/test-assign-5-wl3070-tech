import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy

    N = int(m * ppy)

    t = np.arange(1, N + 1, dtype=float)

    c = face * couponRate / ppy
    cf = np.full(N, c, dtype=float)
    cf[-1] = cf[-1] + face  # add principal at maturity

    disc = (1 + r) ** t
    pvcf = cf / disc

    price = pvcf.sum()

    duration_periods = (t * pvcf).sum() / price
    duration_years = duration_periods / ppy

    return duration_years
