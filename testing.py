import math
import time as pause
import tkinter

# v = u+a*t
# s = u*t+0.5*a*t**2
# s = v*t-0.5*a*t**2
# v**2 = u**2+2*a*s

# F = p/t
# p = m*v

class Equations:
   def __init__(self, displacement, initialVelocity, finalVelocity, acceleration, time):
       self.displacement = displacement
       self.initialVelocity = initialVelocity
       self.finalVelocity = finalVelocity
       self.acceleration = acceleration
       self.time = time

class Forces(Equations):
   def __init__(self, magnitude, angle, mass, momentum, displacement, initialVelocity, finalVelocity, acceleration,
                time, verticalComponent, horizontalComponent, verticalVelocity, horizontalVelocity):
       super().__init__(displacement, initialVelocity, finalVelocity, acceleration, time)
       self.magnitude = magnitude
       self.angle = angle
       self.mass = mass
       self.momentum = momentum
       self.verticalComponent = verticalComponent
       self.horizontalComponent = horizontalComponent
       self.verticalVelocity = verticalVelocity
       self.horizontalVelocity = horizontalVelocity

   def findInitialVelocity(self):
       self.initialVelocity = self.magnitude / self.mass
       return self.initialVelocity

   def findFinalVelocity(self):
       self.finalVelocity = self.initialVelocity + -9.81 * self.time
       return self.finalVelocity

   def findMomentum(self):
       self.momentum = self.mass * self.finalVelocity

   def findVerticalDisplacement(self):
       verticalDisplacement = (self.verticalVelocity * self.time) + 0.5 * -9.81 * self.time * self.time
       return verticalDisplacement

   def findHorizontalDisplacement(self):
       horizontalDisplacement = self.horizontalVelocity * self.time
       return horizontalDisplacement

   def findVerticalVelocity(self):
       self.angle = math.radians(self.angle)
       verticalVelocity = self.finalVelocity * math.sin(self.angle)
       return verticalVelocity

   def findHorizontalVelocity(self):
       self.angle = math.radians(self.angle)
       horizontalVelocity = self.finalVelocity * math.cos(self.angle)
       return horizontalVelocity

   def findDistance(self):
       self.horizontalComponent = float(self.horizontalComponent)
       self.verticalComponent = float(self.verticalComponent)
       displayDisplacement = math.sqrt(
           (self.verticalComponent * self.verticalComponent) + (self.horizontalComponent * self.horizontalComponent))
       return displayDisplacement

   def fuseVelocity(self):
       self.horizontalVelocity = float(self.horizontalVelocity)
       self.verticalVelocity = float(self.verticalVelocity)
       displayVelocity = math.sqrt(
           (self.verticalVelocity * self.verticalVelocity) + (self.horizontalVelocity * self.horizontalVelocity))
       return displayVelocity


values = Forces("","","","","","","","","","","",900,0.1)
print(values.fuseVelocity())