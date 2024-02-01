import pandas as pd
data = {
    'Product':['A','B','A','C','B','A'],
    'Sales':[150,200,100,120,180,250],
    'Profit':[20,30, 15,10,25,35]
    }
sales_data =pd.DataFrame(data)
print (sales_data)
# Step 4: Calculate Total Sales and Profit
total_sales = sales_data['Sales'].sum()
total_profit = sales_data['Profit'].sum()

print(f'Total Sales: {total_sales}')
print(f'Total Profit: {total_profit}')
# Step 5: Average Profit per Sale
average_profit_per_sale = sales_data['Profit'].mean()

print(f'Average Profit per Sale: {average_profit_per_sale}')
# Step 6: Highest Selling Product
highest_selling_product = sales_data.groupby('Product')['Sales'].sum().idxmax()

print(f'Highest Selling Product: {highest_selling_product}')
# Step 7: Profitable Products
profitable_products = sales_data[sales_data['Profit'] > 20]['Product'].tolist()
print(f'Profitable Products: {profitable_products}')
# Step 9: Save to Excel
sales_data.to_csv('output2.csv', index=False)
print(f'DataFrame has been saved to {'output2.csv'}')


