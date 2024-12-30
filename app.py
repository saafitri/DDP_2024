import streamlit as st

# Slide Bar iretory
dashboard = st.Page("./dashboard.py", title = "Dashboard")
nabung = st.Page("./nabung.py", title = "Nabung") 
penarikan = st.Page("./penarikan.py", title = "Penarikan")

pg = st.navigation(
  {
       "Menu Utama": [dashboard],
       "Transaksi" : [nabung, penarikan],
  }
)
if 'jumlah' not in st.session_state:
    st.session_state['jumlah'] = []
    
# Mejalankan Navigasi
pg.run()


