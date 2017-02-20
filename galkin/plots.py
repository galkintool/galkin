# This file has the plotting routines.
# Last update: MP 30 May 2016.


# import system modules
import matplotlib.pyplot as plt


# plot rotation curve. input: list of rotation curve measurements from processdata.ProcessData(inputpars).
def PlotRotationCurve(totallistvc):
    vecRp    =[row[0] for row in totallistvc]    # galactocentric distance [kpc]
    vecerrRp =[row[1] for row in totallistvc]    # error in galactocentric distance [kpc]
    vecvRp   =[row[2] for row in totallistvc]    # rotation velocity [km/s]
    vecerrvRp=[row[3] for row in totallistvc]    # error in rotation velocity [km/s]
    fig, ax1 = plt.subplots()
    fig.canvas.set_window_title('rotation curve measurements')
    fig.patch.set_facecolor('white') # setting background to white
    ax1.errorbar(vecRp, vecvRp, xerr=vecerrRp, yerr=vecerrvRp, fmt='r.')
    ax1.axis([0., max(vecRp)+0.1*(max(vecRp)-0.), min(0.,min(vecvRp)-0.1*(max(vecvRp)-min(vecvRp))) , max(vecvRp)+0.1*(max(vecvRp)-min(vecvRp))])
    ax1.set_xlabel('$R$ [kpc]')
    ax1.set_ylabel('$v_c$ [km/s]')
    #draw()

# plot galactic positions. input: list of positions from processdata.ProcessData(inputpars).
def PlotPositions(totallistpos):
    vecX     =[-row[4] for row in totallistpos]  # galactic X [kpc]
    vecY     =[row[5] for row in totallistpos]   # galactic Y [kpc]
    vecXsun  =[-8.0]                             # galactic X of the sun [kpc]
    vecYsun  =[0.]                               # galactic Y of the sun [kpc]
    vecXGC   =[0.]                               # galactic X of the galactic centre [kpc]
    vecYGC   =[0.]                               # galactic Y of the galactic centre [kpc]
    fig, ax2 = plt.subplots()
    fig.canvas.set_window_title('positions in galactic disk')
    fig.patch.set_facecolor('white') # setting background to white
    ax2.plot(vecY,vecX, 'r.')
    ax2.plot(vecYsun,vecXsun, marker='$\odot$')
    ax2.plot(vecYGC,vecXGC, marker='o',mfc='none', color='black')
    miny=min(vecY)-0.1*(max(vecY)-min(vecY));maxy=max(vecY)+0.1*(max(vecY)-min(vecY));
    minx=min(vecX)-0.1*(max(vecX)-min(vecX));maxx=max(vecX)+0.1*(max(vecX)-min(vecX));
    ax2.axis([min(minx,miny),max(maxx,maxy), min(minx,miny),max(maxx,maxy) ])
    ax2.set_xlabel('$y$ [kpc]')
    ax2.set_ylabel('$-x$ [kpc]')
    #draw()
