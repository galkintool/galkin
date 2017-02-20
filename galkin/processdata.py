# This file imports the original kinematic data and processes it into rotation curve measurements.
# Last update: MP 04 Nov 2016.


# import system modules
import os
from numpy import (pi,cos,sin,arcsin,arccos,sqrt,log,log10,sign)
# import auxiliary modules
import functions     # useful functions


# process data according to input data flags. input: input parameters as outputed from readpars.LaunchWindowAndRead() or readpars.ReadFromFile(inputfilename). outputs: list of velocities, list of positions.
def ProcessData(inputpars):
    R0=inputpars[0];V0=inputpars[1];UsunINUSE=inputpars[2];VsunINUSE=inputpars[3];WsunINUSE=inputpars[4];SYSTDISP=inputpars[5]
    flagProperMotions=inputpars[6];
    SigmaVirMasers = 7.0;  # km/s, virial motion of stars associated to masers, see Sec 3 of Reid 09, Apj 700:137

    flagastropy=inputpars[42];

    totallistvc=[];totallistpos=[];totallistraw=[];

    if(inputpars[7]==1): 	# HI terminal velocities
      print 'processing HI terminal velocities...'
      if(inputpars[8]==1):	 # Fich+ 89 (Table 2)
	print ' processing Fich+ 89 (Table 2)...'
	vec=ProcessFich89tab2(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[9]==1):	 # Malhotra 95
	print ' processing Malhotra 95...'
	vec=ProcessMalhotra95(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[10]==1):	 # McClure-Griffiths & Dickey 07
	print ' processing McClure-Griffiths & Dickey 07...'
	vec=ProcessMcClureGriffithsDickey07(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      
    if(inputpars[11]==1): 	# HI thickness method
      print 'processing HI thickness method...'
      if(inputpars[12]==1):	 #  Honma & Sofue 97
	print ' processing Honma & Sofue 97...'
	vec=ProcessHonmaSofue97(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0]; # this provides no positional data nor raw data
     
    if(inputpars[13]==1): 	# CO terminal velocities
      print 'processing CO terminal velocities...'
      if(inputpars[14]==1):	 # Burton & Gordon 78
	print ' processing Burton & Gordon 78...'
	vec=ProcessBurtonGordon78(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[15]==1):	 # Clemens 85
	print ' processing Clemens 85...'
	vec=ProcessClemens85(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[16]==1):	 #   Knapp+ 85
	print ' processing Knapp+ 85...'
	vec=ProcessKnapp85(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[17]==1):	 # Luna+ 06
	print ' processing Luna+ 06...'
	vec=ProcessLuna06(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[18]==1): 	# HII regions
      print 'processing HII regions...'
      if(inputpars[19]==1):	 # Blitz 79
	print ' processing Blitz 79...'
	vec=ProcessBlitz79(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];	
      if(inputpars[20]==1):	 # Fich+ 89 (Table 1)
	print ' processing Fich+ 89 (Table 1)...'
	vec=ProcessFich89tab1(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,inputpars[21],inputpars[22])
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[21]==1):	 #  Turbide & Moffat 93
	print ' processing Turbide & Moffat 93...'
	vec=ProcessTurbideMoffat93(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,inputpars[22])
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[22]==1):	 # Brand & Blitz 93
	print ' processing Brand & Blitz 93...'
	vec=ProcessBrandBlitz93(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[23]==1):	 # Hou+ 09 (Table A1)
	print ' processing Hou+ 09 (Table A1)...'
	vec=ProcessHou09tabA1(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,inputpars[22])
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[24]==1): 	# giant molecular clouds
      print 'processing giant molecular clouds...'
      if(inputpars[25]==1):	 #  Hou+ 09 (Table A2)
	print ' processing Hou+ 09 (Table A2)...'
	vec=ProcessHou09tabA2(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[26]==1): 	# open clusters
      print 'processing open clusters...'
      if(inputpars[27]==1):	 #  Frinchaboy & Majewski 08
	print ' processing Frinchaboy & Majewski 08...'
	vec=ProcessFrinchaboyMajewski08(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[28]==1): 	# planetary nebulae
      print 'processing planetary nebulae...'
      if(inputpars[29]==1):	 #  Durand+ 98
	print ' processing Durand+ 98...'
	vec=ProcessDurand98(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[30]==1): 	# classical cepheids
      print 'processing classical cepheids...'
      if(inputpars[31]==1):	 # Pont+ 94
	print ' processing Pont+ 94...'
	vec=ProcessPont94(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[32]==1):	 # Pont+ 97
	print ' processing Pont+ 97...'
	vec=ProcessPont97(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[33]==1): 	# carbon stars
      print 'processing carbon stars...'
      if(inputpars[34]==1):	 # Demers & Battinelli 07
	print ' processing Demers & Battinelli 07...'
	vec=ProcessDemersBattinelli07(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[35]==1):	 # Battinelli+ 12
	print ' processing Battinelli+ 12...'
	vec=ProcessBattinelli12(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    if(inputpars[36]==1): 	# masers
      print 'processing masers...'
      if(inputpars[37]==1):	 # Reid+ 14
	print ' processing Reid+ 14...'
	vec=ProcessReid14(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,SigmaVirMasers, flagastropy)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[38]==1):	 # Honma+ 12
	print ' processing Honma+ 12...'
	vec=ProcessHonma12(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,inputpars[37],SigmaVirMasers, flagastropy)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[39]==1):	 #  Stepanishchev & Bobylev 11
	print ' processing Stepanishchev & Bobylev 11...'
	vec=ProcessStepanishchevBobylev11(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,inputpars[37],SigmaVirMasers, flagastropy)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[40]==1):	 # Xu+ 13
	print ' processing Xu+ 13...'
	vec=ProcessXu13(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,inputpars[37],SigmaVirMasers, flagastropy)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];
      if(inputpars[41]==1):	 # Bobylev & Bajkova 13
	print ' processing Bobylev & Bajkova 13...'
	vec=ProcessBobylevBajkova13(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,inputpars[37],SigmaVirMasers, flagastropy)
	totallistvc+=vec[0];totallistpos+=vec[1];totallistraw+=vec[2];

    return (totallistvc,totallistpos,totallistraw)

# process data in Fich+ 89 (Table 2). inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessFich89tab2(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3;VsunData = 15.3;WsunData = 7.7 # km/s, standard solar motion, see Appendix in Reid+ '09 and Table 5 therein
    inputfile = open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Fich89_Table2.dat') ,'r')
    data=[]
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([float(values[0]),float(values[1])])

    print '  selected ', len(data), ' HI terminal velocities'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180. # rad
        vlsrdata=data[i][1];
        errvlsrdata=4.5 # km/s, see Sec. II.b.i
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Fich89_Table2']);

	# correction due to LSR motion in radial direction, see Eq 4
	vlsrdata += (-4.2)*cos(l); # b=0

	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s

	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc

	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'Fich89_Table2']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), data[i][0], 0);
 	listpos.append([Rt, R0*cos(l), data[i][0], 0., vecpos[0], vecpos[1], vecpos[2], 'Fich89_Table2']); # Rp,Dp,l,b,X,Y,Z

    return (listvc,listpos,listraw)

# process data in Malhotra 95. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessMalhotra95(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfileC= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Malhotra95_Figure7_Circles.dat') ,'r')   # format : see Figure 7 in Malhotra ' 95, 1 st quadrant
    inputfileT= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Malhotra95_Figure7_Triangles.dat') ,'r') # format : see Figure 7 in Malhotra ' 95, 1 st quadrant
    inputfileS= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Malhotra95_Figure7_Squares.dat') ,'r')   # format : see Figure 7 in Malhotra ' 95, 4 th quadrant
    data=[]
    i=0
    for line in inputfileC:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([arcsin(float(values[0]))*180./pi,float(values[1])]) # transform R/R0 in l in the 1 st quadrant
    i=0
    for line in inputfileT:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([arcsin(float(values[0]))*180./pi,float(values[1])]) # transform R/R0 in l in the 1 st quadrant
    i=0
    for line in inputfileS:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([360.-arcsin(float(values[0]))*180./pi,float(values[1])]) # transform R/R0 in l in the 4th quadrant

    print '  selected ', len(data), ' HI terminal velocities'

    UsunData = 10.3;VsunData = 15.3;WsunData = 7.7 # km/s, standard solar motion, see Appendix in Reid+ '09 and Table 5 therein

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180. # rad
        vlsrdata=data[i][1];
        errvlsrdata=9.0      # km/s, see Sec. 3.4
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Malhotra95']);

	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s

	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc

	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'Malhotra95']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), data[i][0], 0);
 	listpos.append([Rt, R0*cos(l), data[i][0], 0., vecpos[0], vecpos[1], vecpos[2], 'Malhotra95']); # Rp,Dp,l,b,X,Y,Z

    return (listvc,listpos,listraw)

# process data in McClure-Griffiths & Dickey 07. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessMcClureGriffithsDickey07(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3;VsunData = 15.3; WsunData = 7.7 # km/s, assume the same as for masers, see Appendix in Reid+ '09 and Table 5 therein
    inputfile = open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_McClureGriffithsDickey07.dat') ,'r') 
    dumData=[]
    data=[]
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  dumData.append([float(values[0]),float(values[1])])
	  
    for i in range(len(dumData)):
        if ( abs(dumData[i][0]-306.)<=1.) or abs(dumData[i][0]- 312.) <= 0.5 or abs(dumData[i][0]- 320.) <= 0.5: # longitudes of HI clouds, see Sec. 4
	   continue
        if (abs(sin(dumData[i][0])*pi/180.) > 0.95): # exclude sin l>0.95 because of large width wrt measured value, see Sec. 4.2
           continue
        data.append([dumData[i][0],dumData[i][1]])
    print '  selected ', len(data), ' out of the total sample of ', len(dumData), ' HI terminal velocities'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180. #rad
        vlsrdata=data[i][1];
        errvlsrdata=10.
        if (l*180./pi<325.):
            errvlsrdata = 1. # km/s
        if (l*180./pi>332.5):
            errvlsrdata = 3. # km/s
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'McClureGriffithsDickey07']);
        
	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s

	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc

	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'McClureGriffithsDickey07']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), data[i][0], 0);
 	listpos.append([Rt, R0*cos(l), data[i][0], 0., vecpos[0], vecpos[1], vecpos[2], 'McClureGriffithsDickey07']); # Rp,Dp,l,b,X,Y,Z

    return (listvc,listpos,listraw)

# process data in Honma & Sofue 97. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessHonmaSofue97(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfile = open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_HonmaSofue97.dat') ,'r')
    data=[]
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([float(values[0]),float(values[1]),float(values[2])])

    print '  selected ', len(data), ' HI thickness rings'
   
    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        WRp=data[i][0]; errWRp=5.8 # km/s, this is W (R') and corresponding uncertainty.Uncertainty is based on Sec 2.4
        errWRp = pow(errWRp,2.)+pow(SYSTDISP,2.)
        errWRp=pow(errWRp,1./2.)   # add systematic to the error in vlsr; W (Rp) sinl cosb = vlsr, so this is not totally self - consistent, but gives the gist of the effect of a systematic*
        RpoverR0=data[i][1]; errRpoverR0=data[i][2] # R/R0
        Rp = RpoverR0*R0; errRp = errRpoverR0*R0    # kpc 
        vRp = RpoverR0*(WRp +V0);
        errvRp = pow((errRpoverR0*(WRp + V0)),2.) + pow((RpoverR0*errWRp),2.) # km/s, error in quadrature
        errvRp = pow(errvRp,1./2.) # km/s, error in quadrature
        wRp=(WRp + V0)/R0; errwRp=errWRp/R0 # km/s/kpc
        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'HonmaSofue97']);
        listpos.append(['-',' -', ' -', ' -', ' -', ' -', ' -', 'HonmaSofue97']); # Rp,Dp,l,b,X,Y,Z
	listraw.append(['-', '-', '-', '-', '-', '-', 'HonmaSofue97']);
        
    return (listvc,listpos,listraw)

# process data in Burton & Gordon 78. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessBurtonGordon78(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7 # km/s, assume the standard solar motion direction (see eg Appendix in Reid+ '09 and Table 5 therein)
    inputfile = open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_BurtonGordon78.dat') ,'r')
    data=[]
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([float(values[0]),float(values[1])])
    print '  selected ', len(data), ' CO terminal velocities'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l = data[i][0]*pi/180.; # rad
        vlsrdata = data[i][1] # km/s, already with line width correction (see Sec. 3)
        errvlsrdata = 2.6 # km/s see Sec. 
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'BurtonGordon78']);

	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s
	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc
	
	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'BurtonGordon78']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), data[i][0], 0);
 	listpos.append([Rt, R0*cos(l), data[i][0], 0., vecpos[0], vecpos[1], vecpos[2], 'BurtonGordon78']); # Rp,Dp,l,b,X,Y,Z
    return (listvc,listpos,listraw)

# process data in Clemens 85. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessClemens85(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7 # km/s, assume the standard solar motion direction (see eg Appendix in Reid+ '09 and \Table 5 therein)   
    inputfile = open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Clemens85.dat') ,'r')
    data=[]
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([float(values[0]),float(values[1]),float(values[2])])
    print '  selected ', len(data), ' CO terminal velocities'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l = data[i][0]*pi/180.; # rad
        vlsrdata=data[i][1]-3.0 # km/s, with line width correction (see Sec. II.c)
        errvlsrdata=pow((data[i][2]/0.67),2.)+pow(0.6,2.)
        errvlsrdata=pow(errvlsrdata,1./2.) # km/s
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Clemens85']);

        #correction due to LSR motion, see Sec. II.d
        vlsrdata += 7.0*sin(l) # b=0  # no change of errvlsrdata
	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s

	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc
        
	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'Clemens85']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), data[i][0], 0);
 	listpos.append([Rt, R0*cos(l), data[i][0], 0., vecpos[0], vecpos[1], vecpos[2], 'Clemens85']); # Rp,Dp,l,b,X,Y,Z
    return (listvc,listpos,listraw)


# process data in Knapp+ 85. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessKnapp85(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7 # km/s, assume the standard solar motion direction (see eg Appendix in Reid+ '09 and \Table 5 therein)  
    inputfile1= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Knapp85_Fig5top.dat') ,'r')
    inputfile2= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Knapp85_Fig5middle.dat') ,'r')
    data=[]
    dataDum=[]
    i=0
    for line in inputfile1:
        i+=1
	values=line.split()	
        if(i>1):
	  data.append([float(values[0]),float(values[1]),float(values[2]),float(values[3])])
    print '  selected ', len(data), ' CO terminal velocities'

    i=0
    for line in inputfile2: # opening Middle file for additional error element, to be used later
        i+=1
	values=line.split()	
        if(i>1):
	  dataDum.append([float(values[1])])

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l =arcsin(data[i][0]); # rad l is in first quadrant
        vlsrdata = data[i][1]; # km/s
        errvlsrdata =pow( ( abs(data[i][2]) + abs(data[i][3]))/2.,2.)+pow(dataDum[i][0],2.)
        errvlsrdata=pow(errvlsrdata,1./2.) # take the error to be quadrature of error in Fig 5 (top) and mean sigma in Fig 5 (middle)
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Knapp85']);

	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s

	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc

	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'Knapp85']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), l*180./pi, 0);
 	listpos.append([Rt, R0*cos(l), l*180./pi, 0., vecpos[0], vecpos[1], vecpos[2], 'Knapp85']); # Rp,Dp,l,b,X,Y,Z
    return (listvc,listpos,listraw)


# process data in Luna+ 06. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessLuna06(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3*(14.8/20.); VsunData = 15.3*(14.8/20.); WsunData = 7.7*(14.8/20.); # km/s, assume the standard solar motion direction (see eg Appendix in \Reid + ' 09 and Table 5 therein) and the solar motion of 14.8 km/s as stated in Alvarez + ApJ 348, 495 (1990) (see Sec. IV)
    inputfile= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Luna06.dat') ,'r')
    data=[]
    dumData=[]
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  dumData.append([float(values[0]),float(values[1])])
    for i in range(len(dumData)):
        if ( abs(dumData[i][0])>=280.) and (abs(dumData[i][0]) <= 312.): # longitudes of HI clouds, see Sec. 4
	   continue
        data.append([dumData[i][0],dumData[i][1]])
    print '  selected ', len(data),' out of the total sample of ', len(dumData), ' CO terminal velocities'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180 # rad
        vlsrdata=data[i][1] # km/s
        errvlsrdata = 3.; # km/s for the error in VLSR use 3 km/s (see Sec.3.1)
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Luna06']);

	# transform vlsr in vhelio
	vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, 0.);
	# transform back to LSR using new solar motion
	vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, 0.);
	errvlsr = errvlsrdata; # km/s

	# compute dpprime, Rprime
	Rt = R0*abs(sin(l));errRt = 0.; # kpc
	# compute the velocity v(Rp)
        vRt = (Rt/R0)*(vlsr/sin(l) + V0); errvRt = abs(errvlsr*(Rt/R0)*(1./sin(l))); # km/s
	# compute angular velocity w(Rp)=v(Rp)/Rp
        wRt = (1./R0)*(vlsr/sin(l) + V0); errwRt = abs(errvlsr*(1./R0)*(1./sin(l))); # km/s/kpc

	listvc.append([Rt, errRt, vRt, errvRt, wRt, errwRt, 'Luna06']);
	vecpos = functions.XYZfromDlb(R0, R0*cos(l), l*180./pi, 0);
 	listpos.append([Rt, R0*cos(l), l*180./pi, 0., vecpos[0], vecpos[1], vecpos[2], 'Luna06']); # Rp,Dp,l,b,X,Y,Z
    return (listvc,listpos,listraw)

# process data in Blitz 79. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessBlitz79(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # m/s, standard solar motion, see Appendix in Reid+ '09 and Table 5 therein
    inputfile= open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Blitz79.dat') ,'r')
    data=[]

    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
          data.append([float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6])])
    print '  selected ', len(data), ' HII regions'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l = data[i][4]*pi/180.;b = data[i][5]*pi/180.; # rad
        dprime = data[i][0]; errdprime = data[i][1]; # kpc
        vlsrdata =data[i][2]; errvlsrdata =data[i][3];# km/s, see Sec. II.b.i
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)  

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Blitz79']);

        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b);
        # transform back to LSR using new solar motion
        vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr = errvlsrdata; # km/s
        # compute dpprime, Rprime*
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0);        
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity  
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Blitz79']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][4], data[i][5]);
        listpos.append([Rp, dprime, data[i][4], data[i][5], vecpos[0], vecpos[1], vecpos[2], 'Blitz79']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Fich+ 89 (Table 1).  inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagTurbideMoffat93,flagBrandBlitz93. outputs: list of velocities, list of positions.
def ProcessFich89tab1(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagTurbideMoffat93,flagBrandBlitz93):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s, standard solar motion, see Appendix in Reid+ '09 and Table 5 therein
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Fich89_Table1.dat') ,'r')
    checkfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_BrandBlitz93.dat') ,'r')
    data=[];dataDum=[];dataDum2=[];

    # list of objects in Brand & Blitz 93
    i2=0
    for line2 in checkfile:
	i2+=1
	values2=line2.split()
        if(i2>1):
	  dataDum2.append(values2[0]) 
    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  dataDum.append(values[0])

          if(flagTurbideMoffat93 == 1 and (dataDum[i-2] == 'S283' or dataDum[i-2] == 'S284' or dataDum[i-2] == 'S285' or dataDum[i-2] == 'S305' or dataDum[i-2]  == 'S309')): # exclude the regions reanalysed in Turbide & Moffat 93 : S283, S284, S285, S305, S309
            continue 

          if(flagBrandBlitz93 == 1): # exclude the regions reanalysed in Brand & Blitz 93
            found = 0
	    for name in dataDum2:
		if(dataDum[i-2] == name):
		  # print 'names: ',dataDum[i-2],name
	          found=1
	          break
            if(found==1):
	      continue

	  data.append([float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6])])
    print '  selected ', len(data), ' out of the total sample of ',len(dataDum),' HII regions'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180.;b=data[i][1]*pi/180.; # rad
        dprime=data[i][2];errdprime=data[i][3]; # kpc
        vlsrdata=data[i][4];
        errvlsrdata=pow(data[i][5],2.)+pow(6.4,2.)
        errvlsrdata=pow(errvlsrdata,1./2.)
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Fich89_Table1']);

        vlsrdata+=-4.2*cos(b)*cos(l) # correction due to LSR motion in radial direction, see Eq 4
        # no change of errvlsrdata
        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b);
        # transform back to LSR using new solar motion
        vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr = errvlsrdata; # km/s

        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0);        
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Fich89_Table1']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][0], data[i][1]);
        listpos.append([Rp, dprime, data[i][0], data[i][1], vecpos[0], vecpos[1], vecpos[2], 'Fich89_Table1']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Turbide & Moffat 93.  inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s,flagBrandBlitz93. outputs: list of velocities, list of positions.
def ProcessTurbideMoffat93(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagBrandBlitz93):
    UsunData = 9.; VsunData = 11.; WsunData = 6. # km/s, see after Eq 11
    VmolData = -4.2 # km/s, see after Eq 11
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_TurbideMoffat93.dat') ,'r')
    data=[];dataDum=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
	  dataDum.append(values[0])

          if(flagBrandBlitz93 == 1 and (dataDum[i-2] == 'S283' or dataDum[i-2] == 'S284' or dataDum[i-2] == 'S285')): # exclude the regions reanalysed in Brand & Blitz 93
            continue

	  data.append([values[0],float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),float(values[7]),float(values[8]),float(values[9]),float(values[10]),float(values[11]),float(values[12]),float(values[13]),float(values[14]),float(values[15]),float(values[16])])
    print '  selected ', len(data), ' out of the total sample of ',len(dataDum),' HII regions'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][1]*pi/180.;b=data[i][2]*pi/180.; # rad
        dprime=data[i][11];errdprime=data[i][12]; # kpc
        vlsrdata=data[i][3];
        errvlsrdata=data[i][4] # km/s, note that this is Eq 11 but fixing Vmol=0
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'TurbideMoffat93']);

        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b);
        # transform back to LSR using new solar motion
        vlsr1 = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr1 = errvlsrdata; # km/s

        # now correct for the mean peculiar motion of the CO velocities - correct only the rows in Table 5 not based in Ref 2 therein
        vlsr = functions.LOSboostHelio2LSR(vlsr1, VmolData, 0, 0, l, b) # km/s
        if(data[i][0] == "Bo2" or data[i][0] == "S289"):
          vlsr = vlsr1  # km/s
        errvlsr = errvlsr1 # km/s

        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0);        
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'TurbideMoffat93']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][1], data[i][2]);
        listpos.append([Rp, dprime, data[i][1], data[i][2], vecpos[0], vecpos[1], vecpos[2], 'TurbideMoffat93']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Brand & Blitz 93. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessBrandBlitz93(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s, standard solar motion, see Appendix in Reid+ '09 and Table 5 therein
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_BrandBlitz93.dat') ,'r')
    data=[]
    dumdata=[]

    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
          dumdata.append([float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6])])
    for i in range(len(dumdata)): 
        if (dumdata[i][0]>=360.-15.) or (dumdata[i][0]<=15.) or (abs(dumdata[i][0]-180.)<=15.): # exclude cones of 30 deg around galactic centre and anti galactic centre regions, see Sec. 3.3
            continue
        if (dumdata[i][2]<1.): # exclude d < 1 kpc, see Sec. 3.3
            continue
        data.append([dumdata[i][0],dumdata[i][1],dumdata[i][2],dumdata[i][3],dumdata[i][4],dumdata[i][5]])          
    print '  selected ', len(data), ' out of the total sample of ' , len(dumdata), ' HII regions'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180.;b=data[i][1]*pi/180.; # rad
        dprime=data[i][2];errdprime=data[i][3]; # kpc
        vlsrdata=data[i][4];
        errvlsrdata=pow(data[i][5],2.)+pow(6.4,2.)
        errvlsrdata=pow(errvlsrdata,1./2.)
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'BrandBlitz93']);

        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b);
        # transform back to LSR using new solar motion
        vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr = errvlsrdata; # km/s
        # compute dpprime, Rprime*
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0);        
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity       
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);
        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'BrandBlitz93']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][0], data[i][1]);
        listpos.append([Rp, dprime, data[i][0], data[i][1], vecpos[0], vecpos[1], vecpos[2], 'BrandBlitz93']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Hou+ 09 (Table A1). inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagBrandBlitz93. outputs: list of velocities, list of positions.
def ProcessHou09tabA1(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagBrandBlitz93):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s, assume standard solar motion, see Appendix in Reid+ '09 and Table 5 therein
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Hou09_TableA1.dat') ,'r')
    checkfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_BrandBlitz93.dat') ,'r')
    data=[];dataDum=[];dataDum2=[];dataDum3=[];

    # list of (l,b) in Brand & Blitz 93 with same cuts as applied there
    i2=0
    for line2 in checkfile:
	i2+=1
	values2=line2.split()
        if(i2>1):
	  dataDum3.append([values2[0],float(values2[1]),float(values2[2]),float(values2[3])])
    for i in range(len(dataDum3)): 
        if (dataDum3[i][1]>=360.-15.) or (dataDum3[i][1]<=15.) or (abs(dataDum3[i][1]-180.)<=15.): # exclude cones of 30 deg around galactic centre and anti galactic centre regions, see Sec. 3.3
            continue
        if (dataDum3[i][3]<1.): # exclude d < 1 kpc, see Sec. 3.3
            continue
        dataDum2.append([dataDum3[i][1],dataDum3[i][2]])          

    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
          dataDum.append([float(values[0]),float(values[1]),float(values[2]),values[3],float(values[4]),float(values[5]),values[6],float(values[7]),float(values[8]),values[9],values[10],values[11],float(values[12]),float(values[13]),float(values[14]),float(values[15]),float(values[16]),float(values[17]),float(values[18]),float(values[19]),float(values[20])])

    for i in range(len(dataDum)):
        l = dataDum[i][0];b = dataDum[i][1]; # deg
        Vlsr = dataDum[i][2] # km/s

	# exclude objects without Vlsr
	if(Vlsr == -100000):
	  continue

	# exclude galactic centre and anti-galactic centre as in Brand & Blitz 93
	if( (l >= 360 - 15 or l <= 15.) or abs(l - 180.) <= 15. ):
	  continue

        # select only objects with stellar distances or at tangent points
        dist = -1; errdist = -1;
        if(dataDum[i][7] != -100000):
          dist = dataDum[i][7];errdist = dataDum[i][8]; # kpc
  	if(dataDum[i][7] == -100000 and dataDum[i][10] == 'ktan'):
	  dist = pow(pow(R0,2) - pow(R0*abs(sin(l*pi/180.)),2),1./2.) / cos(b*pi/180.); errdist = 0.; # kpc, distance to tangent point
        if(dist == -1):
	  continue

        # exclude objects in Brand & Blitz '93 - there the Vlsr info and error are better than here
        if(flagBrandBlitz93 == 1):
          found = 0;
          for lb in dataDum2:
	     
    	      if(abs(l - lb[0]) < 0.05-1e-15 and abs(b - lb[1]) < 0.05-1e-15):
                # print 'l=',l,lb[0],abs(l - lb[0]),' b=',b,lb[1],abs(b - lb[1])
		found = 1
		break
   	  if(found == 1):
	    continue

        data.append([l, b, Vlsr, dist, errdist]);
    print '  selected ',len(data), ' out of the total sample of ', len(dataDum), ' HII regions'

    listvc=[];listpos=[];listraw=[];    
    for i in range(len(data)):
        l=data[i][0]*pi/180.;b=data[i][1]*pi/180.; # rad
        dprime=data[i][3];errdprime=data[i][4]; # kpc
        vlsrdata=data[i][2]; # km/s      
        errvlsrdata=3. # km/s, lacking better information assume 3 km/s error, which is typical
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Hou09_TableA1']);

        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b);
        # transform back to LSR using new solar motion
        vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr = errvlsrdata; # km/s
        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0)
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity        
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Hou09_TableA1']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][0], data[i][1]);
        listpos.append([Rp, dprime, data[i][0], data[i][1], vecpos[0], vecpos[1], vecpos[2], 'Hou09_TableA1']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Hou+ 09 (Table A2). inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessHou09tabA2(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s, assume standard solar motion, see Appendix in Reid+ '09 and Table 5 therein
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Hou09_TableA2.dat') ,'r')
    data=[];dataDum=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
          dataDum.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),values[6],values[7],float(values[8]),float(values[9]),float(values[10]),float(values[11]),float(values[12]),float(values[13]),float(values[14]),float(values[15]),float(values[16])])

    for i in range(len(dataDum)):
        l = dataDum[i][0];b = dataDum[i][1]; # deg
        Vlsr = dataDum[i][2] # km/s

	# exclude objects without Vlsr
	if(Vlsr == -100000):
	  continue

	# exclude galactic centre and anti-galactic centre as in Brand & Blitz 93
	if( (l >= 360 - 15 or l <= 15.) or abs(l - 180.) <= 15. ):
	  continue

        # select only objects with stellar distances
	if(dataDum[i][6] != 'stel'):
	  continue

        data.append([l, b, Vlsr, dataDum[i][4], 0.2*dataDum[i][4]]) # assume 20% distance error
    print '  selected ',len(data), ' out of the total sample of ', len(dataDum), ' giant molecular clouds'

    listvc=[];listpos=[];listraw=[];    
    for i in range(len(data)):
        l=data[i][0]*pi/180.;b=data[i][1]*pi/180.; # rad
        dprime=data[i][3];errdprime=data[i][4]; # kpc
        vlsrdata=data[i][2]; # km/s      
        errvlsrdata=3. # km/s, lacking better information assume 3 km/s error, which is typical
        errvlsrdata=pow(errvlsrdata,2.)+pow(SYSTDISP,2.) # add systematic to the error in vlsr
        errvlsrdata=pow(errvlsrdata,1./2.)

	listraw.append([vlsrdata, errvlsrdata, '-', '-', '-', '-', 'Hou09_TableA2']);

        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b);
        # transform back to LSR using new solar motion
        vlsr = functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr = errvlsrdata; # km/s
        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0)
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity        
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Hou09_TableA2']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][0], data[i][1]);
        listpos.append([Rp, dprime, data[i][0], data[i][1], vecpos[0], vecpos[1], vecpos[2], 'Hou09_TableA2']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)


# process data in Frinchaboy & Majewski 08. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagProperMotions. outputs: list of velocities, list of positions.
# proper motions not supported in current version
def ProcessFrinchaboyMajewski08(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions):
    inputfile1=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_FrinchaboyMajewski08_Table1.dat') ,'r')
    inputfile2=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_FrinchaboyMajewski08_Table12.dat') ,'r')
    dumdata1=[]
    dumdata2=[]
    data=[]

    i=0
    for line in inputfile1:
        i+=1
	values=line.split()	
        if(i>1):
          dumdata1.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),float(values[7]),values[8],float(values[9]),float(values[10]),float(values[11]),float(values[12]),float(values[13]),float(values[14]),float(values[15])])
    i=0
    for line in inputfile2:
        i+=1
	values=line.split()	
        if(i>1):
          dumdata2.append([values[0],float(values[1]),values[2],float(values[3]),float(values[4]), float(values[5]), float(values[6]),float(values[7]),float(values[8]),float(values[9]),float(values[10]),float(values[11]),float(values[12]),float(values[13]),float(values[14])])

    if len(dumdata1)!=len(dumdata2):
       print '*** error: check length of loaded tables...'

    # select appropriate clusters
    for i in range(len(dumdata1)):

        if (dumdata1[i][8]=='NGC1513' or dumdata1[i][8]=='NGC7654'): # cluster with one member only, see Sec 6.1
           continue
        if (dumdata1[i][8]=='Collinder258' or dumdata1[i][8]=='Lynga1' or dumdata1[i][8]=='NGC6250'): # cluster with probably wrong memberships, see Sec 6.2.3
           continue
        if (abs(dumdata1[i][1]-180.)<=20.): # exclude anti-centre region
           continue
        if (dumdata1[i][8]=='NGC6416'): # exclude cluster with high residual velocity (a posteriori)
           continue

        # search for open cluster in Table 12
        vel=[];propermotions=[]
        for j in range(len(dumdata2)):
            if (dumdata1[i][8]==dumdata2[j][0]):
               # use V_ {r, 3 D + RV} when possible, otherwise V_ {r, 3 D}
               if (dumdata2[j][5]==-100000):
                  vel.append([dumdata2[j][3],dumdata2[j][4]])
               if (dumdata2[j][5]!=-100000):
                  vel.append([dumdata2[j][5],dumdata2[j][6]])
               propermotions.append([dumdata2[j][11],dumdata2[j][12],dumdata2[j][13],dumdata2[j][14]])

        if len(vel)==0:
           print '*** error, cluster not found in Table 12...'

        data.append([dumdata1[i][0],dumdata1[i][1],dumdata1[i][2],dumdata1[i][8],dumdata1[i][15],vel,propermotions])
    print '  selected ', len(data), ' out of the total sample of ',len(dumdata1), ' open clusters'

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][1]*pi/180.;b=data[i][2]*pi/180.; # rad
        dprime=data[i][4]/1000.;errdprime=0.3*dprime; # kpc, assume 30 % error
        vh=data[i][5][0][0]; errvh=data[i][5][0][1]; # km/s
        errvh=pow(errvh,2.)+pow(SYSTDISP,2.)
        errvh=pow(errvh,1./2.)
        mulstar=data[i][6][0][0];errmulstar=data[i][6][0][1]; # mas/yr
        mub=data[i][6][0][2];errmub=data[i][6][0][3]; # mas/yr

	listraw.append([vh, errvh, mulstar, errmulstar, mub, errmub, 'FrinchaboyMajewski08']);

        # transform vh in vlsr
        vlsr=functions.LOSboostHelio2LSR(vh,UsunINUSE, VsunINUSE, WsunINUSE, l, b) # km/s
        errvlsr=errvh # km/s
 
        # compute dpprime, Rprime     
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp) using l.o.s.
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0)
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity        
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);
        
        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'FrinchaboyMajewski08']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][1], data[i][2]);
        listpos.append([Rp, dprime, data[i][1], data[i][2], vecpos[0], vecpos[1], vecpos[2], 'FrinchaboyMajewski08']); # Rp,Dp,l,b,X,Y,Z 

    return (listvc,listpos,listraw)

# process data in Durand+ 98. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessDurand98(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Durand98.dat') ,'r')
    checkfiletab1=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Zhang95_Table1.dat') ,'r')
    checkfiletab3=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Zhang95_Table3.dat') ,'r')
    data=[];dataZhangtab1=[];dataZhangtab3=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()
        if(i>1):
	  data.append([float(values[0]),float(values[1]),float(values[2]),values[3],float(values[len(values)-2]),float(values[len(values)-1])])

    i=0
    for line in checkfiletab1:
        i+=1
	values=line.split()	
        if(i>1):
          dataZhangtab1.append([float(values[0]),values[1],values[2],float(values[3]),float(values[4]),float(values[5]),values[6],values[7],float(values[8]),float(values[9]),float(values[10])])

    i=0
    for line in checkfiletab3:
        i+=1
	values=line.split()	
        if(i>1):
          dataZhangtab3.append([float(values[0]),values[1],values[2],float(values[3]),float(values[4]),float(values[5]),values[6],values[7],float(values[8]),float(values[9])])

    # select appropriate planetary nebulae
    list1 = [];
    # match distances from Zhang '95 to objects in Durand+ '98
    nfoundIndividualDist = 0; RelativeUncertaintyIndividualDist = 0.25;
    nfoundStatisticalDist = 0; RelativeUncertaintyStatisticalDist = 0.30;
    for i in range(len(data)):
        PNnametolookfororiginal = data[i][3] # planetary nebula name
        PNnametolookfor = (PNnametolookfororiginal.lower()).replace("-",""); # planetary nebula name
        l = data[i][1]*pi/180.;b = data[i][2]*pi/180.; # rad
        distvec = [];

        # look for distance individually determined (Table 1, Zhang '95)
        for j in range(len(dataZhangtab1)):
            PNnameoriginal = dataZhangtab1[j][1];
            PNname = (PNnameoriginal.lower()).replace("-","");
            if(PNname == PNnametolookfor):
              distvec.append([dataZhangtab1[j][3], dataZhangtab1[j][3]*RelativeUncertaintyIndividualDist]);
              nfoundIndividualDist+=1; break

        # if no distance was individually determined, search for statistical distance (Table 3, Zhang '95)
        if(len(distvec) == 0):
          for j in range(len(dataZhangtab3)):
              PNnameoriginal = dataZhangtab3[j][1];
              PNname = (PNnameoriginal.lower()).replace("-","");
              if(PNname == PNnametolookfor):
                distvec.append([dataZhangtab3[j][9],dataZhangtab3[j][9]*RelativeUncertaintyStatisticalDist]);
                nfoundStatisticalDist+=1; break

        if(len(distvec) == 0):
          continue

        if(len(distvec) > 1):
          print '*** error: check distance match for planetary nebulae...'
  
        # exclude 15 high-residual objects (see Section 5.2 in Zhang '95). Note typo on published text: NGC 6320 -> NGC 6302.
  	if(PNnametolookfor == "ngc6565" or PNnametolookfor == "m229" or PNnametolookfor == "m146" or PNnametolookfor == "sa18" or PNnametolookfor == "ngc6741" or PNnametolookfor == "ngc7293" or PNnametolookfor == "vy22" or PNnametolookfor == "ngc6720" or PNnametolookfor == "ngc7094" or PNnametolookfor == "ngc2392" or PNnametolookfor == "ngc4071" or PNnametolookfor == "ngc6026" or PNnametolookfor == "ngc6302" or PNnametolookfor == "m27" or PNnametolookfor == "th314"):
          continue
  
	# exclude BoBn 1, see Section 4.1 in Durand+'98
        if(PNnametolookfor == "bobn1"):
          continue
  
        # exclude |l|<=7deg or |z|>=200pc (see Section 4.2 in Durand+ '98)
        if(l <= 7.*pi/180. or l >= (360. - 7.)*pi/180. or abs(distvec[0][0]*sin(b)) >= 0.2):
	  continue
  
        # exclude objects with high velocity residuals a posteriori (probably the same as in Section 4.2 in Durand+ '98)
        if(PNnametolookfor == "ngc6567" or PNnametolookfor == "a8" or PNnametolookfor == "pu1" or PNnametolookfor == "m15"):
          continue
  
        elemaux = data[i]; elemaux.append(distvec[0][0]);elemaux.append(distvec[0][1]);
        list1.append(elemaux) # format: ID l b Name HelioVel(km/s) HelioVelUncert(km/s) Dist(kpc) DistUnc(kpc)

    # print '   found ', nfoundIndividualDist, ' planetary nebulae with individually determined distances out of a total sample of ', len(data), "|", len(dataZhangtab1);
    # print '   found ', nfoundStatisticalDist,' planetary nebulae with statistically determined distances out of a total sample of ',len(data), "|", len(dataZhangtab3);
    print '  selected ', len(list1),' out of the total sample of ', len(data),' planetary nebulae';
    data = list1;

    listvc=[];listpos=[];listraw=[];    
    for i in range(len(data)):
        l=data[i][1]*pi/180.;b=data[i][2]*pi/180.; # rad
        dprime=data[i][len(data[i])-2];errdprime=data[i][len(data[i])-1]; # kpc
        vh=data[i][len(data[i])-4];errvh=data[i][len(data[i])-3]; # km/s      
        errvh=pow(errvh,2.)+pow(SYSTDISP,2.) # add systematic to the error in vh
        errvh=pow(errvh,1./2.)

	listraw.append([vh, errvh, '-', '-', '-', '-', 'Durand98']);

        # transform vh in vlsr
        vlsr = functions.LOSboostHelio2LSR(vh, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        # take into account asymmetric drift, see Table 3
        Uad = 16.0 - UsunINUSE; errUad = 4.8; # km/s
        Vad = 24.8 - VsunINUSE; errVad = 3.8; # km/s
	vlsr = functions.LOSboostHelio2LSR(vlsr, Uad, Vad, 0., l, b);
	# subtract the mean K-term, see Table 3
	Kterm = 5.1; errKterm = 2.8; # km/s
	vlsr -= Kterm; # km/s
	errvlsr = errvh + errKterm + errUad*cos(l)*cos(b) + errVad*sin(l)*cos(b); # km/s

        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0)
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity        
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Durand98']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][1], data[i][2]);
        listpos.append([Rp, dprime, data[i][1], data[i][2], vecpos[0], vecpos[1], vecpos[2], 'Durand98']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Pont+ 94. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessPont94(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Pont94.dat') ,'r')
    data=[]
    
    i=0
    for line in inputfile:
        i+=1
        values=line.split()
        if(i>1):
          data.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6])])

    # select appropriate cepheid stars
    list1=[];
    for i in range(len(data)):
        # 12 stars with high residuals, see Sec. 11.4
        if (data[i][0]==335.2 and data[i][1]==-3.7) or (data[i][0]==286.9 and data[i][1]==0.6) or (data[i][0]==116.6 and data[i][1]==-1.1) or (data[i][0]==116.8 and data[i][1]==-1.3) or (data[i][0]==299.2 and data[i][1]==-0.6) or (data[i][0]==237.0 and data[i][1]==-1.3) or (data[i][0]==13.3 and data[i][1]==-2.4) or (data[i][0]==27.2 and data[i][1]==-0.4) or (data[i][0]==30.8 and data[i][1]==1.8) or (data[i][0]==276.6 and data[i][1]==-4.2) or (data[i][0]==259.8 and data[i][1]==-1.3) or (data[i][0]==271.5 and data[i][1]==-1.4):
           continue
        # 2 stars with high residulas according to our a posteriori calculations
        if (data[i][0]==1.6 and data[i][1]==-4.0) or (data[i][0]==354.4 and data[i][1]==0.2):
           continue
        # exclude anti - GC region as in Pont + ' 97
        if abs(data[i][0]-180.)<=20.:
           continue
        list1.append(data[i])

    print '  selected ', len(list1), ' out of the total sample of ', len(data), ' cepheids'
    data=list1

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180.; # rad
        b=data[i][1]*pi/180.; # rad
        muFW=data[i][4]; # kpc
        errmuFW=0.23 # kpc, assume 0.23 mag (see Sec. 11.3)
        vh=data[i][5]; errvh=pow(data[i][6],2.)+pow(11.1,2.);errvh=pow(errvh,1./2.); # km/s, see Sec. 11.3
        errvh=pow(errvh,2.)+pow(SYSTDISP,2.)
        errvh=pow(errvh,1./2.) # add systematic to the error in vh

	listraw.append([vh, errvh, '-', '-', '-', '-', 'Pont94']);

        # transform vh in vlsr 
        vlsr=functions.LOSboostHelio2LSR(vh, UsunINUSE,VsunINUSE,WsunINUSE,l,b); # km/s
        # subtract the mean K - term, see Sec. 11.6 (266 sample)
        Kterm=-1.81 # km/s
        vlsr-=Kterm # km/s
        errvlsr=errvh # km/s, ignore error on K - term
        # compute dprim, dpprime Rprime
        dprime=pow(10.,(muFW/5.+1.))/1.e3;errdprime=log(10.)/5.*dprime*errmuFW; # kpc definition of distance module
        dpp=dprime*cos(b);errdpp=errdprime*cos(b) # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp); # kpc
        # compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=abs(errvlsr/R0/(cos(b)*sin(l)))
        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Pont94'])
        vecpos=functions.XYZfromDlb(R0,dprime,data[i][0],data[i][1]);
        listpos.append([Rp,dprime,data[i][0],data[i][1],vecpos[0],vecpos[1],vecpos[2], 'Pont94']) # Rp, Dp, l, b, X, Y, Z
    return (listvc,listpos,listraw)

# process data in Pont+ 97. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessPont97(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Pont97.dat') ,'r')
    data=[]

    i=0
    for line in inputfile:
        i+=1
        values=line.split()
        if(i>1):
          data.append([values[0],float(values[1]),float(values[2]),float(values[3]),float(values[4]),values[5],values[6],values[7],values[8],values[9],values[10],values[11]])

    # select appropriate cepheid stars
    list1=[];
    for i in range(len(data)):
        # exclude stars with no B-V
        if (data[i][5]=='-'):
           continue
        # exclude stars with no Vr
        if (data[i][9]=='-'):
           continue
        # exclude anti - GC region
        if abs(data[i][1]-180.)<=20.:
           continue
        list1.append(data[i])

    print '  selected ', len(list1), ' out of the total sample of ', len(data), ' cepheids'
    data=list1

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][1]*pi/180.;b=data[i][2]*pi/180.; # rad
        Period=data[i][3];colorV=data[i][4];colorBmV=float(data[i][5]);
        colorBmV0 = 0.314 + 0.416*log10(Period); # second equation in Sec. 3.1 without metallicity correction
        ExcessBmV = colorBmV - colorBmV0;
        parR = 3.06 + 0.25*colorBmV0 +0.05*ExcessBmV; # see Pont+ '94, Eq. 5, Sec. 8
        MagcolorV = -3.80*log10(Period) + 2.70*colorBmV0 - 2.27; # see Pont+ '94, Eq. 3, Sec. 8
        muFW = colorV - parR*ExcessBmV - MagcolorV; errmuFW = 0.21; # kpc, assume 0.21mag (see Sec. 3.3), use FW distance as in Pont+ '94, Sec. 8
        vh = float(data[i][9])
        sigma1=2.5; # km/s, take sigma1 to be 1.0 km/s if n_mes (Vr) >=  10 and 2.5 km/s otherwise
        if(float(data[i][11])>=10):
            sigma1=1.
        errvh=pow(sigma1,2.)+pow(11.1,2.) # km/s, see Sec. 11.3 of Pont + 94
        errvh=pow(errvh,1./2.)
        errvh=pow(errvh,2.)+pow(SYSTDISP,2.)
        errvh=pow(errvh,1./2.) # add systematic to the error in vh

	listraw.append([vh, errvh, '-', '-', '-', '-', 'Pont97']);

        # transform vh in vlsr
        vlsr=functions.LOSboostHelio2LSR(vh, UsunINUSE,VsunINUSE,WsunINUSE,l,b); # km/s
        errvlsr=errvh#km/s, ignore error on K - term
        # compute dprim, dpprime Rprime
        dprime=pow(10.,(muFW/5.+1.))/1.e3;errdprime=log(10.)/5.*dprime*errmuFW; # kpc, definition of distance module
        dpp=dprime*cos(b);errdpp=errdprime*cos(b)  # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp); # kpc
        # compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.)+pow(6.,2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=pow(errvlsr/R0/(cos(b)*sin(l)),2.)+pow(6./Rp,2.)
        errwRp=pow(errwRp,1./2.)
        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Pont97'])
        vecpos=functions.XYZfromDlb(R0,dprime,data[i][1],data[i][2]);
        listpos.append([Rp,dprime,data[i][1],data[i][2],vecpos[0],vecpos[1],vecpos[2], 'Pont97']) # Rp, Dp, l, b, X, Y, Z
    return (listvc,listpos,listraw) 

# process data in Demers & Battinelli 07. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessDemersBattinelli07(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfiletab1=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_DemersBattinelli07_Table1.dat') ,'r')
    inputfiletab4=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_DemersBattinelli07_Table4.dat') ,'r')
    datatab1=[];datatab4=[];

    i=0
    for line in inputfiletab1:
        i+=1
	values=line.split()
        if(i>1):
	  datatab1.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),values[6],values[7],float(values[8]),float(values[9]),float(values[10]),float(values[11]),float(values[12]),float(values[13]),float(values[14])])

    i=0
    for line in inputfiletab4:
        i+=1
	values=line.split()
        if(i>1):
	  datatab4aux=[];
          datatab4aux.append(float(values[0]));datatab4aux.append(float(values[1]));datatab4aux.append(float(values[2]));datatab4aux.append(values[3]);datatab4aux.append(values[4]);datatab4aux.append(values[5]);
	  if(len(values)>=6):
	    for j in range(6,len(values)):
                datatab4aux.append(values[j]);
	  datatab4.append(datatab4aux)

    # select appropriate C stars
    list1 = []; list4 = [];
    for i in range(len(datatab4)):
        if(datatab4[i][3] == "-"):
	  continue # stars not observed
        if(datatab4[i][len(datatab4[i])-4] == "not" and datatab4[i][len(datatab4[i])-3] == "a" and datatab4[i][len(datatab4[i])-2] == "C" and datatab4[i][len(datatab4[i])-1] == "star"):
	  continue # stars that are not C stars
        if(abs(datatab4[i][1] - 180.) <= 10.):
          continue # stars near anti-GC, see caption Fig. 6
        if(datatab4[i][0] == 20 or datatab4[i][0] == 23):
          continue # nearby fast stars probably do not belong to the thin nor thick disks, see Sec. 5.2
        if(datatab4[i][0] == 17 or datatab4[i][0] == 18 or datatab4[i][0] == 27 or datatab4[i][0] == 28 or datatab4[i][0] == 35 or datatab4[i][0] == 42 or datatab4[i][0] == 52 or datatab4[i][0] == 56 or  datatab4[i][0] == 58 or datatab4[i][0] == 60):
	  continue # ten stars that possibly belong to Canis Major and have high VLSR, see Sec. 5.2
      
        list1.append(datatab1[i]);
        list4.append(datatab4[i]);

    print '  selected ', len(list4), ' out of the total sample of ',len(datatab4), ' C stars'
    datatab1 = list1;datatab4 = list4;

    listvc=[];listpos=[];listraw=[];    
    for i in range(len(datatab4)):
        l=datatab4[i][1]*pi/180.;b=datatab4[i][2]*pi/180.; # rad
        dprime=datatab1[i][len(datatab1[i])-3];errdprime=0.1*dprime; # kpc, assume 10 % error in distance (see Sec. 5.1)
        vh=float(datatab4[i][3]);errvh=float(datatab4[i][4]); # km/s      
        errvh=pow(errvh,2.)+pow(SYSTDISP,2.) # add systematic to the error in vh
        errvh=pow(errvh,1./2.)

	listraw.append([vh, errvh, '-', '-', '-', '-', 'DemersBattinelli07']);

        # transform vh in vlsr
        vlsr = functions.LOSboostHelio2LSR(vh, UsunINUSE, VsunINUSE, WsunINUSE, l, b); errvlsr = errvh; # km/s
        errvlsr = pow(errvlsr,2.) + pow(20.,2.) # add random motion error of 20km/s, see Sec 5.1
	errvlsr = pow(errvlsr,1./2.)

        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0)
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity        
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'DemersBattinelli07']);
        vecpos = functions.XYZfromDlb(R0, dprime, datatab4[i][1], datatab4[i][2]);
        listpos.append([Rp, dprime, datatab4[i][1], datatab4[i][2], vecpos[0], vecpos[1], vecpos[2], 'DemersBattinelli07']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Battinelli 12. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s. outputs: list of velocities, list of positions.
def ProcessBattinelli12(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP):
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Battinelli12.dat') ,'r')
    data=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()
        if(i>1):
	  data.append([float(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5])])

    # select appropriate C stars
    list1 = [];
    for i in range(len(data)):
        if(data[i][0] == 712):
	  continue # star 712 is likely from Sagittarius dwarf galaxy, see Sec. 4      
        list1.append(data[i]);

    print '  selected ', len(list1), ' out of the total sample of ',len(data), ' C stars'
    data = list1;

    listvc=[];listpos=[];listraw=[];    
    for i in range(len(data)):
        l=data[i][1]*pi/180.;b=data[i][2]*pi/180.; # rad

        Rprimedata = data[i][3] # kpc, this was computed assuming R0=7.62 kpc 
 	# need to solve for heliocentric distance: Rprimedata = Rprime(7.62, dpx*cos(b), l), this is quadratic in dpx
	sol=[(7.62*cos(l) - pow(pow(7.62*cos(l),2.)-7.62*7.62 + Rprimedata*Rprimedata,1./2.))/cos(b) , (7.62*cos(l) + pow(pow(7.62*cos(l),2.)-7.62*7.62 + Rprimedata*Rprimedata,1./2.))/cos(b) ]
	if(min(sol) > 0):
	  print '*** error: check calculation of heliocentric distance - two positive solutions found!'
	dprime = max(sol); # kpc
	if(dprime <= 0):
	  print '*** error: check calculation of heliocentric distance'
 	errdprime=0.1*dprime; # kpc, assume 10 % error in distance (see Sec. 5.1 of Demers & Battinelli ' 07)

        vh=data[i][4];errvh=data[i][5]; # km/s      
        errvh=pow(errvh,2.)+pow(SYSTDISP,2.) # add systematic to the error in vh
        errvh=pow(errvh,1./2.)

	listraw.append([vh, errvh, '-', '-', '-', '-', 'Battinelli12']);

        # transform vh in vlsr
        vlsr = functions.LOSboostHelio2LSR(vh, UsunINUSE, VsunINUSE, WsunINUSE, l, b); errvlsr = errvh; # km/s
        errvlsr = pow(errvlsr,2.) + pow(20.,2.) # add random motion error of 20km/s, see Sec 5.1 of Demers & Battinelli ' 07
	errvlsr = pow(errvlsr,1./2.)

        # compute dpprime, Rprime
        dpp = dprime*cos(b); errdpp =errdprime*cos(b); # kpc
        Rp =functions.Rprime(R0, dpp, l);
        errRp = (1./(2.*Rp)*abs(2.*dpp - 2.*R0*cos(l)))* errdpp; # kpc
        # compute the velocity v(Rp)
        vRp =(Rp/R0)*(vlsr/(cos(b)*sin(l)) +V0)
        errvRp=(errRp/R0)*(V0+vlsr/(cos(b)*sin(l)))
        errvRp=pow(errvRp,2.)
        errvRp+=pow((errvlsr*(Rp/R0)*pow((cos(b)*sin(l)),-1.)),2.)
        errvRp=pow(errvRp,1./2.)
        # computing angular velocity        
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0; errwRp=abs(errvlsr/(cos(b)*sin(l))/R0);

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Battinelli12']);
        vecpos = functions.XYZfromDlb(R0, dprime, data[i][1], data[i][2]);
        listpos.append([Rp, dprime, data[i][1], data[i][2], vecpos[0], vecpos[1], vecpos[2], 'Battinelli12']); # Rp,Dp,l,b,X,Y,Z 
    return (listvc,listpos,listraw)

# process data in Reid+ 14. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagProperMotions. outputs: list of velocities, list of positions.
# proper motions not supported in current version
def ProcessReid14(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,SigmaVirMasers, flagastropy):
    if(flagastropy==1):
      from astropy.coordinates import SkyCoord

    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s
    Uscr = 2.9; Vscr = VsunINUSE - 17.1; Wscr = 0.; # km/s, check Table 4 and page 18
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Reid14.dat') ,'r')
    data=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()
        if(i>1):
	  data.append([float(values[0]),values[1], values[2], float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9]), float(values[10]), float(values[11]), float(values[12]), float(values[13]), float(values[14]), float(values[15]), float(values[16]),values[17]])

    # select appropriate masers
    list1 = [];
    for i in range(len(data)):
        if(data[i][0] == 1):
	  continue # masers with R < 4 kpc, see footnote 3
        if(data[i][0] == 2):
	  continue # outlier masers, see footnote 4
        list1.append(data[i]);

    print '  selected ', len(list1), ' out of the total sample of ',len(data), ' masers'
    data = list1;

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        alpha = (data[i][3]*(360./24.) + data[i][4]*(360./(24*60)) + data[i][5]*(360./(24*60*60)))*pi/180.; # rad
        delta= sign(data[i][6])*(abs(data[i][6]) + data[i][7]*(1./60.) + data[i][8]*(1./(60*60)))*pi/180.; # rad
	veclb= functions.equatorialTOgalactic(alpha, delta);l=veclb[0];b=veclb[1]; # rad
        if(flagastropy==1): coord = SkyCoord(alpha,delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion
        
	parallax = data[i][9]; errparallax =data[i][10] # mas
        dprime = functions.DfromPi(parallax); errdprime =errparallax/pow(parallax,2.); # kpc
        vlsrdata = data[i][15]; errvlsrdata = data[i][16]; # km/s
        errvlsrdata=pow(errvlsrdata,2.)+pow(SigmaVirMasers,2.)+pow(SYSTDISP,2.)
        errvlsrdata=pow(errvlsrdata,1./2.) # add systematic and virial motion to the error in vlsr
        mualphastar = data[i][11]; errmualphastar =  data[i][12]; # mas/yr
        errmualphastar=pow(pow(errmualphastar,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 
        mudelta = data[i][13]; errmudelta = data[i][14]; # mas/yr
        errmudelta=pow(pow(errmudelta,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 

	# convert the equatorial proper motions to galactic ones
	vecmulstarb = functions.equatorialTOgalacticProperMotions(alpha, delta, mualphastar, mudelta) # mas/yr
	mulstar = vecmulstarb[0]; mub = vecmulstarb[1]; # mas/yr
	vecerrmus = functions.equatorialTOgalacticProperMotionsErrors(alpha, delta, errmualphastar,errmudelta, 0.) # mas/yr, assume 0 correlation
	errmulstar = vecerrmus[0]; errmub = vecerrmus[1]; # mas/yr


	listraw.append([vlsrdata, errvlsrdata, mulstar, errmulstar, mub, errmub, 'Reid14']);
         
        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b); # km/s
        # transform back to LSR using new solar motion
        vlsr1= functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr1= errvlsrdata; # km/s
        # now correct for the mean peculiar motion of the maser sources - we are interested in the standard of rest
        vlsr = functions.LOSLSRminusPeculiar(vlsr1, Uscr, Vscr, Wscr, R0, l, b,dprime*cos(b)); errvlsr = errvlsr1; # km/s

 	# compute dpprime, Rprime
        dpp=dprime*cos(b);errdpp=errdprime*cos(b) # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp);# kpc
        #compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=abs(errvlsr/R0/(cos(b)*sin(l)))

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Reid14'])
	vecpos = functions.XYZfromDlb(R0, dprime, l*180./pi, b*180./pi);
	listpos.append([Rp, dprime, l*180./pi, b*180./pi, vecpos[0], vecpos[1], vecpos[2], 'Reid14']) # Rp,Dp,l,b,X,Y,Z 

    return (listvc,listpos,listraw)

# process data in Honma+ 12. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagProperMotions,flagReid14. outputs: list of velocities, list of positions.
# proper motions not supported in current version
def ProcessHonma12(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,flagReid14,SigmaVirMasers, flagastropy):
    if(flagastropy==1):
      from astropy.coordinates import SkyCoord

    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s
    #Uscr = 0.95; Vscr = VsunINUSE - 19.; Wscr = -1.41; # km/s, check Table 7
    Uscr = 2.9; Vscr = VsunINUSE - 17.1; Wscr = 0.; # km/s, check Table 4 and page 18  # use the Reid+ '14 measurement (26.05.2016)
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Honma12.dat') ,'r')
    checkfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Reid14.dat') ,'r')  
    dumdata=[];dumcheck=[];data=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()
        if(i>1):
	  dumdata.append([float(values[0]),float(values[1]), float(values[2]), float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9])])

    i=0
    for line in checkfile:
        i+=1
	values=line.split()	
        if(i>1):
          dumcheck.append([float(values[0]),values[1], values[2], float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9]), float(values[10]), float(values[11]), float(values[12]), float(values[13]), float(values[14]), float(values[15]), float(values[16]),values[17]])

    list1=dumdata;
    if(flagReid14 == 1): # select only those not in Reid+ '14
      list1 = [];
      for i in range(len(dumdata)):
	  l1 = dumdata[i][0]; b1 = dumdata[i][1]; # deg
          # search for this object in Reid+ '14
          nfound = 0;
          for j in range(len(dumcheck)):
	      alpha = (dumcheck[j][3]*(360./24.) + dumcheck[j][4]*(360./(24.*60.)) + dumcheck[j][5]*(360./(24.*60.*60.)))*pi/180.; # rad
    	      delta = sign(dumcheck[j][6])*(abs(dumcheck[j][6]) + dumcheck[j][7]*(1./60.) + dumcheck[j][8]*(1./(60.*60.)))*pi/180.; # rad
    	      veclb = functions.equatorialTOgalactic(alpha, delta); l = veclb[0]*180./pi; b = veclb[1]*180./pi; # deg
              #if(flagastropy==1): coord = SkyCoord(alpha,delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion

  	      if( abs(l - l1) <= 0.01 and abs(b - b1) <= 0.01):
	        nfound+=1
          if(nfound > 1):
	    print '*** warning: found more than 1 coincidence!'
          if(nfound == 0):
	    list1.append(dumdata[i])
    print '  selected ', len(list1), ' out of the total sample of ',len(dumdata), ' masers'
    data=list1;

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][0]*pi/180.;b=data[i][1]*pi/180.; # rad
	vecad = functions.galacticTOequatorial(l, b);alpha = vecad[0];delta=vecad[1]; # rad  
        if(flagastropy==1): coord = SkyCoord(l,b, frame='galactic', unit='rad'); alpha = coord.icrs.ra.rad; delta = coord.icrs.dec.rad; # astropy conversion

	parallax = data[i][2]; errparallax =data[i][3] # mas
        dprime = functions.DfromPi(parallax); errdprime =errparallax/pow(parallax,2.); # kpc
        vlsrdata = data[i][4]; errvlsrdata = data[i][5]; # km/s
        errvlsrdata=pow(errvlsrdata,2.)+pow(SigmaVirMasers,2.)+pow(SYSTDISP,2.)
        errvlsrdata=pow(errvlsrdata,1./2.) # add systematic and virial motion to the error in vlsr
        mualphastar = data[i][6]; errmualphastar =  data[i][7]; # mas/yr
        errmualphastar=pow(pow(errmualphastar,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 
        mudelta = data[i][8]; errmudelta = data[i][9]; # mas/yr
        errmudelta=pow(pow(errmudelta,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 

	# convert the equatorial proper motions to galactic ones
	vecmulstarb = functions.equatorialTOgalacticProperMotions(alpha, delta, mualphastar, mudelta) # mas/yr
	mulstar = vecmulstarb[0]; mub = vecmulstarb[1]; # mas/yr
	vecerrmus = functions.equatorialTOgalacticProperMotionsErrors(alpha, delta, errmualphastar,errmudelta, 0.) # mas/yr, assume 0 correlation
	errmulstar = vecerrmus[0]; errmub = vecerrmus[1]; # mas/yr

	listraw.append([vlsrdata, errvlsrdata, mulstar, errmulstar, mub, errmub, 'Honma12']);
             
        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b); # km/s
        # transform back to LSR using new solar motion
        vlsr1= functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr1= errvlsrdata; # km/s
        # now correct for the mean peculiar motion of the maser sources - we are interested in the standard of rest
        vlsr = functions.LOSLSRminusPeculiar(vlsr1, Uscr, Vscr, Wscr, R0, l, b,dprime*cos(b)); errvlsr = errvlsr1; # km/s

 	# compute dpprime, Rprime
        dpp=dprime*cos(b);errdpp=errdprime*cos(b) # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp);# kpc
        #compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=abs(errvlsr/R0/(cos(b)*sin(l)))

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Honma12'])
	vecpos = functions.XYZfromDlb(R0, dprime, data[i][0],data[i][1]);
	listpos.append([Rp, dprime, data[i][0], data[i][1], vecpos[0], vecpos[1], vecpos[2], 'Honma12']) # Rp,Dp,l,b,X,Y,Z 

    return (listvc,listpos,listraw)

# process data in Stepanischchev & Bobylev 11. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagProperMotions,flagReid14. outputs: list of velocities, list of positions.
# proper motions not supported in current version
def ProcessStepanishchevBobylev11(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,flagReid14,SigmaVirMasers, flagastropy):
    if(flagastropy==1):
      from astropy.coordinates import SkyCoord

    inputfile1=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_StepanishchevBobylev11_Table1.dat') ,'r')
    inputfile2=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_StepanishchevBobylev11_Table2.dat') ,'r')
    checkfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Reid14.dat') ,'r')
    dumdata1=[];dumdata2=[];dumcheck=[];data=[];data2=[];

    i=0
    for line in inputfile1:
        i+=1
	values=line.split()	
        if(i>1):
          dumdata1.append([values[0],float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),float(values[7]),float(values[8]),float(values[9]),float(values[10])])
 
    i=0
    for line in inputfile2:
        i+=1
	values=line.split()	
        if(i>1):
          dumdata2.append([values[0],float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),float(values[7]),float(values[8])])

    i=0
    for line in checkfile:
        i+=1
	values=line.split()	
        if(i>1):
          dumcheck.append([float(values[0]),values[1], values[2], float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9]), float(values[10]), float(values[11]), float(values[12]), float(values[13]), float(values[14]), float(values[15]), float(values[16]),values[17]])

    list1=dumdata1;list2=dumdata2;
    if(flagReid14 == 1): # select only those not in Reid+ '14
      list1 = [];
      for i in range(len(dumdata1)):
	  a1 = dumdata1[i][1]*pi/180.;d1 = dumdata1[i][2]*pi/180.; # rad
          veclb1 = functions.equatorialTOgalactic(a1, d1); l1 = veclb1[0]*180./pi; b1 = veclb1[1]*180./pi; # deg
          if(flagastropy==1): coord = SkyCoord(a1,d1, frame='icrs', unit='rad'); l1 = coord.galactic.l.rad; b1 = coord.galactic.b.rad; # astropy conversion

          # search for this object in Reid+ '14
          nfound = 0;
          for j in range(len(dumcheck)):
	      alpha = (dumcheck[j][3]*(360./24.) + dumcheck[j][4]*(360./(24.*60.)) + dumcheck[j][5]*(360./(24.*60.*60.)))*pi/180.; # rad
    	      delta = sign(dumcheck[j][6])*(abs(dumcheck[j][6]) + dumcheck[j][7]*(1./60.) + dumcheck[j][8]*(1./(60.*60.)))*pi/180.; # rad
    	      veclb = functions.equatorialTOgalactic(alpha, delta); l = veclb[0]*180./pi; b = veclb[1]*180./pi; # deg
              #if(flagastropy==1): coord = SkyCoord(alpha,delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion

  	      if(abs(l - l1) <= 0.01 and abs(b - b1) <= 0.01):
	        nfound+=1
          if(nfound > 1):
	    print '*** warning: found more than 1 coincidence!'
          if(nfound == 0):
	    list1.append(dumdata1[i])
    print '  selected ', len(list1), ' out of the total sample of ',len(dumdata1), ' masers'
    data=list1;data2=list2;

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        alpha = data[i][1]*pi/180.; delta = data[i][2]*pi/180.; # rad
        veclb= functions.equatorialTOgalactic(alpha, delta);l=veclb[0];b=veclb[1]; # rad
        if(flagastropy==1): coord = SkyCoord(alpha,delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion
        
	parallax = data[i][3]; errparallax =data[i][4] # mas
        dprime = functions.DfromPi(parallax); errdprime =errparallax/pow(parallax,2.); # kpc
        vh = data[i][9]; errvh = data[i][10]; # km/s
        errvh=pow(errvh,2.)+pow(SigmaVirMasers,2.)+pow(SYSTDISP,2.)
        errvh=pow(errvh,1./2.) # add systematic and virial motion to the error in vh
        mualphastar = data[i][5]; errmualphastar =  data[i][6]; # mas/yr
        errmualphastar=pow(pow(errmualphastar,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 
        mudelta = data[i][7]; errmudelta = data[i][8]; # mas/yr
        errmudelta=pow(pow(errmudelta,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 

	# convert the equatorial proper motions to galactic ones
	vecmulstarb = functions.equatorialTOgalacticProperMotions(alpha, delta, mualphastar, mudelta) # mas/yr
	mulstar = vecmulstarb[0]; mub = vecmulstarb[1]; # mas/yr
	vecerrmus = functions.equatorialTOgalacticProperMotionsErrors(alpha, delta, errmualphastar,errmudelta, 0.) # mas/yr, assume 0 correlation
	errmulstar = vecerrmus[0]; errmub = vecerrmus[1]; # mas/yr

	listraw.append([vh, errvh, mulstar, errmulstar, mub, errmub, 'StepanishchevBobylev11']);

     	Uscr = data2[i][2]; # km/s
	Vscr = data2[i][4]; # km/s
	Wscr = data2[i][6]; # km/s
        Uscr = 2.9; Vscr = VsunINUSE - 17.1; Wscr = 0.; # km/s, check Table 4 and page 18  # use the Reid+ '14 measurement (26.05.2016)

	# transform vh to LSR using new solar motion
	vlsr1 = functions.LOSboostHelio2LSR(vh, UsunINUSE, VsunINUSE, WsunINUSE, l, b);errvlsr1 = errvh; # km/s
	# now correct for the mean peculiar motion of the maser sources - we are interested in the standard of rest
        vlsr = functions.LOSLSRminusPeculiar(vlsr1, Uscr, Vscr, Wscr, R0, l, b,dprime*cos(b)); errvlsr = errvlsr1; # km/s
              
 	# compute dpprime, Rprime
        dpp=dprime*cos(b);errdpp=errdprime*cos(b) # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp);# kpc
        #compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=abs(errvlsr/R0/(cos(b)*sin(l)))

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'StepanishchevBobylev11'])
	vecpos = functions.XYZfromDlb(R0, dprime, l*180./pi, b*180./pi);
	listpos.append([Rp, dprime, l*180./pi, b*180./pi, vecpos[0], vecpos[1], vecpos[2], 'StepanishchevBobylev11']) # Rp,Dp,l,b,X,Y,Z 

    return (listvc,listpos,listraw)

# process data in Xu+ 13. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagProperMotions,flagReid14. outputs: list of velocities, list of positions.
# proper motions not supported in current version
def ProcessXu13(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,flagReid14,SigmaVirMasers, flagastropy):
    if(flagastropy==1):
      from astropy.coordinates import SkyCoord

    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s
    Uscr = 2.9; Vscr = VsunINUSE - 17.1; Wscr = 0.; # km/s, check Table 4 and page 18 in Reid+ '14
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Xu13.dat') ,'r')
    checkfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Reid14.dat') ,'r')  
    dumdata=[];dumcheck=[];data=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()
        if(i>1):
	  dumdata.append([values[0],float(values[1]), float(values[2]), float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9]),float(values[10])])

    i=0
    for line in checkfile:
        i+=1
	values=line.split()	
        if(i>1):
          dumcheck.append([float(values[0]),values[1], values[2], float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9]), float(values[10]), float(values[11]), float(values[12]), float(values[13]), float(values[14]), float(values[15]), float(values[16]),values[17]])

    list1=dumdata;
    if(flagReid14 == 1): # select only those not in Reid+ '14
      list1 = [];
      for i in range(len(dumdata)):
	  l1 = dumdata[i][1]; b1 = dumdata[i][2]; # deg
          # search for this object in Reid+ '14
          nfound = 0;
          for j in range(len(dumcheck)):
	      alpha = (dumcheck[j][3]*(360./24.) + dumcheck[j][4]*(360./(24.*60.)) + dumcheck[j][5]*(360./(24.*60.*60.)))*pi/180.; # rad
    	      delta = sign(dumcheck[j][6])*(abs(dumcheck[j][6]) + dumcheck[j][7]*(1./60.) + dumcheck[j][8]*(1./(60.*60.)))*pi/180.; # rad
    	      veclb = functions.equatorialTOgalactic(alpha, delta); l = veclb[0]*180./pi; b = veclb[1]*180./pi; # deg
              #if(flagastropy==1): coord = SkyCoord(alpha,delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion

  	      if( abs(l - l1) <= 0.01 and abs(b - b1) <= 0.01):
	        nfound+=1
          if(nfound > 1):
	    print '*** warning: found more than 1 coincidence!'
          if(nfound == 0):
	    list1.append(dumdata[i])
    print '  selected ', len(list1), ' out of the total sample of ',len(dumdata), ' masers'
    data=list1;

    # select only those not in Honma+ '12
    list1 = [];
    for i in range(len(data)):
        if(data[i][0] != "G074.03-01.71" and data[i][0] != "G075.76+00.33" and data[i][0] != "G076.38-00.61" and data[i][0] != "G079.87+01.17" and data[i][0] != "NMLCyg" and data[i][0] != "G090.21+02.32" and data[i][0] != "G092.67+03.07" and data[i][0] != "G105.41+09.87" and data[i][0] != "Oriond" and data[i][0] != "DoAr21/Ophiuchus"):
	  continue
	list1.append(data[i]);
    print '  selected ', len(list1), ' out of the total sample of ',len(data), ' masers'
    data=list1;

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        l=data[i][1]*pi/180.;b=data[i][2]*pi/180.; # rad
	vecad = functions.galacticTOequatorial(l, b);alpha = vecad[0];delta=vecad[1]; # rad  
        if(flagastropy==1): coord = SkyCoord(l,b, frame='galactic', unit='rad'); alpha = coord.icrs.ra.rad; delta = coord.icrs.dec.rad; # astropy conversion
	parallax = data[i][3]; errparallax =data[i][4] # mas
        dprime = functions.DfromPi(parallax); errdprime =errparallax/pow(parallax,2.); # kpc
        vlsrdata = data[i][9]; errvlsrdata = data[i][10]; # km/s
        errvlsrdata=pow(errvlsrdata,2.)+pow(SigmaVirMasers,2.)+pow(SYSTDISP,2.)
        errvlsrdata=pow(errvlsrdata,1./2.) # add systematic and virial motion to the error in vlsr
        mualphastar = data[i][5]; errmualphastar =  data[i][6]; # mas/yr
        errmualphastar=pow(pow(errmualphastar,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 
        mudelta = data[i][7]; errmudelta = data[i][8]; # mas/yr
        errmudelta=pow(pow(errmudelta,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 

	# convert the equatorial proper motions to galactic ones
	vecmulstarb = functions.equatorialTOgalacticProperMotions(alpha, delta, mualphastar, mudelta) # mas/yr
	mulstar = vecmulstarb[0]; mub = vecmulstarb[1]; # mas/yr
	vecerrmus = functions.equatorialTOgalacticProperMotionsErrors(alpha, delta, errmualphastar,errmudelta, 0.) # mas/yr, assume 0 correlation
	errmulstar = vecerrmus[0]; errmub = vecerrmus[1]; # mas/yr

	listraw.append([vlsrdata, errvlsrdata, mulstar, errmulstar, mub, errmub, 'Xu13']);
             
        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b); # km/s
        # transform back to LSR using new solar motion
        vlsr1= functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr1= errvlsrdata; # km/s
        # now correct for the mean peculiar motion of the maser sources - we are interested in the standard of rest
        vlsr = functions.LOSLSRminusPeculiar(vlsr1, Uscr, Vscr, Wscr, R0, l, b,dprime*cos(b)); errvlsr = errvlsr1; # km/s

 	# compute dpprime, Rprime
        dpp=dprime*cos(b);errdpp=errdprime*cos(b) # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp);# kpc
        #compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=abs(errvlsr/R0/(cos(b)*sin(l)))

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'Xu13'])
	vecpos = functions.XYZfromDlb(R0, dprime,data[i][1], data[i][2]);
	listpos.append([Rp, dprime, data[i][1], data[i][2], vecpos[0], vecpos[1], vecpos[2], 'Xu13']) # Rp,Dp,l,b,X,Y,Z 

    return (listvc,listpos,listraw)

# process data in Bobylev & Bajkova 13. inputs: R0 in kpc, V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP in km/s, flagProperMotions,flagReid14. outputs: list of velocities, list of positions.
# proper motions not supported in current version
def ProcessBobylevBajkova13(R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP,flagProperMotions,flagReid14,SigmaVirMasers, flagastropy):
    if(flagastropy==1):
      from astropy.coordinates import SkyCoord

    UsunData = 10.3; VsunData = 15.3; WsunData = 7.7; # km/s
    Uscr = 2.9; Vscr = VsunINUSE - 17.1; Wscr = 0.; # km/s, check Table 4 and page 18 in Reid+ '14
    inputfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_BobylevBajkova13.dat') ,'r')
    checkfile=open( os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/data_Reid14.dat') ,'r')
    dumdata=[];dumcheck=[];data=[];

    i=0
    for line in inputfile:
        i+=1
	values=line.split()	
        if(i>1):
          dumdata.append([values[0],float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),float(values[7]),float(values[8]),float(values[9]),float(values[10]),float(values[11])])

    i=0
    for line in checkfile:
        i+=1
	values=line.split()	
        if(i>1):
          dumcheck.append([float(values[0]),values[1], values[2], float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7]), float(values[8]), float(values[9]), float(values[10]), float(values[11]), float(values[12]), float(values[13]), float(values[14]), float(values[15]), float(values[16]),values[17]])

    list1=dumdata;
    if(flagReid14 == 1): # select only those not in Reid+ '14
      list1 = [];
      for i in range(len(dumdata)):
	  a1 = dumdata[i][1]*pi/180.;d1 = dumdata[i][2]*pi/180.; # rad
          veclb1 = functions.equatorialTOgalactic(a1, d1); l1 = veclb1[0]*180./pi; b1 = veclb1[1]*180./pi; # deg
          #if(flagastropy==1): coord = SkyCoord(a1, d1, frame='icrs', unit='rad'); l1 = coord.galactic.l.rad; b1 = coord.galactic.b.rad; # astropy conversion

          # search for this object in Reid+ '14
          nfound = 0;
          for j in range(len(dumcheck)):
	      alpha = (dumcheck[j][3]*(360./24.) + dumcheck[j][4]*(360./(24.*60.)) + dumcheck[j][5]*(360./(24.*60.*60.)))*pi/180.; # rad
    	      delta = sign(dumcheck[j][6])*(abs(dumcheck[j][6]) + dumcheck[j][7]*(1./60.) + dumcheck[j][8]*(1./(60.*60.)))*pi/180.; # rad
    	      veclb = functions.equatorialTOgalactic(alpha, delta); l = veclb[0]*180./pi; b = veclb[1]*180./pi; # deg
              #if(flagastropy==1): coord = SkyCoord(alpha, delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion

  	      if(abs(l - l1) <= 0.01 and abs(b - b1) <= 0.01):
	        nfound+=1
          if(nfound > 1):
	    print '*** warning: found more than 1 coincidence!'
          if(nfound == 0):
	    list1.append(dumdata[i])
    print '  selected ', len(list1), ' out of the total sample of ',len(dumdata), ' masers'
    data=list1;

    # select only those not in Honma+ '12
    list1 = [];
    for i in range(len(data)):
        if(data[i][0] != "IRAS20143+36" and data[i][0] != "PZCas" and data[i][0] != "IRAS22480+60" and data[i][0] != "RCW122" and data[i][0] != "HDE283572" and data[i][0] != "V773TauAB" and data[i][0] != "W33Af1" and data[i][0] != "W33Af2" and data[i][0] != "W33Mainf2" and data[i][0] != "IRAS05137+39" and data[i][0] != "CygX-1" and data[i][0] != "SgrB2N" and data[i][0] != "SgrB2M"):
	  continue
	list1.append(data[i]);
    print '  selected ', len(list1), ' out of the total sample of ',len(data), ' masers'
    data=list1;

    listvc=[];listpos=[];listraw=[];
    for i in range(len(data)):
        alpha = data[i][1]*pi/180.; delta = data[i][2]*pi/180.; # rad
        veclb= functions.equatorialTOgalactic(alpha, delta);l=veclb[0];b=veclb[1]; # rad
        if(flagastropy==1): coord = SkyCoord(alpha, delta, frame='icrs', unit='rad'); l = coord.galactic.l.rad; b = coord.galactic.b.rad; # astropy conversion
        
	parallax = data[i][3]; errparallax =data[i][4] # mas
        dprime = functions.DfromPi(parallax); errdprime =errparallax/pow(parallax,2.); # kpc
        vlsrdata = data[i][9]; errvlsrdata = data[i][10]; # km/s
        errvlsrdata=pow(errvlsrdata,2.)+pow(SigmaVirMasers,2.)+pow(SYSTDISP,2.)
        errvlsrdata=pow(errvlsrdata,1./2.) # add systematic and virial motion to the error in vlsr
        mualphastar = data[i][5]; errmualphastar =  data[i][6]; # mas/yr
        errmualphastar=pow(pow(errmualphastar,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 
        mudelta = data[i][7]; errmudelta = data[i][8]; # mas/yr
        errmudelta=pow(pow(errmudelta,2.)+pow(SigmaVirMasers/(4.74*dprime),2.),1./2.) # add virial motion to the error 

	# convert the equatorial proper motions to galactic ones
	vecmulstarb = functions.equatorialTOgalacticProperMotions(alpha, delta, mualphastar, mudelta) # mas/yr
	mulstar = vecmulstarb[0]; mub = vecmulstarb[1]; # mas/yr
	vecerrmus = functions.equatorialTOgalacticProperMotionsErrors(alpha, delta, errmualphastar,errmudelta, 0.) # mas/yr, assume 0 correlation
	errmulstar = vecerrmus[0]; errmub = vecerrmus[1]; # mas/yr

	listraw.append([vlsrdata, errvlsrdata, mulstar, errmulstar, mub, errmub, 'BobylevBajkova13']);
             
        # transform vlsr in vhelio
        vhelio = functions.LOSboostLSR2Helio(vlsrdata, UsunData, VsunData, WsunData, l, b); # km/s
        # transform back to LSR using new solar motion
        vlsr1= functions.LOSboostHelio2LSR(vhelio, UsunINUSE, VsunINUSE, WsunINUSE, l, b);
        errvlsr1= errvlsrdata; # km/s
        # now correct for the mean peculiar motion of the maser sources - we are interested in the standard of rest
        vlsr = functions.LOSLSRminusPeculiar(vlsr1, Uscr, Vscr, Wscr, R0, l, b,dprime*cos(b)); errvlsr = errvlsr1; # km/s
              
 	# compute dpprime, Rprime
        dpp=dprime*cos(b);errdpp=errdprime*cos(b) # kpc
        Rp=functions.Rprime(R0,dpp,l);
        errRp=abs(2.*dpp-2.*R0*cos(l))*errdpp/(2.*Rp);# kpc
        #compute the velocity
        vRp=(vlsr/(cos(b)*sin(l))+V0)*Rp/R0;
        errvRp=pow(((errRp/R0)*(vlsr/(cos(b)*sin(l))+V0)),2.)
        errvRp+=pow(errvlsr*(Rp/R0)/(cos(b)*sin(l)),2.);
        errvRp=pow(errvRp,1./2.);
        wRp=(vlsr/(cos(b)*sin(l))+V0)/R0;
        errwRp=abs(errvlsr/R0/(cos(b)*sin(l)))

        listvc.append([Rp, errRp, vRp, errvRp, wRp, errwRp, 'BobylevBajkova13'])
	vecpos = functions.XYZfromDlb(R0, dprime, l*180./pi, b*180./pi);
	listpos.append([Rp, dprime, l*180./pi, b*180./pi, vecpos[0], vecpos[1], vecpos[2], 'BobylevBajkova13']) # Rp,Dp,l,b,X,Y,Z 

    return (listvc,listpos,listraw)
