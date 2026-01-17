from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st


# ---------------------------------------------------------
# Config (must be first Streamlit call)
# ---------------------------------------------------------
st.set_page_config(
    page_title="VERO Risk Calculator",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Paths / assets
# ---------------------------------------------------------
HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

HERO_IMG = ASSETS / "vero_banner.png"
LOGO_IMG = ASSETS / "bioergotech_logo.png"


# ---------------------------------------------------------
# Theme tokens (BioERGOtech)
# ---------------------------------------------------------
THEME = {
    "primary": "#13d6b0",
    "primary_dark": "#0eb093",
    "text": "#1f2937",
    "muted": "rgba(31,41,55,0.75)",
    "border": "rgba(15,23,42,0.12)",
}


def img_to_base64(path: Path) -> str:
    """Return base64 string for an image path."""
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def inject_global_css(theme: dict) -> None:
    """Inject CSS for global layout + sidebar styling + hide Streamlit footer."""
    st.markdown(
        f"""
        <style>
        :root {{
            --primary: {theme["primary"]};
            --primary-dark: {theme["primary_dark"]};
            --text: {theme["text"]};
            --muted: {theme["muted"]};
            --border: {theme["border"]};
        }}

        /* Base font */
        html, body, [class*="css"] {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Roboto, Helvetica, Arial, sans-serif;
            font-size: 18px !important;
            color: var(--text);
        }}

        /* Main container spacing */
        .block-container {{
            padding-top: 0.9rem !important;
            padding-bottom: 1.8rem !important;
            max-width: 100% !important;
        }}

        /* Sidebar background */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(
                180deg,
                rgba(19,214,176,0.12),
                rgba(255,255,255,1) 55%
            );
            border-right: 1px solid var(--border);
        }}

        section[data-testid="stSidebar"] .block-container {{
            padding-top: 1.2rem !important;
        }}

        /* Increase sidebar text size everywhere */
        section[data-testid="stSidebar"] * {{
            font-size: 19px !important;
            line-height: 1.55 !important;
        }}

        /* Sidebar page list */
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] span,
        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a {{
            font-size: 20px !important;
            font-weight: 650 !important;
        }}

        section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a[aria-current="page"] {{
            color: var(--primary-dark) !important;
        }}

        /* Sidebar banner */
        .sidebar-banner {{
            background: rgba(19,214,176,0.14);
            border: 1px solid rgba(19,214,176,0.28);
            border-radius: 16px;
            padding: 18px;
            margin-bottom: 16px;
        }}

        .sidebar-banner h3 {{
            margin: 0 0 6px 0;
            font-size: 1.35rem;
            font-weight: 800;
        }}

        .sidebar-banner p {{
            margin: 0;
            font-size: 1.05rem;
            color: var(--muted);
        }}

        /* Hero section */
        .vero-hero {{
            width: 100%;
            height: calc(100vh - 4.5rem);
            background-size: cover;
            background-repeat: no-repeat;
            background-position: top center;
            border-radius: 20px;
            border: 1px solid var(--border);
            overflow: hidden;
        }}

        @media (max-width: 900px) {{
            .vero-hero {{ height: 55vh; }}
            section[data-testid="stSidebar"] * {{
                font-size: 18px !important;
            }}
        }}

        /* Hide Streamlit footer */
        footer {{ visibility: hidden; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(logo_path: Path) -> None:
    with st.sidebar:
        if logo_path.exists():
            st.image(str(logo_path), use_container_width=True)

        st.markdown(
            """
            <div class="sidebar-banner">
                <h3>VERO Risk Calculator</h3>
                <p>
                    Use the pages below:
                    <br>• <b>Patient Input</b>
                    <br>• <b>Results &amp; Visual Analytics</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption("Start with Patient Input, then review Results & Visual Analytics.")


def render_home(hero_path: Path) -> None:
    """Home page: hero only."""
    if not hero_path.exists():
        st.warning("Hero image not found. Place it at app/assets/vero_banner.png")
        return

    hero_b64 = img_to_base64(hero_path)
    st.markdown(
        f"""
        <div class="vero-hero"
             style="background-image:url('data:image/png;base64,{hero_b64}');">
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# App entry
# ---------------------------------------------------------
inject_global_css(THEME)
render_sidebar(LOGO_IMG)
render_home(HERO_IMG)
