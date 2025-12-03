import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# -----------------------------------------------------------------------------
# 1. Page Config & Premium CSS Styling
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ESG Performance Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a spacious, high-end look
st.markdown("""
<style>
    /* Global Background: Very light grey for contrast with white cards */
    .stApp {
        background-color: #F9FAFB;
    }

    /* Typography: Clean, sans-serif fonts */
    h1, h2, h3 {
        color: #111827;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        letter-spacing: -0.5px;
    }

    /* Metrics Cards: White background, soft shadow, plenty of padding */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    div[data-testid="stMetricLabel"] {
        color: #6B7280;
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div[data-testid="stMetricValue"] {
        color: #111827;
        font-size: 30px;
        font-weight: 700;
    }

    /* Spacing: Increase padding at the top */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        max-width: 95%; /* Prevent content from stretching too wide on huge screens */
    }

    /* Chart Containers: subtle borders */
    .stPlotlyChart {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Sidebar Controls
# -----------------------------------------------------------------------------
st.sidebar.header("Dashboard Controls")
selected_year = st.sidebar.selectbox("Fiscal Year", [2025, 2024, 2023])
selected_scope = st.sidebar.selectbox("Scope", ["Global", "North America", "EMEA", "APAC"])
st.sidebar.markdown("---")
st.sidebar.caption(f"Data Source: Enterprise ESG Hub\nLast Update: {pd.Timestamp.now().strftime('%Y-%m-%d')}")

# Color Palette (Professional/Corporate)
COLOR_PRIMARY = "#0F766E"  # Teal
COLOR_SECONDARY = "#0EA5E9"  # Sky Blue
COLOR_ACCENT = "#F59E0B"  # Amber
COLOR_GREY = "#9CA3AF"

# -----------------------------------------------------------------------------
# 3. Header & Executive Summary
# -----------------------------------------------------------------------------
st.title("ESG Performance Dashboard")
st.markdown(f"Overview of sustainability performance for **{selected_scope}** in **FY {selected_year}**.")
st.markdown("---")

st.subheader("Executive Summary")
# Spacious layout for KPIs
k1, k2, k3, k4, k5 = st.columns(5)

# Dynamic Data Simulation
val_ghg = 54000 if selected_year == 2024 else 49500
val_energy = 120 if selected_year == 2024 else 115

with k1: st.metric("Total GHG Emissions", f"{val_ghg:,} tCO2e", "-8.5%")
with k2: st.metric("Energy Intensity", f"{val_energy} kWh/Unit", "-4.2%")
with k3: st.metric("Water Withdrawal", "1.5M m³", "+1.2%", delta_color="inverse")
with k4: st.metric("ESRS Compliance", "88%", "+12%")
with k5: st.metric("Supplier ESG Score", "74/100", "+2.5")

st.markdown("##")  # Extra spacing

# -----------------------------------------------------------------------------
# 4. Environmental Performance
# -----------------------------------------------------------------------------
st.subheader("Environmental Indicators")

# Layout: 2 Columns (2/3 for Trend, 1/3 for Breakdown)
col_env1, col_env2 = st.columns([2, 1])

with col_env1:
    # GHG Emissions Trend
    dates = pd.date_range(start=f"{selected_year}-01-01", periods=12, freq='M')
    trend_vals = np.linspace(6000, 4500, 12) + np.random.normal(0, 100, 12)
    df_trend = pd.DataFrame({'Date': dates, 'Emissions': trend_vals})

    fig_ghg = px.area(df_trend, x='Date', y='Emissions', title="<b>GHG Emissions Trend</b>")
    fig_ghg.update_traces(line_color=COLOR_PRIMARY, fillcolor="rgba(15, 118, 110, 0.1)")
    fig_ghg.update_layout(template="plotly_white", height=380, margin=dict(t=50, l=20, r=20, b=20))
    st.plotly_chart(fig_ghg, use_container_width=True)

with col_env2:
    # Use tabs to keep it clean and not crowded
    tab1, tab2 = st.tabs(["Energy Breakdown", "Water Usage"])

    with tab1:
        # Energy Consumption by Facility
        fig_energy = px.bar(
            x=['Facility A', 'Facility B', 'Facility C'],
            y=[220, 180, 110],
            title="<b>Energy Consumption by Facility</b>"
        )
        fig_energy.update_traces(marker_color=COLOR_PRIMARY)
        fig_energy.update_layout(template="plotly_white", height=320, xaxis_title=None)
        st.plotly_chart(fig_energy, use_container_width=True)

    with tab2:
        # Water Withdrawal by Region
        fig_water = px.bar(
            x=['Region X', 'Region Y', 'Region Z'],
            y=[50, 40, 25],
            title="<b>Water Withdrawal by Region</b>"
        )
        fig_water.update_traces(marker_color=COLOR_SECONDARY)
        fig_water.update_layout(template="plotly_white", height=320, xaxis_title=None)
        st.plotly_chart(fig_water, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. Social & Governance (Side by Side)
# -----------------------------------------------------------------------------
c_soc, c_gov = st.columns(2)

with c_soc:
    st.subheader("Social Responsibility")
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        # Supplier ESG Score Distribution
        scores = np.random.normal(72, 10, 200)
        fig_dist = px.box(y=scores, title="<b>Supplier ESG Score Dist.</b>")
        fig_dist.update_traces(marker_color=COLOR_ACCENT)
        fig_dist.update_layout(template="plotly_white", height=300, margin=dict(l=20, r=20))
        st.plotly_chart(fig_dist, use_container_width=True)

    with col_s2:
        # Conflict Minerals
        fig_minerals = go.Figure(go.Pie(
            labels=['Compliant', 'Non-Compliant'],
            values=[98, 2],
            hole=0.7,
            marker=dict(colors=[COLOR_PRIMARY, '#EF4444'])
        ))
        fig_minerals.update_layout(
            title="<b>Conflict Minerals (%)</b>",
            template="plotly_white",
            height=300,
            showlegend=False,
            annotations=[dict(text='98%', x=0.5, y=0.5, font_size=24, showarrow=False, font_color=COLOR_PRIMARY)]
        )
        st.plotly_chart(fig_minerals, use_container_width=True)

with c_gov:
    st.subheader("Governance & Compliance")
    col_g1, col_g2 = st.columns(2)

    with col_g1:
        # CSRD Compliance Gauge
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=85,
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "#111827"},
                'steps': [{'range': [0, 100], 'color': "#E5E7EB"}]
            }
        ))
        fig_gauge.update_layout(title="<b>CSRD Readiness</b>", template="plotly_white", height=300,
                                margin=dict(l=30, r=30))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_g2:
        # Incident Count & Response Time
        fig_inc = go.Figure()
        fig_inc.add_trace(go.Bar(x=['Q1', 'Q2', 'Q3', 'Q4'], y=[4, 2, 5, 1], name='Count', marker_color='#EF4444'))
        fig_inc.add_trace(go.Scatter(x=['Q1', 'Q2', 'Q3', 'Q4'], y=[24, 12, 18, 8], name='Hours', yaxis='y2',
                                     line=dict(color='#111827')))
        fig_inc.update_layout(
            title="<b>Incidents & Response</b>",
            template="plotly_white",
            height=300,
            showlegend=False,
            yaxis2=dict(overlaying='y', side='right', showgrid=False)
        )
        st.plotly_chart(fig_inc, use_container_width=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. Value Chain Map
# -----------------------------------------------------------------------------
st.subheader("Value Chain Sustainability Map")

# High-end Sankey Colors (Muted/Professional)
fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20, thickness=15,
        line=dict(color="white", width=0),
        label=["Sourcing", "Manufacturing", "Distribution", "Use Phase", "Recycling", "Landfill"],
        color=["#64748B", "#0F766E", "#0EA5E9", "#F59E0B", "#10B981", "#EF4444"]
    ),
    link=dict(
        source=[0, 1, 1, 2, 3, 3],
        target=[1, 2, 5, 3, 4, 5],
        value=[100, 85, 15, 85, 60, 25],
        color=["rgba(100, 116, 139, 0.2)", "rgba(15, 118, 110, 0.2)", "rgba(239, 68, 68, 0.1)",
               "rgba(14, 165, 233, 0.2)", "rgba(16, 185, 129, 0.2)", "rgba(239, 68, 68, 0.1)"]
    ))])

fig_sankey.update_layout(
    title_text="<b>Traceability & Impact Flow (Scope 3)</b>",
    template="plotly_white",
    height=500,
    font_family="Inter"
)
st.plotly_chart(fig_sankey, use_container_width=True)

st.markdown("""
<div style='text-align: center; margin-top: 50px; color: #9CA3AF; font-size: 12px;'>
    CONFIDENTIAL - INTERNAL USE ONLY
</div>
""", unsafe_allow_html=True)