def secretFcn(x,y,z,T,dt):
  import numpy as np
  t = np.array([])
  X = np.array([])
  Y = np.array([])
  Z = np.array([])
  sigma = 10
  gamma = 28
  b = 8/3
  i = 0
  while (i<T/dt):
    x0 = x
    y0 = y
    z0 = z
    t = np.append(t, [i*dt])
    X = np.append(X, [x0])
    Y = np.append(Y, [y0])
    Z = np.append(Z, [z0])
    err = 1
    while err > 0.0001:
      x = x0 + dt*sigma*(y-x)
      y = y0 + dt*(gamma*x-y-x*z)
      z = z0 + dt*(x*y-b*z)
      err = ((x - (x0 + dt*sigma*(y-x)))**2 + (y - (y0 + dt*(gamma*x-y-x*z)))**2 + (z - (z0 + dt*(x*y-b*z)))**2)**(1/2)
    i=i+1
  return t, X, Y, Z
      

def main():
  import numpy as np
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  t, X, Y, Z = secretFcn(10,1,1,100,1/1000)
#   plt.plot(t,X,'ro')
#   plt.plot(t,Y,'go')
#   plt.plot(t,Z,'bo')
#   plt.show()

  mpl.rcParams['legend.fontsize'] = 10
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.plot(X, Y, Z, label='parametric curve')
  ax.legend()
  plt.show()

  

if __name__ == "__main__":
  main()
  
