country_data= ['UnitedStates','GreatBritain','China','Russia','Germany']
medal_data = [46,27,26,19,17]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of countries")
plt.show()
