import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HomeVista AI",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main{
    background:#0f172a;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

/* Clean Sidebar Navigation */
[data-testid="stSidebar"] [data-testid="stRadio"] > label {
    font-size: 14px;
    font-weight: 600;
    color: #94a3b8;
    margin-bottom: 8px;
}

[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] {
    gap: 6px;
}

/* Completely hide radio circles */
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label > div:first-child,
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label > div:first-child > div:first-child {
    display: none !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] input[type="radio"] {
    display: none !important;
}

/* Navigation items */
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label {
    padding: 11px 14px;
    border-radius: 10px;
    margin: 2px 0;
    color: #e2e8f0;
    font-size: 16px;
    font-weight: 500;
    transition: 0.2s;
}

/* Hover */
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:hover {
    background: #1e3a5f;
}

/* Selected item */
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
    background: #2563eb;
    color: white;
    font-weight: 600;
}

[data-testid="stMetric"]{
    background:#1e293b;
    border-radius:15px;
    padding:15px;
    border:1px solid #334155;
    box-shadow:0 2px 10px rgba(0,0,0,.30);
}

[data-testid="stMetricLabel"]{
    color:white !important;
    font-weight:600;
}

[data-testid="stMetricValue"]{
    color:white !important;
    font-size:34px;
    font-weight:bold;
}

div[data-testid="stVerticalBlock"]>div:has(div.house-card){
    margin-bottom:15px;
}

.house-card{
    background:#1e293b;
    color:white;
    padding:18px;
    border-radius:15px;
    border-left:6px solid #3b82f6;
    box-shadow:0px 4px 15px rgba(0,0,0,.35);
}

.house-card h3,
.house-card p,
.house-card strong,
.house-card span{
    color:white !important;
}

.title{
    font-size:42px;
    font-weight:700;
    color:#0F172A;
}

.subtitle{
    color:#64748B;
    font-size:18px;
}

</style>
""",unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("dataset/clean_house_data.csv")

df=load_data()

@st.cache_resource
def load_model():
    return joblib.load("model/model.pkl")

model=load_model()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("""
# 🏡 HomeVista AI

### Property Analytics Platform

---
""")

page=st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Market Analysis",
        "🔍 Smart House Finder",
        "🤖 Price Prediction",
        "📈 Market Insights"
    ]
)

# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#2563eb,#4f46e5);
    padding:35px;
    border-radius:18px;
    color:white;
    text-align:center;
    margin-bottom:20px;
    ">

    <h1 style="margin:0;font-size:46px;">
    🏡 HomeVista AI
    </h1>

    <p style="font-size:20px;margin-top:10px;">
    AI Powered Property Analytics & Smart Price Prediction
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    total_properties = len(df)
    total_locations = df["location"].nunique()
    avg_price = df["price"].mean()
    avg_sqft = df["total_sqft"].mean()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🏘 Properties",
        f"{total_properties:,}"
    )

    c2.metric(
        "📍 Locations",
        total_locations
    )

    c3.metric(
        "💰 Average Price",
        f"₹ {avg_price:.2f} L"
    )

    c4.metric(
        "📐 Average Area",
        f"{avg_sqft:.0f} sqft"
    )

    st.write("")

    left, right = st.columns([2,1])

    with left:

       

        st.write("")

        st.subheader("Platform Highlights")

        st.markdown("""
    ### 🚀 Features

    ✔ Interactive Market Analysis

    ✔ Smart House Recommendation

    ✔ AI Price Prediction

    ✔ Market Insights Dashboard
    """)

    with right:

        st.subheader("Quick Statistics")

        st.metric(
            "Highest Price",
            f"₹ {df['price'].max():.2f} L"
        )

        st.metric(
            "Lowest Price",
            f"₹ {df['price'].min():.2f} L"
        )

        st.metric(
            "Average Bathrooms",
            f"{df['bath'].mean():.1f}"
        )

        st.metric(
            "Average Balcony",
            f"{df['balcony'].mean():.1f}"
        )


    st.divider()

    st.subheader("📊 Most Active Locations")

    top_locations = (
        df["location"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_locations.columns = [
        "Location",
        "Properties"
    ]

    fig = px.bar(
        top_locations,
        x="Location",
        y="Properties",
        title="Top 10 Locations by Number of Properties"
    )

    fig.update_traces(marker_color="#3b82f6")
    fig.update_layout(

        template="plotly_dark",

        height=500,

        title_x=0.5,

        title_font_size=22,

        margin=dict(l=20,r=20,t=60,b=20)
    )
    title_x=0.5

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ============================================================
# MARKET ANALYSIS
# ============================================================

elif page == "📊 Market Analysis":

    st.markdown("<div class='title'>📊 Housing Market Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Explore trends using interactive visualizations.</div>", unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        selected_location = st.selectbox(
            "📍 Location",
            ["All"] + sorted(df["location"].dropna().unique().tolist())
        )

    with col2:
        selected_bhk = st.selectbox(
            "🛏 BHK",
            ["All"] + sorted(df["BHK"].unique().tolist())
        )

    filtered = df.copy()

    if selected_location != "All":
        filtered = filtered[
            filtered["location"] == selected_location
        ]

    if selected_bhk != "All":
        filtered = filtered[
            filtered["BHK"] == selected_bhk
        ]

    st.success(f"Showing {len(filtered)} Properties")

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        fig = px.histogram(
            filtered,
            x="price",
            nbins=40,
            title="Price Distribution"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.box(
            filtered,
            y="price",
            title="Price Spread"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        bhk = (
            filtered["BHK"]
            .value_counts()
            .sort_index()
        )

        fig = px.bar(
            x=bhk.index,
            y=bhk.values,
            labels={
                "x":"BHK",
                "y":"Properties"
            },
            title="BHK Distribution"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        area = filtered["area_type"].value_counts()

        fig = px.pie(
            values=area.values,
            names=area.index,
            hole=0.45,
            title="Area Type Distribution"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    fig = px.scatter(
        filtered,
        x="total_sqft",
        y="price",
        color="BHK",
        hover_name="location",
        title="Area vs Price"
    )

    fig.update_layout(

        template="plotly_dark",

        height=500,

        title_x=0.5,

        title_font_size=22,

        margin=dict(l=20,r=20,t=60,b=20)
    )
    title_x=0.5

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    top = (
        filtered.groupby("location")["price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="location",
        y="price",
        color="price",
        title="Top 10 Highest Average Price Locations"
    )

    fig.update_traces(marker_color="#3b82f6")

    fig.update_layout(

        template="plotly_dark",

        height=500,

        title_x=0.5,

        title_font_size=22,

        margin=dict(l=20,r=20,t=60,b=20)
    )
    title_x=0.5

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    corr = filtered.select_dtypes(include=np.number).corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )

    fig.update_layout(

        template="plotly_dark",

        height=500,

        title_x=0.5,

        title_font_size=22,

        margin=dict(l=20,r=20,t=60,b=20)
    )
    title_x=0.5

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(
        filtered.head(20),
        use_container_width=True
    )

# ============================================================
# SMART HOUSE FINDER
# ============================================================

elif page == "🔍 Smart House Finder":

    st.markdown("<div class='title'>🔍 Smart House Finder</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Discover properties based on your preferences.</div>", unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        budget = st.slider(
            "💰 Maximum Budget (Lakhs)",
            int(df["price"].min()),
            int(df["price"].max()),
            80
        )

        bhk = st.selectbox(
            "🛏 Bedrooms",
            sorted(df["BHK"].unique())
        )

        area_type = st.selectbox(
            "🏘 Area Type",
            sorted(df["area_type"].unique())
        )

    with col2:

        sqft = st.number_input(
            "📐 Minimum Area (Sqft)",
            min_value=300,
            value=1000
        )

        bath = st.number_input(
            "🚿 Minimum Bathrooms",
            min_value=1,
            value=2
        )

        location = st.selectbox(
            "📍 Preferred Location",
            ["Any"] + sorted(df["location"].unique())
        )

    houses = df.copy()

    houses = houses[
        (houses["price"] <= budget) &
        (houses["BHK"] == bhk) &
        (houses["area_type"] == area_type) &
        (houses["total_sqft"] >= sqft) &
        (houses["bath"] >= bath)
    ]

    if location != "Any":
        houses = houses[houses["location"] == location]

    houses = houses.sort_values("price").head(12)

    st.divider()

    st.subheader(f"Recommended Properties ({len(houses)})")

    if houses.empty:

        st.warning("No matching properties found. Try changing the filters.")

    else:

        for _, row in houses.iterrows():

            with st.container():

                st.markdown(
                    f"""
<div class="house-card">

### 📍 {row['location']}

**💰 Price:** ₹ {row['price']:.2f} Lakhs

**🏘 Area Type:** {row['area_type']}

**🛏 Bedrooms:** {int(row['BHK'])}

**🚿 Bathrooms:** {row['bath']}

**🌇 Balcony:** {row['balcony']}

**📐 Area:** {int(row['total_sqft'])} Sqft

</div>
""",
                    unsafe_allow_html=True
                )

    st.divider()

    st.subheader("Price Distribution of Recommended Properties")

    if not houses.empty:

        fig = px.bar(
            houses,
            x="location",
            y="price",
            color="price",
            title="Recommended Property Prices"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ============================================================
# PRICE PREDICTION
# ============================================================

elif page == "🤖 Price Prediction":

    st.markdown("<div class='title'>🤖 AI Price Prediction</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Estimate the selling price of a residential property.</div>", unsafe_allow_html=True)

    st.divider()

    left, right = st.columns(2)

    with left:

        area_type = st.selectbox(
            "🏘 Area Type",
            sorted(df["area_type"].unique())
        )

        location = st.selectbox(
            "📍 Location",
            sorted(df["location"].unique())
        )

        sqft = st.number_input(
            "📐 Total Area (Sqft)",
            min_value=300,
            max_value=20000,
            value=1200,
            step=50
        )

    with right:

        bath = st.number_input(
            "🚿 Bathrooms",
            min_value=1,
            max_value=10,
            value=2
        )

        balcony = st.number_input(
            "🌇 Balconies",
            min_value=0,
            max_value=5,
            value=1
        )

        bhk = st.number_input(
            "🛏 Bedrooms (BHK)",
            min_value=1,
            max_value=10,
            value=2
        )

    st.divider()

    if st.button("🚀 Predict House Price", use_container_width=True):

        input_df = pd.DataFrame({

            "area_type":[area_type],
            "location":[location],
            "total_sqft":[sqft],
            "bath":[bath],
            "balcony":[balcony],
            "BHK":[bhk]

        })

        with st.spinner("Analyzing property details..."):

            prediction = model.predict(input_df)[0]

        st.success("Prediction Completed Successfully!")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "🏷 Estimated Price",
            f"₹ {prediction:.2f} Lakhs"
        )

        c2.metric(
            "📐 Area",
            f"{sqft} Sqft"
        )

        c3.metric(
            "🛏 BHK",
            bhk
        )

        st.divider()

        st.subheader("Property Summary")

        summary = pd.DataFrame({

            "Feature":[
                "Location",
                "Area Type",
                "Bedrooms",
                "Bathrooms",
                "Balconies",
                "Total Area",
                "Estimated Price"
            ],

            "Value":[
                location,
                area_type,
                bhk,
                bath,
                balcony,
                f"{sqft} Sqft",
                f"₹ {prediction:.2f} Lakhs"
            ]

        })

        st.dataframe(
            summary,
            hide_index=True,
            use_container_width=True
        )

        st.divider()

        st.subheader("Prediction Result")

        if prediction <= df["price"].quantile(0.25):

            st.success("✅ This property falls in the Budget category.")

        elif prediction <= df["price"].quantile(0.75):

            st.info("ℹ This property falls in the Mid-Range category.")

        else:

            st.warning("⭐ This property falls in the Premium category.")

        st.info(
            "The estimated price is generated using the trained Gradient Boosting Machine Learning model."
        )

# ============================================================
# MARKET INSIGHTS
# ============================================================

elif page == "📈 Market Insights":

    st.markdown("<div class='title'>📈 Market Insights</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Explore key insights from the housing market.</div>", unsafe_allow_html=True)

    st.divider()

    # ---------------- KPI ----------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🏘 Total Properties",
        f"{len(df):,}"
    )

    c2.metric(
        "📍 Locations",
        df["location"].nunique()
    )

    c3.metric(
        "💰 Average Price",
        f"₹ {df['price'].mean():.2f} L"
    )

    c4.metric(
        "📐 Average Area",
        f"{df['total_sqft'].mean():.0f} Sqft"
    )

    st.divider()

    col1, col2 = st.columns(2)

    # ---------------- Highest Average Price ----------------

    with col1:

        expensive = (
            df.groupby("location")["price"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            expensive,
            x="location",
            y="price",
            color="price",
            title="Top 10 Highest Average Price Locations"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(fig, use_container_width=True)

    # ---------------- Lowest Average Price ----------------

    with col2:

        cheapest = (
            df.groupby("location")["price"]
            .mean()
            .sort_values()
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            cheapest,
            x="location",
            y="price",
            color="price",
            title="Top 10 Budget Friendly Locations"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    # ---------------- Average Price by BHK ----------------

    with col1:

        bhk_price = (
            df.groupby("BHK")["price"]
            .mean()
            .reset_index()
        )

        fig = px.line(
            bhk_price,
            x="BHK",
            y="price",
            markers=True,
            title="Average Price by BHK"
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(fig, use_container_width=True)

    # ---------------- Area Type ----------------

    with col2:

        fig = px.pie(
            df,
            names="area_type",
            title="Area Type Distribution",
            hole=0.45
        )

        fig.update_layout(

            template="plotly_dark",

            height=500,

            title_x=0.5,

            title_font_size=22,

            margin=dict(l=20,r=20,t=60,b=20)
        )
        title_x=0.5

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Top 15 Most Popular Locations")

    top_locations = (
        df["location"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    top_locations.columns = [
        "Location",
        "Properties"
    ]

    fig = px.bar(
        top_locations,
        x="Location",
        y="Properties",
        color="Properties"
    )
    fig.update_traces(marker_color="#3b82f6")

    fig.update_layout(

        template="plotly_dark",

        height=500,

        title_x=0.5,

        title_font_size=22,

        margin=dict(l=20,r=20,t=60,b=20)
    )
    title_x=0.5

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Housing Dataset Overview")

    st.dataframe(
        df.describe().T,
        use_container_width=True
    )

    st.divider()

    st.caption("🏡 HomeVista AI • Smart House Recommendation & Price Prediction Platform")