import tushare as ts


df = ts.get_stock_basics()

# reslut will be
#'''        name    industry    area       pe   outstanding     totals  totalAssets
#code
#600606   金丰投资     房产服务   上海     0.00     51832.01   51832.01    744930.44
#002285    世联行     房产服务   深圳    71.04     76352.17   76377.60    411595.28
#'''

stock_path = "../data/stock_names.csv"
cols_to_keep = ['name']
df[cols_to_keep].to_csv(stock_path)

