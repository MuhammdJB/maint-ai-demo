import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# ================= CONFIGURATION =================
st.set_page_config(
    page_title="maintAI |",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= ULTRA-MODERN CSS (FIXED CONTRAST) =================
st.markdown("""
<style>
    /* Background: Deep Cyberpunk Blue/Black */
    .stApp { background-color: #0b0f19; color: #e0e0e0; }
    
    /* Hide Streamlit Header/Footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(30, 34, 45, 0.95); /* Increased opacity for readability */
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        color: #ffffff !important; /* Force White Text */
    }
    
    /* Neon Accents */
    h1, h2, h3 {
        background: -webkit-linear-gradient(45deg, #00Cca3, #00F2C3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Force High Contrast Text */
    p, span, label, div {
        color: #e0e0e0;
    }
    .stMarkdown p {
        color: #ffffff !important;
        font-weight: 400;
    }
    
    /* Chat Widget Styling */
    .chat-bubble {
        background-color: #1E2329;
        border-left: 3px solid #00Cca3;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        font-size: 13px;
    }

    /* Metric Value Styling */
    .metric-big { font-size: 36px; font-weight: 800; color: #fff; }
    .metric-small { font-size: 12px; color: #00Cca3; letter-spacing: 1.5px; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "step" not in st.session_state: st.session_state.step = 1

def go_next(): st.session_state.step += 1
def go_back(): 
    if st.session_state.step > 1: st.session_state.step -= 1
def reset(): st.session_state.step = 1

# ================= SIDEBAR CHAT (THE NEW FEATURE) =================
with st.sidebar:
    st.markdown("### 🤖 maintAI Assistant")
    st.markdown("<div class='chat-bubble'><b>AI:</b> System H-6022 is showing thermal stress deviations. How can I help?</div>", unsafe_allow_html=True)
    
    user_q = st.text_input("Ask about asset health...", placeholder="e.g., Root cause?")
    if user_q:
        st.markdown(f"<div class='chat-bubble' style='border-left:3px solid #555;'><b>You:</b> {user_q}</div>", unsafe_allow_html=True)
        time.sleep(0.5)
        st.markdown("<div class='chat-bubble'><b>AI:</b> Analysis indicates seal degradation due to cycling >110°C. Recommend Viton upgrade.</div>", unsafe_allow_html=True)

# ================= TOP NAVIGATION =================
c1, c2, c3 = st.columns([1, 8, 1])
with c1: st.markdown("### 💠 **maintAI**")
with c3: st.markdown(f"**USER:** M.J")

# ================= MAIN CONTENT =================

# --- STEP 1: HOME ---
if st.session_state.step == 1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.title("Asset Hierarchy Explorer")
    st.markdown("**Select a system segment to analyze.** (Click the chart)")
    
    c1, c2 = st.columns([3, 1])
    
    with c1:
        # SUNBURST CHART
        data = dict(
            character=["FPSO", "Process", "Utility", "Safety", "Separation", "Compression", "Power Gen", "Fire Water", "H-6022", "P-101", "V-505", "Turbine A", "Pump B", "P-Main"],
            parent=["", "FPSO", "FPSO", "FPSO", "Process", "Process", "Utility", "Safety", "Separation", "Separation", "Separation", "Power Gen", "Fire Water", "Fire Water"],
            value=[100, 50, 30, 20, 20, 30, 30, 20, 10, 5, 5, 30, 10, 10],
            health=[90, 80, 95, 98, 60, 85, 95, 98, 40, 60, 70, 95, 90, 99] 
        )
        fig = px.sunburst(
            data, names='character', parents='parent', values='value', color='health',
            color_continuous_scale='RdYlGn', title="Fleet Health Heatmap"
        )
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'), height=600)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # TELEMETRY
        st.markdown("### 📡 Live Telemetry")
        st.markdown("""
        <div style="font-family: monospace; font-size: 12px; color: #00Cca3; background: #111; padding: 10px; border-radius: 5px;">
        [10:42:01] P-101 Vib: 4.2 mm/s (ALERT)<br>
        [10:42:05] T-200 Lvl: 45% (NORMAL)<br>
        [10:42:12] K-401 Temp: 88°C (HIGH)<br>
        [10:42:18] Sys: Data Sync OK
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.warning("🚨 **Alert:** H-6022 (Separation) shows critical degradation.")
        if st.button("Analyze H-6022 ➜", type="primary"):
            go_next()
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2: DIGITAL TWIN ---
elif st.session_state.step == 2:
    
    c1, c2 = st.columns([2, 1])
    with c1: st.title("EA-6009 | Digital Twin")
    with c2: st.caption("ANALYSIS PROGRESS"); st.progress(0.4)

    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.image("https://thumbs.dreamstime.com/b/industrial-boiler-pipes-33626233.jpg", caption="MVR Reboiler Unit", use_container_width=True)
        st.markdown("#### Associated Tags")
        st.markdown("`TIT-201` `PIT-404` `XV-99`")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 🧬 Root Cause Diagnosis")
        
        categories = ['Vibration', 'Thermal Stress', 'Corrosion', 'Human Error', 'Design Flaw']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[5, 2, 4, 1, 1], theta=categories, fill='toself', name='Current Status', line_color='#FF4B4B'))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5], gridcolor='#444')),
            paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'), height=300
        )
        st.plotly_chart(fig, use_container_width=True)
        st.error("Conclusion: High vibration correlates with Thermal Cycling.")
        st.markdown("</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 6, 1])
    c1.button("⬅ Back", on_click=go_back)
    c3.button("Solutions ➜", on_click=go_next, type="primary")

# --- STEP 3: SIMULATOR ---
elif st.session_state.step == 3:
    st.title("🔮 Predictive Scenario Simulator")

    col_sim, col_graph = st.columns([1, 2])

    with col_sim:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### Strategy Configuration")
        opt_viton = st.checkbox("Upgrade Seals (Viton)", value=True)
        opt_iot = st.checkbox("Add IoT Vibration Sensor", value=False)
        opt_pm = st.slider("PM Frequency (Months)", 1, 24, 12)
        
        st.markdown("---")
        cost = 0
        if opt_viton: cost += 200
        if opt_iot: cost += 500
        cost += (10000 / opt_pm) 
        
        st.metric("Est. Annual Cost", f"${cost:,.0f}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_graph:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        x = np.linspace(0, 36, 36)
        y_base = 100 * np.exp(-0.1 * x)
        decay_rate = 0.1
        if opt_viton: decay_rate -= 0.03
        if opt_iot: decay_rate -= 0.02
        if opt_pm < 6: decay_rate -= 0.02
        y_sim = 100 * np.exp(-decay_rate * x)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y_base, name='Current Strategy', line=dict(color='#FF4B4B', dash='dash')))
        fig.add_trace(go.Scatter(x=x, y=y_sim, name='Proposed Strategy', line=dict(color='#00Cca3', width=4), fill='tonexty'))
        
        fig.update_layout(
            title="Projected Reliability Curve (3 Years)",
            xaxis_title="Months", yaxis_title="Reliability %",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'), hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 6, 1])
    c1.button("⬅ Back", on_click=go_back)
    c3.button("Execute ➜", on_click=go_next, type="primary")

# --- STEP 4: EXECUTION ---
elif st.session_state.step == 4:
    st.balloons()
    st.markdown("""
    <div class='glass-card' style='text-align: center; border: 2px solid #00Cca3;'>
        <h1 style='font-size: 60px;'>✅</h1>
        <h2>Optimization Deployed</h2>
        <p>The strategy has been committed to the Master Data Governance queue.</p>
        <br>
        <div style='display: flex; justify-content: center; gap: 20px;'>
            <div><span class='metric-small'>WORK ORDER</span><br><span class='metric-big'>#9921</span></div>
            <div><span class='metric-small'>ROI</span><br><span class='metric-big'>315%</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Return to Command Center"): reset()