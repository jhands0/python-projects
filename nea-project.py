import math
from time import sleep
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

 def findFinalVelocity(self):
     self.finalVelocity = self.initialVelocity + -9.81 * self.time
     return self.finalVelocity

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


def mainProgram():
   magnitude = int(E1.get())
   angle = int(E2.get())
   mass = int(E3.get())
   time = 0.001
   values = Forces(magnitude, angle, mass, "", "", "", "", "", "", "", "", "", "")
   velocity = values.findInitialVelocity()
   values = Forces(magnitude, angle, mass, "", "", "", velocity, "", "", "", "", "", "")
   horizontalVelocity = values.findHorizontalVelocity()
   verticalVelocity = values.findVerticalVelocity()
   values = Forces(magnitude, angle, mass, "", "", "", "", "", time, "", "", verticalVelocity, "")
   verticalDisplacement = values.findVerticalDisplacement()
   values = Forces(magnitude, angle, mass, "", "", "", "", "", time, "", "", "", horizontalVelocity)
   horizontalDisplacement = values.findHorizontalDisplacement()
   verticalDisplacementDisplay = tkinter.Label(gui, text=verticalDisplacement)
   horizontalDisplacementDisplay = tkinter.Label(gui, text=horizontalDisplacement)
   object = tkinter.Button(gui, bg='#a9a9a9', activebackground='#a9a9a9', height=1, width=2)
   object.place(x=0, y=680)
   time = 0
   while verticalDisplacement > 0:
       time += 0.01
       values = Forces(magnitude, angle, mass, "", "", "", "", "", time, "", "", verticalVelocity, "")
       verticalDisplacement = values.findVerticalDisplacement()
       values = Forces(magnitude, angle, mass, "", "", "", "", "", time, "", "", "", horizontalVelocity)
       horizontalDisplacement = values.findHorizontalDisplacement()
       object.place(x=(0 + (1000 * horizontalDisplacement)), y=(680 - (1000 * verticalDisplacement)))
       verticalDisplacementDisplay.place(x=0, y=0)
       horizontalDisplacementDisplay.place(x=0, y=20)
       gui.update()
       sleep(1)

gui = tkinter.Tk()
gui.title('Physics Simulation')
gui.geometry('1920x1080')
L1 = tkinter.Label(gui, text='Enter Magnitude (N):')
L1.pack()
E1 = tkinter.Entry(gui, bd=5)
E1.pack()
L2 = tkinter.Label(gui, text='Enter Angle (°):')
L2.pack()
E2 = tkinter.Entry(gui, bd=5)
E2.pack()
L3 = tkinter.Label(gui, text='Enter Mass (kg):')
L3.pack()
E3 = tkinter.Entry(gui, bd=5)
E3.pack()
submit = tkinter.Button(gui, text="Submit", command=mainProgram)
submit.pack()
gui.mainloop()