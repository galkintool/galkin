# This file contains useful geometrical functions to be used in the extraction of the rotation curve.
# Last update: MP 04 Nov 2016.


# import system packages
from numpy import (pi,cos,sin,arcsin,arccos,sqrt,log,log10,sign)

# galactocentric distance of source. inputs: R0,dpprime in kpc, llong in rad. output: kpc.
def Rprime(R0,dpprime,llong):
    dumRprime=pow(dpprime,2.)+pow(R0,2.)-2.0*dpprime*R0*cos(llong)
    dumRprime=sqrt(dumRprime)
    return dumRprime

# distance from parallax (in kpc). input: parallax in milliarcsec (mas). output: kpc.
def DfromPi(parallax):
    dumDfromPi=pow(parallax,-1.)
    return dumDfromPi

# boost from l.o.s. heliocentric velocity to l.o.s. LSR velocity. inputs: vloshelio,Usun,Vsun,Wsun in km/s, llong,blat in rad. output: km/s.
def LOSboostHelio2LSR(vloshelio,Usun,Vsun,Wsun,llong,blat):
    dumLosboosthelio=vloshelio+(Usun*cos(blat)*cos(llong)+Vsun*cos(blat)*sin(llong)+Wsun*sin(blat))
    return dumLosboosthelio

# boost from l.o.s. LSR velocity to l.o.s. heliocentric velocity. inputs: vlosLSR,Usun,Vsun,Wsun in km/s, llong,blat in rad. output: km/s.
def LOSboostLSR2Helio(vlosLSR,Usun,Vsun,Wsun,llong,blat):
    dumLosboostLSR=vlosLSR-(Usun*cos(blat)*cos(llong)+Vsun*cos(blat)*sin(llong)+Wsun*sin(blat))
    return dumLosboostLSR

# boost from transverse (=longitude) heliocentric velocity to transverse LSR velocity. inputs: vlhelio,Usun,Vsun,Wsun in km/s, llong,blat in rad. output: km/s.
def LboostHelio2LSR(vlhelio,Usun,Vsun,Wsun,llong,blat):
    dumLboosthelioLSR=vlhelio-Usun*sin(llong)+Vsun*cos(llong)
    return dumLboosthelioLSR

# boost from transverse (= longitude) LSR velocity to transverse heliocentric velocity. inputs: vlosLSR,Usun,Vsun,Wsun in km/s, llong,blat in rad. output: km/s.
def LboostLSR2Helio(vlLSR,Usun,Vsun,Wsun,llong,blat):
    dumvLSRhelio=vlLSR-(-Usun*sin(llong)+Vsun*cos(llong))
    return dumvLSRhelio

# boost from latitude heliocentric velocity to latitude LSR velocity. inputs: vbhelio,Usun,Vsun,Wsun in km/s, llong,blat in rad. output: km/s.
def BboostHelio2LSR(vbhelio,Usun,Vsun,Wsun,llong,blat):
    dumBboosthelioLSR=vbhelio+(-Usun*sin(blat)*cos(llong)-Vsun*sin(blat)*sin(llong)+Wsun*cos(blat))
    return dumBboosthelioLSR

# boost from latitude LSR velocity to latitude heliocentric velocity. inputs: vlosLSR,Usun,Vsun,Wsun in km/s, llong,blat in rad. output: km/s.
def BboostLSR2Helio(vbLSR,Usun,Vsun,Wsun,llong,blat):
    dumBboostLSRhelio=vbLSR-(-Usun*sin(blat)*cos(llong)-Vsun*sin(blat)*sin(llong)+Wsun*cos(blat))
    return dumBboostLSRhelio

# LSR LOS velocity minus peculiar motion. inputs: vlosLSR,Us,Vs,Ws in km/s, R0,dpp in kpc, l,b in rad. output: km/s.
def LOSLSRminusPeculiar(vlosLSR,Us,Vs,Ws,R0,l,b,dpp):
    Rp = Rprime(R0, dpp, l);
    sinalpha = (R0*cos(l) - dpp)/Rp; cosalpha = R0*sin(l)/Rp; # alpha: angle between GC-source and GC-tangent point
    if (cosalpha >= 0 and sinalpha >= 0):
       alpha = arcsin(sinalpha);
    elif (cosalpha >= 0 and sinalpha < 0):
       alpha = arcsin(sinalpha);
    elif (cosalpha < 0 and sinalpha >= 0):
       alpha = arccos(cosalpha);
    elif (cosalpha < 0 and sinalpha < 0):
       alpha = -arccos(cosalpha);
     
    vaux = vlosLSR - (Us*cos(b)*sin(alpha) + Vs*cos(b)*cos(alpha) +   Ws*sin(b));
    return vaux

# LSR l velocity minus peculiar motion. inputs: vlLSR,Us,Vs, Ws in km/s, R0,dpp in kpc, l,b in rad. output: km/s.
def LLSRminusPeculiar(vlLSR,Us,Vs,Ws,R0,l,b,dpp):
    Rp = Rprime(R0, dpp, l);
    sinalpha = (R0*cos(l) - dpp)/Rp; cosalpha = R0*sin(l)/Rp; # alpha: angle between GC-source and GC-tangent point
    if (cosalpha >= 0 and sinalpha >= 0):
       alpha = arcsin(sinalpha);
    elif (cosalpha >= 0 and sinalpha < 0):
       alpha = arcsin(sinalpha);
    elif (cosalpha < 0 and sinalpha >= 0):
       alpha = arccos(cosalpha);
    elif (cosalpha < 0 and sinalpha < 0):
       alpha = -arccos(cosalpha);
     
    vaux = vlLSR - (-Us*cos(alpha) + Vs*sin(alpha));
    return vaux

# LSR b velocity minus peculiar motion. inputs: vbLSR,Us,Vs,Ws in km/s, R0,dpp in kpc, l,b in rad. output: km/s.
def BLSRminusPeculiar(vbLSR,Us,Vs,Ws,R0,l,b,dpp):
    Rp = Rprime(R0, dpp, l);
    sinalpha = (R0*cos(l) - dpp)/Rp; cosalpha = R0*sin(l)/Rp; # alpha: angle between GC-source and GC-tangent point
    if (cosalpha >= 0 and sinalpha >= 0):
       alpha = arcsin(sinalpha);
    elif (cosalpha >= 0 and sinalpha < 0):
       alpha = arcsin(sinalpha);
    elif (cosalpha < 0 and sinalpha >= 0):
       alpha = arccos(cosalpha);
    elif (cosalpha < 0 and sinalpha < 0):
       alpha = -arccos(cosalpha);
    
    vaux = vbLSR - (-Us*sin(b)*sin(alpha) - Vs*sin(b)*cos(alpha) + Ws*cos(b));
    return vaux

# convert equatorial J2000 coordinates to galactic coordinates, see e.g. Binney & Merrifield, Section 2.1.2. cross-checked with http://fuse.pha.jhu.edu/support/tools/eqtogal.html. inputs: alpha,delta in rad. ouputs: in rad.
def equatorialTOgalactic(alpha, delta):
    aGP=192.85948*pi/180 # rad
    dGP=27.12825*pi/180. # rad
    lCP=122.932*pi/180. # rad, notice typo in Binney & Merrifiedl, this angle is 122.(...) deg
    sinb=sin(dGP)*sin(delta)+cos(dGP)*cos(delta)*cos(alpha-aGP)
    b=arcsin(sinb) # here phi=lCP-l
    sinphi=(cos(delta)*sin(alpha-aGP))/cos(b)
    cosphi=(cos(dGP)*sin(delta)-sin(dGP)*cos(delta)*cos(alpha-aGP))/cos(b)
    if(sinphi>=0.):
	phi=arccos(cosphi)
    if(sinphi<0.):
    	phi=(2.*pi)-arccos(cosphi)
    l=(lCP-phi)%(2*pi)     
    return(l,b) 

# convert galactic coordinates to equatorial J2000 coordinates, see e.g. Binney & Merrifield, Section 2.1.2. cross-checked with http://fuse.pha.jhu.edu/support/tools/eqtogal.html. inputs: llong,blat in rad. ouputs: in rad.
def galacticTOequatorial(llong, blat):
    aGP=192.85948*pi/180 # rad
    dGP=27.12825*pi/180. # rad
    lCP=122.932*pi/180. # rad, notice typo in Binney & Merrifiedl, this angle is 122.(...) deg*)
    sindelta=sin(dGP)*sin(blat)+cos(dGP)*cos(blat)*cos(lCP-llong)
    delta=arcsin(sindelta) # here phi=alpha-aGP
    sinphi=(cos(blat)*sin(lCP-llong))/cos(delta)
    cosphi=(cos(dGP)*sin(blat)-sin(dGP)*cos(blat)*cos(lCP-llong))/cos(delta)
    if(sinphi>=0.):
	phi=arccos(cosphi)
    if(sinphi<0.):
	phi=(2.*pi)-arccos(cosphi)
    alpha=(phi+aGP)%(2*pi)   
    return(alpha,delta)

# convert equatorial J2000 proper motions (mu_alpha*Cos[delta],mu_delta) to galactic proper motions (mu_l*Cos[b],mu_b), see e.g. Eq. 6 in arXiv:1306.2945. inputs: alpha,delta in rad, mualphastar,mudelta in mas/yr. ouputs: mas/yr.
def equatorialTOgalacticProperMotions(alpha,delta,mualphastar,mudelta): 
    aG=192.85948*pi/180 # rad
    dG=27.12825*pi/180. # rad
    C1=sin(dG)*cos(delta)-cos(dG)*sin(delta)*cos(alpha-aG)
    C2=cos(dG)*sin(alpha-aG)
    cosb=sqrt(pow(C1,2.)+pow(C2,2.))
    mulstar=(1./cosb)*(C1*mualphastar+C2*mudelta)
    mub=(1./cosb)*(-C2*mualphastar+C1*mudelta)
    return(mulstar,mub) 

# convert equatorial J2000 proper motions errors (delta_mu_alpha*Cos[delta],delta_mu_delta) to errors on galactic proper motions (delta_mu_l*Cos[b],delta_mu_b with correlation coefficient corr); error propagation of Eq. 6 in arXiv:1306.2945. inputs: alpha,delta in rad, deltamualphastar,deltamudelta in mas/yr, corr unitless. ouputs: mas/yr.
def equatorialTOgalacticProperMotionsErrors(alpha,delta,deltamualphastar,deltamudelta,corr):
    aG=192.85948*pi/180 # rad
    dG=27.12825*pi/180. # rad
    C1=sin(dG)*cos(delta)-cos(dG)*sin(delta)*cos(alpha-aG)
    C2=cos(dG)*sin(alpha-aG)
    cosb=sqrt(pow(C1,2.)+pow(C2,2.))
    # standard error propoagation: sigma_f^2 = sum_{ij} { (df/dxi)*(df/xj)*V_ij }, specialising to two variables: sigma_f^2 = (df/dx1)^2*sigma_x1^2 + (df/dx2)^2*sigma_x2^2 + 2*(df/dx1)*(df/dx2)*V12
    deltamulstar=(1./cosb)*sqrt( pow(C1*deltamualphastar,2.)  + pow(C2*deltamudelta,2.) + 2*C1*C2*corr*deltamualphastar*deltamudelta );
    deltamub=    (1./cosb)*sqrt( pow(-C2*deltamualphastar,2.) + pow(C1*deltamudelta,2.) - 2*C2*C1*corr*deltamualphastar*deltamudelta );
    return(deltamulstar,deltamub) 

# compute cartesian galactic coordinates of a source at heliocentric distance Dp in the direction (l,b). inputs: R0,Dp in kpc, ldeg,bdeg in deg. ouputs: kpc.
def XYZfromDlb(R0,Dp,ldeg, bdeg):
    lrad=ldeg*pi/180.
    brad=bdeg*pi/180.
    dpp=Dp*cos(brad)
    X=R0-dpp*cos(lrad)
    Y=-dpp*sin(lrad)
    Z=Dp*sin(brad)
    return(X,Y,Z)
