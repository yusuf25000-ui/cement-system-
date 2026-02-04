import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات واجهة النظام
st.set_page_config(page_title="نظام المعاينة الجمركية", layout="wide", page_icon="🏗️")

st.title("📋 نظام أتمتة استمارة المعاينة الجمركية")
st.write("يرجى تعبئة كافة الحقول الفنية بدقة ليتم إرسالها لمختص الثمن")

# إنشاء نموذج الإدخال
with st.form("detailed_customs_form", clear_on_submit=True):
    
    # القسم الأول: بيانات عامة والشحنة
    st.subheader("📌 بيانات المستورد والشحنة")
    c1, c2, c3 = st.columns(3)
    with c1:
        importer = st.text_input("اسم المستورد")
        driver_name = st.text_input("اسم السائق")
    with c2:
        statement_no = st.text_input("رقم البيان")
        seal_no = st.text_input("رقم السيل (Seal No)")
    with c3:
        report_date = st.date_input("التاريخ", datetime.now())
        goods_type = st.text_input("نوع البضاعة عامة")

    st.divider()

    # القسم الثاني: تفاصيل الإسمنت والإنتاج
    st.subheader("🏗️ تفاصيل الإسمنت والكميات")
    c4, c5, c6 = st.columns(3)
    with c4:
        cement_type = st.text_input("نوع الإسمنت")
    with c5:
        bags_count = st.number_input("عدد الأكياس", min_value=0, step=1)
    with c6:
        company_origin = st.text_input("إنتاج شركة /")

    st.divider()

    # القسم الثالث: بيانات الوسيلة (السيارة)
    st.subheader("🚛 بيانات وسيلة النقل")
    c7, c8 = st.columns(2)
    with c7:
        plate_no = st.text_input("رقم اللوحة")
    with c8:
        chassis_no = st.text_input("رقم القعادة")

    st.divider()

    # القسم الرابع: المصادقة والتوقيع (رقمي)
    st.subheader("✍️ المصادقة والتواقيع الرسمية")
    c9, c10 = st.columns(2)
    with c9:
        inspector_confirm = st.checkbox("توقيع ومصادقة المعاين (إقرار بصحة البيانات)")
        inspector_name = st.text_input("اسم المعاين المسؤول")
    with c10:
        officer_confirm = st.checkbox("توقيع ومصادقة الضابطة الجمركية")
        officer_name = st.text_input("اسم ضابط النوبة")

    # زر الإرسال النهائي
    submit_to_specialist = st.form_submit_button("🚀 إرسال البيانات آلياً إلى مختص الثمن")

# منطق المعالجة بعد الضغط على الزر
if submit_to_specialist:
    if inspector_confirm and officer_confirm:
        if plate_no and chassis_no and importer:
            # تجميع البيانات لعرضها
            st.success("✅ تمت المصادقة بنجاح. جاري إرسال التقرير الشامل لمختص الثمن...")
            
            summary_data = {
                "المستورد": importer,
                "السائق": driver_name,
                "اللوحة": plate_no,
                "القعادة": chassis_no,
                "نوع الإسمنت": cement_type,
                "الإنتاج": company_origin,
                "عدد الأكياس": bags_count,
                "رقم السيل": seal_no,
                "المعاينة": "تمت المصادقة",
                "الضابطة": "تمت المصادقة"
            }
            st.table(pd.DataFrame([summary_data]))
        else:
            st.error("⚠️ يرجى التأكد من تعبئة الحقول الأساسية (اللوحة، القعادة، المستورد)")
    else:
        st.warning("🚫 لا يمكن الإرسال لمختص الثمن بدون مصادقة 'المعاين' و 'الضابطة الجمركية' معاً.")
            
