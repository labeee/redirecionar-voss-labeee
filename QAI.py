from configurate import *

create_top(big_text_title=project, use_line=True, use_image=False, img_url=r'static/voss-01.png')

st.markdown("""
Esta página tem como único intúito redirecionar os usuários aos webapps oficiais publicados.
            
Acesse-os via os links disponíveis:
            
[Questionário](https://voss-labeee.streamlit.app/)

[Repositório do questionário](https://github.com/suportelabeee/voss-labeee)

[Página de ADM](https://adm-voss-labeee.streamlit.app/)

[Repositório da página de ADM](https://github.com/suportelabeee/adm-voss-labeee)

""")

footer()
