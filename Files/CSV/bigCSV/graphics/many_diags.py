import plotly.graph_objs as go
from plotly.subplots import make_subplots


diag1 = go.Bar(x=['Olya', 'Vasya', 'Petya'], y=[5, 2, 8], name='teeth')
diag2 = go.Bar(x=['milk', 'eggs', 'tomatoes', 'meat'], y=[100000, 40000, 12000, 214000], name='revenue')

# go.Figure(data=[diag1, diag2]).show()

fig = make_subplots(rows=2, cols=2)
fig.add_trace(diag1, row=1, col=2)
fig.add_trace(diag2, row=2, col=1)
fig.show()
