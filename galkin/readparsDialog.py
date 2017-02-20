# This file imports all the relevant input galactic parameters and data flags through a dialog window.
# Last update: MP 04 Nov 2016.


# import system modules
import sys
import wx


# definition of the dialog box
class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(600, 620))

	# all parameters
	self.pars=[]
	for i in range(43): #i: 0 to 42
	    self.pars.append(-10000)

	# galactic parameters field
        wx.StaticBox(self, -1, 'galactic parameters', pos=(5, 5), size=(590, 100))

 	wx.StaticText(self, -1, 'R0 [kpc]=', pos=(25, 30))
        self.boxR0=wx.TextCtrl(self, -1, '8.0', pos=(113,27), size=(45, 25))

  	wx.StaticText(self, -1, 'V0 [km/s]=', pos=(175, 30))
        self.boxV0=wx.TextCtrl(self, -1, '230.0', pos=(263,27), size=(45, 25))

        wx.StaticText(self, -1, 'syst [km/s]=', pos=(325, 30))
        self.boxSyst=wx.TextCtrl(self, -1, '0.0', pos=(418,27), size=(45, 25))

	wx.StaticText(self, -1, 'Usun [km/s]=', pos=(25, 70))
        self.boxUsun=wx.TextCtrl(self, -1, '11.10', pos=(113,67), size=(45, 25))

	wx.StaticText(self, -1, 'Vsun [km/s]=', pos=(175, 70))
        self.boxVsun=wx.TextCtrl(self, -1, '12.24', pos=(263,67), size=(45, 25))

        wx.StaticText(self, -1, 'Wsun [km/s]=', pos=(325, 70))
        self.boxWsun=wx.TextCtrl(self, -1, '07.25', pos=(418,67), size=(45, 25))


        # data flags field
 	wx.StaticBox(self, -1, 'data to use', pos=(5, 110), size=(590, 453))

	wx.StaticBox(self, -1, '', pos=(12, 119), size=(283, 438))

	self.HIt=wx.CheckBox(self, -1 ,'HI terminal velocities', pos=(15, 130));self.HIt.SetValue(wx.CHK_CHECKED)
	self.HIt1=wx.CheckBox(self, -1 ,'Fich+ 89 (Table 2)', pos=(35, 150));self.HIt1.SetValue(wx.CHK_CHECKED);
        if(self.HIt.GetValue()==wx.CHK_UNCHECKED): self.HIt1.Enable(False)
	self.HIt2=wx.CheckBox(self, -1 ,'Malhotra 95', pos=(35, 170));self.HIt2.SetValue(wx.CHK_CHECKED);
	if(self.HIt.GetValue()==wx.CHK_UNCHECKED): self.HIt2.Enable(False)
	self.HIt3=wx.CheckBox(self, -1 ,'McClure-Griffiths && Dickey 07', pos=(35, 190));self.HIt3.SetValue(wx.CHK_CHECKED);
	if(self.HIt.GetValue()==wx.CHK_UNCHECKED): self.HIt3.Enable(False)
	wx.EVT_CHECKBOX(self, self.HIt.GetId(), self.MakeGrayHIt) # make references gray if primary button is not checked

	self.HIth=wx.CheckBox(self, -1 ,'HI thickness', pos=(15, 220));self.HIth.SetValue(wx.CHK_CHECKED)
	self.HIth1=wx.CheckBox(self, -1 ,'Honma && Sofue 97', pos=(35, 240));self.HIth1.SetValue(wx.CHK_CHECKED);
        if(self.HIth.GetValue()==wx.CHK_UNCHECKED): self.HIth1.Enable(False)
	wx.EVT_CHECKBOX(self, self.HIth.GetId(), self.MakeGrayHIth) # make references gray if primary button is not checked

	self.COt=wx.CheckBox(self, -1 ,'CO terminal velocities', pos=(15, 270));self.COt.SetValue(wx.CHK_CHECKED)
	self.COt1=wx.CheckBox(self, -1 ,'Burton && Gordon 78', pos=(35, 290));self.COt1.SetValue(wx.CHK_CHECKED);
        if(self.COt.GetValue()==wx.CHK_UNCHECKED): self.COt1.Enable(False)
	self.COt2=wx.CheckBox(self, -1 ,'Clemens 85', pos=(35, 310));self.COt2.SetValue(wx.CHK_CHECKED);
	if(self.COt.GetValue()==wx.CHK_UNCHECKED): self.COt2.Enable(False)
	self.COt3=wx.CheckBox(self, -1 ,'Knapp+ 85', pos=(35, 330));self.COt3.SetValue(wx.CHK_CHECKED);
	if(self.COt.GetValue()==wx.CHK_UNCHECKED): self.COt3.Enable(False)
	self.COt4=wx.CheckBox(self, -1 ,'Luna+ 06', pos=(35, 350));self.COt4.SetValue(wx.CHK_CHECKED);
	if(self.COt.GetValue()==wx.CHK_UNCHECKED): self.COt4.Enable(False)
	wx.EVT_CHECKBOX(self, self.COt.GetId(), self.MakeGrayCOt) # make references gray if primary button is not checked

	self.HII=wx.CheckBox(self, -1 ,'HII regions', pos=(15, 380));self.HII.SetValue(wx.CHK_CHECKED)
	self.HII1=wx.CheckBox(self, -1 ,'Blitz 79', pos=(35, 400));self.HII1.SetValue(wx.CHK_CHECKED);
        if(self.HII.GetValue()==wx.CHK_UNCHECKED): self.HII1.Enable(False)
	self.HII2=wx.CheckBox(self, -1 ,'Fich+ 89 (Table 1)', pos=(35, 420));self.HII2.SetValue(wx.CHK_CHECKED);
	if(self.HII.GetValue()==wx.CHK_UNCHECKED): self.HII2.Enable(False)
	self.HII3=wx.CheckBox(self, -1 ,'Turbide && Moffat 93', pos=(35, 440));self.HII3.SetValue(wx.CHK_CHECKED);
	if(self.HII.GetValue()==wx.CHK_UNCHECKED): self.HII3.Enable(False)
	self.HII4=wx.CheckBox(self, -1 ,'Brand && Blitz 93', pos=(35, 460));self.HII4.SetValue(wx.CHK_CHECKED);
	if(self.HII.GetValue()==wx.CHK_UNCHECKED): self.HII4.Enable(False)
	self.HII5=wx.CheckBox(self, -1 ,'Hou+ 09 (Table A1)', pos=(35, 480));self.HII5.SetValue(wx.CHK_CHECKED);
	if(self.HII.GetValue()==wx.CHK_UNCHECKED): self.HII5.Enable(False)
	wx.EVT_CHECKBOX(self, self.HII.GetId(), self.MakeGrayHII) # make references gray if primary button is not checked

	self.GMC=wx.CheckBox(self, -1 ,'giant molecular clouds', pos=(15, 510));self.GMC.SetValue(wx.CHK_CHECKED)
	self.GMC1=wx.CheckBox(self, -1 ,'Hou+ 09 (Table A2)', pos=(35, 530));self.GMC1.SetValue(wx.CHK_CHECKED);
        if(self.GMC.GetValue()==wx.CHK_UNCHECKED): self.GMC1.Enable(False)
	wx.EVT_CHECKBOX(self, self.GMC.GetId(), self.MakeGrayGMC) # make references gray if primary button is not checked


	wx.StaticBox(self, -1, '', pos=(305, 119), size=(283, 248))

	self.OPC=wx.CheckBox(self, -1 ,'open clusters', pos=(310, 130));self.OPC.SetValue(wx.CHK_CHECKED)
	self.OPC1=wx.CheckBox(self, -1 ,'Frinchaboy && Majewski 08', pos=(330, 150));self.OPC1.SetValue(wx.CHK_CHECKED);
        if(self.OPC.GetValue()==wx.CHK_UNCHECKED): self.OPC1.Enable(False)
	wx.EVT_CHECKBOX(self, self.OPC.GetId(), self.MakeGrayOPC) # make references gray if primary button is not checked

	self.PNe=wx.CheckBox(self, -1 ,'planetary nebulae', pos=(310, 180));self.PNe.SetValue(wx.CHK_CHECKED)
	self.PNe1=wx.CheckBox(self, -1 ,'Durand+ 98', pos=(330, 200));self.PNe1.SetValue(wx.CHK_CHECKED);
        if(self.PNe.GetValue()==wx.CHK_UNCHECKED): self.PNe1.Enable(False)
	wx.EVT_CHECKBOX(self, self.PNe.GetId(), self.MakeGrayPNe) # make references gray if primary button is not checked

	self.CEP=wx.CheckBox(self, -1 ,'classical cepheids', pos=(310, 230));self.CEP.SetValue(wx.CHK_CHECKED)
	self.CEP1=wx.CheckBox(self, -1 ,'Pont+ 94', pos=(330, 250));self.CEP1.SetValue(wx.CHK_CHECKED);
        if(self.CEP.GetValue()==wx.CHK_UNCHECKED): self.CEP1.Enable(False)
	self.CEP2=wx.CheckBox(self, -1 ,'Pont+ 97', pos=(330, 270));self.CEP2.SetValue(wx.CHK_CHECKED);
	if(self.CEP.GetValue()==wx.CHK_UNCHECKED): self.CEP2.Enable(False)
	wx.EVT_CHECKBOX(self, self.CEP.GetId(), self.MakeGrayCEP) # make references gray if primary button is not checked

	self.CST=wx.CheckBox(self, -1 ,'carbon stars', pos=(310, 300));self.CST.SetValue(wx.CHK_CHECKED)
	self.CST1=wx.CheckBox(self, -1 ,'Demers && Battinelli 07', pos=(330, 320));self.CST1.SetValue(wx.CHK_CHECKED);
        if(self.CST.GetValue()==wx.CHK_UNCHECKED): self.CST1.Enable(False)
	self.CST2=wx.CheckBox(self, -1 ,' Battinelli+ 12', pos=(330, 340));self.CST2.SetValue(wx.CHK_CHECKED);
	if(self.CST.GetValue()==wx.CHK_UNCHECKED): self.CST2.Enable(False)
	wx.EVT_CHECKBOX(self, self.CST.GetId(), self.MakeGrayCST) # make references gray if primary button is not checked


	wx.StaticBox(self, -1, '', pos=(305, 362), size=(283, 137))

	self.MAS=wx.CheckBox(self, -1 ,'masers', pos=(310, 372));self.MAS.SetValue(wx.CHK_CHECKED)
	self.MAS1=wx.CheckBox(self, -1 ,'Reid+ 14', pos=(330, 392));self.MAS1.SetValue(wx.CHK_CHECKED);
        if(self.MAS.GetValue()==wx.CHK_UNCHECKED): self.MAS1.Enable(False)
	self.MAS2=wx.CheckBox(self, -1 ,'Honma+ 12', pos=(330, 412));self.MAS2.SetValue(wx.CHK_CHECKED);
	if(self.MAS.GetValue()==wx.CHK_UNCHECKED): self.MAS2.Enable(False)
	self.MAS3=wx.CheckBox(self, -1 ,'Stepanishchev && Bobylev 11', pos=(330, 432));self.MAS3.SetValue(wx.CHK_CHECKED);
	if(self.MAS.GetValue()==wx.CHK_UNCHECKED): self.MAS3.Enable(False)
	self.MAS4=wx.CheckBox(self, -1 ,'Xu+ 13', pos=(330, 452));self.MAS4.SetValue(wx.CHK_CHECKED);
	if(self.MAS.GetValue()==wx.CHK_UNCHECKED): self.MAS4.Enable(False)
	self.MAS5=wx.CheckBox(self, -1 ,'Bobylev && Bajkova 13', pos=(330, 472));self.MAS5.SetValue(wx.CHK_CHECKED);
	if(self.MAS.GetValue()==wx.CHK_UNCHECKED): self.MAS5.Enable(False)
	wx.EVT_CHECKBOX(self, self.MAS.GetId(), self.MakeGrayMAS) # make references gray if primary button is not checked


	# proper motions not supported in current version
	#self.PM=wx.CheckBox(self, -1 ,'use proper motions when available', pos=(310, 510));self.PM.SetValue(wx.CHK_UNCHECKED)
	#self.PM1=wx.CheckBox(self, -1 ,'l', pos=(330, 530));self.PM1.SetValue(wx.CHK_CHECKED);
	#self.PM2=wx.CheckBox(self, -1 ,'b', pos=(380, 530));self.PM2.SetValue(wx.CHK_UNCHECKED);
	#self.PM3=wx.CheckBox(self, -1 ,'l and b', pos=(432, 530));self.PM3.SetValue(wx.CHK_UNCHECKED);
        #if(self.PM.GetValue()==wx.CHK_UNCHECKED): self.PM1.Enable(False);self.PM2.Enable(False);self.PM3.Enable(False)
	#if(self.PM1.GetValue()==wx.CHK_CHECKED): self.PM2.SetValue(wx.CHK_UNCHECKED);self.PM3.SetValue(wx.CHK_UNCHECKED)
	#if(self.PM2.GetValue()==wx.CHK_CHECKED): self.PM1.SetValue(wx.CHK_UNCHECKED);self.PM3.SetValue(wx.CHK_UNCHECKED)
	#if(self.PM3.GetValue()==wx.CHK_CHECKED): self.PM1.SetValue(wx.CHK_UNCHECKED);self.PM2.SetValue(wx.CHK_UNCHECKED)
	#wx.EVT_CHECKBOX(self, self.PM.GetId(), self.MakeGrayPM) # make references gray if primary button is not checked
	#wx.EVT_CHECKBOX(self, self.PM1.GetId(), self.TogglePM1)
	#wx.EVT_CHECKBOX(self, self.PM2.GetId(), self.TogglePM2)
	#wx.EVT_CHECKBOX(self, self.PM3.GetId(), self.TogglePM3)


	self.astropy=wx.CheckBox(self, -1 ,'use astropy conversions', pos=(310, 535));self.astropy.SetValue(wx.CHK_UNCHECKED) # astropy conversions


        wx.Button(self, 1, 'OK', (534, 565), (60, -1))  # OK button
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)

        self.Centre()
        self.ShowModal()
        self.Destroy()


    def MakeGrayHIt(self, event):
        if(self.HIt.GetValue()==wx.CHK_UNCHECKED):
	  self.HIt1.Enable(False);self.HIt2.Enable(False);self.HIt3.Enable(False)
	else:
	  self.HIt1.Enable(True);self.HIt2.Enable(True);self.HIt3.Enable(True)
    
    def MakeGrayHIth(self, event):
        if(self.HIth.GetValue()==wx.CHK_UNCHECKED):
	  self.HIth1.Enable(False)
	else:
	  self.HIth1.Enable(True);

    def MakeGrayCOt(self, event):
        if(self.COt.GetValue()==wx.CHK_UNCHECKED):
	  self.COt1.Enable(False);self.COt2.Enable(False);self.COt3.Enable(False);self.COt4.Enable(False)
	else:
	  self.COt1.Enable(True);self.COt2.Enable(True);self.COt3.Enable(True);self.COt4.Enable(True)

    def MakeGrayHII(self, event):
        if(self.HII.GetValue()==wx.CHK_UNCHECKED):
	  self.HII1.Enable(False);self.HII2.Enable(False);self.HII3.Enable(False);self.HII4.Enable(False);self.HII5.Enable(False)
	else:
	  self.HII1.Enable(True);self.HII2.Enable(True);self.HII3.Enable(True);self.HII4.Enable(True);self.HII5.Enable(True)

    def MakeGrayGMC(self, event):
        if(self.GMC.GetValue()==wx.CHK_UNCHECKED):
	  self.GMC1.Enable(False)
	else:
	  self.GMC1.Enable(True);

    def MakeGrayOPC(self, event):
        if(self.OPC.GetValue()==wx.CHK_UNCHECKED):
	  self.OPC1.Enable(False)
	else:
	  self.OPC1.Enable(True);

    def MakeGrayPNe(self, event):
        if(self.PNe.GetValue()==wx.CHK_UNCHECKED):
	  self.PNe1.Enable(False)
	else:
	  self.PNe1.Enable(True);

    def MakeGrayCEP(self, event):
        if(self.CEP.GetValue()==wx.CHK_UNCHECKED):
	  self.CEP1.Enable(False);self.CEP2.Enable(False)
	else:
	  self.CEP1.Enable(True);self.CEP2.Enable(True)

    def MakeGrayCST(self, event):
        if(self.CST.GetValue()==wx.CHK_UNCHECKED):
	  self.CST1.Enable(False);self.CST2.Enable(False)
	else:
	  self.CST1.Enable(True);self.CST2.Enable(True)

    def MakeGrayMAS(self, event):
        if(self.MAS.GetValue()==wx.CHK_UNCHECKED):
	  self.MAS1.Enable(False);self.MAS2.Enable(False);self.MAS3.Enable(False);self.MAS4.Enable(False);self.MAS5.Enable(False)
	else:
	  self.MAS1.Enable(True);self.MAS2.Enable(True);self.MAS3.Enable(True);self.MAS4.Enable(True);self.MAS5.Enable(True)

    # proper motions not supported in current version
    #def MakeGrayPM(self, event):
    #    if(self.PM.GetValue()==wx.CHK_UNCHECKED):
    #	  self.PM1.Enable(False);self.PM2.Enable(False);self.PM3.Enable(False)
    #	else:
    #	  self.PM1.Enable(True);self.PM2.Enable(True);self.PM3.Enable(True)
    #def TogglePM1(self, event):
    #    if(self.PM1.GetValue()==wx.CHK_CHECKED):
    #	  self.PM2.SetValue(wx.CHK_UNCHECKED);self.PM3.SetValue(wx.CHK_UNCHECKED)
    #	else:
    #	  self.PM1.SetValue(wx.CHK_CHECKED)
    #def TogglePM2(self, event):
    #    if(self.PM2.GetValue()==wx.CHK_CHECKED):
    #	  self.PM1.SetValue(wx.CHK_UNCHECKED);self.PM3.SetValue(wx.CHK_UNCHECKED)
    #	else:
    #	  self.PM2.SetValue(wx.CHK_CHECKED)
    #def TogglePM3(self, event):
    #    if(self.PM3.GetValue()==wx.CHK_CHECKED):
    #	  self.PM1.SetValue(wx.CHK_UNCHECKED);self.PM2.SetValue(wx.CHK_UNCHECKED)
    #	else:
    #	  self.PM3.SetValue(wx.CHK_CHECKED)

    # read parameters after OK is pressed
    def OnClose(self, event):
	self.Close()
	self.pars[0]=float(self.boxR0.GetValue());self.pars[1]=float(self.boxV0.GetValue());
	self.pars[2]=float(self.boxUsun.GetValue());self.pars[3]=float(self.boxVsun.GetValue());self.pars[4]=float(self.boxWsun.GetValue());
	self.pars[5]=float(self.boxSyst.GetValue());

        # proper motions not supported in current version
        self.pars[6]=0
	#if(self.PM.GetValue()==wx.CHK_UNCHECKED): self.pars[6]=0
	#if(self.PM.GetValue()==wx.CHK_CHECKED and self.PM1.GetValue()==wx.CHK_CHECKED and self.PM2.GetValue()==wx.CHK_UNCHECKED and self.PM3.GetValue()==wx.CHK_UNCHECKED): self.pars[6]=1
	#if(self.PM.GetValue()==wx.CHK_CHECKED and self.PM1.GetValue()==wx.CHK_UNCHECKED and self.PM2.GetValue()==wx.CHK_CHECKED and self.PM3.GetValue()==wx.CHK_UNCHECKED): self.pars[6]=2
	#if(self.PM.GetValue()==wx.CHK_CHECKED and self.PM1.GetValue()==wx.CHK_UNCHECKED and self.PM2.GetValue()==wx.CHK_UNCHECKED and self.PM3.GetValue()==wx.CHK_CHECKED): self.pars[6]=3

	if(self.HIt.GetValue()==wx.CHK_UNCHECKED): self.pars[7]=0;self.pars[8]=0;self.pars[9]=0;self.pars[10]=0
	else:
	  self.pars[7]=1
	  if(self.HIt1.GetValue()==wx.CHK_CHECKED): self.pars[8]=1
	  else: self.pars[8]=0
	  if(self.HIt2.GetValue()==wx.CHK_CHECKED): self.pars[9]=1
	  else: self.pars[9]=0
	  if(self.HIt3.GetValue()==wx.CHK_CHECKED): self.pars[10]=1
	  else: self.pars[10]=0

	if(self.HIth.GetValue()==wx.CHK_UNCHECKED): self.pars[11]=0;self.pars[12]=0
	else:
	  self.pars[11]=1
	  if(self.HIth1.GetValue()==wx.CHK_CHECKED): self.pars[12]=1
	  else: self.pars[12]=0

	if(self.COt.GetValue()==wx.CHK_UNCHECKED): self.pars[13]=0;self.pars[14]=0;self.pars[15]=0;self.pars[16]=0;self.pars[17]=0
	else:
	  self.pars[13]=1
	  if(self.COt1.GetValue()==wx.CHK_CHECKED): self.pars[14]=1
	  else: self.pars[14]=0
	  if(self.COt2.GetValue()==wx.CHK_CHECKED): self.pars[15]=1
	  else: self.pars[15]=0
	  if(self.COt3.GetValue()==wx.CHK_CHECKED): self.pars[16]=1
	  else: self.pars[16]=0
	  if(self.COt4.GetValue()==wx.CHK_CHECKED): self.pars[17]=1
	  else: self.pars[17]=0

	if(self.HII.GetValue()==wx.CHK_UNCHECKED): self.pars[18]=0;self.pars[19]=0;self.pars[20]=0;self.pars[21]=0;self.pars[22]=0;self.pars[23]=0
	else:
	  self.pars[18]=1
	  if(self.HII1.GetValue()==wx.CHK_CHECKED): self.pars[19]=1
	  else: self.pars[19]=0
	  if(self.HII2.GetValue()==wx.CHK_CHECKED): self.pars[20]=1
	  else: self.pars[20]=0
	  if(self.HII3.GetValue()==wx.CHK_CHECKED): self.pars[21]=1
	  else: self.pars[21]=0
	  if(self.HII4.GetValue()==wx.CHK_CHECKED): self.pars[22]=1
	  else: self.pars[22]=0
	  if(self.HII5.GetValue()==wx.CHK_CHECKED): self.pars[23]=1
	  else: self.pars[23]=0

	if(self.GMC.GetValue()==wx.CHK_UNCHECKED): self.pars[24]=0;self.pars[25]=0
	else:
	  self.pars[24]=1
	  if(self.GMC1.GetValue()==wx.CHK_CHECKED): self.pars[25]=1
	  else: self.pars[25]=0

	if(self.OPC.GetValue()==wx.CHK_UNCHECKED): self.pars[26]=0;self.pars[27]=0
	else:
	  self.pars[26]=1
	  if(self.OPC1.GetValue()==wx.CHK_CHECKED): self.pars[27]=1
	  else: self.pars[27]=0

	if(self.PNe.GetValue()==wx.CHK_UNCHECKED): self.pars[28]=0;self.pars[29]=0
	else:
	  self.pars[28]=1
	  if(self.PNe1.GetValue()==wx.CHK_CHECKED): self.pars[29]=1
	  else: self.pars[29]=0

	if(self.CEP.GetValue()==wx.CHK_UNCHECKED): self.pars[30]=0;self.pars[31]=0;self.pars[32]=0
	else:
	  self.pars[30]=1
	  if(self.CEP1.GetValue()==wx.CHK_CHECKED): self.pars[31]=1
	  else: self.pars[31]=0
	  if(self.CEP2.GetValue()==wx.CHK_CHECKED): self.pars[32]=1
	  else: self.pars[32]=0

	if(self.CST.GetValue()==wx.CHK_UNCHECKED): self.pars[33]=0;self.pars[34]=0;self.pars[35]=0
	else:
	  self.pars[33]=1
	  if(self.CST1.GetValue()==wx.CHK_CHECKED): self.pars[34]=1
	  else: self.pars[34]=0
	  if(self.CST2.GetValue()==wx.CHK_CHECKED): self.pars[35]=1
	  else: self.pars[35]=0

	if(self.MAS.GetValue()==wx.CHK_UNCHECKED): self.pars[36]=0;self.pars[37]=0;self.pars[38]=0;self.pars[39]=0;self.pars[40]=0;self.pars[41]=0
	else:
	  self.pars[36]=1
	  if(self.MAS1.GetValue()==wx.CHK_CHECKED): self.pars[37]=1
	  else: self.pars[37]=0
	  if(self.MAS2.GetValue()==wx.CHK_CHECKED): self.pars[38]=1
	  else: self.pars[38]=0
	  if(self.MAS3.GetValue()==wx.CHK_CHECKED): self.pars[39]=1
	  else: self.pars[39]=0
	  if(self.MAS4.GetValue()==wx.CHK_CHECKED): self.pars[40]=1
	  else: self.pars[40]=0
	  if(self.MAS5.GetValue()==wx.CHK_CHECKED): self.pars[41]=1
	  else: self.pars[41]=0

	if(self.astropy.GetValue()==wx.CHK_CHECKED): self.pars[42]=1
	else: self.pars[42]=0
	

# launch dialog window and read parameters. output: input parameters.
def LaunchWindowAndRead():
    app = wx.App(0)
    diag=MyDialog(None, -1, 'enter input parameters')
    parvec=diag.pars # read parameters
    app.MainLoop()
    return parvec
