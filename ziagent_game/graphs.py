

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def graph_moves(swerves, straights):

    """
    Motified code from: 
    http://matplotlib.org/examples/axes_grid/scatter_hist.html
    """
    print 'Swerves (x-axis) to Straights (y-axis)'
    x = swerves
    y = straights

    fig = plt.figure(1, figsize=(10,10))

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    # the scatter plot:
    axScatter = plt.subplot(111)
    axScatter.scatter(x, y)
    axScatter.set_aspect(1.)

    # create new axes on the right and on the top of the current axes
    # The first argument of the new_vertical(new_horizontal) method is
    # the height (width) of the axes to be created in inches.
    divider = make_axes_locatable(axScatter)
    axHistx = divider.append_axes("top", 1.2, pad=0.1, sharex=axScatter)
    axHisty = divider.append_axes("right", 1.2, pad=0.1, sharey=axScatter)

    # make some labels invisible
    plt.setp(axHistx.get_xticklabels() + axHisty.get_yticklabels(),
             visible=False)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
    lim = ( int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(0, lim + binwidth, binwidth)
    axHistx.hist(x, bins=bins)
    axHisty.hist(y, bins=bins, orientation='horizontal')

    # the xaxis of axHistx and yaxis of axHisty are shared with axScatter,
    # thus there is no need to manually adjust the xlim and ylim of these
    # axis.

    #axHistx.axis["bottom"].major_ticklabels.set_visible(False)
    for tl in axHistx.get_xticklabels():
        tl.set_visible(False)
    
    # calculate realistic histogram scale
    z = (len(x)/6)
    z -= z % -5
    z = round(z, (len(str(z)) - 1) * -1)
    axHistx.set_yticks([0, z, z*2])

    #axHisty.axis["left"].major_ticklabels.set_visible(False)
    for tl in axHisty.get_yticklabels():
        tl.set_visible(False)
    axHisty.set_xticks([0, z, z*2])


    plt.draw()
    plt.show()

def graph_payoffs(payoffs, population):
    p_array = np.array(payoffs)
    mu = np.mean(payoffs)
    sigma = np.std(payoffs)
    x = mu + sigma*p_array

    # the histogram of the data
    bins =  population/20
    if bins < 10:
        bins = 10
    n, bins, patches = plt.hist(payoffs, bins, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('Payoffs')
    plt.ylabel('Probability')
    plt.title('Payoffs: mu=%s, sigma=%s' % (population,round(sigma,2)))

    plt.axis([mu - 3*sigma, mu + 3*sigma, 0, round(np.amax(y) + 0.1, 2)])
    plt.grid(True)

    plt.show()

