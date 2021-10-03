import plotly.graph_objs as go


students = ['Masha', 'Pasha', 'Vasya', 'Olya']
marks = [12, 10, 3, 11]

diag = go.Bar(x=students, y=marks)
go.Figure(data=[diag]).write_html('marks.html', auto_open=True)
