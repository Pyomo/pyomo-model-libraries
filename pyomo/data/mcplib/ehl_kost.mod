/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

   Reference: Michael M. Kostreva,
   "Elasto-hydrodynamic lubrication: a non-linear
   complementarity problem", Int. Journal for Num. Methods
   in Fluids (4), 377-397 (1984).

   The lubricant film gap and pressure between two lubricated
   elastic cylinders in line contact is calculated.  When the pressure
   is positive, Reynolds' equation applies and must be satisfied;
   when the pressure is 0, the surfaces must diverge.

   The load (in pounds) is represented by alpha.
   The speed (in rpm) of the cylinders is represented by lambda. 
   (alpha, lambda) pairs are given in the tables alph and lam, respectively.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */

param N integer >= 1, := 100;	/* grid 0 .. N */
				/* half-points go 1 .. N */

param pi := 4 * atan(1);
param xa := -3;
param xf > xa, := 2;
param dx := (xf - xa) / N;
param alpha := 2.832;
param lambda := 6.057;

param k_init := 1.6;
param p_init {i in 1..N} := max(0, 1 - abs((xa +1 + i*dx)/2));
param w {i in 0..N} := (if i in {0,N} then 0.5 else 1);
/*let w[0] := 0.5;
let w[N] := 0.5; */

var k := k_init;
var p {i in 1..N} >= 0, := p_init[i];

psum :
	k complements
( 1 - dx*2/pi * sum {i in 1..N} w[i]*p[i] )
	= 0;

reynolds {i in 1..N}:
	p[i] >= 0  complements
( (lambda / dx) * (
	((xa + (i+.5)*dx)^2 + k + 1
	+ 1/pi * (sum {l in 0..N} w[l] * (l-i-.5)*dx
		* log(abs(l-i-.5)*dx) *
		 ((if l < N then p[l+1]) - (if l > 1 then p[l-1]) )
	) )
	- 
	((xa + (i-.5)*dx)^2 + k + 1
	+ 1/pi * (sum {l in 0..N} w[l] * (l-i+.5)*dx
		* log(abs(l-i+.5)*dx) *
		 ((if l < N then p[l+1]) - (if l > 1 then p[l-1]) )
	) )
	)


  - (1/dx^2) * (
	((xa + (i+.5)*dx)^2 + k + 1
	+ 1/pi * (sum {l in 0..N} w[l] * (l-i-.5)*dx
		* log(abs(l-i-.5)*dx) *
		 ((if l < N then p[l+1]) - (if l > 1 then p[l-1]) )
	) )^3 * ((if i < N then p[i+1])-p[i]) /
		exp(alpha*((if i < N then p[i+1])+p[i])*.5)
	-
	((xa + (i-.5)*dx)^2 + k + 1
	+ 1/pi * (sum {l in 0..N} w[l] * (l-i+.5)*dx
		* log(abs(l-i+.5)*dx) *
		 ((if l < N then p[l+1]) - (if l > 1 then p[l-1]) )
	) )^3  * (p[i]-(if i > 1 then p[i-1])) /
		exp(alpha*(p[i]+(if i > 1 then p[i-1]))*.5)
	)
) >= 0;

