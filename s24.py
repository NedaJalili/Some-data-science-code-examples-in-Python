import statistics as ss

data1=[0,-1,3,4,3,4,0,5,8,9,-4,0,4,5]
data2=[456.7,547.8,926.6,236.1,543,439]
print("mean data1 = ",ss.mean(data1))
print("fmean data2 = ",ss.fmean(data2))
print("geometric_mean data2 = ",ss.geometric_mean(data2))
print("harmonic_mean data1 = ",ss.harmonic_mean(data1),"(oops! doesn't work!)")
print("harmonic_mean data2 = ",ss.harmonic_mean(data2))
print("median data1 = ",ss.median(data1))
print("median data2 = ",ss.median(data2))
print("multimode data1 = ",ss.multimode(data1))
print("multimode data2 = ",ss.multimode(data2))
print("variance data1 = ",ss.variance(data1))
print("pvariance data1 = ",ss.pvariance(data1))
print("variance data2 = ",ss.variance(data2))
print("pvariance data2 = ",ss.pvariance(data2))
print("stdev data1 = ",ss.stdev(data1))
print("pstdev data1 = ",ss.pstdev(data1))
print("stdev data2 = ",ss.stdev(data2))
print("pstdev data2 = ",ss.pstdev(data2))



