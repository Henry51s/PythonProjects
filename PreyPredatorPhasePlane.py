from pylab import *
import numpy as np

r,f = meshgrid(arange(0,3,0.1), arange(0,3,0.1))

rdot = r-(r*f)

fdot = (f*r)-f

streamplot(r,f,rdot,fdot)
xlabel("Rabbits")
ylabel("Foxes")


show()