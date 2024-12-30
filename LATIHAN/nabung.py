import streamlit as st
 
st.title("Halaman Menabung")

#  Halaman Menabung
with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)")
    submit_button = st.form_submit_button(label="Menabung")
    if submit_button:
         st.session_state['jumlah'].append({
             "Tipe" : "Menabung",
             "Nama" : nama,
             "Jumlah" : jumlah
         })
         st.success("Anda Berhasil menabung")
    else:
        st.error("Gagal")
        