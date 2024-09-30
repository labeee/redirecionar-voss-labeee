import streamlit as st

# ---------------VARIÁVEIS---------------

project = "VOSS"
support_mail = "escritorios.qai.bot@gmail.com"


def initialize_page():
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        [data-testid="stToolbarActions"] {
            display: none
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True,)
    

def create_top(big_text_title: str = None, subtitle: str = None, subtitle2: str = None, subsubtitle: str = None, img_url: str = None, use_line: bool = True, use_progress: bool = False, progress_percentage:int = 0, use_image: bool = True):
    st.set_page_config(
    page_title=f'{project}',
    page_icon = '🖥️',
    layout='wide',
    initial_sidebar_state='collapsed'
    )
    st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    [data-testid="stToolbarActions"] {
        display: none
    }
    [data-testid="stHeader"] {
        display: none;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,)
    if use_image:
        _,col,_ = st.columns([5,1,5])
        col.image(r'static/voss-01.png', width=100, use_column_width=True)
    with st.container():
        esquerda, meio, direita = st.columns(3)
        if use_progress:
            meio.progress(progress_percentage)

    with st.container():
        esquerda, direita = st.columns(2, gap='medium')
        if big_text_title:
            esquerda.title('')
            esquerda.title('')
            esquerda.title('')
            esquerda.title(big_text_title)
        if img_url:
            direita.image(img_url, width=300)
    if use_line:
        st.markdown('---')


def footer():
    st.title('')
    col1, _, col2, col3 = st.columns(4)
    col1.image(r'static/lab_banner.png', width=300)
    col2.markdown(f"[SOBRE NÓS](https://voss-labeee.streamlit.app/SobreNos)")
    col3.markdown(f"[SUPORTE](mailto:{support_mail})")