import streamlit as st

from lib.maps import Mapping
from lib.sections import Sections
from lib.toolkit import DSToolKit

st.set_page_config(
    page_title="Jeová - Bornlogic",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

toolkit = DSToolKit()
mapping = Mapping()


def pergunta_1(df_metrics, df_historic):
    st.subheader(
        "Pergunta 1 - Visualizações das métricas de desenvolvimento humano"
    )
    column1, column2 = st.columns(2)

    variable_globe = column1.selectbox(
        "Variável - Dataset de 2021", df_metrics.columns[2:])
    globe_fig = mapping.globe_figure(df_metrics, variable_globe)
    column1.plotly_chart(globe_fig, use_container_width=True)

    variable_mundi = column2.selectbox(
        "Variável - Dataset histórico", df_historic.columns[2:-1], 7
    )
    mundi_fig = mapping.mundi_figure(df_historic, variable_mundi)
    column2.plotly_chart(mundi_fig, use_container_width=True)


def pergunta_2(df_metrics, df_historic):
    st.subheader("Pergunta 2 - Identificação da região do mundo")
    col_pca, col_forest = st.columns(2)

    col_pca.subheader("Espaço de Embedding PCA")
    fig_metrics_pca = toolkit.plot_embedding("metrics_pca_tsne")
    col_pca.plotly_chart(fig_metrics_pca, use_container_width=True)

    fig_historic_pca = toolkit.plot_embedding("historic_pca_tsne")
    col_pca.plotly_chart(fig_historic_pca, use_container_width=True)

    col_forest.subheader("Espaço de Embedding PCA")
    fig_metrics_pca = toolkit.plot_embedding("metrics_forest_tsne")
    col_forest.plotly_chart(fig_metrics_pca, use_container_width=True)

    fig_historic_pca = toolkit.plot_embedding("historic_forest_tsne")
    col_forest.plotly_chart(fig_historic_pca, use_container_width=True)


def pergunta_3(df_historic):
    st.subheader("Pergunta 3 - Impacto da pandemia")

    fig_positive, fig_negative = mapping.regional_average(df=df_historic)
    st.plotly_chart(fig_positive, use_container_width=True)
    st.plotly_chart(fig_negative, use_container_width=True)

    col_n_years, col_thresh = st.columns(2)
    n_years = col_n_years.slider(
        "Número de anos antes de 2020",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
    )
    std_thresh = col_thresh.slider(
        "Limite de desvios padrões",
        min_value=1.0,
        max_value=10.0,
        value=2.0,
        step=0.1,
    )
    fig_anomaly = mapping.plot_anomaly(df_historic, n_years, std_thresh)

    st.plotly_chart(fig_anomaly, use_container_width=True)


def main():
    df_metrics, df_historic = toolkit.load_datasets()

    pergunta_1(df_metrics, df_historic)
    pergunta_2(df_metrics, df_historic)
    pergunta_3(df_historic)


if __name__ == "__main__":
    Sections().header()
    Sections.hello_card()
    main()
