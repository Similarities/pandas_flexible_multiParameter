# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:53:23 2019

@author: sweedy
"""

__author__ = 'similarities'

import math

import numpy as np



# insert laser parameter (Area [cm^2], EL [J], LambdaL [mum],"name", reprate [Hz])


class Intensity_calculation:

    def __init__(self, A, EL, tau, lambdaL, name, reprate, IL=float, a0=float, E_flux=float):
        self.A = A
        self.EL = EL
        self.tau = tau
        self.lambdaL = lambdaL
        self.name = name
        self.reprate = reprate
        self.IL = IL
        self.a0 = a0
        self.E_flux = E_flux
        self.content = 0.40
        self.transmission = self.content




    def calc_I(self):
        self.IL = self.EL * self.transmission/(self.A * self.tau)
        #print(self.name, format(self.IL, ".3E"), "Intensity [W/cm^2]", "with", self.content,"fraction of EL in focus")
        return self.IL

    def calc_Eflux(self):
        self.E_flux = self.EL / self.A
        #print(self.name, format(self.E_flux, "0.3E"), "EnergyFlux [J/cm^2]", "reprate:", self.reprate)

    def calc_a0(self):
        # 0.15 gives the ratio of energy content in focal region
        self.a0 = math.sqrt((self.IL* self.lambdaL**2)/(1.38*1E18))
        #print(self.name, format(self.a0, "0.3E"), "a0 with:", self.content," energy content in FHWM")
        return self.a0



# insert beam parameter (anlge [rad], distance from focusing optic [cm], beam diameter [cm],
# focal length [cm], radius of area [cm], LambdaL [mum], "name")
class Beam_Area_calculation:

    def __init__(self, theta, length, diameter, focalLength, radius, lambdaL, name, waist0 = float, waist = float):
        self.theta = theta
        self.length = length
        self.diameter = diameter
        self.focalLength = focalLength
        self.name = name
        self.radius = radius
        self.lambdaL = lambdaL
        self.waist0 = waist0
        self.waist = waist
        self.rayleigh = float




    def beamwaist_Gaussian(self):

        self.waist0 = 0.5*(4 * self.lambdaL / math.pi) * self.focalLength / self.diameter
        #print('half beam waist in um:', self.waist0)
        self.rayleigh = math.pi * (self.waist0**2)/self.lambdaL*1.4
        #print (self.rayleigh, "Rayleigh length in mum")
        #print("diffraction limit (linear) in mum", self.lambdaL/(self.diameter/self.focalLength))
        #print("minimum beamwaist w0/2 in mum", format(self.waist0, "0.3E"), "f:", self.focalLength)
        self.waist =abs( self.waist0 * 1E-4 * math.sqrt(1 + (self.length / (self.rayleigh * 1E-4)) ** 2))

        #print("at length of:", self.length*1E4, '[um]' ,self.waist*1E4, 'unit [um]')


        return self.waist



    def areaCalc_Gaussian(self):

        area = math.pi * (self.waist)**2

        #print("Gaussian calculation", format(area, "0.3E"), "Area in [cm^2]")

        return area


# plot parameter (array_y, array_x, "color", "name of plot", "axis label y", "axis label x")
def plot_xy(array_y,array_x, colour, name, name_y, name_x):

    #plot=plt.scatter(array_y, array_x, color=colour,label=name)semilogy
    plt.plot(array_y, array_x, color=colour,label=name)
    plt.legend() #handles=[plot]
   #plt.grid(True)

    plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
    plt.ylabel(name_y)
    plt.xlabel(name_x)





# call Class main(stepsize) for functionalized/ plotted output of either beamwaist, area, I, a0 as a function
# of defocusing length [m], calculates in 100 mum step

class I_calc:

    def __init__(self, z_value, tauL, EL_on_target):

       self.z_value_cm =abs( z_value)*1E-4
       self.tauL = tauL
       self.EL = EL_on_target
       
       
    def calc_A_and_I(self):
       
       single_Area = Beam_Area_calculation(0, self.z_value_cm, 12, 150, 0, 0.8, "no1 +i * 100 x um defocusing")
       w = single_Area.beamwaist_Gaussian()
       A = single_Area.areaCalc_Gaussian()
       single_Intensity  = Intensity_calculation(A, self.EL ,self.tauL, 0.8, "no 1 +i", 1)
       


       
       return single_Intensity.calc_I()
       
       
       
#test = Main(100, 20*1E-15, 3.)









