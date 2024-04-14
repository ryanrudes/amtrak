from amtrak.api.endpoints.trains import get_trains

def test_get_trains():
    trains = get_trains()
        
    import plotly.express as px
    import pandas as pd

    df = pd.DataFrame([{"id": train.object_id, "lat": train.latitude, "lon": train.longitude, "route": train.route} for train in trains])

    fig = px.scatter_geo(df, lat = "lat", lon = "lon", hover_name = "id", symbol = "route", color = "route")
    fig.update_layout(title = 'Train Map', title_x = 0.5)
    fig.show()