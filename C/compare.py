import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d as Axes3D
import matplotlib.animation as animation
import PIL
import json, time

data = json.loads(open("solar_0_1.json").read())
data = [list(map(lambda x: list(x["pos"].values()), j.values())) for j in data.values()]
pos = np.array(data)
pos = np.swapaxes(pos, 0, 1)
pos = np.swapaxes(pos, 1, 2)
print(pos.shape)
