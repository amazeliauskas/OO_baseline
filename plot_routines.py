fw=4
gr=4/3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import scienceplots
import matplotlib.colors as mcolors

plt.style.use(['science', 'nature'])

plt.rcParams['axes.prop_cycle'] = plt.cycler('color', ['#0085CA', '#008F00', '#FF9500', '#FF2C00', '#845B97', '#474747', '#9e9e9e', mcolors.CSS4_COLORS["salmon"]])

plt.rcParams['font.size'] = 11
plt.rcParams['xtick.minor.visible'] = False
plt.rcParams['ytick.minor.visible'] = False
plt.rcParams['axes.linewidth'] = 0.5
plt.rcParams['axes.labelsize'] =  11
plt.rcParams['axes.labelsize'] =  11
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

trans=0.5




#cols=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
#cols=["C0","C1", "C2", "C3", "C4", "C5"]
#ls=["-","-","-", "-","-", "--"]

def merge(x,y):
    return (np.array([x,y]).T).flatten()
def double(x):
    return (np.array([x,x]).T).flatten()
def make_pale(color, alpha=0.5):
    """
    Mixes the given color with white.
    alpha=0.0 returns white
    alpha=1.0 returns original color
    """
    base = mcolors.to_rgb(color)
    white = (1, 1, 1)
    pale = tuple(alpha * c + (1 - alpha) * w for c, w in zip(base, white))
    return pale
# make a band plot from data file with x and y scaling
def plot_data_band(ax, fname, xfac=1,yfac=1,style=0, label=""):
    data=np.loadtxt(fname)
    x=data[:,0]
    y=data[:,1]
    yerr=data[:,2]
    ax.plot(x*xfac,y*yfac,color=cols[style], linestyle=ls[style], label=label)
    ax.fill_between(x*xfac,(y-yerr)*yfac,(y+yerr)*yfac,color=cols[style], alpha=0.5 )

# make a constant yval line plot
def plot_line(ax, xrange, yval,col="k",ls="--", label="", log=False):
    if log:
        x=np.exp(np.linspace(np.log(xrange[0]),np.log(xrange[1])))
    else:
        x=np.linspace(xrange[0],xrange[1])
    ax.plot(x,np.ones_like(x)*yval,color=col, ls=ls, label=label)
def set_labels(ax, xrange,yrange, xlabel,ylabel,scale='linear'):
    ax.set_xlim(xrange)
    ax.set_ylim(yrange)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if scale=='loglog':
        ax.set_xscale('log')
        ax.set_yscale('log')

def set_legend(ax, title="",loc="upper right",ncols=1,anchor=None):
    ax.legend(frameon=False, title=title,labelspacing=0.2, handlelength=2,loc=loc,ncols=ncols,columnspacing=0.5,bbox_to_anchor=anchor)


