import streamlit as st

st.title("hello")
st.write("書くことが出来る")
st.markdown("# でかい文字")
st.markdown("## やや大きい文字")
st.markdown("### 少し大きい文字")

chk = st.checkbox("チェックしてヨシ") #コメントだよ

if chk:
    st.button("ボタン")
    st.selectbox("メニューリスト", ("あした", "あさって", "明々後日"))
    st.multiselect("メニューリスト複数おｋ", ("カレー", "牛丼", "ハンバーガー"))
    st.radio("選択してね", ("A型", "B型", "O型", "AB型"))
    st.text_input("文字入力欄")
    st.text_area("テキストエリア")

st.sidebar.text_input("どうぞご利用ください")
st.sidebar.text_area("あなたの感想をお聞かせください")