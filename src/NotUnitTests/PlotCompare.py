import matplotlib
import matplotlib.pyplot as plt
import numpy as np

width = 0.35  # the width of the bars

java_times = [20, 35, 30, 35, 27, 8]
python_times = [25, 32, 34, 20, 25, 9]
networkX_times = [22, 33, 29, 19, 26, 10]
xlabels = ['G_10_80', 'G_100_800', 'G_1k_80k', 'G_10k_80k',
           'G_20k_160k', 'G_30k_240k']


def plot_data(java_stats, python_stats, networkx_stats, labels):
    ind = np.arange(len(java_stats))  # the x locations for the groups
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, java_stats, width,
                    label='java')
    rects2 = ax.bar(ind, python_stats, width,
                    label='python')
    rects3 = ax.bar(ind + width / 2, networkx_stats, width * 0.8,
                    label='networkx')
    autolabel(rects1, ax, "left")
    autolabel(rects2, ax, "center")
    autolabel(rects3, ax, "right")

    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    ax.legend()

    return fig, ax


def autolabel(rects, ax, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos] * 3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


if __name__ == '__main__':
    figp, axp = plot_data(java_times, python_times, networkX_times, xlabels)
    axp.set_ylabel('time to calculate')
    axp.set_title('shortest path')

    figp.tight_layout()

    plt.show()
