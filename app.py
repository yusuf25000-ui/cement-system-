import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="معاينة الأسمنت", page_icon="🏗️")
st.title("🏗️ نظام تسجيل قواطر الأسمنت")

with st.form("cement_form"):
    plate = st.text_input("رقم اللوحة")
    chassis = st.text_input("رقم القعادة")
    qty = st.number_input("الكمية (طن)", min_value=0.0)
    count = st.number_input("العدد", min_value=0)
    submit = st.form_submit_button("إرسال البيانات")

if submit:
    if plate and chassis:
        st.success("✅ تم التسجيل بنجاح")
        data = {"التاريخ": datetime.now().strftime("%Y-%m-%d %H:%M"), "اللوحة": plate, "القعادة": chassis, "الكمية": qty, "العدد": count}
        st.table(pd.DataFrame([data]))
        st.info("سيتم تحويل هذه البيانات للمختص")
    else:
        st.error("يرجى تعبئة الحقول الأساسية")
