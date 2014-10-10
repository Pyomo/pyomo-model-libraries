\* Source Pyomo model name=unknown *\

min 
x1:
+1 x4
+2 x5

s.t.

c_l_x2_:
+3 x4
+4 x5
>= 1

c_l_x3_:
+2 x4
+5 x5
>= 2

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds 
   0 <= x4 <= +inf
   0 <= x5 <= +inf
end 
