# ==>pies.mod

/* %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

A linear program with a variable rhs in the constraint system
is expressed as a complementarity problem.

LP:	min 	<c,x>
		Ax = q(p),
	s.t.	Bx = b,
		x >= 0

where the prices p are the duals to the first constraint.

MCP:	       A'p + B'v + c >= 0, x >= 0, comp.
	-Ax + q(p)           =  0, p free, comp.
	-Bx              + b =  0, v free, comp.

Of course, the variables x and v are going to be
split up further in the model.

References:
William W. Hogan, Energy Policy Models for Project Independence,
Computers \& Operations Research (2), 1975.

N. Josephy, A Newton Method for the PIES energy model,
Tech Report, Mathematics Research Center, UW-Madison, 1979.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% */

set comod ordered;		/* coal and light and heavy oil */
set R;				/* resources */
data;
set comod := C L H;
set R := Capital Steel;
model;
set creg := 1 .. 2;		/* coal producing regions */
set oreg := 1 .. 2;		/* crude oil producing regions */
set ctyp := 1 .. 3;		/* increments of coal production */
set otyp := 1 .. 2;		/* increments of oil production */
set refin := 1 .. 2;		/* refineries */
set users := 1 .. 2;		/* consumption regions */

param rmax {R}; 		/* maximum resource usage */
param cmax {creg,ctyp};	/* coal prod. limits */
param omax {oreg,otyp};	/* oil prod. limits */
param rcost {refin};		/* refining cost */
param q0 {comod};		/* base demand for commodities */
param p0 {comod};		/* base prices for commodities */
param demand {comod,users};	/* computed at optimality */
param output {refin,comod};	/* % output of light/heavy oil */
param esub {comod,comod};	/* cross-elasticities of substitution */
param cruse {R,creg,ctyp}; /* resource use in coal prod */
param oruse {R,oreg,otyp}; /* resource use in oil prod */
param ccost {creg,ctyp};	/* coal prod. cost */
param ocost {oreg,otyp};	/* oil prod. cost */
param ctcost {creg,users};
param otcost {oreg,refin};
param ltcost {refin,users};	/* light oil trans costs */
param htcost {refin,users};	/* heavy oil trans costs */

param i_c {creg,ctyp};
param i_o {oreg,otyp};
param i_ct {creg,users};	/* initial trans */
param i_ot {oreg,refin};	/* initial trans */
param i_lt {refin,users};	/* initial trans */
param i_ht {refin,users};	/* initial trans */
param iprice {comod,users};	/* initial price estimate */

var c {cr in creg,ct in ctyp} := i_c[cr,ct];	/* coal production */
var o {r in oreg,ot in otyp} := i_o[r,ot];	/* oil production */
var ct {cr in creg,u in users} := i_ct[cr,u];	/* coal transportation levels */
var ot {Or in oreg,r in refin} := i_ot[Or,r];	/* crude oil transportation levels */
var lt {r in refin,u in users} := i_lt[r,u];	/* light transportation levels */
var ht {r in refin,u in users} := i_ht[r,u];	/* heavy transportation levels */
var p {co in comod,u in users} := iprice[co,u];	/* commodity prices */
var mu {R} := 1;		/* dual to ruse cons.; marginal utility */
var cv {creg} := 1;	/* dual to cmbal */
var ov {oreg} := 1;
var lv {refin} := 1;
var hv {refin} := 1;

delc {cr in creg,t in ctyp}:
  0 <= c[cr,t] <= cmax[cr,t] complements
	ccost[cr,t] + (sum {res in R} cruse[res,cr,t]*mu[res]) - cv[cr];

delo {r in oreg,t in otyp}:
  0 <= o[r,t] <= omax[r,t] complements
  ocost[r,t] + (sum {res in R} oruse[res,r,t]*mu[res]) - ov[r];

delct {cr in creg,u in users}:
  0 <= ct[cr,u] complements
  ctcost[cr,u] + cv[cr] >= p["C",u];

delot {Or in oreg,r in refin}:
  0 <= ot[Or,r] complements
  otcost[Or,r] + rcost[r] + ov[Or]   >=
  output[r,"L"] * lv[r] + output[r,"H"] * hv[r];

dellt {r in refin,u in users}:
  0 <= lt[r,u] complements
  ltcost[r,u] + lv[r] >= p["L",u];

delht {r in refin,u in users}:
  0 <= ht[r,u] complements
  htcost[r,u] + hv[r] >= p["H",u];

dembal {co in comod,u in users}:		/* excess supply of product */
  .1 <= p[co,u] complements
  (if ord(co) = 1 then sum {r in creg} ct[r,u])
  + (if ord(co) = 2 then sum {r in refin} lt[r,u])
  + (if ord(co) = 3 then sum {r in refin} ht[r,u])
  >= q0[co] * prod {cc in comod} (p[cc,u]/p0[cc])**esub[co,cc];

cmbal {cr in creg}:			/* coal material balance */
  cv[cr] complements
  sum {t in ctyp} c[cr,t] = sum {u in users} ct[cr,u];
  
ombal {Or in oreg}:			/* oil material balance */
  ov[Or] complements
  sum {t in otyp} o[Or,t] = sum {r in refin} ot[Or,r];

lmbal {r in refin}:			/* light material balance */
  lv[r] complements
  sum {Or in oreg} ot[Or,r] * output[r,"L"] = 
  sum {u in users} lt[r,u];

hmbal {r in refin}:			/* heavy material balance */
  hv[r] complements
  sum {Or in oreg} ot[Or,r] * output[r,"H"] =
  sum {u in users} ht[r,u];

ruse {res in R}:			/* resource use constraints */
  0 <= mu[res] complements
  rmax[res] >=
    sum {cr in creg, t in ctyp} c[cr,t]*cruse[res,cr,t]
  + sum {Or in oreg, t in otyp} o[Or,t]*oruse[res,Or,t];

