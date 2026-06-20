import streamlit as st
import pandas as pd

# إعدادات الصفحة الأساسية
st.set_page_config(
page_title="Al Jawda CMMS Dashboard",
page_icon="🏗️",
layout="wide",
initial_sidebar_state="expanded"
)

# تخصيص الألوان الرسمية للشركة عبر الـ CSS
st.markdown("""
<style>
.main { background-color: #111111; color: #ffffff; }
.stApp { background-color: #0d0d0d; }
h1, h2, h3 { color: #bd1a1a !important; font-family: 'Cairo', sans-serif; }
div[data-testid="stMetricValue"] { color: #bd1a1a !important; font-size: 28px; font-weight: bold; }
div[data-testid="stMetricLabel"] { color: #aaaaaa !important; }
</style>
""", unsafe_allow_html=True)

# عنوان لوحة التحكم الرئيسي
st.title("Al Jawda Al Motaqadema")
st.subheader("Contracting LLC — CMMS Dashboard")
st.markdown("---")

# دالة جلب البيانات موزونة الفراغات بالملي
def load_data():
try:
# هنا يمكنك وضع رابط جدول بيانات جوجل الفعلي لاحقاً
df = pd.read_csv("https://raw.githubusercontent.com/streamlit/datasets/master/mnist_test.csv")
return df
except:
data = {
"Ticket Status": ["Total Tickets", "In Progress", "Emergency Tickets"],
"Count": [5, 1, 2]
}
return pd.DataFrame(data)

df = load_data()

# عرض الإحصائيات العلوية (KPIs)
col1, col2, col3, col4 = st.columns(4)

with col1:
st.metric(label="Total Tickets", value="5")
with col2:
st.metric(label="In Progress", value="1")
with col3:
st.metric(label="Total Revenue", value="460 AED")
with col4:
st.metric(label="Avg. Satisfaction", value="5/5")

st.markdown("---")

# القائمة الجانبية للتنقل
st.sidebar.title("🏗️ Al Jawda CMMS")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Work Orders", "New Request"])

if menu == "Dashboard":
st.subheader("📊 System Overview")
st.info("المنظومة تعمل بكفاءة عالية لتتبع مشاريع الـ DLP والصيانة الحالية.")
st.markdown("### Recent Maintenance Tickets")
st.dataframe(df, use_container_width=True)

elif menu == "Work Orders":
st.subheader("📋 Work Orders & Maintenance Status")
st.write("هنا تظهر أوامر العمل المسندة للفريق والعمال بالتفصيل.")
st.dataframe(df, use_container_width=True)

elif menu == "New Request":
st.subheader("➕ Submit New Maintenance Request")
with st.form("request_form"):
title = st.text_input("Issue / Ticket Title")
description = st.text_area("Detailed Description")
priority = st.selectbox("Priority Level", ["Low", "Medium", "High", "Emergency"])
submitted = st.form_submit_button("Submit Request to DLP Team")
if submitted:
st.success("تم تسجيل بلاغ الصيانة بنجاح وجاري تحديث النظام فوراً!")
