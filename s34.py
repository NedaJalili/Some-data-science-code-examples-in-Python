import pandas as pd
data={"phisics":[18,12,19],"chemistry":[16.25,15,20],"math":[14,13,18],
      "literature":[17,15,17]}
df=pd.DataFrame(data,index=["Ali","Mohammd","Reza"])

print(df)
print("-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.")
print(df.describe())
print("-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.")
print(df.corr())
