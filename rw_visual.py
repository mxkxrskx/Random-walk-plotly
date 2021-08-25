from randomwalk import RandomWalk
from plotly import offline
import plotly.graph_objects as go

while True:
    times = 50000
    rw = RandomWalk(times)
    rw.fill_walk()
    rw.take_first_dot()
    rw.take_last_dot()

    # Create figure
    fig = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=rw.x_first_dot, y=rw.y_first_dot,
        mode='markers', marker_color='rgba(207, 0, 15, 1)',
        name='First dot', marker_line_width=1, marker_size=10))

    fig.add_trace(go.Scatter(x=rw.x_values, y=rw.y_values,
        mode='markers', marker_color='rgba(255, 182, 193, .9)',
        marker_line_width=1, marker_size=5))

    fig.add_trace(go.Scatter(
        x=rw.x_last_dot, y=rw.y_last_dot,
        mode='markers', marker_color='rgba(77, 5, 232, 1)',
        name='Last dot', marker_line_width=2, marker_size=10))

    fig.update_layout(
        title=f'Random walk - {times} times', yaxis_zeroline=False,
        xaxis_zeroline=False, plot_bgcolor='white',
        legend=dict(
        orientation='h',
        yanchor='bottom',
        xanchor='left'
        ))

    #show a diagramm
    offline.plot(fig, filename='rw.html')

    keep_runing = input('Make another walk? (y/n) ')
    if keep_running.lower() == 'n':
        break
