import matplotlib as mpl
import cv2
# import matplotlib.pyplot as plt
#
# plt.plot([1,2,3,4])
# plt.show()
print(mpl.get_configdir())
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
line, = ax.plot([1, 2, 3, 4])
s, (width, height) = canvas.print_to_buffer()
canvas.print_figure('tth001.jpg')
# from PIL import Image
# im = Image.frombytes("RGBA", (width, height), s)
# cv2.imshow('image',im)
# im.show()
