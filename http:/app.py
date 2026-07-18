import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="مستخرج خرائط جوجل", page_icon="📍", layout="centered")

st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div.stButton > button:first-child { background-color: #2ecc71; color: white; width: 100%; border-radius: 8px; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

st.title("📍 مستخرج بيانات خرائط جوجل")
st.write("احصل على بيانات عملائك المستهدفين بضغطة زر واحدة!")

keyword = st.text_input("🎯 نوع النشاط التجاري (مثال: مطاعم):")
country = st.text_input("🌍 الدولة:")
region = st.text_input("📍 المنطقة أو المدينة:")

STORE_URL = "https://payhip.com"

if st.button("🚀 ابدأ استخراج الداتا مجاناً"):
    if keyword and country and region:
        progress_bar = st.progress(0)
        demo_data = []
        for i in range(1, 51):
            time.sleep(0.02)
            progress_bar.progress(int((i / 50) * 100))
            demo_data.append({
                "الاسم": f"نشاط {keyword} - رقم {i}",
                "العنوان": f"{region}، {country}",
                "الهاتف": f"+201234567{i:02d}",
                "الإيميل": f"info@domain{i}.com",
                "رقم الواتساب": f"https://wa.me{i:02d}"
            })
        
        df = pd.DataFrame(demo_data)
        df.to_excel("Google_Maps_Data.xlsx", index=False)
        
        with open("Google_Maps_Data.xlsx", "rb") as file:
            st.download_button(label="📥 تحميل العينة المجانية (Excel)", data=file, file_name="Data_Demo.xlsx")
            
        st.markdown(f"""
            <div style="background-color:#fcf8e3; padding:20px; border-radius:10px; text-align:center; margin-top:20px;">
                <h4>هل تريد داتا أضخم وبدون قيود؟</h4>
                <p>تم استخراج العينة بنجاح! 🎉 هل تريد داتا غير محدودة مخصصة لمجالك الحالي، أو لأي مجال وتخصص آخر تريده بدون أي قيود؟</p>
                <a href="{STORE_URL}" target="_blank"><button style="background-color:#e74c3c; color:white; border:none; padding:12px; font-size:16px; border-radius:5px; width:100%; font-weight:bold;">🛒 اشترِ النسخة الكاملة الآن من متجرنا واكتسح سوقك!</button></a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ يرجى ملء جميع الحقول أولاً.")
