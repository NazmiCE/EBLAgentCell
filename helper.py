import matplotlib.pyplot as plt

def func_to_vectorize(x,y,dx,dy,scaling = 0.5):
    plt.arrow(x,y,dx*scaling, dy*scaling, fc = "k", ec="k", head_width = 0.006, head_length = 0.01)
