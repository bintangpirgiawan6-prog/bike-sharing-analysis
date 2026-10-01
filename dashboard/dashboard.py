import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="BikeScope | Bike Sharing Analytics",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 80% 0%,
            rgba(59, 130, 246, 0.10),
            transparent 28%
        ),
        #0b1120;
    color: #f8fafc;
}

/* Hide default Streamlit elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* Sidebar */

[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid rgba(148, 163, 184, 0.12);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
}


/* Main content */

.block-container {
    max-width: 1450px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}


/* Header */

.dashboard-label {
    color: #60a5fa;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.dashboard-title {
    font-size: 42px;
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #f8fafc;
    margin-bottom: 12px;
}

.dashboard-description {
    color: #94a3b8;
    font-size: 15px;
    line-height: 1.7;
    max-width: 720px;
}


/* KPI Cards */

.kpi-card {
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(148, 163, 184, 0.13);
    border-radius: 18px;
    padding: 22px 22px 20px 22px;
    min-height: 125px;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
    transition: 0.2s ease;
}

.kpi-card:hover {
    border-color: rgba(96, 165, 250, 0.4);
    transform: translateY(-2px);
}

.kpi-title {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 500;
    margin-bottom: 10px;
}

.kpi-value {
    color: #f8fafc;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
}

.kpi-subtitle {
    color: #60a5fa;
    font-size: 12px;
    margin-top: 7px;
}


/* Section */

.section-title {
    color: #f8fafc;
    font-size: 21px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 5px;
}

.section-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}


/* Chart containers */

.chart-card {
    background: rgba(15, 23, 42, 0.70);
    border: 1px solid rgba(148, 163, 184, 0.11);
    border-radius: 18px;
    padding: 8px 12px 2px 12px;
}


/* Insight */

.insight-card {
    background: linear-gradient(
        135deg,
        rgba(30, 64, 175, 0.18),
        rgba(15, 23, 42, 0.7)
    );
    border: 1px solid rgba(96, 165, 250, 0.18);
    border-radius: 18px;
    padding: 20px 22px;
    margin-top: 15px;
}

.insight-title {
    color: #60a5fa;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 8px;
}

.insight-text {
    color: #cbd5e1;
    font-size: 14px;
    line-height: 1.7;
}


/* Sidebar text */

.sidebar-brand {
    font-size: 21px;
    font-weight: 700;
    color: #f8fafc;
}

.sidebar-caption {
    color: #64748b;
    font-size: 12px;
    margin-top: 4px;
    margin-bottom: 25px;
}


/* Footer */

.footer {
    text-align: center;
    color: #475569;
    font-size: 12px;
    padding-top: 35px;
    border-top: 1px solid rgba(148, 163, 184, 0.08);
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    day_df = pd.read_csv("data/day.csv")
    hour_df = pd.read_csv("data/hour.csv")

    # Convert date
    day_df["dteday"] = pd.to_datetime(day_df["dteday"])
    hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

    # Year labels
    year_map = {
        0: 2011,
        1: 2012
    }

    day_df["year"] = day_df["yr"].map(year_map)
    hour_df["year"] = hour_df["yr"].map(year_map)

    # Weather labels
    weather_map = {
        1: "Clear / Partly Cloudy",
        2: "Mist / Cloudy",
        3: "Light Snow / Rain",
        4: "Heavy Rain / Snow"
    }

    day_df["weather_label"] = day_df["weathersit"].map(weather_map)
    hour_df["weather_label"] = hour_df["weathersit"].map(weather_map)

    # Working day labels
    workingday_map = {
        0: "Non-Working Day",
        1: "Working Day"
    }

    day_df["workingday_label"] = day_df["workingday"].map(
        workingday_map
    )

    hour_df["workingday_label"] = hour_df["workingday"].map(
        workingday_map
    )

    return day_df, hour_df


day_df, hour_df = load_data()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand">🚲 BikeScope</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-caption">'
        'Bike Sharing Analytics'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Filter Data")

    selected_year = st.multiselect(
        "Tahun",
        options=[2011, 2012],
        default=[2011, 2012]
    )

    selected_days = st.multiselect(
        "Status Hari",
        options=["Non-Working Day", "Working Day"],
        default=["Non-Working Day", "Working Day"]
    )

    st.markdown("---")

    st.caption(
        "Gunakan filter untuk melihat perubahan pola "
        "penyewaan berdasarkan periode yang dipilih."
    )


# =========================================================
# FILTER
# =========================================================

filtered_day = day_df[
    day_df["year"].isin(selected_year)
].copy()

filtered_hour = hour_df[
    (hour_df["year"].isin(selected_year)) &
    (hour_df["workingday_label"].isin(selected_days))
].copy()


# =========================================================
# EMPTY FILTER HANDLING
# =========================================================

if filtered_day.empty or filtered_hour.empty:

    st.markdown(
        '<div class="dashboard-label">DATA ANALYTICS · 2011—2012</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-title">'
        'Bike Sharing Analytics'
        '</div>',
        unsafe_allow_html=True
    )

    st.warning(
        "Data tidak tersedia untuk kombinasi filter yang dipilih. "
        "Silakan pilih minimal satu tahun dan satu status hari."
    )

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="dashboard-label">DATA ANALYTICS · 2011—2012</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-title">'
    'Bike Sharing Analytics'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-description">'
    'Memahami pola penggunaan layanan bike sharing melalui '
    'waktu, hari kerja, dan kondisi cuaca untuk mendukung '
    'perencanaan operasional berbasis data.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# KPI CALCULATION
# =========================================================

total_rentals = filtered_day["cnt"].sum()

average_daily = filtered_day["cnt"].mean()

hourly_avg = (
    filtered_hour
    .groupby("hr")["cnt"]
    .mean()
)

if len(hourly_avg) > 0:

    peak_hour = int(hourly_avg.idxmax())
    peak_value = hourly_avg.max()

else:

    peak_hour = 0
    peak_value = 0


weather_avg = (
    filtered_day
    .groupby("weather_label")["cnt"]
    .mean()
)

if len(weather_avg) > 0:
    top_weather = weather_avg.idxmax()
else:
    top_weather = "-"


# =========================================================
# KPI CARDS
# =========================================================

k1, k2, k3, k4 = st.columns(4)


with k1:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">TOTAL PENYEWAAN</div>
            <div class="kpi-value">{total_rentals:,.0f}</div>
            <div class="kpi-subtitle">Sepeda disewa</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with k2:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">RATA-RATA HARIAN</div>
            <div class="kpi-value">{average_daily:,.0f}</div>
            <div class="kpi-subtitle">Penyewaan per hari</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with k3:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">JAM TERPADAT</div>
            <div class="kpi-value">{peak_hour:02d}:00</div>
            <div class="kpi-subtitle">
                ± {peak_value:,.0f} penyewaan
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with k4:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">KONDISI CUACA UTAMA</div>
            <div class="kpi-value" style="font-size:20px;">
                {top_weather}
            </div>
            <div class="kpi-subtitle">
                Rata-rata penyewaan tertinggi
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "Overview",
    "Time Pattern",
    "Weather"
])


# =========================================================
# TAB 1 — OVERVIEW
# =========================================================

with tab1:

    st.markdown(
        '<div class="section-title">Gambaran Umum Penyewaan</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Distribusi rata-rata penyewaan berdasarkan jam dan kondisi cuaca.'
        '</div>',
        unsafe_allow_html=True
    )

    col_a, col_b = st.columns([1.4, 1])


    # -----------------------------------------------------
    # Hour chart
    # -----------------------------------------------------

    with col_a:

        overview_hour = (
            filtered_hour
            .groupby("hr")["cnt"]
            .mean()
            .reset_index()
        )

        fig = px.area(
            overview_hour,
            x="hr",
            y="cnt",
            markers=True
        )

        fig.update_traces(
            line=dict(width=3),
            fillcolor="rgba(59,130,246,0.15)"
        )

        fig.update_layout(
            title="Pola Penyewaan Sepanjang Hari",
            xaxis_title="Jam",
            yaxis_title="Rata-rata Penyewaan",
            template="plotly_dark",
            height=420,
            margin=dict(l=20, r=20, t=55, b=20),
            hovermode="x unified"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )


    # -----------------------------------------------------
    # Weather chart
    # -----------------------------------------------------

    with col_b:

        weather_chart = (
            filtered_day
            .groupby("weather_label")["cnt"]
            .mean()
            .reset_index()
            .sort_values("cnt")
        )

        fig_weather = px.bar(
            weather_chart,
            x="cnt",
            y="weather_label",
            orientation="h"
        )

        fig_weather.update_layout(
            title="Rata-rata Berdasarkan Cuaca",
            xaxis_title="Rata-rata Penyewaan",
            yaxis_title="",
            template="plotly_dark",
            height=420,
            margin=dict(l=20, r=20, t=55, b=20)
        )

        st.plotly_chart(
            fig_weather,
            width="stretch"
        )


# =========================================================
# TAB 2 — TIME PATTERN
# =========================================================

with tab2:

    st.markdown(
        '<div class="section-title">Time Pattern</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Perbandingan pola penyewaan antara hari kerja dan hari non-kerja.'
        '</div>',
        unsafe_allow_html=True
    )

    time_data = (
        filtered_hour
        .groupby(["hr", "workingday_label"])["cnt"]
        .mean()
        .reset_index()
    )

    fig_time = px.line(
        time_data,
        x="hr",
        y="cnt",
        color="workingday_label",
        markers=True,
        labels={
            "hr": "Jam",
            "cnt": "Rata-rata Penyewaan",
            "workingday_label": "Status Hari"
        }
    )

    fig_time.update_layout(
        template="plotly_dark",
        height=500,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(
        fig_time,
        width="stretch"
    )

    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-title">KEY INSIGHT</div>
            <div class="insight-text">
                Jam dengan rata-rata penyewaan tertinggi adalah
                <b>{peak_hour:02d}:00</b>, dengan sekitar
                <b>{peak_value:,.0f}</b> penyewaan.
                Pola waktu ini dapat menjadi pertimbangan dalam
                pengelolaan ketersediaan sepeda.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TAB 3 — WEATHER
# =========================================================

with tab3:

    st.markdown(
        '<div class="section-title">Weather Impact</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Melihat hubungan kondisi cuaca dengan jumlah penyewaan.'
        '</div>',
        unsafe_allow_html=True
    )

    weather_detail = (
        filtered_day
        .groupby("weather_label")["cnt"]
        .agg(["mean", "sum"])
        .reset_index()
        .sort_values("mean", ascending=False)
    )

    fig_weather_detail = px.bar(
        weather_detail,
        x="weather_label",
        y="mean",
        text_auto=".0f",
        labels={
            "weather_label": "Kondisi Cuaca",
            "mean": "Rata-rata Penyewaan"
        }
    )

    fig_weather_detail.update_layout(
        template="plotly_dark",
        height=480,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(
        fig_weather_detail,
        width="stretch"
    )

    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-title">KEY INSIGHT</div>
            <div class="insight-text">
                Kondisi <b>{top_weather}</b> memiliki rata-rata
                jumlah penyewaan tertinggi pada data yang sedang
                ditampilkan.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        BikeScope · Bike Sharing Dataset · Data Analysis Project
    </div>
    """,
    unsafe_allow_html=True
)
