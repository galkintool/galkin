# This file imports all the relevant input galactic parameters and data flags through an input file.
# Last update: MP 04 Nov 2016.


# import system modules
import sys
import ConfigParser


# read parameters from given input file (for old non-standard configuration). input: input file name. output: input parameters.
def ReadFromFileOLD(inputfilename):
    R0=-10000;V0=-10000;UsunINUSE=-10000;VsunINUSE=-10000;WsunINUSE=-10000;SYSTDISP=-10000
    flagPROPERMOTIONS=0; # proper motions not supported in current version
    flagHITERMINAL=-10000;flagFich89tab2=-10000;flagMalhotra95=-10000;flagMcClureGriffithsDickey07=-10000
    flagHITHICKNESS=-10000;flagHonmaSofue97=-10000;flagCOTERMINAL=-10000;flagBurtonGordon78=-10000;flagClemens85=-10000;flagKnapp85=-10000;flagLuna06=-10000
    flagHIIREGIONS=-10000;flagBlitz79=-10000;flagFich89tab1=-10000;flagTurbideMoffat93=-10000;flagBrandBlitz93=-10000;flagHou09tabA1=-10000
    flagGMC=-10000;flagHou09tabA2=-10000;flagOPENCLUSTERS=-10000;flagFrinchaboyMajewski08=-10000;flagPLANETARYNEBULAE=-10000;flagDurand98=-10000
    flagCEPHEIDS=-10000;flagPont94=-10000;flagPont97=-10000;flagCSTARS=-10000;flagDemersBattinelli07=-10000;flagBattinelli12=-10000
    flagMASERS=-10000;flagReid14=-10000;flagHonma12=-10000;flagStepanishchevBobylev11=-10000;flagXu13=-10000;flagBobylevBajkova13=-10000
    flagastropy=-10000;
    
    print 'reading inputfile: ',inputfilename
    inputfile = open(inputfilename,'r')
    for line in inputfile:
        values=line.split()
 	if(values[0]=='R0'): R0=float(values[1])
	if(values[0]=='V0'): V0=float(values[1])
	if(values[0]=='UsunINUSE'): UsunINUSE=float(values[1])
	if(values[0]=='VsunINUSE'): VsunINUSE=float(values[1])
	if(values[0]=='WsunINUSE'): WsunINUSE=float(values[1])
	if(values[0]=='SYSTDISP'): SYSTDISP=float(values[1])
	#if(values[0]=='flagPROPERMOTIONS'): flagPROPERMOTIONS=int(values[1]) # proper motions not supported in current version
	if(values[0]=='flagHITERMINAL'): flagHITERMINAL=int(values[1])
	if(values[0]=='flagFich89tab2'): flagFich89tab2=int(values[1])
	if(values[0]=='flagMalhotra95'): flagMalhotra95=int(values[1])
	if(values[0]=='flagMcClureGriffithsDickey07'): flagMcClureGriffithsDickey07=int(values[1])
	if(values[0]=='flagHITHICKNESS'): flagHITHICKNESS=int(values[1])
	if(values[0]=='flagHonmaSofue97'): flagHonmaSofue97=int(values[1])
  	if(values[0]=='flagCOTERMINAL'): flagCOTERMINAL=int(values[1])
	if(values[0]=='flagBurtonGordon78'): flagBurtonGordon78=int(values[1])
	if(values[0]=='flagClemens85'): flagClemens85=int(values[1])
	if(values[0]=='flagKnapp85'): flagKnapp85=int(values[1])
	if(values[0]=='flagLuna06'): flagLuna06=int(values[1])
	if(values[0]=='flagHIIREGIONS'): flagHIIREGIONS=int(values[1])
	if(values[0]=='flagBlitz79'): flagBlitz79=int(values[1])
	if(values[0]=='flagFich89tab1'): flagFich89tab1=int(values[1])
	if(values[0]=='flagTurbideMoffat93'): flagTurbideMoffat93=int(values[1])
	if(values[0]=='flagBrandBlitz93'): flagBrandBlitz93=int(values[1])
	if(values[0]=='flagHou09tabA1'): flagHou09tabA1=int(values[1])
	if(values[0]=='flagGMC'): flagGMC=int(values[1])
	if(values[0]=='flagHou09tabA2'): flagHou09tabA2=int(values[1])
	if(values[0]=='flagOPENCLUSTERS'): flagOPENCLUSTERS=int(values[1])
	if(values[0]=='flagFrinchaboyMajewski08'): flagFrinchaboyMajewski08=int(values[1])
	if(values[0]=='flagPLANETARYNEBULAE'): flagPLANETARYNEBULAE=int(values[1])
	if(values[0]=='flagDurand98'): flagDurand98=int(values[1])
	if(values[0]=='flagCEPHEIDS'): flagCEPHEIDS=int(values[1])
	if(values[0]=='flagPont94'): flagPont94=int(values[1])
	if(values[0]=='flagPont97'): flagPont97=int(values[1])
	if(values[0]=='flagCSTARS'): flagCSTARS=int(values[1])
	if(values[0]=='flagDemersBattinelli07'): flagDemersBattinelli07=int(values[1])
	if(values[0]=='flagBattinelli12'): flagBattinelli12=int(values[1])
	if(values[0]=='flagMASERS'): flagMASERS=int(values[1])
	if(values[0]=='flagReid14'): flagReid14=int(values[1])
 	if(values[0]=='flagHonma12'): flagHonma12=int(values[1])
	if(values[0]=='flagStepanishchevBobylev11'): flagStepanishchevBobylev11=int(values[1])
	if(values[0]=='flagXu13'): flagXu13=int(values[1])
	if(values[0]=='flagBobylevBajkova13'): flagBobylevBajkova13=int(values[1])
	if(values[0]=='flagastropy'): flagastropy=int(values[1])
    inputfile.close()
    return (R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP, flagPROPERMOTIONS,flagHITERMINAL,flagFich89tab2,flagMalhotra95,flagMcClureGriffithsDickey07, flagHITHICKNESS,flagHonmaSofue97,flagCOTERMINAL,flagBurtonGordon78,flagClemens85,flagKnapp85,flagLuna06, flagHIIREGIONS,flagBlitz79,flagFich89tab1,flagTurbideMoffat93,flagBrandBlitz93,flagHou09tabA1, flagGMC,flagHou09tabA2,flagOPENCLUSTERS,flagFrinchaboyMajewski08,flagPLANETARYNEBULAE,flagDurand98,flagCEPHEIDS,flagPont94,flagPont97, flagCSTARS,flagDemersBattinelli07,flagBattinelli12, flagMASERS,flagReid14,flagHonma12,flagStepanishchevBobylev11,flagXu13,flagBobylevBajkova13,flagastropy);


# read parameters from given input file (for old ConfigParser configuration). input: input file name. output: input parameters.
def ReadFromFileConfigParser(inputfilename):
    R0=-10000;V0=-10000;UsunINUSE=-10000;VsunINUSE=-10000;WsunINUSE=-10000;SYSTDISP=-10000
    flagPROPERMOTIONS=0; # proper motions not supported in current version
    flagHITERMINAL=-10000;flagFich89tab2=-10000;flagMalhotra95=-10000;flagMcClureGriffithsDickey07=-10000
    flagHITHICKNESS=-10000;flagHonmaSofue97=-10000;flagCOTERMINAL=-10000;flagBurtonGordon78=-10000;flagClemens85=-10000;flagKnapp85=-10000;flagLuna06=-10000
    flagHIIREGIONS=-10000;flagBlitz79=-10000;flagFich89tab1=-10000;flagTurbideMoffat93=-10000;flagBrandBlitz93=-10000;flagHou09tabA1=-10000
    flagGMC=-10000;flagHou09tabA2=-10000;flagOPENCLUSTERS=-10000;flagFrinchaboyMajewski08=-10000;flagPLANETARYNEBULAE=-10000;flagDurand98=-10000
    flagCEPHEIDS=-10000;flagPont94=-10000;flagPont97=-10000;flagCSTARS=-10000;flagDemersBattinelli07=-10000;flagBattinelli12=-10000
    flagMASERS=-10000;flagReid14=-10000;flagHonma12=-10000;flagStepanishchevBobylev11=-10000;flagXu13=-10000;flagBobylevBajkova13=-10000
    flagastropy=-10000;

    print 'reading inputfile: ',inputfilename
    Config = ConfigParser.ConfigParser();
    Config.read(inputfilename)
    #GalacticParameters = Config.options("GalacticParameters")
    #Flags = Config.options("Flags")

    # Galactic parameters
    R0=float(Config.get("GalacticParameters","R0"))
    V0=float(Config.get("GalacticParameters","V0"))
    UsunINUSE=float(Config.get("GalacticParameters","UsunINUSE"))
    VsunINUSE=float(Config.get("GalacticParameters","VsunINUSE"))
    WsunINUSE=float(Config.get("GalacticParameters","WsunINUSE"))
    SYSTDISP=float(Config.get("GalacticParameters","SYSTDISP"))

    # Flags
    #flagPROPERMOTIONS=int(Config.get("Flags","flagPROPERMOTIONS")) # proper motions not supported in current version
    flagHITERMINAL=int(Config.get("Flags","flagHITERMINAL"))
    flagFich89tab2=int(Config.get("Flags","flagFich89tab2"))
    flagMalhotra95=int(Config.get("Flags","flagMalhotra95"))
    flagMcClureGriffithsDickey07=int(Config.get("Flags","flagMcClureGriffithsDickey07"))
    flagHITHICKNESS=int(Config.get("Flags","flagHITHICKNESS"))
    flagHonmaSofue97=int(Config.get("Flags","flagHonmaSofue97"))
    flagCOTERMINAL=int(Config.get("Flags","flagCOTERMINAL"))
    flagBurtonGordon78=int(Config.get("Flags","flagBurtonGordon78"))
    flagClemens85=int(Config.get("Flags","flagClemens85"))
    flagKnapp85=int(Config.get("Flags","flagKnapp85"))
    flagLuna06=int(Config.get("Flags","flagLuna06"))
    flagHIIREGIONS=int(Config.get("Flags","flagHIIREGIONS"))
    flagBlitz79=int(Config.get("Flags","flagBlitz79"))
    flagFich89tab1=int(Config.get("Flags","flagFich89tab1"))
    flagTurbideMoffat93=int(Config.get("Flags","flagTurbideMoffat93"))
    flagBrandBlitz93=int(Config.get("Flags","flagBrandBlitz93"))
    flagHou09tabA1=int(Config.get("Flags","flagHou09tabA1"))
    flagGMC=int(Config.get("Flags","flagGMC"))
    flagHou09tabA2=int(Config.get("Flags","flagHou09tabA2"))
    flagOPENCLUSTERS=int(Config.get("Flags","flagOPENCLUSTERS"))
    flagFrinchaboyMajewski08=int(Config.get("Flags","flagFrinchaboyMajewski08"))
    flagPLANETARYNEBULAE=int(Config.get("Flags","flagPLANETARYNEBULAE"))
    flagDurand98=int(Config.get("Flags","flagDurand98"))
    flagCEPHEIDS=int(Config.get("Flags","flagCEPHEIDS"))
    flagPont94=int(Config.get("Flags","flagPont94"))
    flagPont97=int(Config.get("Flags","flagPont97"))
    flagCSTARS=int(Config.get("Flags","flagCSTARS"))
    flagDemersBattinelli07=int(Config.get("Flags","flagDemersBattinelli07"))
    flagBattinelli12=int(Config.get("Flags","flagBattinelli12"))
    flagMASERS=int(Config.get("Flags","flagMASERS"))
    flagReid14=int(Config.get("Flags","flagReid14"))
    flagHonma12=int(Config.get("Flags","flagHonma12"))
    flagStepanishchevBobylev11=int(Config.get("Flags","flagStepanishchevBobylev11"))
    flagXu13=int(Config.get("Flags","flagXu13"))
    flagBobylevBajkova13=int(Config.get("Flags","flagBobylevBajkova13"))
    flagastropy=int(Config.get("Flags","flagastropy"))

    return (R0,V0,UsunINUSE,VsunINUSE,WsunINUSE,SYSTDISP, flagPROPERMOTIONS,flagHITERMINAL,flagFich89tab2,flagMalhotra95,flagMcClureGriffithsDickey07, flagHITHICKNESS,flagHonmaSofue97,flagCOTERMINAL,flagBurtonGordon78,flagClemens85,flagKnapp85,flagLuna06, flagHIIREGIONS,flagBlitz79,flagFich89tab1,flagTurbideMoffat93,flagBrandBlitz93,flagHou09tabA1, flagGMC,flagHou09tabA2,flagOPENCLUSTERS,flagFrinchaboyMajewski08,flagPLANETARYNEBULAE,flagDurand98,flagCEPHEIDS,flagPont94,flagPont97, flagCSTARS,flagDemersBattinelli07,flagBattinelli12, flagMASERS,flagReid14,flagHonma12,flagStepanishchevBobylev11,flagXu13,flagBobylevBajkova13,flagastropy);


# check validity of read parameters and print them. input: input parameters.
def CheckAndPrintParameters(pars):
    R0=pars[0];V0=pars[1];UsunINUSE=pars[2];VsunINUSE=pars[3];WsunINUSE=pars[4];SYSTDISP=pars[5]
    flagPROPERMOTIONS=pars[6];flagHITERMINAL=pars[7];flagFich89tab2=pars[8];flagMalhotra95=pars[9];flagMcClureGriffithsDickey07=pars[10]
    flagHITHICKNESS=pars[11];flagHonmaSofue97=pars[12];flagCOTERMINAL=pars[13];flagBurtonGordon78=pars[14];flagClemens85=pars[15];flagKnapp85=pars[16];flagLuna06=pars[17]
    flagHIIREGIONS=pars[18];flagBlitz79=pars[19];flagFich89tab1=pars[20];flagTurbideMoffat93=pars[21];flagBrandBlitz93=pars[22];flagHou09tabA1=pars[23]
    flagGMC=pars[24];flagHou09tabA2=pars[25];flagOPENCLUSTERS=pars[26];flagFrinchaboyMajewski08=pars[27];flagPLANETARYNEBULAE=pars[28];flagDurand98=pars[29]
    flagCEPHEIDS=pars[30];flagPont94=pars[31];flagPont97=pars[32];flagCSTARS=pars[33];flagDemersBattinelli07=pars[34];flagBattinelli12=pars[35]
    flagMASERS=pars[36];flagReid14=pars[37];flagHonma12=pars[38];flagStepanishchevBobylev11=pars[39];flagXu13=pars[40];flagBobylevBajkova13=pars[41]
    flagastropy=pars[42];

    print 'checking validity of input parameters...'

    if(len(pars)!=43): print '*** error: incomplete input parameters: ',len(pars),'. check your inputfile. exiting now.';sys.exit()
 
    if(R0<=0 or R0==-10000): print '*** error: invalid R0: ',R0,'. exiting now.';sys.exit()
    elif(R0<6 or R0>12): print '*** warning: unlikely value for R0: ',R0,'kpc. if you want to proceed with that value, comment out this if-statement in the code. exiting now.';sys.exit()
    if(V0<=0 or V0==-10000): print '*** error: invalid V0: ',V0,'km/s. exiting now.';sys.exit()
    elif(V0<150 or V0>300): print '*** warning: unlikely value for V0: ',V0,'km/s. if you want to proceed with that value, comment out this if-statement in the code. exiting now.';sys.exit()
    if(UsunINUSE==-10000): print '*** error: invalid UsunINUSE: ',UsunINUSE,'km/s. exiting now.';sys.exit()
    elif(UsunINUSE<-50 or UsunINUSE>50): print '*** warning: unlikely value for UsunINUSE: ',UsunINUSE,'km/s. if you want to proceed with that value, comment out this if-statement in the code. exiting now.';sys.exit()
    if(VsunINUSE==-10000): print '*** error: invalid VsunINUSE: ',VsunINUSE,'km/s. exiting now.';sys.exit()
    elif(VsunINUSE<-50 or VsunINUSE>50): print '*** warning: unlikely value for VsunINUSE: ',VsunINUSE,'km/s. if you want to proceed with that value, comment out this if-statement in the code. exiting now.';sys.exit()
    if(WsunINUSE==-10000): print '*** error: invalid WsunINUSE: ',WsunINUSE,'km/s. exiting now.';sys.exit()
    elif(WsunINUSE<-50 or WsunINUSE>50): print '*** warning: unlikely value for WsunINUSE: ',WsunINUSE,'km/s. if you want to proceed with that value, comment out this if-statement in the code. exiting now.';sys.exit()
    if(SYSTDISP<0 or SYSTDISP==-10000): print '*** error: invalid SYSTDISP: ',SYSTDISP,'km/s. exiting now.';sys.exit()
    elif(SYSTDISP>50): print '*** warning: unlikely value for SYSTDISP: ',SYSTDISP,'km/s. if you want to proceed with that value, comment out this if-statement in the code. exiting now.';sys.exit()

    # proper motions not supported in current version
    if (flagPROPERMOTIONS!=0):
       print '*** error: proper motions not supported in current version. exiting now.';sys.exit()
    #if (flagPROPERMOTIONS!=0 and flagPROPERMOTIONS!=1 and flagPROPERMOTIONS!=2 and flagPROPERMOTIONS!=3):
    #   print '*** error: wrong proper motions flag: ',flagPROPERMOTIONS,'. exiting now.';sys.exit()
    if flagHITERMINAL!=0 and flagHITERMINAL!=1:
       print '*** error: wrong HI terminal velocities flag: ',flagHITERMINAL,'. exiting now.';sys.exit()
    if flagFich89tab2!=0 and flagFich89tab2!=1:
       print '*** error: wrong Fich+ 89 (Table 2) flag: ',flagFich89tab2,'. exiting now.';sys.exit()
    if flagMalhotra95!=0 and flagMalhotra95!=1:
       print '*** error: wrong Malhotra 95 flag: ', flagMalhotra95,'. exiting now.';sys.exit()
    if flagMcClureGriffithsDickey07!=0 and flagMcClureGriffithsDickey07!=1:
       print '*** error: wrong McClure-Griffiths & Dickey 07 flag: ', flagMcClureGriffithsDickey07,'. exiting now.';sys.exit()
    if flagHITERMINAL==0 and flagFich89tab2==1:
       print '--- warning: overriding Fich+ 89 (Table 2)...'
    if flagHITERMINAL==0 and flagMalhotra95==1:
       print '--- warning: overriding Malhotra 95...'
    if flagHITERMINAL==0 and flagMcClureGriffithsDickey07==1:
       print '--- warning: overriding McClure-Griffiths & Dickey 07...'
    if flagHITHICKNESS!=0 and flagHITHICKNESS!=1:
       print '*** error: wrong HI thickness method flag: ', flagHITHICKNESS,'. exiting now.';sys.exit()
    if flagHonmaSofue97!=0 and flagHonmaSofue97!=1:
       print '*** error: wrong Honma & Sofue 97 flag: ', flagHonmaSofue97,'. exiting now.';sys.exit()
    if flagHITHICKNESS==0 and flagHonmaSofue97==1:
       print '--- warning: overriding Honma & Sofue 97...'
    if flagCOTERMINAL!=0 and flagCOTERMINAL!=1:
       print '*** error: wrong CO terminal velocities flag: ', flagCOTERMINAL,'. exiting now.';sys.exit()
    if flagBurtonGordon78!=0 and flagBurtonGordon78!=1:
       print '*** error: wrong Burton & Gordon 78 flag: ', flagBurtonGordon78,'. exiting now.';sys.exit()
    if flagClemens85!=0 and flagClemens85!=1:
       print '*** error: wrong Clemens 85 flag: ', flagClemens85,'. exiting now.';sys.exit()
    if flagKnapp85!=0 and flagKnapp85!=1:
       print '*** error: wrong Knapp+ 85 flag: ', flagKnapp85,'. exiting now.';sys.exit()
    if flagLuna06!=0 and flagLuna06!=1:
       print '*** error: wrong Luna+ 06 flag: ', flagLuna06,'. exiting now.';sys.exit()
    if flagCOTERMINAL==0 and flagBurtonGordon78==1:
       print '--- warning: overriding Burton & Gordon 78...'
    if flagCOTERMINAL==0 and flagClemens85==1:
       print '--- warning: overriding Clemens 85...'
    if flagCOTERMINAL==0 and flagKnapp85==1:
       print '--- warning: overriding Knapp+ 85...'
    if flagCOTERMINAL==0 and flagLuna06==1:
       print '--- warning: overriding Luna+ 06...'
    if flagHIIREGIONS!=0 and flagHIIREGIONS!=1:
       print '*** error: wrong HII regions flag: ', flagHIIREGIONS,'. exiting now.';sys.exit()
    if flagBlitz79!=0 and flagBlitz79!=1:
       print '*** error: wrong Blitz 79 flag: ', flagBlitz79,'. exiting now.';sys.exit()
    if flagFich89tab1!=0 and flagFich89tab1!=1:
      print '*** error: wrong Fich+ 89 (Table 1) flag: ', flagFich89tab1,'. exiting now.';sys.exit()
    if flagTurbideMoffat93!=0 and flagTurbideMoffat93!= 1:
       print '*** error: wrong Turbide & Moffat 93 flag: ', flagTurbideMoffat93,'. exiting now.';sys.exit()
    if flagBrandBlitz93!=0 and flagBrandBlitz93!=1:
       print '*** error: wrong Brand & Blitz 93 flag: ', flagBrandBlitz93,'. exiting now.';sys.exit()
    if flagHou09tabA1!=0 and flagHou09tabA1!=1:
       print '*** error: wrong Hou+ 09 (Table A1) flag: ', flagHou09tabA1,'. exiting now.';sys.exit()
    if flagHIIREGIONS==0 and flagBlitz79==1:
       print '--- warning: overriding Blitz 79...'
    if flagHIIREGIONS==0 and flagFich89tab1==1:
       print '--- warning: overriding Fich+ 89 (Table 1)...'
    if flagHIIREGIONS==0 and flagTurbideMoffat93==1:
       print '--- warning: overriding Turbide & Moffat 93...'
    if flagHIIREGIONS==0 and flagBrandBlitz93==1:
       print '--- warning: overriding Brand & Blitz 93...'
    if flagHIIREGIONS==0 and flagHou09tabA1==1:
       print '--- warning: overriding Hou+ 09 (Table A1)...'
    if flagGMC!=0 and flagGMC!=1:
       print '*** error: wrong giant molecular clouds flag: ', flagGMC,'. exiting now.';sys.exit()
    if flagHou09tabA2!=0 and flagHou09tabA2!=1:
       print '*** error: wrong Hou+ 09 (Table A2) flag: ', flagHou09tabA2,'. exiting now.';sys.exit()
    if flagGMC==0 and flagHou09tabA2==1:
       print '--- warning: overriding Hou+ 09 (Table A2)...'
    if flagOPENCLUSTERS!=0 and flagOPENCLUSTERS!=1:
       print '*** error: wrong open clusters flag: ', flagOPENCLUSTERS,'. exiting now.';sys.exit()
    if flagFrinchaboyMajewski08!=0 and flagFrinchaboyMajewski08!=1:
       print '*** error: wrong Frinchaboy & Majewski 08 flag: ', flagFrinchaboyMajewski08,'. exiting now.';sys.exit()
    if flagOPENCLUSTERS==0 and flagFrinchaboyMajewski08==1:
       print '--- warning: overriding Frinchaboy & Majewski 08...'
    if flagPLANETARYNEBULAE!=0 and flagPLANETARYNEBULAE!=1:
       print '*** error: wrong planetary nebulae flag: ', flagPLANETARYNEBULAE,'. exiting now.';sys.exit()
    if flagDurand98!=0 and flagDurand98!=1:
       print '*** error: wrong Durand+ 98 flag: ', flagDurand98,'. exiting now.';sys.exit()
    if flagPLANETARYNEBULAE==0 and flagDurand98==1:
       print '--- warning: overriding Durand+ 98...'
    if flagCEPHEIDS!=0 and flagCEPHEIDS!=1:
       print '*** error: wrong cepheids flag: ', flagCEPHEIDS,'. exiting now.';sys.exit()
    if flagPont94!=0 and flagPont94!=1:
       print '*** error: wrong Pont+ 94 flag: ', flagPont94,'. exiting now.';sys.exit()
    if flagPont97!=0 and flagPont97!=1:
       print '*** error: wrong Pont+ 97 flag: ', flagPont97,'. exiting now.';sys.exit()
    if flagCEPHEIDS==0 and flagPont94==1:
       print '--- warning: overriding Pont+ 94...'
    if flagCEPHEIDS==0 and flagPont97==1:
       print '--- warning: overriding Pont+ 97...'
    if flagCSTARS!=0 and flagCSTARS!=1:
       print '*** error: wrong C stars flag: ', flagCSTARS,'. exiting now.';sys.exit()
    if flagDemersBattinelli07!=0 and flagDemersBattinelli07!=1:
       print '*** error: wrong Demers & Battinelli 07 flag: ', flagDemersBattinelli07,'. exiting now.';sys.exit()
    if flagBattinelli12!=0 and flagBattinelli12!= 1:
       print '*** error: wrong Battinelli+ 12 flag: ', flagBattinelli12,'. exiting now.';sys.exit()
    if flagCSTARS==0 and flagDemersBattinelli07==1:
       print '--- warning: overriding Demers & Battinelli 07...'
    if flagCSTARS==0 and flagBattinelli12==1:
       print '--- warning: overriding Battinelli 12...'
    if flagMASERS!=0 and flagMASERS!=1:
       print '*** error: wrong masers flag: ', flagMASERS,'. exiting now.';sys.exit()
    if flagReid14!=0 and flagReid14!=1:
       print '*** error: wrong Reid+ 14 flag: ', flagReid14,'. exiting now.';sys.exit()
    if flagHonma12!=0 and flagHonma12!=1:
       print '*** error: wrong Honma+ 12 flag: ', flagHonma12,'. exiting now.';sys.exit()
    if flagStepanishchevBobylev11!=0 and flagStepanishchevBobylev11!= 1:
       print '*** error: wrong Stepanishchev & Bobylev 11 flag: ', flagStepanishchevBobylev11,'. exiting now.';sys.exit()
    if flagXu13!=0 and flagXu13!=1:
       print '*** error: wrong Xu+ 13 flag: ', flagXu13,'. exiting now.';sys.exit()
    if flagBobylevBajkova13!=0 and flagBobylevBajkova13!=1:
       print '*** error: wrong Bobylev & Bajkova 13 flag: ', flagBobylevBajkova13,'. exiting now.';sys.exit()
    if flagMASERS==0 and flagReid14==1:
       print '--- warning: overriding Reid+ 14...'
    if flagMASERS==0 and flagHonma12==1:
       print '--- warning: overriding Honma+ 12...'
    if flagMASERS==0 and flagStepanishchevBobylev11==1:
       print '--- warning: overriding Stepanishchev & Bobylev 11...'
    if flagMASERS==0 and flagXu13==1:
       print '--- warning: overriding Xu+ 13...'
    if flagMASERS==0 and flagBobylevBajkova13==1:
       print '--- warning: overriding Bobylev & Bajkova 13...'


    print 'printing input parameters...'
    print ' R0= ', R0,' kpc'
    print ' V0= ', V0,' km/s'
    print ' (Usun,Vsun,Wsun) = (', UsunINUSE,',',VsunINUSE,',',WsunINUSE, ') km/s'
    print ' systematic dispersion = ', SYSTDISP, ' km/s'

    # proper motions not supported in current version
    #print ' use proper motion?                    ', flagPROPERMOTIONS

    print ' use HI terminal velocities?           ', flagHITERMINAL
    if flagHITERMINAL==1:
       print '  use Fich+ 89(Table 2)?                 ', flagFich89tab2
       print '  use Malhotra 95?                       ', flagMalhotra95
       print '  use McClure-Griffiths & Dickey 07?     ', flagMcClureGriffithsDickey07

    print ' use HI thickness method?              ', flagHITHICKNESS
    if flagHITHICKNESS==1:
       print '  use Honma & Sofue 97?                  ', flagHonmaSofue97

    print ' use CO terminal velocities?           ', flagCOTERMINAL
    if flagCOTERMINAL==1:
       print '  use Burton & Gordon 78?                ', flagBurtonGordon78
       print '  use Clemens 85?                        ', flagClemens85
       print '  use Knapp+ 85?                         ', flagKnapp85
       print '  use Luna+ 06?                          ', flagLuna06

    print ' use HII regions?                      ', flagHIIREGIONS
    if flagHIIREGIONS==1:
       print '  use Blitz 79?                          ', flagBlitz79
       print '  use Fich+ 89 (Table 1)?                ', flagFich89tab1
       print '  use Turbide & Moffat 93?               ', flagTurbideMoffat93
       print '  use Brand & Blitz 93?                  ', flagBrandBlitz93
       print '  use Hou+ 09 (Table A1)?                ', flagHou09tabA1

    print ' use giant molecular clouds?           ', flagGMC
    if flagGMC==1:
       print '  use Hou+ 09 (Table A2)?                ', flagHou09tabA2

    print ' use open clusters?                    ', flagOPENCLUSTERS
    if flagOPENCLUSTERS==1:
       print '  use Frinchaboy & Majewski 08?          ', flagFrinchaboyMajewski08

    print ' use planetary nebulae?                ', flagPLANETARYNEBULAE
    if flagPLANETARYNEBULAE==1:
       print '  use Durand+ 98?                        ', flagDurand98

    print ' use cepheids?                         ', flagCEPHEIDS
    if flagCEPHEIDS==1:
       print '  use Pont+ 94?                          ', flagPont94
       print '  use Pont+ 97?                          ', flagPont97

    print ' use C stars?                          ', flagCSTARS
    if flagCSTARS==1:
       print '  use Demers & Battinelli 07?            ', flagDemersBattinelli07
       print '  use Battinelli+ 12?                    ', flagBattinelli12

    print ' use masers?                           ', flagMASERS
    if flagMASERS==1:
       print '  use Stepanishchev & Bobylev 11?        ', flagStepanishchevBobylev11
       print '  use Honma+ 12?                         ', flagHonma12
       print '  use Xu+ 13?                            ', flagXu13
       print '  use Bobylev & Bajkova 13?              ', flagBobylevBajkova13
       print '  use Reid+ 14?                          ', flagReid14

    print ' use astropy?                          ', flagastropy
    return
