import streamlit as st
from pathlib import Path

# ---- Load CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# ---- Navigation Tabs ----
tabs = st.tabs(["About", "Resume", "Projects", "Skills", "Contact"])

with tabs[0]:
    st.markdown("<h1>Amogh M Sabane</h1>", unsafe_allow_html=True)
    st.markdown("🚀 Business Analytics | Product Strategy", unsafe_allow_html=True)
    st.write("Welcome to my portfolio! Explore my background, skills, and projects below.")

    st.subheader("About Me")
    st.write("""
    I'm a Business Analyst, keen on shaping business and product strategy through data.
    I enjoy solving high-impact problems at the intersection of business, analytics, and technology.

    With a background in both chemical engineering and engineering management, I bring a structured, analytical
    mindset to every challenge I take on. I've worked in AI-driven onboarding, B2B SaaS, and digital transformation
    for industries like gaming and media.

    Outside of work, I love building data-driven tools, analyzing sports trends, and reading about product strategy.
    """)

with tabs[1]:
    st.header("Work Experience")

    st.subheader("FlairX.ai – Product Management Analyst (Jul 2024 - Present)")
    st.write("""
    - Built Monte Carlo simulations and regression models to optimize pricing; increased lead conversion by 17%
    - Analyzed product/marketing data across 5 markets (SOM: $45M) using SQL
    - Conducted competitor analysis of 15+ firms, shaped strategic roadmap for B2B interview platform
    - Managed B2B SaaS product lifecycle and improved project timelines by 3 weeks
    - Boosted qualified leads by 1.3x using automated social campaigns
    """)

    st.subheader("Quantiphi Analytics – Business Analyst (Jul 2021 - Jun 2023)")
    st.write("""
    - Led 7 AI-enabled onboarding initiatives for banking/insurance clients
    - Reduced onboarding time by 20%, increased conversion by 32 basis points
    - Built predictive models and SQL frameworks for UAT, testing KPIs and product performance
    - Partnered with Google Cloud to develop: Video Deduplication & Watch Party (boosted engagement by 16%)
    - A/B tested metadata tagging; improved CTR by 14%, repeat visits by 23%
    """)

    st.header("Education")
    st.write("🎓 Master's in Engineering Management – University of Texas at Austin, 2024")
    st.write("🎓 B.Tech in Chemical Engineering – NIT Karnataka, 2021")

    st.download_button("📄 Download Resume", Path("Amogh_Sabane_Resume.pdf").read_bytes(), file_name="Amogh_Sabane_Resume_BA.pdf")

with tabs[2]:
    st.header("Projects")

    with st.expander("Supply Chain Optimization (Sep–Nov 2024)"):
        st.write("""
        - Applied machine learning to inventory management
        - Reduced holding costs by 20%, aligned with sustainability goals
        """)
        st.markdown("🔗 [GitHub Repo](https://github.com/AmoghSabane10/supply-chain-optimizer)")

    with st.expander("Customer Segmentation for Marketing (May–Aug 2024)"):
        st.write("""
        - Used SQL & Python on e-commerce data to cluster customers
        - Boosted campaign effectiveness and customer retention
        """)
        st.markdown("🔗 [GitHub Repo](https://github.com/AmoghSabane10/customer-segmentation)")

    with st.expander("FIFA 21 Transfer Predictions (Aug–Nov 2023)"):
        st.write("""
        - Built ML model to predict player value based on attributes
        - Enabled smarter transfer recommendations
        """)

with tabs[3]:
    st.header("Skills")
    st.write("**Technical Skills:** Python, SQL, Tableau, Power BI, UI/UX, Agile, SharePoint, Lean principles, Jira, QA support")
    st.write("**Business Skills:** Product Management, Business Analysis, GTM Strategy, Project Management, Communication, Consulting")
    st.write("**Certifications:** AWS Cloud Practitioner (2021), GCP Cloud Digital Leader (2022), GCP Associate Cloud Engineer (2023), IBM Product Manager Professional Certificate (2024)")

with tabs[4]:
    st.header("Contact Me")
    st.markdown("""
    - 📧 [Email](mailto:amogh.sabane10@gmail.com)
    - 💼 [LinkedIn](https://www.linkedin.com/in/amogh-sabane/)
    - 📍 Austin, TX
    """)

