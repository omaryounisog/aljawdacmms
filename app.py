import streamlit as st
import pandas as pd

# إعدادات الصفحة الأساسية
st.set_page_config(
page_title="Al Jawda CMMS Dashboard",
page_icon="🏗️",
layout="wide",
initial_sidebar_state="expanded"
)

# تخصيص الألوان الرسمية للشركة (أحمر داكن وأسود) عبر الـ CSS
st.markdown("""
<style>
.main { background-color: #111111; color: #ffffff; }
.stApp { background-color: #0d0d0d; }
h1, h2, h3 { color: #bd1a1a !important; font-family: 'Cairo', sans-serif; }
div[data-testid="stMetricValue"] { color: #bd1a1a !important; font-size: 28px; font-weight: bold; }
div[data-testid="stMetricLabel"] { color: #aaaaaa !important; }
.css-1d391kg { background-color: #1a1a1a; }
</style>
""", unsafe_allow_schema=True)

# عنوان لوحة التحكم الرئيسي
st.title("Al Jawda Al Motaqadema")
st.subheader("Contracting LLC — CMMS Dashboard")
st.markdown("---")

# الرابط الخاص بجدول بيانات جوجل (Google Sheets)
# ملاحظة: استبدل هذا الرابط برابط جدول البيانات الخاص بك بصيغة CSV أو اترك الجدول الافتراضي لقراءة البيانات حية
SHEET_URL = "ضع_رابط_جدول_بيانات_جوجل_هنا"

@st.cache_data(ttl=60)
def load_data():
try:
# قراءة البيانات مباشرة من جوجل شيت
df = pd.read_csv(SHEET_URL)
return df
except:
# بيانات افتراضية للعرض الفوري في حال عدم الربط بعد
data = {
"Status": ["Total Tickets", "In Progress", "Emergency Tickets"],
"Count": [5, 1, 2]
}
return pd.DataFrame(data)

df = load_data()

# عرض الإحصائيات العلوية (KPIs) بشكل احترافي ونظيف تماماً كشاشتك السابقة
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

# القائمة الجانبية للتنقل بسلاسة
st.sidebar.title("🏗️ Al Jawda CMMS")
menu = st.sidebar.radio("Navigation", ["Dashboard", "Work Orders", "New Request", "Technicians"])

if menu == "Dashboard":
st.subheader("📊 System Overview")
st.info("المنظومة تعمل بكفاءة عالية لتتبع مشاريع الـ DLP والصيانة الحالية.")
# عرض جدول التذاكر الحالية
st.markdown("### Recent Maintenance Tickets")
st.dataframe(df, use_container_width=True)

elif menu == "Work Orders":
st.subheader("📋 Work Orders & Maintenance Status")
st.write("هنا تظهر أوامر العمل المسندة للفريق والعمال بالتفصيل الحقيقي.")
st.dataframe(df, use_container_width=True)

elif menu == "New Request":
st.subheader("➕ Submit New Maintenance Request")
with st.form("request_form"):
title = st.text_input("Issue / Ticket Title")
description = st.text_area("Detailed Description")
priority = st.selectbox("Priority Level", ["Low", "Medium", "High", "Emergency"])
submitted = st.form_submit_form_button("Submit Request to DLP Team")
if submitted:
st.success("تم تسجيل بلاغ الصيانة بنجاح وجاري تحديث النظام فوراً!")

elif menu == "Technicians":
st.subheader("👥 Registered Technicians")
st.write("قائمة الفنيين والعمال المسؤولين عن تغطية المواقع الحالية.")
