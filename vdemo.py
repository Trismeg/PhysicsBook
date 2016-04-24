from __future__ import division,print_function
from visual import *

G = 6.7e-11

# create objects
giant = sphere(pos=vector(-1e11,0,0),radius=2e10,mass=2e30,color=color.red)
giant.p = vector(0,0,-1e4) * giant.mass
dwarf = sphere(pos=vector(1.5e11,0,0),radius=1e10,mass=1e30,color=color.yellow)
dwarf.p = -giant.p

for a in [giant,dwarf]:
  a.orbit = curve(color=a.color,radius=2e9)

dt = 86400
while 1:
  rate(100)
  dist = dwarf.pos - giant.pos
  force = G * giant.mass * dwarf.mass * dist / mag(dist)**3
  giant.p = giant.p + force*dt
  dwarf.p = dwarf.p - force*dt
  for a in [giant,dwarf]:
    a.pos = a.pos + a.p/a.mass * dt
    a.orbit.append(pos=a.pos)

