import yfinance as yf
from scipy.stats import pearsonr
import matplotlib.pyplot as py
import seaborn as sns
from sklearn.preprocessing import normalize
import numpy as np
import math

#Download datasets 
treasury = yf.download("^TNX", "2019-02-10", "2021-02-28")['Close']
tesla = yf.download("TSLA", "2019-02-10", "2021-02-28")['Close'][:len(treasury)]
volume = yf.download("^NYA", "2019-02-10", "2021-02-28")['Close'][:len(treasury)]

print(len(treasury))
print(len(tesla))
print(len(volume))

# Convert string values to float
for x in range(len(treasury)):
    treasury[x] = float(treasury[x])
    tesla[x] = float(tesla[x])
    volume[x] = float(volume[x])

# Calculate correlation
corr1, _ = pearsonr(tesla, treasury)
corr2, _ = pearsonr(volume,tesla)
corr3, _ = pearsonr(volume, treasury)
print(corr1,corr2,corr3)

# Get normalized values to plot regression line

tesla_norm = normalize(np.array(tesla).reshape(1, -1))
treasury_norm =  normalize(np.array(treasury).reshape(1, -1))
volume_norm =  normalize(np.array(volume).reshape(1, -1))

# Plot scatter graph with regression line 
tes_tres_plot = sns.regplot(tesla_norm, treasury_norm, ci=None).set(title="Normalised TSLA vs ^TNX     Rsquared: " +str(np.round(corr1,decimals=2)),xlabel='TSLA Close',ylabel='^TNX Close')
py.show()

vol_tres_plot = sns.regplot(volume_norm, tesla_norm, ci=None).set(title="Normalised  ^NYA vs TSLA      Rsquared:" +str(np.round(corr2,decimals=2)),xlabel='^NYA Close',ylabel='TSLA Close')
py.show()

vol_tes_plot = sns.regplot(volume_norm, treasury_norm, ci=None).set(title="Normalised ^NYA vs ^TNX     Rsquared:" +str(np.round(corr3,decimals=2)),xlabel='^NYA Close',ylabel='^TNX Close')
py.show()

apple = yf.download("AAPL", "2019-02-10", "2021-02-28")['Close'][:len(treasury)]

for x in range(len(apple)):
    apple[x] = float(apple[x])

corr4, _ = pearsonr(tesla, apple)
print(corr4)
apple_norm =  normalize(np.array(apple).reshape(1, -1))
tes_apple_plot = sns.regplot(tesla_norm, apple_norm, ci=None).set(title="Normalised TSLA vs AAPL     Rsquared: " +str(np.round(corr4,decimals=2)),xlabel='TSLA Close',ylabel='AAPL Close')
py.show()