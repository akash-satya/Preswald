import pandas as pd
import plotly.express as px

from preswald import connect, get_df, text, table, slider, plotly

# 1. Init
connect()
df = get_df("my_dataset")

# 2. Clean up
df.columns = [c.strip().strip("'") for c in df.columns]
df["Present_Price"] = pd.to_numeric(df["Present_Price"], errors="coerce")
df["Kms_Driven"]   = pd.to_numeric(df["Kms_Driven"], errors="coerce")

# Header
text("# 🚗 Car Price Explorer")
text("Use the slider below to filter by price, and explore two different charts.")

# Slider and Table
min_price = slider("Min Present Price (lakhs)", min_val=0, max_val=15, default=5)
filtered = df[df["Present_Price"] > min_price]

text(f"Showing **{len(filtered)}** cars with price > {min_price} lakhs:")
table(filtered, title="Filtered Cars")

# Scatter Plot
text("## 📊 Scatter: Kms Driven vs Present Price")
fig_scatter = px.scatter(
    filtered,
    x="Kms_Driven",
    y="Present_Price",
    color="Fuel_Type",
    hover_data=["Car_Name", "Year"]
)
plotly(fig_scatter)

# Histogram
text("## 📈 Distribution: Present Price")
fig_hist = px.histogram(
    filtered,
    x="Present_Price",
    nbins=20,
    title="How many cars fall into each price bucket?"
)
plotly(fig_hist)
