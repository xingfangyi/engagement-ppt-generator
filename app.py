"""
Streamlit app for Engagement Survey PPT Analysis and Generation
This app converts engagement survey PPTs into improvement action plans
"""

import streamlit as st
import os
from pathlib import Path
from modules.ppt_parser import parse_ppt
from modules.data_analyzer import analyze_data
from modules.suggestion_generator import generate_suggestions
from modules.ppt_generator import generate_ppt

# Page configuration
st.set_page_config(
    page_title="Engagement Survey PPT Generator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #FF000F;
        font-size: 2.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🎯 Engagement Survey PPT Generator")
st.markdown("### Transform Your Engagement Survey into an Action Plan")
st.markdown("---")

# Introduction
with st.container():
    st.markdown("""
    **How it works:**
    1. Upload your engagement survey PPT (like PPT A)
    2. Our system analyzes the data
    3. Generates 12 improvement action items
    4. Creates a complete improvement plan PPT
    
    **What you'll get:**
    - Current status analysis
    - Key issues identified
    - 6 actions for sense of belonging
    - 6 actions for work-life balance
    - Leadership development support
    - Implementation timeline
    """)

st.markdown("---")

# Main application
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📤 Upload Survey PPT")
    uploaded_file = st.file_uploader(
        "Select your engagement survey PPT file",
        type=['pptx'],
        help="Upload a PowerPoint file (.pptx) containing employee engagement survey data"
    )

with col2:
    st.subheader("📊 File Info")
    if uploaded_file:
        st.info(f"File: {uploaded_file.name}\nSize: {uploaded_file.size} bytes")

st.markdown("---")

if uploaded_file:
    # Step 1: Parse PPT
    st.subheader("Step 1️⃣: Parsing Your Survey Data...")
    
    with st.spinner("Analyzing PPT structure..."):
        try:
            ppt_data = parse_ppt(uploaded_file)
            st.success("✅ PPT parsed successfully!")
        except Exception as e:
            st.error(f"❌ Error parsing PPT: {str(e)}")
            st.stop()
    
    # Display extracted data
    with st.expander("📋 Extracted Survey Data", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Department",
                ppt_data['department'][:20] + "..." if len(ppt_data['department']) > 20 else ppt_data['department']
            )
        
        with col2:
            st.metric(
                "Overall Score",
                f"{ppt_data['overall_score']:.1f}%"
            )
        
        with col3:
            st.metric(
                "Participants",
                ppt_data['total_participants']
            )
        
        with col4:
            st.metric(
                "Total Metrics",
                len(ppt_data['all_scores'])
            )
        
        if ppt_data['lowest_scores']:
            st.write("**Score Distribution:**")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"Lowest Score: **{ppt_data['lowest_scores'][0]}%**")
            with col2:
                st.write(f"Highest Score: **{ppt_data['highest_scores'][0]}%**")
    
    st.markdown("---")
    
    # Step 2: Analyze Data
    st.subheader("Step 2️⃣: Analyzing Data...")
    
    with st.spinner("Performing analysis..."):
        try:
            analysis = analyze_data(ppt_data)
            st.success("✅ Analysis completed!")
        except Exception as e:
            st.error(f"❌ Error analyzing data: {str(e)}")
            st.stop()
    
    # Display analysis results
    with st.expander("📊 Analysis Results", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Key Issues Identified:**")
            for i, issue in enumerate(analysis['key_issues'], 1):
                st.write(f"{i}. {issue}")
        
        with col2:
            st.write("**Priority Improvement Areas:**")
            for area in analysis['priority_areas']:
                st.write(f"• {area}")
        
        st.write(f"\n**Improvement Potential:** {analysis['improvement_potential']}")
    
    st.markdown("---")
    
    # Step 3: Generate Suggestions
    st.subheader("Step 3️⃣: Generating Improvement Suggestions...")
    
    with st.spinner("Creating improvement recommendations..."):
        try:
            suggestions = generate_suggestions(analysis)
            st.success("✅ Suggestions generated!")
        except Exception as e:
            st.error(f"❌ Error generating suggestions: {str(e)}")
            st.stop()
    
    # Display suggestions
    with st.expander("💡 Improvement Suggestions", expanded=True):
        
        st.write("### 🤝 Sense of Belonging Actions (6 items)")
        for i, suggestion in enumerate(suggestions['belonging'], 1):
            st.write(f"**{i}. {suggestion}**")
        
        st.write("\n### ⚖️ Work-Life Balance Actions (6 items)")
        for i, suggestion in enumerate(suggestions['work_life_balance'], 1):
            st.write(f"**{i}. {suggestion}**")
        
        st.write("\n### 📈 Leadership Development Support")
        for suggestion in suggestions['leadership']:
            st.write(f"• {suggestion}")
        
        if suggestions.get('additional_notes'):
            st.info(f"**📌 Note:** {suggestions['additional_notes']}")
    
    st.markdown("---")
    
    # Step 4: Generate PPT
    st.subheader("Step 4️⃣: Generate Action Plan PPT")
    
    generate_button = st.button(
        "🚀 Generate Improvement Plan PPT",
        key="generate_ppt",
        use_container_width=True
    )
    
    if generate_button:
        with st.spinner("Creating your improvement plan PPT..."):
            try:
                output_ppt = generate_ppt(ppt_data, analysis, suggestions)
                st.success("✅ PPT generated successfully!")
                
                # Read the file for download
                with open(output_ppt, 'rb') as f:
                    ppt_content = f.read()
                
                # Create download button
                st.download_button(
                    label="📥 Download Improvement Plan PPT",
                    data=ppt_content,
                    file_name=f"{ppt_data['department']}_Improvement_Plan_2026.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    use_container_width=True
                )
                
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Error generating PPT: {str(e)}")
                st.error("Please try again with a different file.")

else:
    st.info("👆 Please upload an engagement survey PPT file to get started!")

st.markdown("---")
st.markdown("""
**About This Tool:**
- Automatically analyzes engagement survey data
- Identifies key improvement areas
- Generates actionable recommendations
- Creates professional improvement plans
- Supports multiple departments

**Questions?** Contact your HR team for more information.
""")
