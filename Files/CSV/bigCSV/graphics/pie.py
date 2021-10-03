import plotly.graph_objs as go


products = ['nokia 12x', 'xiaomi 11', 'sasung 10s', 'iphone 13', 'oppo xsx']
prices = [12000, 4000, 15000, 20000, 13000]

diag = go.Pie(labels=products, values=prices)
go.Figure(data=[diag]).show()
