print ''
print ''
print '####################################################################################################'
print '# galkin, version 1.0, by Miguel Pato and Fabio Iocco.'
print '# Last update: MP 30 May 2016.'
print '############'
print '# A tool to handle the available data on the rotation curve of the Milky Way.'
print '####################################################################################################'
print ''


# import system modules
import sys
sys.path.append('..')
import matplotlib.pyplot as plt

# import auxiliary modules
import galkin.plots   # routines to plot data


print ''
print '### read filenames ###'
# check arguments passed by the user
if (len(sys.argv)==3):   # read filenames
   vcfilename= sys.argv[1] # rotation curve data
   posfilename=sys.argv[2] # position data
   print 'rotation curve data:\t',vcfilename
   print 'position data:\t\t',posfilename

   vcfile = open(vcfilename,'r')
   totallistvc=[]
   i=0
   for line in vcfile:
       i+=1
       values=line.split()	
       if(i>2):
	 totallistvc.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),values[6]])

   posfile = open(posfilename,'r')
   totallistpos=[]
   i=0
   for line in posfile:
       i+=1
       values=line.split()	
       if(i>2):
	 totallistpos.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),values[7]])

else:  # give error message
   print '*** error: too many or too few arguments given. please give one rotation curve data file (e.g. vcdata.dat) and one position data file (e.g. posdata.dat). exiting now.';sys.exit()


print ''
print '### plot data ###'
if(len(totallistvc)!=0):  # plot rotation curve measurements
  galkin.plots.PlotRotationCurve(totallistvc)
if(len(totallistpos)!=0): # plot positions in galactic plane
  galkin.plots.PlotPositions(totallistpos)
if(len(totallistvc)!=0 or len(totallistpos)!=0):
  plt.show()
  print 'done.'




