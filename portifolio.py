import base64
from html import escape
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="William Eustáquio | Desenvolvedor de IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

pdf_path = Path("Curriculo_Moderno_William_Eustaquio.pdf")
pdf_bytes = pdf_path.read_bytes() if pdf_path.exists() else None


def image_to_data_uri(path: str) -> str | None:
    image_path = Path(path)
    if not image_path.exists():
        return None

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(image_path.suffix.lower())
    if not mime_type:
        return None

    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def badge_group(items: list[str], badge_class: str = "tag-badge") -> str:
    return "".join(
        f'<span class="{badge_class}">{escape(item)}</span>' for item in items
    )


def project_card_html(title: str, description: str, tags: list[str], url: str, image_path: str) -> str:
    image_uri = image_to_data_uri(image_path)
    media = (
        f'<div class="project-media"><img src="{image_uri}" alt="{escape(title)}"></div>'
        if image_uri
        else '<div class="project-media project-media-fallback">Preview indisponivel</div>'
    )
    return f"""
    <article class="project-card card-strong">
        {media}
        <div class="project-title">{escape(title)}</div>
        <div class="project-text">{escape(description)}</div>
        <div class="badge-row">{badge_group(tags)}</div>
        <div class="button-row">
            <a class="action-button" href="{escape(url)}" target="_blank">Acessar projeto</a>
        </div>
    </article>
    """


def certificate_card_html(title: str, provider: str, period: str, hours: str) -> str:
    return f"""
    <article class="certificate-card card-soft">
        <div class="section-kicker">Certificado</div>
        <div class="project-title">{escape(title)}</div>
        <div class="timeline-meta">{escape(provider)}</div>
        <div class="section-text">{escape(period)}</div>
        <div class="badge-row badge-row-top">
            <span class="tech-badge">{escape(hours)}</span>
        </div>
    </article>
    """


profile_image_uri = image_to_data_uri("perfil/imagem-oculos1.jpg")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --surface-1: rgba(255,255,255,0.055);
    --surface-2: rgba(15,23,42,0.76);
    --surface-3: rgba(2,6,23,0.62);
    --border-soft: rgba(148,163,184,0.16);
    --border-strong: rgba(56,189,248,0.22);
    --text-main: #e5e7eb;
    --text-soft: #cbd5e1;
    --text-muted: #94a3b8;
    --accent-a: #22d3ee;
    --accent-b: #3b82f6;
    --accent-c: #38bdf8;
}

* { font-family: 'Inter', sans-serif; }

html, body, [class*="css"] {
    color: var(--text-main);
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(34,211,238,0.12), transparent 20%),
        radial-gradient(circle at 100% 0%, rgba(59,130,246,0.13), transparent 25%),
        radial-gradient(circle at 100% 100%, rgba(14,165,233,0.10), transparent 22%),
        linear-gradient(135deg, #020617 0%, #0b1120 45%, #111827 100%);
}

.block-container {
    max-width: 1360px;
    padding-top: 1.2rem;
    padding-bottom: 2.6rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(2,6,23,0.98), rgba(15,23,42,0.98));
    border-right: 1px solid rgba(255,255,255,0.06);
}

.hero-card, .glass-card, .project-card, .contact-card, .placeholder-shot, .profile-card, .certificate-card, .action-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(15,23,42,0.76));
    border: 1px solid var(--border-soft);
    border-radius: 28px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.24);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    animation: fadeUp 0.55s ease both;
    transition: transform 0.28s ease, border-color 0.28s ease, box-shadow 0.28s ease, background 0.28s ease;
}

.hero-card::before, .glass-card::before, .project-card::before, .contact-card::before, .profile-card::before, .certificate-card::before, .action-card::before {
    content: "";
    position: absolute;
    inset: 0 auto auto 0;
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, rgba(34,211,238,0.55), rgba(59,130,246,0.18), transparent 78%);
}

.hero-card { padding: 36px; }
.glass-card, .project-card, .contact-card, .placeholder-shot, .profile-card, .certificate-card, .action-card { padding: 22px; }

.glass-card:hover, .project-card:hover, .contact-card:hover, .profile-card:hover, .certificate-card:hover, .action-card:hover {
    transform: translateY(-5px);
    border-color: rgba(56,189,248,0.3);
    box-shadow: 0 24px 60px rgba(0,0,0,0.28);
}

.card-compact { min-height: 188px; }
.card-medium { min-height: 238px; }
.card-tall { min-height: 320px; }
.card-strong { min-height: 540px; }
.card-soft { min-height: 200px; }

.profile-card {
    min-height: 238px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 16px;
    background: radial-gradient(circle at top, rgba(34,211,238,0.14), transparent 45%), linear-gradient(180deg, rgba(255,255,255,0.06), rgba(15,23,42,0.82));
}

.profile-photo {
    width: min(100%, 230px);
    aspect-ratio: 4 / 5;
    object-fit: cover;
    display: block;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 18px 45px rgba(0,0,0,0.32);
}

.profile-name {
    color: #f8fafc;
    font-size: 1.32rem;
    font-weight: 800;
    line-height: 1.2;
}

.profile-role {
    color: var(--text-soft);
    font-size: 0.96rem;
    line-height: 1.7;
    max-width: 28ch;
}

.profile-meta {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
}

.avatar-wrap {
    width: 88px;
    height: 88px;
    border-radius: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #0ea5e9, #2563eb);
    color: white;
    font-size: 2rem;
    font-weight: 900;
    box-shadow: 0 16px 30px rgba(14,165,233,0.25);
    margin-bottom: 18px;
}

.eyebrow {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(56,189,248,0.10);
    border: 1px solid rgba(56,189,248,0.20);
    color: #7dd3fc;
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 16px;
}

.status-badge {
    display: inline-block;
    margin-left: 10px;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.25);
    color: #86efac;
    font-size: 0.8rem;
    font-weight: 800;
}

.hero-title {
    font-size: 3.2rem;
    line-height: 1.02;
    font-weight: 900;
    color: #f8fafc;
    margin-bottom: 12px;
}

.hero-gradient {
    background: linear-gradient(90deg, #22d3ee 0%, #60a5fa 45%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1.04rem;
    line-height: 1.9;
    color: #cbd5e1;
    max-width: 900px;
    margin-bottom: 22px;
}

.badges-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 18px;
}

.tech-badge, .tag-badge {
    display: inline-block;
    border-radius: 999px;
    padding: 9px 14px;
    font-size: 0.83rem;
    font-weight: 700;
}

.tech-badge {
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
}

.tag-badge {
    background: rgba(56,189,248,0.10);
    border: 1px solid rgba(56,189,248,0.16);
    color: #7dd3fc;
}

.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.badge-row-top {
    margin-top: 18px;
}

.section-title {
    font-size: 1.12rem;
    color: #f8fafc;
    font-weight: 800;
    margin-bottom: 14px;
}

.section-text {
    color: var(--text-soft);
    line-height: 1.85;
    font-size: 0.96rem;
}

.section-kicker {
    color: #7dd3fc;
    font-size: 0.78rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 14px;
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 14px;
    margin-top: 18px;
}

.metric-box {
    background: rgba(2,6,23,0.46);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 18px;
    padding: 18px;
}

.metric-label {
    color: #94a3b8;
    font-size: 0.8rem;
    margin-bottom: 6px;
}

.metric-value {
    color: #f8fafc;
    font-weight: 800;
    font-size: 1.12rem;
}

.contact-line {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: var(--text-main);
    font-size: 0.95rem;
}

.contact-line:last-child {
    border-bottom: none;
}

.contact-anchor {
    color: inherit;
    text-decoration: none;
    word-break: break-word;
    overflow-wrap: anywhere;
}

.contact-anchor:hover {
    color: #7dd3fc;
}

.project-card {
    display: flex;
    flex-direction: column;
}

.project-media {
    width: 100%;
    aspect-ratio: 16 / 10;
    border-radius: 22px;
    overflow: hidden;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    background: linear-gradient(135deg, rgba(34,211,238,0.12), rgba(37,99,235,0.18));
}

.project-media img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.project-media-fallback {
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.82rem;
}

.project-title {
    font-size: 1.08rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 8px;
}

.project-text {
    color: var(--text-soft);
    line-height: 1.78;
    font-size: 0.95rem;
    margin-bottom: 16px;
}

.button-row {
    margin-top: auto;
    padding-top: 18px;
}

.action-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 50px;
    padding: 12px 18px;
    border-radius: 16px;
    border: 1px solid rgba(56,189,248,0.24);
    background: linear-gradient(135deg, rgba(14,165,233,0.22), rgba(37,99,235,0.22));
    color: #f8fafc;
    text-decoration: none;
    font-weight: 700;
    letter-spacing: 0.01em;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
    transition: transform 0.22s ease, border-color 0.22s ease, background 0.22s ease, box-shadow 0.22s ease;
}

.action-button:hover {
    transform: translateY(-2px);
    border-color: rgba(125,211,252,0.46);
    background: linear-gradient(135deg, rgba(34,211,238,0.32), rgba(37,99,235,0.32));
    box-shadow: 0 12px 30px rgba(14,165,233,0.18);
}

.action-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    margin-top: 18px;
}

.certificate-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(15,23,42,0.86));
}

.placeholder-shot {
    min-height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #94a3b8;
    border-style: dashed;
    margin-bottom: 12px;
}

.timeline-role {
    color: #f8fafc;
    font-size: 1rem;
    font-weight: 800;
    margin-bottom: 6px;
}

.timeline-meta {
    color: #7dd3fc;
    font-size: 0.90rem;
    font-weight: 700;
    margin-bottom: 10px;
}

.timeline-text {
    color: var(--text-soft);
    font-size: 0.95rem;
    line-height: 1.8;
}

.footer-text {
    color: #94a3b8;
    font-size: 0.9rem;
    line-height: 1.8;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    margin-bottom: 14px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    color: var(--text-main);
    padding: 12px 18px;
    min-height: 48px;
    transition: transform 0.22s ease, background 0.22s ease, border-color 0.22s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    transform: translateY(-1px);
    border-color: rgba(56,189,248,0.25);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, rgba(14,165,233,0.18), rgba(37,99,235,0.18));
    border: 1px solid rgba(56,189,248,0.35);
}

.stButton > button,
a[data-testid="stLinkButton"],
div[data-testid="stDownloadButton"] button,
div[data-testid="stPopover"] button {
    width: 100%;
    border-radius: 14px !important;
    min-height: 50px;
    border: 1px solid rgba(56,189,248,0.22) !important;
    background: linear-gradient(135deg, rgba(14,165,233,0.18), rgba(37,99,235,0.18)) !important;
    color: #f8fafc !important;
    transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease !important;
}

.stButton > button:hover,
a[data-testid="stLinkButton"]:hover,
div[data-testid="stDownloadButton"] button:hover,
div[data-testid="stPopover"] button:hover {
    transform: translateY(-2px);
    border-color: rgba(125,211,252,0.46) !important;
    box-shadow: 0 12px 30px rgba(14,165,233,0.16) !important;
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(14px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 900px) {
    .hero-title { font-size: 2.25rem; }
    .metric-grid { grid-template-columns: 1fr; }
    .status-badge {
        display: block;
        margin-left: 0;
        margin-top: 10px;
        width: fit-content;
    }
    .action-grid { grid-template-columns: 1fr; }
    .card-strong, .card-tall, .card-medium, .card-compact, .card-soft { min-height: auto; }
}
</style>
"""

WHATSAPP_FLOAT = """
<a
    href="https://wa.me/5531998417976"
    target="_blank"
    style="
        position: fixed;
        right: 22px;
        bottom: 22px;
        z-index: 99999;
        min-width: 196px;
        height: 58px;
        padding: 0 20px 0 16px;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.14);
        background: linear-gradient(135deg, #25d366, #128c7e);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        color: white;
        text-decoration: none;
        font-size: 0.96rem;
        font-weight: 700;
        letter-spacing: 0.01em;
        box-shadow: 0 18px 34px rgba(18,140,126,0.32);
        transition: transform 0.2s ease, box-shadow 0.2s ease, filter 0.2s ease;
    "
    onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 22px 40px rgba(18,140,126,0.42)';this.style.filter='brightness(1.03)'"
    onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 18px 34px rgba(18,140,126,0.32)';this.style.filter='brightness(1)'"
    aria-label="Conversar no WhatsApp"
>
    <span style="width:32px;height:32px;border-radius:999px;background:rgba(255,255,255,0.16);display:flex;align-items:center;justify-content:center;flex:0 0 auto;">
        <svg width="18" height="18" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M27.281 4.695A15.84 15.84 0 0016.04 0C7.308 0 .192 7.114.188 15.858c0 2.772.724 5.48 2.1 7.87L0 32l8.482-2.224a15.796 15.796 0 007.554 1.924h.006c8.73 0 15.846-7.114 15.85-15.858A15.75 15.75 0 0027.28 4.695zm-11.24 24.33h-.005a13.14 13.14 0 01-6.69-1.828l-.48-.285-5.033 1.32 1.344-4.905-.313-.502a13.097 13.097 0 01-2.02-6.97C2.848 8.58 8.77 2.67 16.04 2.67c3.513.001 6.815 1.37 9.296 3.854a13.07 13.07 0 013.848 9.31c-.003 7.274-5.926 13.19-13.143 13.19zm7.208-9.83c-.394-.197-2.33-1.15-2.693-1.28-.362-.132-.626-.198-.89.197-.263.394-1.02 1.28-1.25 1.543-.23.263-.46.296-.854.099-.394-.197-1.664-.613-3.17-1.955-1.17-1.042-1.96-2.33-2.19-2.724-.23-.394-.024-.607.173-.803.177-.176.394-.46.592-.69.197-.23.263-.394.394-.657.132-.263.066-.493-.033-.69-.099-.197-.89-2.144-1.22-2.935-.322-.773-.65-.668-.89-.68-.23-.011-.493-.014-.756-.014-.263 0-.69.099-1.052.493-.362.394-1.38 1.35-1.38 3.29 0 1.94 1.413 3.814 1.61 4.077.197.263 2.78 4.245 6.735 5.95.94.406 1.674.648 2.246.83.944.3 1.803.258 2.482.157.758-.113 2.33-.952 2.66-1.872.329-.92.329-1.708.23-1.872-.099-.164-.362-.263-.756-.46z" fill="white"/>
        </svg>
    </span>
    <span style="display:flex;flex-direction:column;line-height:1.05;align-items:flex-start;">
        <span style="font-size:0.74rem;opacity:0.86;font-weight:600;letter-spacing:0.04em;text-transform:uppercase;">Atendimento</span>
        <span>Chamar no WhatsApp</span>
    </span>
</a>
"""

st.html(CSS)
st.html(WHATSAPP_FLOAT)

with st.sidebar:
    st.markdown("## William Eustáquio")
    st.markdown("Desenvolvedor Python | Automação & IA")
    if Path("perfil/imagem-oculos1.jpg").exists():
        st.image("perfil/imagem-oculos1.jpg", use_container_width=True)
    st.markdown("---")
    st.markdown("### Especialidades")
    st.markdown("- 🐍 Python")
    st.markdown("- ⚡ FastAPI")
    st.markdown("- 🌿 Django")
    st.markdown("- 📊 Streamlit")
    st.markdown("- 🧱 SQLAlchemy")
    st.markdown("- 🐘 PostgreSQL")
    st.markdown("- 🧠 Servidor MCP")
    st.markdown("- 🤖 Agentes de IA")
    st.markdown("- ⚙️ Automação de processos")
    st.markdown("---")
    st.markdown("### Qualidades")
    st.markdown(
        "Resolução de problemas, criatividade, foco em resultados, proatividade e organização.")
    st.markdown("---")
    if pdf_bytes:
        st.download_button(
            "Baixar currículo em PDF",
            data=pdf_bytes,
            file_name="William_Eustaquio_Curriculo.pdf",
            mime="application/pdf"
        )


tab1, tab2, tab3, tab4 = st.tabs(
    ["Visão geral", "Projetos", "Certificados", "Contato"])

with tab1:
    top_left, top_center, top_right = st.columns([0.85, 1.45, 1.1], gap="large")

    with top_left:
        profile_markup = (
            f'''
            <div class="profile-card card-medium">
                <img class="profile-photo" src="{profile_image_uri}" alt="William Eustáquio">
                <div class="profile-name">William Eustáquio</div>
                <div class="profile-role">Desenvolvedor Python focado em automação, aplicações web e integração com IA.</div>
                <div class="profile-meta">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">FastAPI</span>
                    <span class="tech-badge">IA aplicada</span>
                </div>
            </div>
            '''
            if profile_image_uri
            else '''
            <div class="profile-card card-medium">
                <div class="profile-name">William Eustáquio</div>
                <div class="profile-role">Desenvolvedor Python focado em automação, aplicações web e integração com IA.</div>
            </div>
            '''
        )
        st.markdown(profile_markup, unsafe_allow_html=True)

    with top_center:
        st.markdown("""
        <div class="glass-card card-medium">
            <div class="section-kicker">Perfil profissional</div>
            <div class="section-title">Resumo profissional</div>
            <div class="section-text">
                Profissional com sólida experiência nas áreas de qualidade, suporte técnico e automação de processos.
                Especializado em desenvolvimento de sistemas com Python, APIs modernas e soluções com inteligência artificial.
                Atuação destacada na implantação de sistemas, automação de rotinas, desenvolvimento de chatbots e agentes de IA.
                Perfil proativo, criativo, com foco em resultados e aprendizado contínuo.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with top_right:
        st.markdown("""
        <div class="contact-card card-medium">
            <div class="section-kicker">Conexao direta</div>
            <div class="section-title">Contato</div>
            <div class="contact-line">📧 <a class="contact-anchor" href="mailto:williamllider@gmail.com">williamllider@gmail.com</a></div>
            <div class="contact-line">📱 <a class="contact-anchor" href="https://wa.me/5531998417976" target="_blank">(31) 99841-7976</a></div>
            <div class="contact-line">📍 Eldorado, Contagem - MG</div>
            <div class="contact-line">🔗 <a class="contact-anchor" href="https://linkedin.com/in/william-silva-40888223a" target="_blank">linkedin.com/in/william-silva-40888223a</a></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    left, right = st.columns([1, 1.5], gap="large")

    with left:
        st.markdown("""
        <div class="glass-card card-compact">
            <div class="section-title">Competências principais</div>
            <div class="badge-row">
                <span class="tag-badge">Automação de processos empresariais</span>
                <span class="tag-badge">APIs modernas e escaláveis</span>
                <span class="tag-badge">Programação com IA</span>
                <span class="tag-badge">Agentes de IA</span>
                <span class="tag-badge">Chatbots</span>
                <span class="tag-badge">Integrações inteligentes</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card card-tall">
            <div class="section-title">Habilidades técnicas</div>
            <div class="badge-row">
                <span class="tag-badge">Python</span>
                <span class="tag-badge">HTML</span>
                <span class="tag-badge">JavaScript</span>
                <span class="tag-badge">SQLAlchemy</span>
                <span class="tag-badge">PostgreSQL</span>
                <span class="tag-badge">MySQL</span>
                <span class="tag-badge">FastAPI</span>
                <span class="tag-badge">Django</span>
                <span class="tag-badge">Streamlit</span>
                <span class="tag-badge">SAP</span>
                <span class="tag-badge">MarketUp</span>
                <span class="tag-badge">Trello</span>
                <span class="tag-badge">Make Automation</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="glass-card card-tall">
            <div class="section-title">Experiência profissional</div>
            <div class="timeline-role">Programador de Sistema de Gestão (MarketUp)</div>
            <div class="timeline-meta">Brasil Ferro e Aço • 09/2021 — 09/2023</div>
            <div class="timeline-text">
                Implantação e configuração do sistema MarketUp, gestão dos módulos de clientes, produtos,
                estoque, financeiro, NF-e e RH, além de treinamento e suporte remoto aos usuários,
                com redução de erros operacionais e aumento de produtividade.
            </div>
            <br>
            <div class="timeline-role">Inspetor de Qualidade</div>
            <div class="timeline-meta">Vallourec – Soluções Tubulares do Brasil • 09/2017 — 09/2019</div>
            <div class="timeline-text">
                Inspeção técnica de tubos, testes de conformidade, medições com instrumentos de metrologia
                e apoio à melhoria contínua na produção.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3, gap="large")

    with b1:
        st.markdown("""
        <div class="glass-card card-compact">
            <div class="section-title">Objetivos profissionais</div>
            <div class="section-text">
                Desenvolvedor Python Pleno/Sênior, Especialista em Automação de Processos,
                Desenvolvedor de Chatbots e IA, Arquiteto de Soluções Python e Analista de Sistemas com foco em APIs e IA.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="glass-card card-compact">
            <div class="section-title">Qualidades</div>
            <div class="section-text">
                Resolução de problemas, criatividade, foco em resultados, proatividade e organização.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b3:
        st.markdown("""
        <div class="glass-card card-compact">
            <div class="section-title">Trabalho voluntário</div>
            <div class="section-text">
                Recepcionista na Comunidade Cristã Recomeçar desde 2014,
                com atuação em atendimento e recepção em cultos e eventos.
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="glass-card card-compact">
        <div class="section-title">Projetos em destaque</div>
        <div class="section-text">
            Área preparada para exibir os principais sistemas desenvolvidos,
            com espaço visual para screenshots e links diretos para as aplicações.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3, gap="large")

    with p1:
        st.markdown(project_card_html(
            "Cripto Bot",
            "Cripto Bot, um analista sênior de criptoativos especializado em protocolos DeFi, tokens, pools de liquidez e estratégias de Day Trade. Tire dúvidas, obtenha análises detalhadas e receba recomendações personalizadas para suas operações.",
            ["Streamlit", "Dashboard", "Finanças"],
            "https://cripto-bot.streamlit.app",
            "perfil/crypto-bot.png"
        ), unsafe_allow_html=True)

    with p2:
        st.markdown(project_card_html(
            "Chef Delivery",
            "Um agente de IA treinado para fazer vendas de carne online, com capacidade para sustentar centenas de atendimentos simultâneos, 24 horas por dia, 7 dias por semana, sem pausas humanas.",
            ["UX/UI", "Produto", "Layout"],
            "https://chef-delivery.streamlit.app",
            "perfil/chef-delivery.png"
        ), unsafe_allow_html=True)

    with p3:
        st.markdown(project_card_html(
            "Oráculo Analista",
            "Oráculo Analista é um especialista em análise de dados com foco em respostas objetivas, precisas e claras. Faça upload dos arquivos, envie perguntas e receba diagnósticos orientados por IA.",
            ["IA", "Automação", "Integração"],
            "https://oraculo-studant.streamlit.app/",
            "perfil/oraculo-analista-home1.png"
        ), unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="glass-card card-compact">
        <div class="section-kicker">Formação em andamento</div>
        <div class="section-title">Inteligência Artificial e Machine Learning</div>
        <div class="section-text">
            Cursando Inteligência Artificial e Machine Learning na faculdade Uniasselvi.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card card-compact">
        <div class="section-title">Certificações em destaque</div>
        <div class="section-text">
            Formação complementar alinhada a backend Python, desenvolvimento web, APIs modernas,
            bancos de dados, cloud e visualização de dados.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:
        st.markdown(certificate_card_html(
            "Programação em Python do básico ao avançado",
            "Geek University",
            "20/09/2021 a 14/03/2022",
            "64 horas"
        ), unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
        st.markdown(certificate_card_html(
            "Programação Web com Python e Django Framework: Essencial",
            "Geek University",
            "08/02/2022 a 30/04/2022",
            "35.5 horas"
        ), unsafe_allow_html=True)

    with c2:
        st.markdown(certificate_card_html(
            "FastAPI - APIs Modernas e Assíncronas com Python",
            "Geek University",
            "28/05/2022 a 17/02/2025",
            "12 horas"
        ), unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
        st.markdown(certificate_card_html(
            "FastAPI - Websites Modernos e Assíncronos com Python",
            "Geek University",
            "29/01/2024 a 17/02/2024",
            "14 horas"
        ), unsafe_allow_html=True)

    with c3:
        st.markdown(certificate_card_html(
            "SQL Alchemy: Essencial",
            "Geek University",
            "08/06/2023 a 21/02/2024",
            "15 horas"
        ), unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
        st.markdown(certificate_card_html(
            "Amazon Web Services: Essencial",
            "Geek University",
            "30/04/2025 a 22/06/2025",
            "12.5 horas"
        ), unsafe_allow_html=True)

    with c4:
        st.markdown(certificate_card_html(
            "Visualização de Dados com Python",
            "Geek University",
            "20/08/2025 a 25/08/2025",
            "6 horas"
        ), unsafe_allow_html=True)
        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
        st.markdown(certificate_card_html(
            "SQL e Power Query",
            "Empowerdata",
            "31/12/2021 e 20/10/2021",
            "3.5h + 5h"
        ), unsafe_allow_html=True)

with tab4:
    c_left, c_right = st.columns([1, 1.2], gap="large")

    with c_left:
        st.markdown("""
        <div class="contact-card card-medium">
            <div class="section-kicker">Disponivel para projetos</div>
            <div class="section-title">Contato profissional</div>
            <div class="contact-line">📧 <a class="contact-anchor" href="mailto:williamllider@gmail.com">williamllider@gmail.com</a></div>
            <div class="contact-line">📱 <a class="contact-anchor" href="https://wa.me/5531998417976" target="_blank">(31) 99841-7976</a></div>
            <div class="contact-line">📍 Eldorado, Contagem - MG</div>
            <div class="contact-line">🔗 <a class="contact-anchor" href="https://linkedin.com/in/william-silva-40888223a" target="_blank">linkedin.com/in/william-silva-40888223a</a></div>
        </div>
        """, unsafe_allow_html=True)

    with c_right:
        st.markdown("""
        <div class="glass-card card-medium">
            <div class="section-title">Áreas de atuação</div>
            <div class="section-text">
                Desenvolvimento backend com Python, APIs modernas com FastAPI,
                aplicações web com Django e Streamlit, automação de processos,
                integração com IA, chatbots e agentes inteligentes.
            </div>
            <div class="badge-row badge-row-top">
                <span class="tag-badge">Backend Python</span>
                <span class="tag-badge">FastAPI</span>
                <span class="tag-badge">Django</span>
                <span class="tag-badge">Streamlit</span>
                <span class="tag-badge">Automação</span>
                <span class="tag-badge">IA aplicada</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="action-card card-compact">
        <div class="section-title">Ações rápidas</div>
        <div class="action-grid">
            <a class="action-button" href="https://linkedin.com/in/william-silva-40888223a" target="_blank">LinkedIn</a>
            <a class="action-button" href="mailto:williamllider@gmail.com">Enviar e-mail</a>
            <a class="action-button" href="https://wa.me/5531998417976" target="_blank">WhatsApp</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)
