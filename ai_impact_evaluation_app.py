
import streamlit as st
from PIL import Image
import pandas as pd

# Load and display logo
logo = Image.open("logo.jpg")
st.image(logo, width=160)

st.markdown("""
# Hello AI: Impact Evaluation Tool
### AI for Life. One Byte at a Time.
""")

# 1. Organisation Profile
st.header("1. Organisation Profile")
org_name = st.text_input("Organisation Name")
domain = st.selectbox("Select Your Domain", ["Education", "Finance", "Healthcare", "Retail", "Other"])
num_employees = st.number_input("Total Staff", min_value=1)
num_depts = st.number_input("Number of Departments/Divisions", min_value=1)
ai_lead = st.radio("Is there an appointed AI lead?", ["Yes", "No"])

# 2. Current AI Usage
st.header("2. Current AI Usage")
ai_usage = st.radio("Are AI tools in use?", ["Yes", "No"])
ai_tools = st.multiselect("Which AI tools are being used?", ["ChatGPT", "MS Copilot", "Custom Models", "Turnitin AI", "AI LMS", "CRM AI Assistant"]) if ai_usage == "Yes" else []
usage_areas = st.multiselect("Where are they used?", ["Teaching", "Admin", "Customer Support", "Finance", "HR", "Student Support", "Clinical Support"])
confidence_level = st.slider("Staff AI confidence (estimated %)", 0, 100, 50)
ai_training = st.radio("Have staff received any AI training?", ["Yes", "No"])

# 3. Strategic Readiness
st.header("3. Strategic Readiness")
has_strategy = st.radio("Do you have an AI strategy?", ["Yes", "No"])
ai_budget = st.radio("Is there a dedicated AI budget?", ["Yes", "No", "Unsure"])
ai_goals = st.multiselect("Top goals for AI?", ["Efficiency", "Innovation", "Cost Saving", "Compliance", "Student/Customer Experience"])

# 4. Governance & Risk
st.header("4. Governance & Risk")
ai_policy = st.radio("Is there a formal AI usage policy?", ["Yes", "No", "In progress"])
risk_review = st.radio("Is there a risk review process for AI?", ["Yes", "No"])
integrity_risk = st.radio("Are AI-related misuse or integrity issues being tracked?", ["Yes", "No", "Not Applicable"])
data_ethics = st.radio("Are indigenous/cultural data principles considered?", ["Yes", "No", "Not Sure"])

# 5. Performance & ROI
st.header("5. Performance & ROI")
productivity_gain = st.slider("Estimated productivity gain from AI (%)", 0, 100, 20)
weekly_repetitive_hours = st.slider("Average weekly hours spent on repetitive tasks", 0, 40, 15)
tool_cost = st.number_input("Current AI-related tool costs (annual, NZD)", min_value=0)
planned_investment = st.number_input("Planned AI investment for next year (NZD)", min_value=0)

# 6. Domain-Specific Questions
st.header("6. Domain-Specific Evaluation")

if domain == "Education":
    st.subheader("🎓 Education Sector")
    num_courses_ai = st.number_input("Courses using AI-enhanced content/tools", min_value=0)
    misconduct_cases = st.number_input("Reported AI-related academic misconduct cases", min_value=0)
    ai_in_student_support = st.radio("Is AI used in student services (e.g., chatbots, timetabling)?", ["Yes", "No"])

elif domain == "Healthcare":
    st.subheader("🏥 Healthcare Sector")
    ai_in_diagnostics = st.radio("Is AI used in diagnostics or clinical decisions?", ["Yes", "No"])
    patient_data_use = st.radio("Is patient data used for training or analytics?", ["Yes", "No"])
    ethics_review = st.radio("Are AI tools reviewed by a health ethics board?", ["Yes", "No", "Not Sure"])

elif domain == "Finance":
    st.subheader("💰 Finance Sector")
    ai_in_fraud = st.radio("Is AI used for fraud detection or risk modelling?", ["Yes", "No"])
    regulatory_ai_policy = st.radio("Do AI systems comply with AML/FMA or related regulation?", ["Yes", "No", "Unsure"])
    customer_data_automation = st.radio("Is AI used in customer insights or credit scoring?", ["Yes", "No"])

elif domain == "Retail":
    st.subheader("🛒 Retail Sector")
    ai_in_inventory = st.radio("Is AI used in demand prediction or inventory management?", ["Yes", "No"])
    ai_chatbots = st.radio("Are AI chatbots used for customer service?", ["Yes", "No"])
    personalisation_ai = st.radio("Is AI used in product recommendations or pricing?", ["Yes", "No"])

# Submit Button
if st.button("Generate AI Impact Summary"):
    st.success("Evaluation Complete. Summary below:")

    # Simple scoring model
    readiness_score = 0
    readiness_score += 20 if has_strategy == "Yes" else 5
    readiness_score += 15 if ai_policy == "Yes" else 0
    readiness_score += int(confidence_level * 0.2)
    readiness_score += 15 if ai_goals else 5
    risk_flag = (integrity_risk == "No" or data_ethics == "No")

    # Score Interpretation
    st.subheader("📊 Readiness Score")
    st.write(f"**{readiness_score}/100**")
    if readiness_score > 70:
        st.success("✅ High Readiness: Strong foundation for responsible AI adoption.")
    elif readiness_score > 40:
        st.warning("⚠️ Moderate Readiness: Consider prioritising policy, training, and governance.")
    else:
        st.error("🚨 Low Readiness: Immediate strategy and policy development needed.")

    if risk_flag:
        st.warning("⚠️ Risk Alert: Governance and integrity procedures need urgent attention.")

    # Suggested Next Steps
    st.subheader("📋 Suggested Actions")
    st.markdown("""
    - Develop an organisation-wide AI policy
    - Conduct training workshops for all staff roles
    - Appoint or empower an AI lead / working group
    - Start pilot projects and track performance metrics
    - Ensure cultural and ethical frameworks are in place
    """)
