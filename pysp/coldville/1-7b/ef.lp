\ Begin objective block for master
min 
obj: 
+1.000000 MASTER_EXPECTED_COST_RootNode

\ End objective block for master

s.t.

\ Begin constraint block for master
MASTER_c_l_COST_WarmWinterNode_SecondStageCost_None_:
+1.000000 MASTER_EXPECTED_COST_WarmWinterNode
-1.000000 MASTER_WarmWinterNode_SecondStageCost
>= 0.0

MASTER_c_u_COST_WarmWinterNode_SecondStageCost_None_:
+1.000000 MASTER_EXPECTED_COST_WarmWinterNode
-1.000000 MASTER_WarmWinterNode_SecondStageCost
<= 0.0

MASTER_c_l_ColdWinterScenario_SummerMaterialPurchase_SALT_:
-1.000000 ColdWinterScenario_SummerMaterialPurchase(SALT)
+1.000000 MASTER_RootNode_SummerMaterialPurchase(SALT)
>= 0.0

MASTER_c_u_ColdWinterScenario_SummerMaterialPurchase_SALT_:
-1.000000 ColdWinterScenario_SummerMaterialPurchase(SALT)
+1.000000 MASTER_RootNode_SummerMaterialPurchase(SALT)
<= 0.0

MASTER_c_l_WarmWinterScenario_WarmWinterNode_SecondStageCost_None_:
+1.000000 MASTER_WarmWinterNode_SecondStageCost
-1.000000 WarmWinterScenario_SecondStageCost
>= 0.0

MASTER_c_u_WarmWinterScenario_WarmWinterNode_SecondStageCost_None_:
+1.000000 MASTER_WarmWinterNode_SecondStageCost
-1.000000 WarmWinterScenario_SecondStageCost
<= 0.0

MASTER_c_l_WarmWinterScenario_SummerMaterialPurchase_FUEL_:
+1.000000 MASTER_RootNode_SummerMaterialPurchase(FUEL)
-1.000000 WarmWinterScenario_SummerMaterialPurchase(FUEL)
>= 0.0

MASTER_c_u_WarmWinterScenario_SummerMaterialPurchase_FUEL_:
+1.000000 MASTER_RootNode_SummerMaterialPurchase(FUEL)
-1.000000 WarmWinterScenario_SummerMaterialPurchase(FUEL)
<= 0.0

MASTER_c_l_ColdWinterScenario_ColdWinterNode_SecondStageCost_None_:
-1.000000 ColdWinterScenario_SecondStageCost
+1.000000 MASTER_ColdWinterNode_SecondStageCost
>= 0.0

MASTER_c_u_ColdWinterScenario_ColdWinterNode_SecondStageCost_None_:
-1.000000 ColdWinterScenario_SecondStageCost
+1.000000 MASTER_ColdWinterNode_SecondStageCost
<= 0.0

MASTER_c_l_WarmWinterScenario_SummerMaterialPurchase_SALT_:
+1.000000 MASTER_RootNode_SummerMaterialPurchase(SALT)
-1.000000 WarmWinterScenario_SummerMaterialPurchase(SALT)
>= 0.0

MASTER_c_u_WarmWinterScenario_SummerMaterialPurchase_SALT_:
+1.000000 MASTER_RootNode_SummerMaterialPurchase(SALT)
-1.000000 WarmWinterScenario_SummerMaterialPurchase(SALT)
<= 0.0

MASTER_c_l_COST_RootNode_FirstStageCost_None_:
-0.600000 MASTER_EXPECTED_COST_ColdWinterNode
+1.000000 MASTER_EXPECTED_COST_RootNode
-0.400000 MASTER_EXPECTED_COST_WarmWinterNode
-1.000000 MASTER_RootNode_FirstStageCost
>= 0.0

MASTER_c_u_COST_RootNode_FirstStageCost_None_:
-0.600000 MASTER_EXPECTED_COST_ColdWinterNode
+1.000000 MASTER_EXPECTED_COST_RootNode
-0.400000 MASTER_EXPECTED_COST_WarmWinterNode
-1.000000 MASTER_RootNode_FirstStageCost
<= 0.0

MASTER_c_l_ColdWinterScenario_RootNode_FirstStageCost_None_:
-1.000000 ColdWinterScenario_FirstStageCost
+1.000000 MASTER_RootNode_FirstStageCost
>= 0.0

MASTER_c_u_ColdWinterScenario_RootNode_FirstStageCost_None_:
-1.000000 ColdWinterScenario_FirstStageCost
+1.000000 MASTER_RootNode_FirstStageCost
<= 0.0

MASTER_c_l_ColdWinterScenario_SummerMaterialPurchase_FUEL_:
-1.000000 ColdWinterScenario_SummerMaterialPurchase(FUEL)
+1.000000 MASTER_RootNode_SummerMaterialPurchase(FUEL)
>= 0.0

MASTER_c_u_ColdWinterScenario_SummerMaterialPurchase_FUEL_:
-1.000000 ColdWinterScenario_SummerMaterialPurchase(FUEL)
+1.000000 MASTER_RootNode_SummerMaterialPurchase(FUEL)
<= 0.0

MASTER_c_l_WarmWinterScenario_RootNode_FirstStageCost_None_:
+1.000000 MASTER_RootNode_FirstStageCost
-1.000000 WarmWinterScenario_FirstStageCost
>= 0.0

MASTER_c_u_WarmWinterScenario_RootNode_FirstStageCost_None_:
+1.000000 MASTER_RootNode_FirstStageCost
-1.000000 WarmWinterScenario_FirstStageCost
<= 0.0

MASTER_c_l_COST_ColdWinterNode_SecondStageCost_None_:
-1.000000 MASTER_ColdWinterNode_SecondStageCost
+1.000000 MASTER_EXPECTED_COST_ColdWinterNode
>= 0.0

MASTER_c_u_COST_ColdWinterNode_SecondStageCost_None_:
-1.000000 MASTER_ColdWinterNode_SecondStageCost
+1.000000 MASTER_EXPECTED_COST_ColdWinterNode
<= 0.0

MASTER_c_e_ONE_VAR_CONSTANT: 
MASTER_ONE_VAR_CONSTANT = 1.0

\ End constraint block for master 
\ Begin constraint block for scenario WarmWinterScenario
WarmWinterScenario_c_u_TotalTruckdayRule_:
+1.000000 WarmWinterScenario_TruckdayUsedinMethod(PLOWING)
+1.000000 WarmWinterScenario_TruckdayUsedinMethod(SALTING)
<= 5000.0

WarmWinterScenario_c_e_ComputeSecondStageCost_:
+65.000000 WarmWinterScenario_SalvagedMaterial(FUEL)
+15.000000 WarmWinterScenario_SalvagedMaterial(SALT)
+1.000000 WarmWinterScenario_SecondStageCost
-110.000000 WarmWinterScenario_TruckdayUsedinMethod(PLOWING)
-110.000000 WarmWinterScenario_TruckdayUsedinMethod(SALTING)
-73.000000 WarmWinterScenario_WinterMaterialPurchase(FUEL)
-30.000000 WarmWinterScenario_WinterMaterialPurchase(SALT)
= 0.0

WarmWinterScenario_c_l_DemandRule_:
+1.000000 WarmWinterScenario_TruckdayUsedinMethod(PLOWING)
+1.200000 WarmWinterScenario_TruckdayUsedinMethod(SALTING)
>= 3500.0

WarmWinterScenario_c_e_BalanceRule(FUEL)_:
-1.000000 WarmWinterScenario_SalvagedMaterial(FUEL)
+1.000000 WarmWinterScenario_SummerMaterialPurchase(FUEL)
-1.000000 WarmWinterScenario_TruckdayUsedinMethod(PLOWING)
-1.000000 WarmWinterScenario_TruckdayUsedinMethod(SALTING)
+1.000000 WarmWinterScenario_WinterMaterialPurchase(FUEL)
= 0.0

WarmWinterScenario_c_e_BalanceRule(SALT)_:
-1.000000 WarmWinterScenario_SalvagedMaterial(SALT)
+1.000000 WarmWinterScenario_SummerMaterialPurchase(SALT)
+0.000000 WarmWinterScenario_TruckdayUsedinMethod(PLOWING)
-1.000000 WarmWinterScenario_TruckdayUsedinMethod(SALTING)
+1.000000 WarmWinterScenario_WinterMaterialPurchase(SALT)
= 0.0

WarmWinterScenario_c_e_ComputeFirstStageCost_:
+1.000000 WarmWinterScenario_FirstStageCost
-70.000000 WarmWinterScenario_SummerMaterialPurchase(FUEL)
-20.000000 WarmWinterScenario_SummerMaterialPurchase(SALT)
= 0.0

WarmWinterScenario_c_e_ONE_VAR_CONSTANT: 
WarmWinterScenario_ONE_VAR_CONSTANT = 1.0

\ End constraint block for scenario WarmWinterScenario

\ Begin constraint block for scenario ColdWinterScenario
ColdWinterScenario_c_u_TotalTruckdayRule_:
+1.000000 ColdWinterScenario_TruckdayUsedinMethod(PLOWING)
+1.000000 ColdWinterScenario_TruckdayUsedinMethod(SALTING)
<= 5000.0

ColdWinterScenario_c_e_ComputeSecondStageCost_:
+65.000000 ColdWinterScenario_SalvagedMaterial(FUEL)
+15.000000 ColdWinterScenario_SalvagedMaterial(SALT)
+1.000000 ColdWinterScenario_SecondStageCost
-120.000000 ColdWinterScenario_TruckdayUsedinMethod(PLOWING)
-120.000000 ColdWinterScenario_TruckdayUsedinMethod(SALTING)
-73.000000 ColdWinterScenario_WinterMaterialPurchase(FUEL)
-32.000000 ColdWinterScenario_WinterMaterialPurchase(SALT)
= 0.0

ColdWinterScenario_c_l_DemandRule_:
+1.000000 ColdWinterScenario_TruckdayUsedinMethod(PLOWING)
+1.100000 ColdWinterScenario_TruckdayUsedinMethod(SALTING)
>= 5100.0

ColdWinterScenario_c_e_BalanceRule(FUEL)_:
-1.000000 ColdWinterScenario_SalvagedMaterial(FUEL)
+1.000000 ColdWinterScenario_SummerMaterialPurchase(FUEL)
-1.000000 ColdWinterScenario_TruckdayUsedinMethod(PLOWING)
-1.000000 ColdWinterScenario_TruckdayUsedinMethod(SALTING)
+1.000000 ColdWinterScenario_WinterMaterialPurchase(FUEL)
= 0.0

ColdWinterScenario_c_e_BalanceRule(SALT)_:
-1.000000 ColdWinterScenario_SalvagedMaterial(SALT)
+1.000000 ColdWinterScenario_SummerMaterialPurchase(SALT)
+0.000000 ColdWinterScenario_TruckdayUsedinMethod(PLOWING)
-1.000000 ColdWinterScenario_TruckdayUsedinMethod(SALTING)
+1.000000 ColdWinterScenario_WinterMaterialPurchase(SALT)
= 0.0

ColdWinterScenario_c_e_ComputeFirstStageCost_:
+1.000000 ColdWinterScenario_FirstStageCost
-70.000000 ColdWinterScenario_SummerMaterialPurchase(FUEL)
-20.000000 ColdWinterScenario_SummerMaterialPurchase(SALT)
= 0.0

ColdWinterScenario_c_e_ONE_VAR_CONSTANT: 
ColdWinterScenario_ONE_VAR_CONSTANT = 1.0

\ End constraint block for scenario ColdWinterScenario

bounds

\ Begin variable bounds block for master
     -inf <=  MASTER_ColdWinterNode_SecondStageCost  <= +inf
     -inf <=  MASTER_EXPECTED_COST_ColdWinterNode  <= +inf
     -inf <=  MASTER_EXPECTED_COST_RootNode  <= +inf
     -inf <=  MASTER_EXPECTED_COST_WarmWinterNode  <= +inf
     -inf <=  MASTER_RootNode_FirstStageCost  <= +inf
     -inf <=  MASTER_RootNode_SummerMaterialPurchase(FUEL)  <= +inf
     -inf <=  MASTER_RootNode_SummerMaterialPurchase(SALT)  <= +inf
     -inf <=  MASTER_WarmWinterNode_SecondStageCost  <= +inf
\ End variable bounds block for master

\ Begin variable bounds block for scenario WarmWinterScenario
     -inf <=  WarmWinterScenario_FirstStageCost  <= +inf
    0.0 <=  WarmWinterScenario_SalvagedMaterial(FUEL)  <= +inf
    0.0 <=  WarmWinterScenario_SalvagedMaterial(SALT)  <= +inf
     -inf <=  WarmWinterScenario_SecondStageCost  <= +inf
    0.0 <=  WarmWinterScenario_SummerMaterialPurchase(FUEL)  <= +inf
    0.0 <=  WarmWinterScenario_SummerMaterialPurchase(SALT)  <= +inf
    0.0 <=  WarmWinterScenario_TruckdayUsedinMethod(PLOWING)  <= +inf
    0.0 <=  WarmWinterScenario_TruckdayUsedinMethod(SALTING)  <= +inf
    0.0 <=  WarmWinterScenario_WinterMaterialPurchase(FUEL)  <= +inf
    0.0 <=  WarmWinterScenario_WinterMaterialPurchase(SALT)  <= +inf
\ End variable bounds block for scenario WarmWinterScenario

\ Begin variable bounds block for scenario ColdWinterScenario
     -inf <=  ColdWinterScenario_FirstStageCost  <= +inf
    0.0 <=  ColdWinterScenario_SalvagedMaterial(FUEL)  <= +inf
    0.0 <=  ColdWinterScenario_SalvagedMaterial(SALT)  <= +inf
     -inf <=  ColdWinterScenario_SecondStageCost  <= +inf
    0.0 <=  ColdWinterScenario_SummerMaterialPurchase(FUEL)  <= +inf
    0.0 <=  ColdWinterScenario_SummerMaterialPurchase(SALT)  <= +inf
    0.0 <=  ColdWinterScenario_TruckdayUsedinMethod(PLOWING)  <= +inf
    0.0 <=  ColdWinterScenario_TruckdayUsedinMethod(SALTING)  <= +inf
    0.0 <=  ColdWinterScenario_WinterMaterialPurchase(FUEL)  <= +inf
    0.0 <=  ColdWinterScenario_WinterMaterialPurchase(SALT)  <= +inf
\ End variable bounds block for scenario ColdWinterScenario

end
