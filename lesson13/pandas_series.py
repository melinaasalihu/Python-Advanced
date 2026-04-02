import pandas as pd

product = ['apples', 'bananas', 'oranges', 'grapes','pineapples']

sales = [150,200,180,90,60]

sales_series = pd.series(sales, index=product)

print(sales_series)


print(sales_series['grapes'])

total_sales = sales_series.sum()
print(total_sales)


best_selling_product = sales_series.idmax()
print(f"best selling product: {best_selling_product}")

