import numpy as np
import matplotlib.pyplot as plt
import k_medoids

dt = np.random.randint(0,100, (100,2))
kmedoid = k_medoids.KMedoidsClass(dt,5,5)
kmedoid.fit()