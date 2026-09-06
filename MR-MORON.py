import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MR MORON — Reverse Engineering Lab",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

PROJECTS = [
    {"id": 1, "name": "My Voice v1", "slug": "my-voice-v1", "category": "Workplace Feedback", "version": "v1", "short": "Workplace experience sharing UI", "full": "Early Streamlit interface for associates to record and review workplace life experiences. Reverse-engineered from real station feedback loops."},
    {"id": 2, "name": "Rural Service Rural Reverse Engineering v1", "slug": "rural-service-rural-reverse-engineering-v1", "category": "Reverse Engineering", "version": "v1", "short": "RSR process and system reverse-engineering tool", "full": "Documents and reconstructs Rural / Rural Super Rural workflows, systems, and station operating patterns."},
    {"id": 3, "name": "Amazon My Voice v1", "slug": "amazon-my-voice-v1", "category": "Workplace Feedback", "version": "v1", "short": "Share workplace life experiences", "full": "A user interface that allows the user to share their experiences regarding workplace life."},
    {"id": 4, "name": "RSR Plus HR Tools — Station Conduct Tool", "slug": "amazon-rsr-plus-hr-tools", "category": "HR / Conduct", "version": "v1", "short": "Role-tied station conduct logger", "full": "Logs and reviews conduct tied to Process Assistant, Area Manager, and Operations Manager duties at RSR Plus stations. Each entry is bound to a station, an employee, and a specific duty so notes stay traceable to the responsibility they relate to."},
    {"id": 5, "name": "RSR Site-Level Planning Tool", "slug": "rsr-site-level-planning-tool", "category": "Planning", "version": "v1", "short": "Site-level operations planning", "full": "Planning workspace for RSR site labor, volume, and daily operating plans."},
    {"id": 6, "name": "Same-Day Site Planning Tool", "slug": "same-day-site-planning-tool", "category": "Planning", "version": "v1", "short": "Same-day station planning", "full": "Same-day site planning for staffing, volume, and execution adjustments during the operating day."},
    {"id": 7, "name": "Amazon Harassment Complaint Compiler", "slug": "amazon-harassment-complaint-compiler", "category": "Workplace Complaints", "version": "v1", "short": "Compile harassment complaint records", "full": "Organizes dates, people, locations, and narrative details of workplace harassment complaints into a structured packet."},
    {"id": 8, "name": "Amazon Rural Super Rural Plus Stowing v1", "slug": "amazon-rural-super-rural-plus-stowing-v1", "category": "Operations", "version": "v1", "short": "RSR+ stowing workflow tool", "full": "Stowing operations tool for Rural Super Rural Plus stations covering bin flow, rates, and stow-path tracking."},
    {"id": 9, "name": "DSP Amazon", "slug": "dsp-amazon", "category": "Delivery Partners", "version": "v1", "short": "DSP operations workspace", "full": "Delivery Service Partner workflows, routes, and partner-station coordination."},
    {"id": 10, "name": "Business Oversight Research", "slug": "business-oversight-research", "category": "Research / Oversight", "version": "v1", "short": "Business oversight research notebook", "full": "Research and documentation app for oversight findings, metrics, and follow-up questions."},
    {"id": 11, "name": "Navigation App v1", "slug": "navigation-app-v1", "category": "Logistics", "version": "v1", "short": "Route and navigation helper", "full": "Navigation and routing helper for rural / last-mile delivery context."},
    {"id": 12, "name": "Inventory Control System", "slug": "inventory-control-system", "category": "Inventory", "version": "v1", "short": "Inventory tracking and control", "full": "Counts, locations, discrepancies, and reconciliation."},
    {"id": 13, "name": "The Adventures of John Doe", "slug": "the-adventures-of-john-doe", "category": "Narrative / Demo", "version": "v1", "short": "Narrative case-study app", "full": "Story-driven walkthrough using a John Doe persona to reconstruct workplace scenarios and documented events."},
    {"id": 14, "name": "Business Metrics Tracker", "slug": "business-metrics-tracker", "category": "Metrics", "version": "v1", "short": "Track core business metrics", "full": "Logs and charts operational and business metrics over time."},
    {"id": 15, "name": "C-D-O-Q v1", "slug": "c-d-o-q-v1", "category": "Quality / Ops", "version": "v1", "short": "Cost Delivery Operations Quality tracker", "full": "Tracks Cost / Delivery / Operations / Quality indicators reconstructed from station reporting language."},
    {"id": 16, "name": "RSR Reporting Data v1", "slug": "rsr-reporting-data-v1", "category": "Reporting", "version": "v1", "short": "RSR reporting dataset viewer", "full": "Data layer and viewer for Rural Service Rural reporting extracts and station datasets."},
    {"id": 17, "name": "RSR Plus Stations Reporting Tool v1", "slug": "rsr-plus-stations-reporting-tool-v1", "category": "Reporting", "version": "v1", "short": "RSR+ multi-station reporting", "full": "Reporting for RSR Plus station performance, volume, and exception summaries."},
    {"id": 18, "name": ".eml-to-.json-v1", "slug": "eml-to-json-v1", "category": "Utilities", "version": "v1", "short": "Convert .eml files to JSON", "full": "Parses email .eml files into structured JSON for logs, evidence packets, and searchable archives."},
    {"id": 19, "name": "Amazon RSR Plus Performance Grader v1", "slug": "amazon-rsr-plus-performance-grader-v1", "category": "Performance", "version": "v1", "short": "Grade RSR+ role performance", "full": "Scores RSR Plus leadership and associate performance against defined duty and metric rubrics."},
    {"id": 20, "name": "Linear Regression v1", "slug": "linear-regression-v1", "category": "Analytics", "version": "v1", "short": "Linear regression analysis app", "full": "Runs linear regression on operational datasets and visualizes predicted vs actual results."},
    {"id": 21, "name": "Amazon RSR Plus Associate Tools v1", "slug": "amazon-rsr-plus-associate-tools-v1", "category": "Associate Tools", "version": "v1", "short": "Associate-facing RSR+ toolkit", "full": "Associate utilities for RSR Plus stations: task aids, lookups, and self-service logs."},
    {"id": 22, "name": "Workplace Racial Discrimination v1", "slug": "workplace-racial-discrimination-v1", "category": "Workplace Complaints", "version": "v1", "short": "Document racial discrimination reports", "full": "Records workplace racial discrimination incidents, evidence, and follow-up status. Original slug: workplace-racial-descirimination-v1."},
    {"id": 23, "name": "Workplace Accountability App v1", "slug": "workplace-accountability-app-v1", "category": "Accountability", "version": "v1", "short": "Track workplace accountability items", "full": "Commitments, incidents, owners, due dates, and closure status."},
    {"id": 24, "name": "Contradictory Data-Driven Environment v1", "slug": "contradictory-data-driven-environment-v1", "category": "Research / Analytics", "version": "v1", "short": "Flag conflicting operational data", "full": "Surfaces contradictions between stated metrics, policy, and observed station data."},
    {"id": 25, "name": "Talk-Time Wage Theft Tool", "slug": "talk-time-wage-theft-tool", "category": "Timekeeping / Labor", "version": "v1", "short": "Analyze talk-time vs paid time", "full": "Compares talk-time, meeting time, and unpaid off-clock intervals against scheduled and paid hours."},
    {"id": 26, "name": "Amazon RSR Plus Pick Stow Pack v1", "slug": "amazon-rsr-plus-pick-stow-pack-v1", "category": "Operations", "version": "v1", "short": "Pick stow pack operations suite", "full": "Combined pick / stow / pack operations app for RSR Plus path, rates, and process checks."},
    {"id": 27, "name": "60-Day Interval Amazon Events Reporting Tool v1", "slug": "60-day-interval-amazon-events-reporting-tool-v1", "category": "Reporting", "version": "v1", "short": "60-day event interval reports", "full": "Groups Amazon workplace and station events into rolling 60-day intervals."},
    {"id": 28, "name": "HERO Amazon Rating Tool v1", "slug": "helping-engaging-respectful-obsessed-amazon-rating-tool-v1", "category": "Performance / Culture", "version": "v1", "short": "HERO leadership rating rubric", "full": "Rates leadership and workplace interactions on Helping, Engaging, Respectful, Obsessed (HERO) criteria."},
    {"id": 29, "name": "Amazon RSR Complaint Tool v1", "slug": "amazon-rsr-complaint-tool-v1", "category": "Workplace Complaints", "version": "v1", "short": "Log and organize RSR complaints", "full": "Complaint intake and case organization for Rural / RSR Plus station issues."},
    {"id": 30, "name": "Amazon Time Keeper v1", "slug": "amazon-time-keeper-v1", "category": "Timekeeping / Labor", "version": "v1", "short": "Track worked vs scheduled time", "full": "Punches, breaks, talk time, and discrepancies between worked and paid hours."},
    {"id": 31, "name": "Thinking Backwards v1", "slug": "thinking-backwards-v1", "category": "Problem Solving", "version": "v1", "short": "Work-backward problem solver", "full": "Traces outcomes backward to root process and decision points."},
    {"id": 32, "name": "Gas Stations Filter 56003-56001", "slug": "gas-stations-filter-56003-56001", "category": "Local Utilities", "version": "v1", "short": "Filter gas stations by ZIP 56003/56001", "full": "Location filter for gas stations in ZIP codes 56003 and 56001 (Mankato / North Mankato, MN area)."},
    {"id": 33, "name": "AI Agent Tools", "slug": "ai-agent-tools", "category": "AI / Automation", "version": "v1", "short": "AI agent utility suite", "full": "AI agent helpers, prompts, and task runners for project research and documentation."},
    {"id": 34, "name": "Flex Delivery App Reverse Engineering", "slug": "flex-delivery-app-reverse-engineering", "category": "Reverse Engineering", "version": "v1", "short": "Amazon Flex delivery app RE notes", "full": "Reverse-engineering notebook for Amazon Flex delivery app flows, screens, and operational logic."},
    {"id": 35, "name": "Scheduling", "slug": "scheduling", "category": "Planning", "version": "v1", "short": "Shift and labor scheduling", "full": "Shifts, coverage, and station labor plans."},
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

    .stApp {
        background:
            radial-gradient(1200px 500px at 10% -10%, #1b3a2f 0%, transparent 50%),
            radial-gradient(900px 400px at 110% 0%, #3a2a12 0%, transparent 45%),
            #0b0d0c;
        color: #e8efe9;
    }

    [data-testid="stSidebar"] {
        background: #101412;
        border-right: 1px solid #24332c;
    }

    .hero {
        border: 1px solid #2f4a3d;
        background: linear-gradient(135deg, #121916 0%, #1a241c 60%, #241c12 100%);
        padding: 28px 32px;
        border-radius: 16px;
        margin-bottom: 18px;
    }
    .kicker {
        font-family: 'IBM Plex Mono', monospace;
        letter-spacing: 0.18em;
        font-size: 12px;
        color: #c9a227;
        margin-bottom: 8px;
    }
    .hero h1 {
        margin: 0;
        font-size: 42px;
        line-height: 1.05;
        color: #f4f7f4;
    }
    .hero h1 span { color: #d4af37; }
    .hero p {
        margin: 10px 0 0 0;
        max-width: 820px;
        color: #c5d2c8;
        font-size: 16px;
    }
    .sig {
        margin-top: 14px;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 13px;
        color: #9fb7a8;
    }

    .metric-box {
        background: #141a16;
        border: 1px solid #2a3b32;
        border-radius: 12px;
        padding: 14px 16px;
    }
    .metric-box .lbl {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 11px;
        color: #8fa396;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    .metric-box .val {
        font-size: 28px;
        font-weight: 700;
        color: #f0f5
