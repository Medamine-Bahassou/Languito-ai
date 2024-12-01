import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LanguitoAI - Your Advanced Language Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add logo at the top of sidebar
import os

# Get the absolute path to the image
image_path = os.path.join(os.getcwd(), 'images', 'logo.png')

# Display the image in the sidebar
st.sidebar.image(image_path, width=300)

# Custom CSS
st.markdown("""
    <style>
        /* Main container styling */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        /* Header styling */
        .header-container {
            text-align: center;
            padding: 3rem 0;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            animation: fadeIn 1s ease-in;
        }
        
        .main-title {
            font-size: 3.5rem;
            color: #2c3e50;
            margin-bottom: 1rem;
            font-weight: bold;
        }
        
        .subtitle {
            font-size: 1.4rem;
            color: #34495e;
            opacity: 0.9;
        }
        
        /* Feature card styling */
        .feature-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            margin: 1rem 0;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        /* Statistics box styling */
        .stat-box {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .stat-box:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            .subtitle {
                font-size: 1.2rem;
            }
        }
    </style>
""", unsafe_allow_html=True)



# Header
banner_path = os.path.join(os.getcwd(), 'images', 'banner.png')


st.image(banner_path, use_container_width=True)


st.markdown("""
    <div class="header-container">
        <h1 class="main-title">🌏 Welcome to LanguitoAI</h1>
        <p class="subtitle">Learn, play, and grow: Language fun for kids!</p>
    </div>
""", unsafe_allow_html=True)

# Feature sections
st.markdown("""
    <div class="feature-card">
        <h2>Features</h2>
        <ul>
            <li>Quizes </li>
            <li>AI chat assistant </li>
            <li>Translator</li>
            <li>Prononciation guide</li>
            <li>Dictionnary</li>
        </ul>
    </div>
    
""", unsafe_allow_html=True)

# workflow
st.markdown("""
        <h2>Workflow</h2>
""", unsafe_allow_html=True)
# st.image("images/workflow.png")
workflow_path = os.path.join(os.getcwd(), 'images', 'workflow.png')
st.image(workflow_path)

 
# Call to action
st.markdown("""
    <div style='text-align: center; margin-top: 3rem; padding: 2rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'>
        <h2>Ready to Get Started?</h2>
        <p style='margin: 1rem 0;'>Choose a feature from the sidebar to begin your learning journey!</p>
    </div>
""", unsafe_allow_html=True)
