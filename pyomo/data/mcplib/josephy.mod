/* josephy.mod

   Complementarity problem from Kojima, via Josephy.

*/

set Rn := 1 .. 4;
set initpoint := 1 .. 8;

param A {Rn,Rn,Rn};
param B {Rn,Rn};
param c {Rn};
param xinit {Rn,initpoint} >= 0;

var x {j in Rn} >= 0;
f {i in Rn}:
 0 <= x[i] complements 
 c[i] + sum {j in Rn} (B[i,j]*x[j] + sum {k in Rn} A[i,j,k]*x[j]*x[k]) >= 0;

data;
param xinit 
:	1	2	3	4	5	6	7	8	:=
1	0	1	100	1	1	0	0	1.25
2	0	1	100	0	0	1	1	0
3	0	1	100	1	0	1	0	0
4	0	1	100	0	0	0	1	0.5 ;

param A default 0 := 
1,1,1	3
1,1,2	2
1,2,2	2
2,1,1	2
2,2,2	1
3,1,1	3
3,1,2	1
3,2,2	2
4,1,1	1
4,2,2	3 ;

param B default 0 :
	1	2	3	4 :=
1	.	.	1	3
2	1	.	3	2
3	.	.	2	3
4	.	.	2	3 ;
param c :=
1	-6
2	-2
3	-1
4	-3 ;

for {point in initpoint} 
{
	let{i in Rn} x[i] := xinit[i,point];
	solve;
	include compchk
}
