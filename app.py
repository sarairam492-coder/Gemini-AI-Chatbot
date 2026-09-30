
import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# ---------------- LOAD ENVIRONMENT ----------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="✨",
    layout="centered"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* ===== MAIN BACKGROUND ===== */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(59, 130, 246, 0.35),
                transparent 35%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(168, 85, 247, 0.35),
                transparent 35%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(14, 165, 233, 0.25),
                transparent 40%
            ),
            linear-gradient(
                135deg,
                #0f172a,
                #172554,
                #312e81
            );

        color: white;
        min-height: 100vh;
    }


    /* ===== MAIN CONTAINER ===== */
    .block-container {
        max-width: 850px;
        padding-top: 50px;
        padding-bottom: 50px;
    }


    /* ===== TITLE ===== */
    h1 {
        text-align: center;

        font-size: 48px !important;
        font-weight: 800 !important;

        color: white !important;

        text-shadow:
            0 0 10px #60a5fa,
            0 0 25px #818cf8,
            0 0 45px #a855f7;

        margin-bottom: 5px;
    }


    /* ===== SUBTITLE ===== */
    .subtitle {
        text-align: center;

        color: #c7d2fe;

        font-size: 18px;

        margin-bottom: 30px;
    }


    /* ===== GEMINI ICON ===== */
    .gemini-icon {
        text-align: center;

        font-size: 55px;

        margin-bottom: 5px;

        filter:
            drop-shadow(0 0 10px #60a5fa)
            drop-shadow(0 0 20px #a855f7);
    }


    /* ===== STATUS ===== */
    .status {
        width: fit-content;

        margin: 0 auto 30px auto;

        padding: 8px 20px;

        border-radius: 30px;

        background: rgba(34, 197, 94, 0.12);

        border: 1px solid rgba(74, 222, 128, 0.35);

        color: #86efac;

        font-size: 14px;

        box-shadow:
            0 0 20px rgba(34, 197, 94, 0.15);
    }


    /* ===== INPUT LABEL ===== */
    .input-label {
        color: #e0e7ff;

        font-size: 17px;

        font-weight: 600;

        margin-bottom: 8px;
    }


    /* ===== TEXT AREA ===== */
    textarea {
        background: rgba(15, 23, 42, 0.65) !important;

        color: white !important;

        border: 2px solid rgba(129, 140, 248, 0.45) !important;

        border-radius: 18px !important;

        font-size: 16px !important;

        padding: 15px !important;

        backdrop-filter: blur(15px);

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.25);
    }


    textarea:focus {
        border: 2px solid #818cf8 !important;

        box-shadow:
            0 0 20px rgba(129, 140, 248, 0.4) !important;
    }


    textarea::placeholder {
        color: #94a3b8 !important;
    }


    /* ===== GENERATE BUTTON ===== */
    div.stButton > button {

        width: 100%;

        height: 55px;

        border-radius: 18px;

        border: none;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #7c3aed,
                #c026d3
            );

        color: white;

        font-size: 17px;

        font-weight: 700;

        margin-top: 15px;

        box-shadow:
            0 8px 25px rgba(99, 102, 241, 0.35);

        transition: all 0.3s ease;
    }


    div.stButton > button:hover {

        transform: translateY(-3px);

        box-shadow:
            0 12px 30px rgba(168, 85, 247, 0.5);

        background:
            linear-gradient(
                135deg,
                #3b82f6,
                #8b5cf6,
                #d946ef
            );
    }


    /* ===== RESPONSE CARD ===== */
    .response-card {

        margin-top: 30px;

        padding: 25px;

        border-radius: 22px;

        background:
            linear-gradient(
                135deg,
                rgba(59, 130, 246, 0.18),
                rgba(168, 85, 247, 0.18)
            );

        border: 1px solid rgba(255, 255, 255, 0.15);

        backdrop-filter: blur(15px);

        box-shadow:
            0 10px 35px rgba(0, 0, 0, 0.25);
    }


    /* ===== RESPONSE TITLE ===== */
    .response-title {

        font-size: 20px;

        font-weight: 700;

        color: #ddd6fe;

        margin-bottom: 12px;
    }


    /* ===== RESPONSE TEXT ===== */
    .response-text {

        color: #f8fafc;

        font-size: 16px;

        line-height: 1.7;

        white-space: pre-wrap;
    }


    /* ===== FOOTER ===== */
    .footer {

        text-align: center;

        margin-top: 45px;

        padding-top: 20px;

        border-top:
            1px solid rgba(255,255,255,0.1);

        color: #94a3b8;

        font-size: 13px;
    }


    /* ===== WARNING ===== */
    .warning-box {

        padding: 12px 18px;

        border-radius: 12px;

        background: rgba(245, 158, 11, 0.12);

        border: 1px solid rgba(245, 158, 11, 0.35);

        color: #fcd34d;

        margin-top: 15px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="gemini-icon">✨</div>',
    unsafe_allow_html=True
)

st.title("Gemini AI Chatbot")

st.markdown(
    '<div class="subtitle">'
    'Ask questions, explore ideas, and learn with Gemini AI'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="status">🟢 Gemini AI is Ready</div>',
    unsafe_allow_html=True
)


# ---------------- PROMPT ----------------

st.markdown(
    '<div class="input-label">💬 Enter your prompt</div>',
    unsafe_allow_html=True
)

prompt = st.text_area(
    "",
    placeholder="Example: Explain Artificial Intelligence in simple words...",
    height=150,
    label_visibility="collapsed"
)


# ---------------- BUTTON ----------------

if st.button("✨ Generate Response"):

    if prompt.strip():

        with st.spinner("✨ Gemini is thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                st.success("Response generated successfully!")

                # Response card
                st.markdown(
                    '<div class="response-card">'
                    '<div class="response-title">🤖 Gemini Response</div>'
                    '<div class="response-text">'
                    + response.text +
                    '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    "Something went wrong while generating the response."
                )

                st.write(e)

    else:

        st.markdown(
            '<div class="warning-box">'
            '⚠️ Please enter a prompt before generating a response.'
            '</div>',
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer">'
    '✨ Powered by Google Gemini AI • '
    '🎨 Streamlit • '
    '🚀 AI Assistant'
    '</div>',
    unsafe_allow_html=True
)