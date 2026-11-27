from dash import Dash, dcc, html
import plotly.graph_objects as go

from main import build_market_snapshot


snapshot = build_market_snapshot()
instrument = snapshot["instrument"]
benchmark = snapshot["benchmark"]

figure = go.Figure()

for asset, series in (
    (instrument, snapshot["instrument_base_100"]),
    (benchmark, snapshot["benchmark_base_100"]),
):
    figure.add_trace(
        go.Scatter(
            x=[row["date"] for row in series],
            y=[row["value"] for row in series],
            mode="lines",
            name=f"{asset['ticker']} – {asset['name']}",
        )
    )

figure.update_layout(
    title="Instrument vs Benchmark — Base 100",
    xaxis_title="Date",
    yaxis_title="Base 100",
    hovermode="x unified",
)

app = Dash(__name__)
app.title = "MarketPulse"

app.layout = html.Main([
    html.H1("MarketPulse"),
    html.P(f"Provider: {snapshot['provider']}"),
    html.P(f"Access mode: {snapshot['access_mode']}"),
    html.P(f"Instrument: {instrument['ticker']} – {instrument['name']}"),
    html.P(f"Benchmark: {benchmark['ticker']} – {benchmark['name']}"),
    html.P(f"Period: {snapshot['lookback']}"),
    html.P(f"Interval: {snapshot['interval']}"),

    html.H2("Performance"),
    html.P(f"Instrument return: {snapshot['instrument_return']:+.2f}%"),
    html.P(f"Benchmark return: {snapshot['benchmark_return']:+.2f}%"),
    html.P(
        f"Relative performance: "
        f"{snapshot['relative_performance']:+.2f} percentage points"
    ),

    dcc.Graph(figure=figure),
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)