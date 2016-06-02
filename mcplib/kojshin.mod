#==> kojshin.mod
/* ****************************************************************

This simple four-variable problem was given by:
M. Kojima and S. Shindo, "Extensions of Newton and Quasi-Newton
Method to PC^1 equations", Journal of Operations Research Society of
Japan (29) p352-374.

Two solutions: x1 = (1.2247, 0, 0, 0.5), x2 = (1, 0, 3, 0).

******************************************************************* */

set Rn	:=  1 .. 4 ;
set initpoint := 1 .. 8;

var x {j in Rn};
var sx {j in Rn: j <= 2} = x[j]**2;

subject to f {j in Rn}:
	0 <= x[j] <= Infinity complements
	  (if j = 1 then (3*sx[1]+2*x[1]*x[2]+2*sx[2]+x[3]+3*x[4]-6))
	+ (if j = 2 then (2*sx[1]+x[1]+sx[2]+10*x[3]+2*x[4]-2))
	+ (if j = 3 then (3*sx[1]+x[1]*x[2]+2*sx[2]+2*x[3]+9*x[4]-9))
	+ (if j = 4 then (sx[1]+3*sx[2]+2*x[3]+3*x[4]-3));

param xinit {Rn,initpoint} >= 0;

data;
param xinit 
:	1	2	3	4	5	6	7	8	:=
1	0	1	100	1	1	0	0	1.25
2	0	1	100	0	0	1	1	0
3	0	1	100	1	0	1	0	0
4	0	1	100	0	0	0	1	0.5 ;

for {point in initpoint} 
{
	let{i in Rn} x[i] := xinit[i,point];
	solve;
	include compchk
}
