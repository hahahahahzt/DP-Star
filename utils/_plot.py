#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: nomalocaris <nomalocaris.top>
"""
    the functions for plot.
"""
from __future__ import (absolute_import, unicode_literals)
import numpy as np
import matplotlib.pyplot as plt
from utils import ProgressBar


def plot_scatter(points, fig_size=(6, 6), color='purple', size=5):
    """plot the points
    """
    plt.figure(figsize=fig_size)
    plt.scatter(x=[p[0] for p in points], y=[p[1] for p in points], color=color, s=size)
    plt.show()


def plot_traj(trajs, fig_size=(6, 6), color="mediumpurple", size=5,
              title='',
              is_plot_line=False, od_only=False, offset=None):
    """plot the traj
    """
    if offset is None:
        offset = [0, 0]
    p = ProgressBar(len(trajs), '绘制轨迹图')
    plt.figure(figsize=fig_size)
    for i in range(len(trajs)):
        p.update(i)
        traj = np.array(trajs[i])
        if od_only:
            traj = [traj[0], traj[-1]]
        x = [x[0] + np.random.uniform(-offset[0], offset[0]) for x in traj]
        y = [y[1] + np.random.uniform(-offset[1], offset[1]) for y in traj]

        if od_only:
            if is_plot_line:
                plt.plot(x[0], y[0], c=color)
                plt.plot(x[1], y[1], c="yellowgreen")
            plt.scatter(x[0], y[0], c=color, s=size)
            plt.scatter(x[1], y[1], c="yellowgreen", s=size)
        else:
            if is_plot_line:
                plt.plot(x, y, c=color)
            plt.scatter(x, y, c=color, s=size)
    plt.title(title)
    plt.show()
