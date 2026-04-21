import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Statistik Sektoral", layout="wide")

st.title("📊 Dashboard Statistik Sektoral")
st.write("Analisis data sektoral dari OPD")

# Upload file
uploaded_file = st.file_uploader("Upload dataset (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Baca data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # Pilih kolom
    st.sidebar.header("🔍 Filter Data")

    kolom = df.columns.tolist()

    col_tahun = st.sidebar.selectbox("Pilih Kolom Tahun", kolom)
    col_indikator = st.sidebar.selectbox("Pilih Kolom Indikator", kolom)
    col_nilai = st.sidebar.selectbox("Pilih Kolom Nilai", kolom)

    # Filter tahun
    tahun_unik = df[col_tahun].unique()
    tahun_pilih = st.sidebar.multiselect("Filter Tahun", tahun_unik, default=tahun_unik)

    df_filter = df[df[col_tahun].isin(tahun_pilih)]

    st.subheader("📊 Statistik Ringkas")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Data", len(df_filter))
    col2.metric("Rata-rata", round(df_filter[col_nilai].mean(), 2))
    col3.metric("Nilai Maksimum", df_filter[col_nilai].max())

    # Grafik
    st.subheader("📈 Visualisasi Data")

    fig, ax = plt.subplots()

    sns.lineplot(
        data=df_filter,
        x=col_tahun,
        y=col_nilai,
        hue=col_indikator,
        marker="o",
        ax=ax
    )

    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Download hasil
    st.subheader("⬇️ Download Data")
    csv = df_filter.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "data_filtered.csv", "text/csv")

else:
    st.info("Silakan upload dataset terlebih dahulu.")
