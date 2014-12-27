
param M integer >= 1, := 30;	/* subjects or consumers */
param N integer >= 1, := 14;	/* brand names */

set subjects := 1 .. M;
set brands := 1 .. N;
set ingred := {"asp","asub","caff","aing"};

param chi >= 0, := 3;	/* randomness increases as chi decreases */
param Kdemand;		/* demand for no drug at all */
param K := 1;		/* constant term in probability function */
			/* representing "no purchase" option */
param x {j in brands, k in ingred};	/* j's amount of ingredient k */
param y {i in subjects, k in ingred};	/* i's preference for k */
param v {i in subjects};		/* i's importance weight for all k */
param w {i in subjects};		/* constant in DU eqn */
param b {i in subjects};		/* constant in DU eqn */
param c {j in brands};			/* average cost for producing j */
param p_current {j in brands};		/* existing market prices */
param p_init {j in brands} := c[j] + .01;	/* initial price iterate */
param p_solu {j in brands};		/* soln from Choi, DeSarbo, Harker */
param demand {j in brands};		/* computed demands */
param DU {i in subjects, j in brands} :=
	-chi * (v[i] * sum {k in ingred} (x[j,k]-y[i,k])^2 + b[i]);
/* DU is a computed parameter, such that
   -chi(DU_{ij}) = w_i*p_j + DU[i,j]
*/

param p_lo {j in brands} := (if j != 8 then c[j] else .199);
param p_up {j in brands} := (if j != 8 then Infinity else .199);

var p {j in brands} >= p_lo[j], <= p_up[j], := p_init[j];
var dutil {i in subjects, j in brands} = exp(w[i]*p[j]+DU[i,j]);

mprofit {j in brands}:	/* marginal profit for brand j */
	p[j] *
(	(-1/M) * sum {i in subjects}
	( dutil[i,j]
	  / ( K + sum {jj in brands} dutil[i,jj] )
	  * (1 + (p[j]-c[j]) * w[i]
	    * ( K + sum {jj in brands:jj != j} dutil[i,jj] )
	    / ( K + sum {jj in brands} dutil[i,jj] )
	    )
	)
)
	= 0;
