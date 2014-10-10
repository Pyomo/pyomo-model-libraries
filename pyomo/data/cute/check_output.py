import sys
import os

#name = sys.argv[1]

tests = ['aljazzaf','arwhead','avion2','bard','bdqrtic','biggs5','blockqp2','booth','bqp1var','bt10','bt13','bt1','bt2','bt3','bt9','byrdsphr','camel6','cantilvr','catena','cb2','cb3','chaconn1','chaconn2','chemrctb','cresc100','csfi2','degenlpa','degenlpb','demymalo','denschna','denschnb','denschnc','dixchlng','dixmaana','dixmaanb','dixon3dq','dqdrtic','dqrtic','eg1','eg2','eg3','engval1','errinros','expfit','explin2','explin','expquad','extrasim','extrosnb','fccu','hager1','hager2','makela1','makela3','matrix2','mifflin2','mistake','nondia','oet1','palmer1','powell20','robot','s368','sim2bqp','sisser','sosqp1','spiral','synthes1','tame','tfi2']

print len(tests)

for name in tests:
    os.system("ipopt %s.test.nl >new.out" %(name))
    os.system("ipopt %s.pyomo.nl >old.out" %(name))
    print name
    raw_input()
    os.system("diff new.out old.out")
    print
    raw_input()
