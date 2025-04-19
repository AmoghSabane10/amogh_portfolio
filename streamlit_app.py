import streamlit as st

# ---- Load CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# ---- Sidebar Navigation ----
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "About", "Resume", "Projects", "Skills", "Contact"])

# ---- Home ----
if section == "Home":
    st.markdown("<h1>Amogh M Sabane</h1>", unsafe_allow_html=True)
    st.markdown("🚀 Product Analyst | Data Strategist", unsafe_allow_html=True)
    st.write("Welcome to my portfolio! Explore my background, skills, and projects below.")

# ---- About ----
elif section == "About":
    st.header("About Me")
    st.write("""
    I'm a Product Management Analyst at FlairX.ai, where I use data to drive product decisions.
    I enjoy solving problems at the intersection of product, data, and business.
    """)

# ---- Resume ----
elif section == "Resume":
    st.header("Work Experience")

    st.subheader("FlairX.ai – Product Management Analyst (Jul 2024 - Present)")
    st.write("""
    - Built Monte Carlo simulations to optimize pricing.
    - 17% increase in lead conversion, 1.3x rise in qualified leads via automation.
    """)

    st.subheader("Quantiphi Analytics – Business Analyst (Jul 2021 - Jun 2023)")
    st.write("""
    - Spearheaded AI-enabled onboarding products.
    - Partnered with Google Cloud on 2 innovative AI tools.
    """)

    st.header("Education")
    st.write("🎓 Master's in Engineering Management – UT Austin, 2024")
    st.write("🎓 B.Tech in Chemical Engineering – NIT Karnataka, 2021")

# ---- Projects ----
elif section == "Projects":
    st.header("Projects")

    with st.expander("Supply Chain Optimization (Sep–Nov 2024)"):
        st.write("""
        - Used ML to reduce inventory holding costs by 20%.
        - Applied predictive analytics to improve procurement decisions.
        """)

    with st.expander("Customer Segmentation for Marketing (May–Aug 2024)"):
        st.write("""
        - Clustered users using SQL + Python.
        - Boosted customer retention and campaign ROI.
        """)

    with st.expander("FIFA 21 Transfer Predictions (Aug–Nov 2023)"):
        st.write("""
        - Used ML to model player ratings and predict transfer value replacements.
        """)

# ---- Skills ----
elif section == "Skills":
    st.header("Skills")
    st.write("**Technical Skills:** Python, SQL, Tableau, Power BI, UI/UX, Agile")
    st.write("**Business Skills:** Product Management, Stakeholder Management, GTM Strategy")
    st.write("**Certifications:** AWS Cloud Practitioner, GCP Cloud Digital Leader, IBM PM Certificate")

# ---- Contact ----
elif section == "Contact":
    st.header("Contact Me")
    st.markdown("""
    - 📧 [Email](mailto:amogh.sabane10@gmail.com)
    - 💼 [LinkedIn](https://www.linkedin.com/in/amogh-sabane/)
    - 📍 Based in Austin, TX
    """)

