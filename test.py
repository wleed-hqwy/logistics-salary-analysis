import pandas as pd 
import matplotlib.pyplot as plt
df_report = pd.read_csv("city_summary_report_csv")
plt.figure(figsize=(8, 5))
plt.bar(df_report["City"], df_report["Total_Comp"], color='skyblue', edgecolor='black')
plt.title("Average income by city", fontsize=14, fontweight='bold')
plt.xlabel("المدينة", fontsize=12)
plt.ylabel("اجمالي الدخل", fontsize=12)
plt.savefig("city_chart.png")
print("The graph has been created and saved")
plt.show()