import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
f = pd.read_csv("telecom_churn.csv")


a = pd.DataFrame({"Customer service calls": f['Customer service calls'], "Churn": f['Churn']})
x = f['Customer service calls']
y = f['Churn']
plt.scatter(x,y)
plt.show()

fdsfsdf
print(a)