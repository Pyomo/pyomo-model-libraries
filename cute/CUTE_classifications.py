#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2025
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

import sys
import glob
import pprint

all_models = [name.replace('_cute.py','') for name in glob.glob('*_cute.py')]

smoke_models = []
moderate_models = []
expensive_models = []

asl_skipped_models = []
baseline_skipped_models = []

if sys.version_info[0] == 3:
    # These models use to many explicit opertions in a single
    # expression and crash the interpreter resulting in a message like
    # "RuntimeError: maximum recursion depth exceeded during compilation"
    asl_skipped_models.append('aug3dc')
    baseline_skipped_models.append('aug3dc')
    asl_skipped_models.append('aug3dcqp')
    baseline_skipped_models.append('aug3dcqp')

# Smoke Models ( pyomo construct time < 0.5s )
smoke_models.extend([\
'denschnb','denschna','alsotame','argauss','bratu1d','explin2',\
'hs084','mistake','hs080','hs081','hs083','demymalo','bt10','bt13',\
'cantilvr','powell20','explin','cresc100','rosenbr','byrdsphr',\
'mifflin1','mifflin2','avgasb','aircrftb','aircrfta','hs079','hs078',\
'sisser','aug2d','hs071','hs073','hs072','hs075','hs074','hs077',\
'fletcher','allinitu','aljazzaf','bard','allinitc','matrix2',\
'extrosnb','expfit','camel6','expquad','hs062','hs063','hs060',\
'hs061','hs066','hs067','hs064','avgasa','catena','bt1','bt3','bt2',\
'errinros','bt9','hs070','gigomez1','hs057','hs056','hs055','hs059',\
'chaconn1','denschnc','biggs6','hs076','biggs3','fccu','avion2',\
'dixchlng','extrasim','spiral','tame','arglinb','polak1','ncvxbqp1',\
'oet1','sosqp1','sim2bqp','box3','box2','brownden','booth','synthes1',\
'makela4','arglinc','makela2','makela3','makela1','palmer1','beale',\
'eg3','biggsc4','nondia','zy2','allinit','core1','csfi2','chaconn2',\
'bqp1var','cb2','cb3','fletchbv','hs065','dixon3dq','biggs5','s368',\
'degenlpb','degenlpa','robot','eg2','eg1','concon','congigmz',\
'clnlbeam','catenary','bt11','bt12','coolhans','brownal','brkmcc',\
'cresc4','cbratu2d','bt5','bt4','bt7','bt6','bt1','csfi1','cresc50',\
'bt8','cliff','cluster','cube','chnrosnb','brownbs','hvycrash',\
'hs268','hs087','hs088','hypcir','hs44new','hs35mod','hs105','hs104',\
'hs107','hs106','hs101','hs100','hs103','hs102','hs111lnp','hs99exp',\
'hs109','hs108','indef','hubfit','hs100lnp','jensmp','hs3mod','hs099',\
'hs098','hs093','hs097','hs096','hs095','hs116','hs117','hs114',\
'hs21mod','hs112','hs113','hs110','hs111','humps','hs118','hs119',\
'launch','lakes','linspanh','kowosb','kiwcresc','kissing','lewispol',\
'lch'])

asl_skipped_models.append('hs087')         # uses Piecewise (naming scheme is different)
asl_skipped_models.append('coolhans')      # AMPL does not eleminate Var*0 from expressions in NL file

baseline_skipped_models.extend([])




# Moderate Models ( 0.5 <= pyomo construct time < 5.0 )
moderate_models.extend([\
'corkscrw','brainpc0','brainpc1','bdexp','biggsb1','aug3dqp',\
'bdqrtic','hager1','dqdrtic','dqrtic','airport','artif','bdvalue',\
'chemrctb','blockqp5','aug3dc','bloweya','aug3dcqp','tfi2',\
'blockqp1','blockqp2','blockqp3','blockqp4','aug3d','dixmaana',\
'bigbank','argtrig','chenhark','cragglvy','chandheq','chebyqad',\
'cosine','chemrcta','chainwoo','broydn3d','broydn7d','huestis',\
'integreq','hs085','hs089','hues-mod','hs092','hs091','hs090',\
'hairy','growthls','gausselm','fletchcr','engval2','djtl',\
'fminsurf','gulf','genhs28','hart6','goffin','growth','gilbert',\
'dixmaane','genrose','haldmads','gottfr','genhumps','harkerp2',\
'hatflda','gouldqp2','gouldqp3','fminsrf2','expfita','expfitc',\
'expfitb','edensch','liswet1','liarwhd','liswet2','ksip',\
'liswet12','liswet10','liswet5','liswet4','liswet3'])

asl_skipped_models.append('hs085')         # AMPL model uses "substitution" vars exposing an ASL bug
                                           # therefore we can't compare the models through asl (yet)
asl_skipped_models.append('brainpc0')      # unexplained differences with AMPL
asl_skipped_models.append('haldmads')      # AMPL does not reclassify a nonlinear constraint that becomes linear
asl_skipped_models.append('djtl')          # unexplained differences with AMPL

baseline_skipped_models.extend([])




# Expensive Models ( 5.0 <= t )
expensive_models.extend([\
'hager3','arwhead','cvxqp3','tridia','dtoc1l','hager4',\
'drcav3lq','arglina','engval1','dixmaanb','hager2','srosenbr',\
'clplatea','clplatec','clplateb','brybnd','curly10','curly20',\
'curly30','freuroth','gpp','dixmaanc','dixmaand','dixmaanf'])

asl_skipped_models.extend([])

baseline_skipped_models.extend([])


if set(all_models) != set(smoke_models+moderate_models+expensive_models):
    sys.stdout.write("\n")
    sys.stdout.write("WARNING: The following cute models are not classifed and so will not be tested:\n")
    sys.stdout.write("         (someone should classify them)\n")
    sys.stdout.write("\n")
    pprint.pprint(set(all_models).difference(set(smoke_models+moderate_models+expensive_models)))

if len(asl_skipped_models+baseline_skipped_models) > 0:
    sys.stdout.write("\n")
    sys.stdout.write("***NOTE: The following cute models are being skipped in various tests:\n")
    sys.stdout.write("\n")
    pprint.pprint(set(asl_skipped_models+baseline_skipped_models))
