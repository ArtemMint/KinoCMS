"""
Charts
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')

from ..repositories.users import *


def get_pie_chart():
    fig, ax = plt.subplots()
    ax.pie(
        [get_men_count(), get_women_count()],
        explode=(0.1, 0),
        labels=['Male', 'Female', ],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
    )
    ax.axis('equal')
    plt.savefig('media/sale_purchase_peichart.png', dpi=100)


def get_bar_chart():
    objects = [get_men_avg_age(), get_women_avg_age()]
    y_pos = np.arange(len(objects))
    fig, ax = plt.subplots()
    plt.bar(y_pos, objects, align='center', alpha=0.5)
    plt.xticks(y_pos, ['Male', 'Female'])
    plt.ylabel('Average age')
    plt.savefig('media/barchart.png')
