"""
Represents an optical Gaussian source.
"""

class OpticalElementSourceGaussian(object):
    def __init__(self, name):
        pass

    def setX(self, x): #Transverse Coordinates of Gaussian Beam Center at Waist [m]
        self.__x = x         
               
    def x(self): #Transverse Coordinates of Gaussian Beam Center at Waist [m]
        return self.__x         
         
    def setY(self, y):
        self.__y = y

    def y(self):
        return self.__y

    def setZ(self, z):  #Longitudinal Coordinate of Waist [m]
        self.__z = z
     
    def z(self):  #Longitudinal Coordinate of Waist [m]
        return self.__z

    def setXp(self, xp): #Average Angles of Gaussian Beam at Waist [rad]
        self.__xp = xp
    
    def xp(self): #Average Angles of Gaussian Beam at Waist [rad]
        return self.__xp

    def setYp(self, yp):
        self.__yp = yp
    
    def yp(self):
        return self.__yp

    def setAveragePhotonEnergy(self, average_photon_energy):
        self.__average_photon_energy = average_photon_energy
    
    def averagePhotonEnergy(self):
        return self.__average_photon_energy

    def setPulseEnergy(self, pulse_energy):
        self.__pulse_energy = pulse_energy 
    
    def pulseEnergy(self):
        return self.__pulse_energy
    
    def setRepititionRate(self, repitition_rate):
        self.__repitition_rate = repitition_rate

    def repititionRate(self):
        return self.__repitition_rate

    def setPolarization(self, polarization):
        self.__polarization = polarization
        
    def polarization(self):
        return self.__polarization

    def setSigmaX(self, sigma_x):
        self.__sigma_x = sigma_x
        
    def sigmaX(self):
        return self.__sigma_x

    def setSigmaY(self, sigma_y):
        self.__sigma_y = sigma_y
    
    def sigmaY(self):
        return self.__sigma_y

    def setSigmaT(self, sigma_t):
        self.__sigma_t = sigma_t
    
    def sigmaT(self):
        return self.__sigma_t
