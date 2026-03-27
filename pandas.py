import pandas as pd
import matplotlib.pyplot as plt

# Sales data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [200, 250, 300, 280, 350]
}

df = pd.DataFrame(data)

# Total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Plot line graph
plt.plot(df["Month"], df["Sales"], marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()