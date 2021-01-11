import matplotlib
import matplotlib.pyplot as plt
import numpy as np

java_means = (20, 35, 30, 35, 27)
python_means = (25, 32, 34, 20, 25)
networkX_means = (22, 33, 29, 19, 26)

ind = np.arange(len(java_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, java_means, width,
                label='java')
rects2 = ax.bar(ind, python_means, width,
                label='python')
rects3 = ax.bar(ind + width / 2, networkX_means, width * 0.8,
                label='networkx')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()


def autolabel(rects, xpos='center'):
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
    autolabel(rects1, "left")
    autolabel(rects2, "center")
    autolabel(rects3, "right")

    fig.tight_layout()

    plt.show()
