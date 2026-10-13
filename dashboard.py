
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Midnight Velocity | Bike Analytics",
    page_icon="🚴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS - MIDNIGHT VELOCITY
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #090e1a;
    --panel: #111a2b;
    --panel2: #172338;
    --border: rgba(148, 163, 184, 0.16);
    --text: #edf4ff;
    --muted: #8493ad;
    --cyan: #55e6ff;
    --purple: #a78bfa;
    --green: #69f0ae;
    --orange: #ffb86b;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, rgba(85,230,255,.08), transparent 32%),
        radial-gradient(ellipse at 90% 15%, rgba(167,139,250,.08), transparent 30%),
        var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1600px;
    padding: 2rem 2.3rem;
}

[data-testid="stSidebar"] {
    background: #0d1423;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: #dce7f8;
}

[data-testid="stSidebar"] [data-baseweb="select"] {
    background: #172338;
    border: 1px solid #2a3952;
    border-radius: 10px;
}

[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #edf4ff !important;
}

[data-testid="stSidebar"] label {
    font-size: 13px;
    font-weight: 600;
}

[data-testid="stSidebar"] hr {
    border-color: #27344a;
}

.brand {
    padding: 14px 2px 25px;
}

.brand-mark {
    color: var(--cyan);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2.5px;
}

.brand h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 29px;
    line-height: 1.15;
    font-weight: 700;
    color: white;
    margin: 12px 0 8px;
}

.brand p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.8;
}

.section-label {
    color: var(--cyan);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 25px 0 12px;
}

.hero {
    background: linear-gradient(115deg, #14253b, #111a2b 60%, #211b3a);
    border: 1px solid rgba(85,230,255,.20);
    border-radius: 22px;
    padding: 32px;
    margin-bottom: 27px;
    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "↗";
    position: absolute;
    right: 28px;
    top: -25px;
    font-size: 155px;
    font-weight: 800;
    color: rgba(85,230,255,.07);
}

.hero-kicker {
    color: var(--cyan);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(30px, 4vw, 45px);
    line-height: 1.12;
    font-weight: 700;
    letter-spacing: -1.5px;
    color: white;
    margin: 14px 0;
}

.hero p {
    max-width: 650px;
    color: #a9b9d0;
    font-size: 13px;
    line-height: 1.9;
    margin-bottom: 0;
}

.section-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 10px;
    margin: 28px 0 14px;
}

.section-head h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 21px;
    font-weight: 700;
    color: #f2f7ff;
    margin: 0;
}

.section-head span {
    color: var(--muted);
    font-size: 11px;
}

.kpi-card {
    background: linear-gradient(145deg, #172338, #101827);
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 20px;
    min-height: 145px;
    box-shadow: 0 12px 30px rgba(0,0,0,.12);
    transition: transform .2s ease, border-color .2s ease;
}

.kpi-card:hover {
    transform: translateY(-3px);
    border-color: rgba(85,230,255,.4);
}

.kpi-label {
    color: #91a2bd;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.1px;
    text-transform: uppercase;
}

.kpi-value {
    color: #fff;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(22px, 2.1vw, 30px);
    font-weight: 700;
    margin-top: 18px;
    letter-spacing: -1px;
    overflow-wrap: anywhere;
}

.kpi-icon {
    float: right;
    font-size: 20px;
    background: rgba(85,230,255,.10);
    border: 1px solid rgba(85,230,255,.18);
    padding: 7px 9px;
    border-radius: 11px;
}

.kpi-note {
    color: #8493ad;
    font-size: 10px;
    margin-top: 5px;
}

.chart-card {
    background: linear-gradient(150deg, #131e30, #0f1726);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 21px;
    margin-top: 16px;
    box-shadow: 0 15px 35px rgba(0,0,0,.10);
}

.chart-title {
    font-family: 'Space Grotesk', sans-serif;
    color: #f2f7ff;
    font-size: 17px;
    font-weight: 700;
}

.chart-subtitle {
    color: #8191aa;
    font-size: 11px;
    line-height: 1.7;
    margin: 5px 0 13px;
}

.insight-card {
    background: linear-gradient(110deg, rgba(85,230,255,.09), rgba(167,139,250,.07));
    border: 1px solid rgba(85,230,255,.18);
    border-left: 3px solid var(--cyan);
    border-radius: 12px;
    padding: 17px 20px;
    color: #c7d5e9;
    font-size: 12px;
    line-height: 1.9;
    margin: 18px 0;
}

.insight-card b {
    color: var(--cyan);
}

div[data-testid="stTabs"] {
    margin-top: 24px;
}

div[data-testid="stTabs"] button {
    color: #8d9db6;
    font-size: 12px;
    font-weight: 700;
    border-radius: 10px 10px 0 0;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--cyan);
    border-bottom: 2px solid var(--cyan);
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

.footer {
    border-top: 1px solid var(--border);
    color: #63738d;
    font-size: 10px;
    letter-spacing: 1.5px;
    text-align: center;
    padding: 25px 0 8px;
    margin-top: 30px;
}

#MainMenu, footer {
    visibility: hidden;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1.1rem;
    }

    .hero {
        padding: 22px;
    }

    .section-head {
        align-items: start;
        flex-direction: column;
    }

    .kpi-card {
        padding: 15px;
        min-height: 125px;
    }

    .chart-card {
        padding: 14px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    possible_paths = [
        Path("day.csv"),
        Path("main_data.csv"),
        Path("data/day.csv"),
        Path("../data/day.csv"),
        Path("dashboard/main_data.csv"),
        Path(__file__).resolve().parent / "day.csv",
        Path(__file__).resolve().parent / "main_data.csv",
        Path(__file__).resolve().parent.parent / "data" / "day.csv"
    ]

    for path in possible_paths:
        if path.exists():
            return pd.read_csv(path)

    raise FileNotFoundError(
        "Dataset tidak ditemukan. Letakkan day.csv atau main_data.csv "
        "di folder dashboard, atau day.csv di folder data."
    )


try:
    df = load_data()
except FileNotFoundError as error:
    st.error(str(error))
    st.stop()

# =========================================================
# DATA PREPARATION
# =========================================================

df["dteday"] = pd.to_datetime(df["dteday"])

month_names = {
    1: "Januari", 2: "Februari", 3: "Maret",
    4: "April", 5: "Mei", 6: "Juni",
    7: "Juli", 8: "Agustus", 9: "September",
    10: "Oktober", 11: "November", 12: "Desember"
}

season_names = {
    1: "Musim Semi",
    2: "Musim Panas",
    3: "Musim Gugur",
    4: "Musim Dingin"
}

weather_names = {
    1: "Cerah",
    2: "Berkabut",
    3: "Hujan Ringan",
    4: "Hujan Lebat"
}

df["year_label"] = df["yr"].map({0: "2011", 1: "2012"})
df["month_name"] = df["mnth"].map(month_names)
df["season_name"] = df["season"].map(season_names)
df["weather_name"] = df["weathersit"].map(weather_names)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-mark">URBAN MOBILITY / DATA LAB</div>
        <h1>Midnight<br>Velocity.</h1>
        <p>Explore the pulse of urban cycling through data and interactive insights.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">01 — Periode Data</div>',
        unsafe_allow_html=True
    )

    selected_years = st.multiselect(
        "Tahun",
        options=sorted(df["year_label"].dropna().unique()),
        default=sorted(df["year_label"].dropna().unique())
    )

    selected_months = st.multiselect(
        "Bulan",
        options=list(month_names.values()),
        default=list(month_names.values())
    )

    st.markdown(
        '<div class="section-label">02 — Kondisi Lingkungan</div>',
        unsafe_allow_html=True
    )

    selected_seasons = st.multiselect(
        "Musim",
        options=list(season_names.values()),
        default=list(season_names.values())
    )

    st.markdown("---")
    st.caption("BIKE SHARING DATASET")
    st.caption("Periode observasi: 2011–2012")
    st.caption("Pilih filter untuk mengeksplorasi data.")

# =========================================================
# FILTER DATA
# =========================================================

filtered_df = df[
    (df["year_label"].isin(selected_years)) &
    (df["month_name"].isin(selected_months)) &
    (df["season_name"].isin(selected_seasons))
].copy()

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-kicker">Bike Sharing Intelligence / Dashboard</div>
    <h1>Ride the data.<br>Discover the pattern.</h1>
    <p>
        Dashboard interaktif untuk mengeksplorasi permintaan penyewaan sepeda,
        pola musiman, kondisi cuaca, dan karakteristik pengguna.
        Gunakan filter di samping untuk menemukan insight dari periode pilihanmu.
    </p>
</div>
""", unsafe_allow_html=True)

if filtered_df.empty:
    st.warning(
        "Tidak ada data untuk kombinasi filter ini. "
        "Coba pilih tahun, bulan, atau musim lainnya."
    )
    st.stop()

# =========================================================
# KPI CARDS
# =========================================================

total_rentals = int(filtered_df["cnt"].sum())
average_daily = int(filtered_df["cnt"].mean())
total_days = len(filtered_df)
registered_users = int(filtered_df["registered"].sum())
casual_users = int(filtered_df["casual"].sum())
total_users = registered_users + casual_users

registered_percentage = (
    registered_users / total_users * 100
    if total_users > 0 else 0
)

all_rentals = int(df["cnt"].sum())
period_share = total_rentals / all_rentals * 100 if all_rentals else 0

st.markdown("""
<div class="section-head">
    <h2>Data Overview</h2>
    <span>Ringkasan berdasarkan filter aktif</span>
</div>
""", unsafe_allow_html=True)

kpis = [
    ("Total Rentals", f"{total_rentals:,}", "🚲",
     f"{period_share:.1f}% dari seluruh penyewaan"),
    ("Daily Average", f"{average_daily:,}", "↗️",
     "Rata-rata perjalanan per hari"),
    ("Days Analyzed", f"{total_days:,}", "🗓️",
     "Jumlah hari yang dianalisis"),
    ("Registered Share", f"{registered_percentage:.1f}%", "👥",
     "Proporsi penyewaan registered")
]

kpi_cols = st.columns(4)

for col, (label, value, icon, note) in zip(kpi_cols, kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <span class="kpi-label">{label}</span>
            <span class="kpi-icon">{icon}</span>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# CHART THEME
# =========================================================

chart_font = dict(
    family="Plus Jakarta Sans",
    color="#dce7f8",
    size=11
)

grid_color = "rgba(148, 163, 184, 0.12)"

def style_chart(fig, height=400):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=chart_font,
        height=height,
        margin=dict(l=15, r=20, t=25, b=15),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#c7d5e9")
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            color="#8493ad",
            title_font=dict(color="#8493ad")
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=grid_color,
            zeroline=False,
            color="#8493ad",
            title_font=dict(color="#8493ad")
        )
    )
    return fig

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "◈  Overview",
    "✳  Season & Weather",
    "♧  Rider Analytics"
])

# =========================================================
# TAB 1 — OVERVIEW
# =========================================================

with tab1:
    st.markdown("""
    <div class="section-head">
        <h2>Demand Over Time</h2>
        <span>Volume bulanan dan tren harian</span>
    </div>
    """, unsafe_allow_html=True)

    monthly = (
        filtered_df.groupby(
            ["mnth", "month_name"], as_index=False
        )["cnt"]
        .sum()
        .sort_values("mnth")
    )

    col1, col2 = st.columns([1, 1.45], gap="large")

    with col1:
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Monthly Performance</div>
            <div class="chart-subtitle">
                Total penyewaan pada setiap bulan
            </div>
        """, unsafe_allow_html=True)

        fig_month = px.bar(
            monthly,
            x="month_name",
            y="cnt",
            text="cnt",
            color_discrete_sequence=["#55e6ff"]
        )

        fig_month.update_traces(
            texttemplate="%{text:,.0f}",
            textposition="outside",
            cliponaxis=False,
            marker_line_width=0
        )

        fig_month.update_layout(
            xaxis_title="",
            yaxis_title="Total rentals",
            showlegend=False,
            xaxis=dict(
                categoryorder="array",
                categoryarray=list(month_names.values()),
                showgrid=False,
                tickangle=-35
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor=grid_color,
                rangemode="tozero"
            )
        )

        style_chart(fig_month, 390)
        st.plotly_chart(fig_month, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Daily Rental Rhythm</div>
            <div class="chart-subtitle">
                Perubahan volume penyewaan dari hari ke hari
            </div>
        """, unsafe_allow_html=True)

        fig_daily = px.area(
            filtered_df.sort_values("dteday"),
            x="dteday",
            y="cnt"
        )

        fig_daily.update_traces(
            line=dict(color="#a78bfa", width=2),
            fillcolor="rgba(167,139,250,0.20)"
        )

        fig_daily.update_layout(
            xaxis_title="Tanggal",
            yaxis_title="Penyewaan",
            showlegend=False
        )

        style_chart(fig_daily, 390)
        st.plotly_chart(fig_daily, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if not monthly.empty:
        peak_month = monthly.loc[monthly["cnt"].idxmax()]

        st.markdown(f"""
        <div class="insight-card">
            <b>↗ KEY INSIGHT</b><br>
            Bulan dengan total penyewaan tertinggi pada filter aktif
            adalah <b>{peak_month["month_name"]}</b>, dengan
            <b>{int(peak_month["cnt"]):,}</b> penyewaan.
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TAB 2 — SEASON & WEATHER
# =========================================================

with tab2:
    st.markdown("""
    <div class="section-head">
        <h2>Environmental Signals</h2>
        <span>Bagaimana musim dan cuaca berkaitan dengan permintaan</span>
    </div>
    """, unsafe_allow_html=True)

    seasonal = (
        filtered_df.groupby("season_name", as_index=False)["cnt"]
        .mean()
    )

    seasonal["season_order"] = seasonal["season_name"].map(
        {v: k for k, v in season_names.items()}
    )

    seasonal = seasonal.sort_values("season_order")

    weather = (
        filtered_df.groupby("weather_name", as_index=False)["cnt"]
        .mean()
        .sort_values("cnt", ascending=True)
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Average Rentals by Season</div>
            <div class="chart-subtitle">
                Rata-rata jumlah penyewaan harian berdasarkan musim
            </div>
        """, unsafe_allow_html=True)

        fig_season = px.bar(
            seasonal,
            x="cnt",
            y="season_name",
            orientation="h",
            text="cnt",
            color_discrete_sequence=["#69f0ae"]
        )

        fig_season.update_traces(
            texttemplate="%{text:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_season.update_layout(
            xaxis_title="Rata-rata penyewaan",
            yaxis_title="",
            showlegend=False,
            xaxis=dict(
                showgrid=True,
                gridcolor=grid_color,
                rangemode="tozero"
            ),
            yaxis=dict(showgrid=False)
        )

        style_chart(fig_season, 400)
        st.plotly_chart(fig_season, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Weather Impact</div>
            <div class="chart-subtitle">
                Perbandingan rata-rata penyewaan menurut kondisi cuaca
            </div>
        """, unsafe_allow_html=True)

        fig_weather = px.bar(
            weather,
            x="cnt",
            y="weather_name",
            orientation="h",
            text="cnt",
            color_discrete_sequence=["#ffb86b"]
        )

        fig_weather.update_traces(
            texttemplate="%{text:,.0f}",
            textposition="outside",
            cliponaxis=False
        )

        fig_weather.update_layout(
            xaxis_title="Rata-rata penyewaan",
            yaxis_title="",
            showlegend=False,
            xaxis=dict(
                showgrid=True,
                gridcolor=grid_color,
                rangemode="tozero"
            ),
            yaxis=dict(showgrid=False)
        )

        style_chart(fig_weather, 400)
        st.plotly_chart(fig_weather, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if not seasonal.empty:
        top_season = seasonal.loc[seasonal["cnt"].idxmax()]

        st.markdown(f"""
        <div class="insight-card">
            <b>✳ SEASONAL SIGNAL</b><br>
            Musim dengan rata-rata penyewaan harian tertinggi adalah
            <b>{top_season["season_name"]}</b>, dengan rata-rata sekitar
            <b>{top_season["cnt"]:,.0f}</b> penyewaan per hari.
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TAB 3 — RIDER ANALYTICS
# =========================================================

with tab3:
    st.markdown("""
    <div class="section-head">
        <h2>Who Is Riding?</h2>
        <span>Komposisi pengguna dan pola penyewaan</span>
    </div>
    """, unsafe_allow_html=True)

    user_data = pd.DataFrame({
        "Tipe Pengguna": ["Registered", "Casual"],
        "Total Penyewaan": [
            registered_users,
            casual_users
        ]
    })

    col1, col2 = st.columns([0.9, 1.4], gap="large")

    with col1:
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">Rider Composition</div>
            <div class="chart-subtitle">
                Proporsi penyewaan registered dan casual
            </div>
        """, unsafe_allow_html=True)

        fig_users = px.pie(
            user_data,
            names="Tipe Pengguna",
            values="Total Penyewaan",
            hole=0.67,
            color="Tipe Pengguna",
            color_discrete_map={
                "Registered": "#55e6ff",
                "Casual": "#a78bfa"
            }
        )

        fig_users.update_traces(
            textposition="outside",
            textinfo="percent+label",
            marker=dict(
                line=dict(
                    color="#111a2b",
                    width=4
                )
            ),
            pull=[0.035, 0]
        )

        fig_users.update_layout(
            showlegend=False,
            annotations=[dict(
                text="RIDER<br>MIX",
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(
                    family="Space Grotesk",
                    size=17,
                    color="#edf4ff"
                )
            )]
        )

        style_chart(fig_users, 400)
        st.plotly_chart(fig_users, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="chart-card">
            <div class="chart-title">User Type Across Seasons</div>
            <div class="chart-subtitle">
                Perbandingan total penyewaan kedua kelompok pengguna
            </div>
        """, unsafe_allow_html=True)

        user_season = (
            filtered_df.groupby("season_name")[
                ["casual", "registered"]
            ]
            .sum()
            .reset_index()
        )

        user_season["season_order"] = user_season["season_name"].map(
            {v: k for k, v in season_names.items()}
        )

        user_season = user_season.sort_values("season_order")

        fig_user_season = go.Figure()

        fig_user_season.add_trace(go.Bar(
            x=user_season["season_name"],
            y=user_season["casual"],
            name="Casual",
            marker=dict(
                color="#a78bfa",
                line=dict(width=0)
            )
        ))

        fig_user_season.add_trace(go.Bar(
            x=user_season["season_name"],
            y=user_season["registered"],
            name="Registered",
            marker=dict(
                color="#55e6ff",
                line=dict(width=0)
            )
        ))

        fig_user_season.update_layout(
            barmode="group",
            xaxis_title="Musim",
            yaxis_title="Total penyewaan",
            legend=dict(
                orientation="h",
                y=1.12,
                x=0
            ),
            xaxis=dict(showgrid=False),
            yaxis=dict(
                showgrid=True,
                gridcolor=grid_color
            )
        )

        style_chart(fig_user_season, 400)
        st.plotly_chart(fig_user_season, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-card">
        <b>♧ RIDER INSIGHT</b><br>
        Pengguna registered menyumbang
        <b>{registered_percentage:.1f}%</b> dari total penyewaan
        pada periode yang dipilih. Sisanya berasal dari pengguna casual.
        Komposisi ini membantu memahami kontribusi setiap tipe pengguna.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    MIDNIGHT VELOCITY &nbsp;·&nbsp; BIKE SHARING ANALYTICS
    &nbsp;·&nbsp; DATA 2011—2012
</div>
""", unsafe_allow_html=True)
