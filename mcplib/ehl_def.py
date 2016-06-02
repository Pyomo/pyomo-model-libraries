# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   Reference: Michael M. Kostreva,
#   "Elasto-hydrodynamic lubrication: a non-linear
#   complementarity problem", Int. Journal for Num. Methods
#   in Fluids (4), 377-397 (1984).
#
#   The lubricant film gap and pressure between two lubricated
#   elastic cylinders in line contact is calculated.  When the pressure
#   is positive, Reynolds' equation applies and must be satisfied;
#   when the pressure is 0, the surfaces must diverge.
#
#   The load (in pounds) is represented by alpha.
#   The speed (in rpm) of the cylinders is represented by lambda. 
#   (alpha, lambda) pairs are given in the tables alph and lam, respectively.
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

N = 100 
I = list(range(1,N+1))
pi = 4.0 * atan(1)
xa = -3.0
xf = 2.0
dx = (xf - xa) / N
alpha = 2.832
Lambda = 6.057

k_init = 1.6
p_init = dict((i, max(0, 1 - abs((xa +1 + i*dx)/2))) for i in range(1, N+1))
w = dict((i, 0.5 if i in [0,N] else 1) for i in range(0, N+1))

model.k = Var(initialize=k_init)
model.p = Var(I, within=NonNegativeReals, initialize=p_init)

def h_init(model, j):
    return ( xa + (j+.5)*dx)**2 + k + 1
	    + 1/pi * sum(w[i] * (i-j-0.5)*dx
		    * log(abs(i-j-.5)*dx) *
		    ((model.p[i+1] if i < N else 0) - (model.p[i-1] if i > 1 else 0) )
	    for i in range(0,N+1))
model.h = Var(range(0,N+1), initialize=h_init)

model.psum = Complementarity(expr=complements(model.k,
                    ( 1 - dx*2/pi * sum(w[i]*model.p[i] for i in I) == 0))

def reynolds_rule(model, i):
    return complements(model.p[i] >= 0,
( (Lambda / dx) * (h[i]-h[i-1])
  - (1/dx**2) * (
	    h[i]**3 * ((model.p[i+1] if i < N else 0)-model.p[i]) /
		exp(alpha*((model.p[i+1] if i < N else 0)+model.p[i])*.5)
	- h[i-1]**3 * (model.p[i]-(model.p[i-1] if i > 1 else 0)) /
		exp(alpha*(model.p[i]+(model.p[i-1] if i > 1 else 0))*.5)
	)
)
	>= 0;
model.reynolds = Complementarity(I, rule=reynolds_rule)

