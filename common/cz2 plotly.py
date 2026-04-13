import plotly.express as px

#x = [1,2,3,4,5]
#y = [10,15,13,20,17]
#fig = px.line(x=x, y=y)
#fig.show()


import dash
from dash import dcc, html
import plotly.express as px
from plotly.matplotlylib.mpltools import prep_xy_axis
from pyarrow import show_info

# Dane
# x = [1,2,3,4,5]
# y1 = [10,15,13,20,17]
# y2 = [3,7,4,9,6]
#
# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]
#
# etykiety = ["Python","Java","C++","Javascript"]
# wartosci = [40,25,15,20]

# Wykresy
# fig_line = px.line(x=x, y=y1, title="Trend", markers=True)
# fig_bar = px.bar(x=produkty, y=wyniki, title="Produkty")
# fig_scatter = px.scatter(x=x, y=y2, title="Relacja")
# fig_hist = px.histogram(x=oceny, nbins=4, title="Oceny")
# fig_pie = px.pie(names=etykiety, values=wartosci, title="Języki")

# Dashboard
# app = dash.Dash(__name__)
#
# app.layout = html.Div(
#     style={"fontFamily": "Arial", "backgroundColor": "#f5f7fa"},
#     children=[
#         html.H1("Mój Dashboard", style={"textAlign": "center"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_line),
#             dcc.Graph(figure=fig_bar),
#         ], style={"display": "flex"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_scatter),
#             dcc.Graph(figure=fig_hist),
#         ], style={"display": "flex"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_pie)
#         ])
#     ]
# )
#
# if __name__ == "__main__":
#     app.run(debug=True)


#zad.4
#godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
#wyniki = [40, 50, 55, 60, 70, 75, 85]

#fig=px.scatter(x=godziny_nauki,y=wyniki, title = "wpływ czasu pswięconego na nauke na wyniki", labels={"x":"godziny", "y":"wyniki"})
#fig.show()

# #zad 5
# jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
# udzial = [35, 30, 15, 10, 10]
#
# fig_pie = px.pie (names =jezyki, values= udzial, title="Popularność języków programowania")
# fig_pie.show()

# #zad.6
# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# temperatura = [18, 20, 19, 23, 25, 22, 21]
#
# fig_line = px.line(x=dni, y=temperatura,title ="Temperatura w kolejnych dniach tygodnia",markers=True)
# fig_line.show()






















