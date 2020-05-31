import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# fig = plt.figure()
# axes = plt.subplot(111, projection='3d')
# x = np.arange(1,11)
# y = np.arange(1,11)
# z = np.arange(1,11) #2 dim
# # axes.plot_wireframe(x,y,np.array([z]),color='r',linestyle='--')
# axes.scatter(x,y,np.array([z]),color='r',marker='*',s=180)
# axes.set_xlabel('nilai X')
# axes.set_ylabel('nilai Y')
# axes.set_zlabel('nilai Z')

import plotly
import plotly.graph_objects as go

# create plot
plot = go.Scatter(
    x = np.arange(10),
    y = np.arange(10)
)
# create figure
fig = go.Figure(
    data = plot
)
fig.show()