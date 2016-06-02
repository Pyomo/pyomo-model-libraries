/* ******************************************************

A non-cooperative game example; a Nash equilibrium is sought;

References:
F.H. Murphy, H.D. Sherali, and A.L. Soyster, "A mathematical
programming approach for determining oligopolistic market
equilibrium", Mathematical Programming 24 (1986) 92-106
P.T. Harker, "Accelerating the convergence . . .", Mathematical
Programming 41 (1988) 29 - 59.

********************************************************** */

set Rn := 1 .. 10;

param gamma := 1.2;

param c {i in Rn};
param beta {i in Rn};
param L {i in Rn} := 10;

var q {i in Rn} >= 0;		/* production vector */
var Q = sum {i in Rn} q[i];
var divQ = (5000/Q)**(1/gamma);

feas {i in Rn}: /* delf - p - q(I)*delp */
	q[i] complements 
	0 <= c[i] + (L[i] * q[i])**(1/beta[i])
	- divQ - q[i] * (-1/gamma) * divQ / Q
	<= Infinity;

set initpoint := 1 .. 4;

param initval {Rn,initpoint} >= 0;

data;

param c	:= 
1	5
2	3
3	8
4	5
5	1
6	3
7	7
8	4
9	6
10	3	;

param beta :=
1	1.2
2	1
3	.9
4	.6
5	1.5
6	1
7	.7
8	1.1
9	.95
10	.75	;

param  initval
:	1	2	3	4 :=
1	1       10	1.0	7
2	1       10	1.2	4
3	1       10	1.4	3
4	1       10	1.6	1
5	1       10	1.8	18
6	1       10	2.1	4
7	1       10	2.3	1
8	1       10	2.5	6
9	1       10	2.7	3
10	1	10	2.9	2	;

for {point in initpoint} 
{
	let{i in Rn} q[i] := initval[i,point];
	solve;
	include compchk
}
