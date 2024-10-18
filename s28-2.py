import numpy_financial as npf
pmt=-100
nper=10*12
rate=0.05/12
fv=15692.93
x=npf.pv(rate,nper,pmt,fv)
print("pv = ",x)
