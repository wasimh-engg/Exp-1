import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
student={
    "Name":["John","Mary","David"],
    "Marks":[85,90,78]

}

df=pd.DataFrame(student)
sns.barplot(x="Name",y="Marks",data=df)
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()
print(df)