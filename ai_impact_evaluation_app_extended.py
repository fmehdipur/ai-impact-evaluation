
import streamlit as st
from PIL import Image
import pandas as pd
from io import BytesIO
from datetime import datetime

st.set_page_config(page_title="Nova – AI Impact Evaluation", layout="wide")


# Load logo
logo = Image.open("logo.jpg")
st.image(logo, width=160)

# Update app name and subtitle
st.markdown("# Nova – AI Impact Evaluation App")
st.markdown("### Navigate your AI readiness with confidence.")


# --- Form Inputs ---
st.header("1. Organisation Profile")
org_name = st.text_input("Organisation Name")
domain = st.selectbox("Select Your Domain", ["Education", "Finance", "Healthcare", "Retail", "Other"])
num_employees = st.number_input("Total Staff", min_value=1)
num_depts = st.number_input("Number of Departments", min_value=1)
ai_lead = st.radio("Is there an appointed AI lead?", ["Yes", "No"])

st.header("2. Current AI Usage")
ai_usage = st.radio("Are AI tools currently in use?", ["Yes", "No"])
ai_tools = st.multiselect("Which tools?", ["ChatGPT", "MS Copilot", "Custom Models", "Turnitin AI", "AI LMS", "CRM AI Assistant"]) if ai_usage == "Yes" else []
usage_areas = st.multiselect("Where are AI tools used?", ["Teaching", "Admin", "Support", "Finance", "HR", "Student Services"])
confidence_level = st.slider("Staff AI confidence (%)", 0, 100, 50)
ai_training = st.radio("Have staff received training?", ["Yes", "No"])

st.header("3. Strategic Readiness")
has_strategy = st.radio("Do you have an AI strategy?", ["Yes", "No"])
ai_budget = st.radio("Is there a budget?", ["Yes", "No", "Unsure"])
ai_goals = st.multiselect("Top AI goals?", ["Efficiency", "Innovation", "Cost Saving", "Compliance", "Experience"])

st.header("4. Governance & Risk")
ai_policy = st.radio("Is there an AI usage policy?", ["Yes", "No", "In progress"])
risk_review = st.radio("Is there a risk review process?", ["Yes", "No"])
integrity_risk = st.radio("Is AI misuse tracked?", ["Yes", "No", "N/A"])
data_ethics = st.radio("Are cultural/indigenous data principles considered?", ["Yes", "No", "Not Sure"])

st.header("5. Performance & ROI")
productivity_gain = st.slider("Estimated productivity gain (%)", 0, 100, 20)
weekly_repetitive_hours = st.slider("Weekly repetitive task hours", 0, 40, 10)
tool_cost = st.number_input("Current AI tool costs (annual, NZD)", min_value=0)
planned_investment = st.number_input("Planned AI investment (next year, NZD)", min_value=0)

st.header("6. Domain-Specific (Education Example)")
if domain == "Education":
    num_courses_ai = st.number_input("Courses using AI", min_value=0)
    misconduct_cases = st.number_input("AI-related misconduct cases", min_value=0)
    ai_in_support = st.radio("Is AI used in student support?", ["Yes", "No"])

# --- Generate Report ---
def generate_report():
    today = datetime.today().strftime('%Y-%m-%d')
    score = 20 if has_strategy == "Yes" else 5
    score += 15 if ai_policy == "Yes" else 0
    score += int(confidence_level * 0.2)
    score += 15 if ai_goals else 5
    risk_flag = (integrity_risk == "No" or data_ethics == "No")

    report = f"""
    <h2>Nova AI Impact Evaluation Report – {org_name}</h2>
    <p><b>Date:</b> {today}</p>
    <h3>1. Organisation Snapshot</h3>
    <ul>
        <li><b>Domain:</b> {domain}</li>
        <li><b>Total Staff:</b> {num_employees}</li>
        <li><b>Departments:</b> {num_depts}</li>
        <li><b>AI Lead Appointed:</b> {ai_lead}</li>
    </ul>

    <h3>2. AI Usage Overview</h3>
    <ul>
        <li><b>AI Tools Used:</b> {', '.join(ai_tools)}</li>
        <li><b>Usage Areas:</b> {', '.join(usage_areas)}</li>
        <li><b>Confidence Level:</b> {confidence_level}%</li>
        <li><b>Training Provided:</b> {ai_training}</li>
    </ul>

    <h3>3. Strategic Readiness</h3>
    <ul>
        <li><b>Strategy in Place:</b> {has_strategy}</li>
        <li><b>AI Budget:</b> {ai_budget}</li>
        <li><b>Goals:</b> {', '.join(ai_goals)}</li>
        <li><b>Readiness Score:</b> {score}/100</li>
    </ul>

    <h3>4. Governance & Risk Profile</h3>
    <ul>
        <li><b>AI Policy:</b> {ai_policy}</li>
        <li><b>Risk Review:</b> {risk_review}</li>
        <li><b>Misuse Tracking:</b> {integrity_risk}</li>
        <li><b>Data Ethics Considered:</b> {data_ethics}</li>
    </ul>
    <p><b>Risk Flag:</b> {"⚠️ Yes – Review needed." if risk_flag else "No significant flag."}</p>

    <h3>5. ROI & Performance Potential</h3>
    <ul>
        <li><b>Productivity Gain:</b> {productivity_gain}%</li>
        <li><b>Weekly Repetitive Work:</b> {weekly_repetitive_hours} hours</li>
        <li><b>Annual Tool Cost:</b> ${tool_cost}</li>
        <li><b>Planned Investment:</b> ${planned_investment}</li>
    </ul>

    <h3>6. Recommendations</h3>
    <ul>
        <li>Develop or update your AI policy framework</li>
        <li>Establish an AI governance or advisory board</li>
        <li>Run staff capability workshops on AI integration</li>
        <li>Use pilot projects to measure ROI and risks</li>
    </ul>
    """
    return report, score

# Display full report in browser
if st.button("Generate Detailed Report"):
    html_report, score = generate_report()
    st.components.v1.html(html_report, height=900, scrolling=True)
