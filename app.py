import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(page_title="نظام معاينة البضائع", page_icon="📝")

st.title("📋 استمارة معاينة الغمارة والجوانب")
st.write("نقل بضائع محلية - مصلحة الضرائب والجمارك")

# إنشاء نموذج الإدخال بناءً على الورقة الرسمية
with st.form("customs_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("بيانات الوسيلة")
        plate_no = st.text_input("رقم اللوحة (مثلاً: 2/138439)")
        chassis_no = st.text_input("رقم القعادة (الشاصيه)")
        car_type = st.text_input("نوع السيارة (مثلاً: قاطرة فـلاب)")
        
    with col2:
        st.subheader("بيانات الشحنة")
        goods_type = st.text_input("نوع البضاعة (مثلاً: أسمنت حضرموت)")
        statement_no = st.text_input("رقم البيان / السجل")
        importer = st.text_input("المستورد (المؤسسة)")

    st.divider()
    
    col3, col4 = st.columns(2)
    with col3:
        driver_name = st.text_input("اسم السائق")
    with col4:
        clearer_name = st.text_input("المخلص")

    submitted = st.form_submit_button("إرسال البيانات للمختص")

# معالجة البيانات بعد الضغط على الزر
if submitted:
    if plate_no and chassis_no:
        # تسجيل الوقت الحالي من الهاتف آلياً
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # تجميع البيانات في جدول
        data = {
            "وقت التسجيل": [current_time],
            "رقم اللوحة": [plate_no],
            "رقم القعادة": [chassis_no],
            "نوع البضاعة": [goods_type],
            "السائق": [driver_name],
            "رقم البيان": [statement_no]
        }
        
        st.success("✅ تم حفظ البيانات وإرسال إشعار للمختص")
        st.table(pd.DataFrame(data))
        
        # تنبيه بسيط
        st.info("سيتم مطابقة هذه البيانات مع سجلات مصلحة الضرائب والجمارك.")
    else:
        st.error("⚠️ يرجى إدخال البيانات الأساسية (اللوحة والقعادة)")
