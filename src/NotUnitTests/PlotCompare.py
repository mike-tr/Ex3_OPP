import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_data(java_stats, python_stats, networkx_stats, labels):
    width = 0.35  # the width of the bars

    ind = np.arange(len(java_stats))  # the x locations for the groups
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, java_stats, width,
                    label='java')
    rects2 = ax.bar(ind, python_stats, width,
                    label='python')
    if networkx_stats is not None:
        rects3 = ax.bar(ind + width / 2, networkx_stats, width * 0.8,
                        label='networkx')
        autolabel(rects3, ax, "right")

    autolabel(rects1, ax, "left")
    autolabel(rects2, ax, "center")

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


def plot_jsons():
    java_times = [20, 35, 30, 35, 27, 8]
    python_times = [25, 32, 34, 20, 25, 9]
    network_times = [22, 33, 29, 19, 26, 10]
    x_labels = ['G_10_80', 'G_100_800', 'G_1k_80k', 'G_10k_80k',
                'G_20k_160k', 'G_30k_240k']

    figp, axp = plot_data(java_times, python_times, network_times, x_labels)
    axp.set_ylabel('time to calculate')
    axp.set_title('shortest path')

    figp.tight_layout()

    plt.show()


def plot_scc():
    java_times = [0.437, 0.760, 2.905, 1.24, 4.98, 0]
    python_times = [4.09, 2.33, 9.74, 5.32, 18.56, 27.76]
    network_times = [0.50, 1.51, 6.00, 3.50, 5.359, 18.16]
    x_labels = ['G_100k_100k', 'G_100k_1m', 'G_100k_5m', 'G_1m_0',
                'G_1m_1m', 'G_1m_10m']

    figp, axp = plot_data(java_times, python_times, network_times, x_labels)
    axp.set_ylabel('time to calculate')
    axp.set_title('shortest path')

    figp.tight_layout()

    plt.show()


def plot_scc_single():
    java_times = [0.06, 0.645, 1.577, 0.055, 0.046]
    python_times = [0.12, 2.32, 9.64, 1.22, 1.22]
    network_times = None
    x_labels = ['G_100k_100k', 'G_100k_1m', 'G_100k_5m', 'G_1m_0', 'G_1m_1m']

    figp, axp = plot_data(java_times, python_times, network_times, x_labels)
    axp.set_ylabel('time to calculate')
    axp.set_title('shortest path')

    figp.tight_layout()

    plt.show()


def plot_paths():
    java_times = [0.017, 0.168, 0.586, 0.049, 0.037, 0]
    python_times = [0.00, 1.88, 4.99, 0.00, 0.00, 47.71]
    network_times = [0.00, 0.44, 2.31, 0.00, 0.00, 12.92]
    x_labels = ['G_100k_100k', 'G_100k_1m', 'G_100k_5m', 'G_1m_0',
                'G_1m_1m', 'G_1m_10m']

    figp, axp = plot_data(java_times, python_times, network_times, x_labels)
    axp.set_ylabel('time to calculate')
    axp.set_title('shortest path')

    figp.tight_layout()

    plt.show()
    figure



if __name__ == '__main__':
    # plot_scc()
    plot_paths()
    plot_scc_single()
    plot_scc()
