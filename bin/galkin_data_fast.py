# This file shows an example of how galkin can be used inside another code to process the original data and output the rotation curve measurements.
print ''
print ''
print '####################################################################################################'
print '# galkin, version 1.0, by Miguel Pato and Fabio Iocco.'
print '# Last update: MP 04 Nov 2016.'
print '############'
print '# A tool to handle the available data on the rotation curve of the Milky Way.'
print '####################################################################################################'
print ''


# import system modules
import sys
sys.path.append('..')

# import auxiliary modules
import galkin.processdata   # routines to process kinematic data
import galkin.readparsFile  # routines to read and check input parameters


print ''
print '### setting input ###' # set here the desired input parameters
# Galactic parameters
R0=8.0 						# Galactocentric distance (kpc)
V0=230.						# local circular velocity (km/s)
UsunINUSE=11.10					# solar motion in the U-direction (km/s), e.g. from Schoenrich+ '10, MNRAS 403, 1829 (2010)
VsunINUSE=12.24					# solar motion in the V-direction (km/s), e.g. from Schoenrich+ '10, MNRAS 403, 1829 (2010)
WsunINUSE=07.25					# solar motion in the W-direction (km/s), e.g. from Schoenrich+ '10, MNRAS 403, 1829 (2010)
SYSTDISP=0.					# systematic dispersion due to spiral arm streaming (km/s), e.g. 11.8 km/s from Brand & Blitz '93, A&A 275, 67 (1993)
# Flags
flagPROPERMOTIONS=0	 			# proper motions not supported in current version - please keep at 0
flagHITERMINAL=1				# whether to use HI terminal velocities
flagFich89tab2=1				# whether to use Fich+ '89, ApJ 342, 272 (1989) (Table 2)
flagMalhotra95=1				# whether to use Malhotra '95, ApJ 448, 138 (1995)
flagMcClureGriffithsDickey07=1			# whether to use McClure-Griffiths & Dickey '07, ApJ 671, 427 (2007)
flagHITHICKNESS=1				# whether to use the HI thickness method
flagHonmaSofue97=1				# whether to use Honma & Sofue '97, PASJ 49, 453 (1997)
flagCOTERMINAL=1				# whether to use CO terminal velocities
flagBurtonGordon78=1				# whether to use Burton & Gordon '78, A&A 63, 7 (1978)
flagClemens85=1					# whether to use Clemens '85, ApJ 295, 422 (1985)
flagKnapp85=1					# whether to use Knapp+ '85, AJ 90, 2 (1985)
flagLuna06=1					# whether to use Luna+ '06, ApJ 641, 938 (2006)
flagHIIREGIONS=1				# whether to use HII regions
flagBlitz79=1					# whether to use Blitz '79, ApJL 231, L115 (1979)
flagFich89tab1=1				# whether to use Fich+ '89, ApJ 342, 272 (1989) (Table 1)	
flagTurbideMoffat93=1				# whether to use Turbide & Moffat '93, AJ 105, 5 (1993)
flagBrandBlitz93=1				# whether to use Brand & Blitz '93, A&A 275, 67 (1993)
flagHou09tabA1=1				# whether to use Hou+ '09, A&A 499, 473 (2009) (Table A1)
flagGMC=1					# whether to use giant molecular clouds
flagHou09tabA2=1				# whether to use Hou+ '09, A&A 499, 473 (2009) (Table A2)
flagOPENCLUSTERS=1				# whether to use open clusters
flagFrinchaboyMajewski08=1			# whether to use Frinchaboy & Majewski '08, AJ 136, 118 (2008)
flagPLANETARYNEBULAE=1				# whether to use planetary nebulae
flagDurand98=1					# whether to use Durand+ '98, A&AS 132, 13 (1998)
flagCEPHEIDS=1					# whether to use classical cepheids
flagPont94=1					# whether to use Pont+ '94, A&A 285, 415 (1994)
flagPont97=1					# whether to use Pont+ '97, A&A 318, 416 (1997)
flagCSTARS=1					# whether to use carbon stars
flagDemersBattinelli07=1			# whether to use Demers & Battinelli '07, A&A 473, 143 (2007)
flagBattinelli12=1				# whether to use Battinelli+ '12, Ap 56, 68 (2013)
flagMASERS=1					# whether to use masers
flagReid14=1					# whether to use Reid+ '14, ApJ 783, 130 (2014)
flagHonma12=1					# whether to use Honma+ '12, PASJ 64, 136 (2012)
flagStepanishchevBobylev11=1			# whether to use Stepanishchev & Bobylev '11, AstL 37, 4 (2011)
flagXu13=1					# whether to use Xu+ '13, ApJ 769, 15 (2013)
flagBobylevBajkova13=1				# whether to use Bobylev & Bajkova '13, AstL 39, 809 (2013)
flagastropy=0				 	# whether to use astropy for equatorial-to-galactic conversions

inputpars=(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP, flagPROPERMOTIONS,flagHITERMINAL,flagFich89tab2,flagMalhotra95,flagMcClureGriffithsDickey07, flagHITHICKNESS,flagHonmaSofue97,flagCOTERMINAL,flagBurtonGordon78,flagClemens85,flagKnapp85,flagLuna06, flagHIIREGIONS,flagBlitz79,flagFich89tab1,flagTurbideMoffat93,flagBrandBlitz93,flagHou09tabA1, flagGMC,flagHou09tabA2,flagOPENCLUSTERS,flagFrinchaboyMajewski08,flagPLANETARYNEBULAE,flagDurand98,flagCEPHEIDS,flagPont94,flagPont97, flagCSTARS,flagDemersBattinelli07,flagBattinelli12, flagMASERS,flagReid14,flagHonma12,flagStepanishchevBobylev11,flagXu13,flagBobylevBajkova13,flagastropy)


# comment out the following three lines to make the process faster
print ''
print '### checking input ###'
galkin.readparsFile.CheckAndPrintParameters(inputpars)    # check and print parameters


print ''
print '### process data ###'
vecout=galkin.processdata.ProcessData(inputpars)
totallistvc=vecout[0]; # list of {R[kpc], delta_R[kpc], vc[km/s], delta_vc[km/s], wc[km/s/kpc], delta_wc[km/s/kpc], Reference}


# do here whatever you need to do with the output rotation curve, e.g. print the first and last point
print ''
print '### output data ###'
print totallistvc[0]
print totallistvc[len(totallistvc)-1]


