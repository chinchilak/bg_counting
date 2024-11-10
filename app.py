from utils import *

pages = {
    "Deskovky": [
        st.Page("svet_divu.py", title="Svět divů"),
        st.Page("7_divu.py", title="7 divů (duel)"),
    ]
}

pg = st.navigation(pages)
pg.run()