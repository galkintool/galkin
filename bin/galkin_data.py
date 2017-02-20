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

# import auxiliary modules
import galkin.readparsFile
import galkin.processdata


print ''
print '### read input ###'
# check arguments passed by the user
if (len(sys.argv)==1):   # launch window to ask input parameters
   import galkin.readparsDialog # import dialog here to avoid importing wx module for GUI when not needed
   print 'launching window...'
   inputpars=galkin.readparsDialog.LaunchWindowAndRead() 	  # launch dialog window and read parameters. the output is a list of all parameters (R0,V0,Usun,Vsun,Wsun,syst, [flags])
   galkin.readparsFile.CheckAndPrintParameters(inputpars)    # check and print parameters
elif (len(sys.argv)==2): # read input file given by the user
   inputfilename=sys.argv[1]
   inputpars=galkin.readparsFile.ReadFromFileConfigParser(inputfilename) # read parameters from file. the output is a list of all parameters (R0,V0,Usun,Vsun,Wsun,syst, [flags])
   galkin.readparsFile.CheckAndPrintParameters(inputpars)    # check and print parameters
elif (len(sys.argv)>2):  # give error message
   print '*** error: too many arguments given. exiting now.';sys.exit()


print ''
print '### process data ###'
vecout=galkin.processdata.ProcessData(inputpars)
totallistvc=vecout[0];totallistpos=vecout[1];totallistraw=vecout[2];


print ''
print '### output data ###'

fileoutvc = open('output/vcdata.dat', 'w')     # file with rotation curve measurements
fileoutvc.write('# R0[kpc]=');fileoutvc.write(str(inputpars[0]));
fileoutvc.write('\t v0[km/s]=');fileoutvc.write(str(inputpars[1]));
fileoutvc.write('\t Usun[km/s]=');fileoutvc.write(str(inputpars[2]));
fileoutvc.write('\t Vsun[km/s]=');fileoutvc.write(str(inputpars[3]));
fileoutvc.write('\t Wsun[km/s]=');fileoutvc.write(str(inputpars[4]));
fileoutvc.write('\n');
fileoutvc.write('# R[kpc] \t delta_R[kpc] \t vc[km/s] \t delta_vc[km/s] \t wc[km/s/kpc] \t delta_wc[km/s/kpc] \t Reference\n')
for elem1 in totallistvc:
    for elem2 in elem1:
        fileoutvc.write(str(elem2)+'\t')
    fileoutvc.write('\n')
fileoutvc.close()
print 'rotation curve data: vcdata.dat'

fileoutpos = open('output/posdata.dat', 'w')   # file with positional data
fileoutpos.write('# R0[kpc]=');fileoutpos.write(str(inputpars[0]));
fileoutpos.write('\t v0[km/s]=');fileoutpos.write(str(inputpars[1]));
fileoutpos.write('\t Usun[km/s]=');fileoutpos.write(str(inputpars[2]));
fileoutpos.write('\t Vsun[km/s]=');fileoutpos.write(str(inputpars[3]));
fileoutpos.write('\t Wsun[km/s]=');fileoutpos.write(str(inputpars[4]));
fileoutpos.write('\n');
fileoutpos.write('# R[kpc] \t D[kpc] \t l[deg] \t b[deg] \t x[kpc] \t y[kpc] \t z[kpc] \t Reference\n')
for elem1 in totallistpos:
    for elem2 in elem1:
        fileoutpos.write(str(elem2)+'\t')
    fileoutpos.write('\n')
fileoutpos.close()
print 'position data:       posdata.dat'

fileoutraw = open('output/rawdata.dat', 'w')     # file with rotation curve measurements
fileoutraw.write('# v_los[km/s] \t delta_v_los[km/s] \t mu_ell*[mas/yr] \t delta_mu_ell*[mas/yr] \t mu_b[mas/yr] \t delta_mu_b[mas/yr] \t Reference\n')
for elem1 in totallistraw:
    for elem2 in elem1:
        fileoutraw.write(str(elem2)+'\t')
    fileoutraw.write('\n')
fileoutraw.close()
print 'raw data:            rawdata.dat'

