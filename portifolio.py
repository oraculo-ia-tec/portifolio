import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="William Eustáquio | Desenvolvedor de IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

pdf_path = Path("Curriculo_Moderno_William_Eustaquio.pdf")
pdf_bytes = pdf_path.read_bytes() if pdf_path.exists() else None

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* { font-family: 'Inter', sans-serif; }

html, body, [class*="css"] {
    color: #e5e7eb;
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

.hero-card, .glass-card, .project-card, .contact-card, .placeholder-shot {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 28px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.24);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
}

.hero-card { padding: 36px; }
.glass-card, .project-card, .contact-card, .placeholder-shot { padding: 22px; }

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

.section-title {
    font-size: 1.12rem;
    color: #f8fafc;
    font-weight: 800;
    margin-bottom: 14px;
}

.section-text {
    color: #cbd5e1;
    line-height: 1.85;
    font-size: 0.96rem;
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
    align-items: center;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: #e5e7eb;
    font-size: 0.95rem;
}

.contact-line:last-child {
    border-bottom: none;
}

.project-card {
    min-height: 265px;
    transition: transform 0.28s ease, border-color 0.28s ease, box-shadow 0.28s ease;
}

.project-card:hover, .glass-card:hover, .contact-card:hover {
    transform: translateY(-5px);
    border-color: rgba(56,189,248,0.28);
    box-shadow: 0 24px 60px rgba(0,0,0,0.28);
}

.project-title {
    font-size: 1.08rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 8px;
}

.project-text {
    color: #cbd5e1;
    line-height: 1.78;
    font-size: 0.95rem;
    margin-bottom: 16px;
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
    color: #cbd5e1;
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
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    color: #e5e7eb;
    padding: 10px 18px;
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
        width: 58px;
        height: 58px;
        border-radius: 999px;
        background: linear-gradient(135deg, #22c55e, #16a34a);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.5rem;
        text-decoration: none;
        box-shadow: 0 18px 32px rgba(34,197,94,0.32);
    "
>
    💬
</a>
"""

st.html(CSS)
st.html(WHATSAPP_FLOAT)

with st.sidebar:
    st.markdown("## William Eustáquio")
    st.markdown("Desenvolvedor Python | Automação & IA")
    st.markdown("---")
    st.markdown("### Especialidades")
    st.markdown("- Python")
    st.markdown("- FastAPI")
    st.markdown("- Django")
    st.markdown("- Streamlit")
    st.markdown("- SQLAlchemy")
    st.markdown("- PostgreSQL")
    st.markdown("- Agentes de IA")
    st.markdown("- Automação de processos")
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


st.markdown("""
<div style='display: flex; flex-direction: column; align-items: center; margin-top: 24px; margin-bottom: 24px;'>
""", unsafe_allow_html=True)
st.image("perfil/imagem-oculos1.jpg", width=200)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(
    ["Visão geral", "Projetos", "Certificados", "Contato"])

with tab1:
    left, right = st.columns([1, 1.5], gap="large")

    with left:
        st.markdown("""
        <div class="contact-card">
            <div class="section-title">Contato</div>
            <div class="contact-line">📧 williamllider@gmail.com</div>
            <div class="contact-line">📱 (31) 99841-7976</div>
            <div class="contact-line">📍 Eldorado, Contagem - MG</div>
            <div class="contact-line">🔗 linkedin.com/in/william-silva-40888223a</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Competências principais</div>
            <span class="tag-badge">Automação de processos empresariais</span>
            <span class="tag-badge">APIs modernas e escaláveis</span>
            <span class="tag-badge">Programação com IA</span>
            <span class="tag-badge">Agentes de IA</span>
            <span class="tag-badge">Chatbots</span>
            <span class="tag-badge">Integrações inteligentes</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Habilidades técnicas</div>
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
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Resumo profissional</div>
            <div class="section-text">
                Profissional com sólida experiência nas áreas de qualidade, suporte técnico e automação de processos.
                Especializado em desenvolvimento de sistemas com Python, APIs modernas e soluções com inteligência artificial.
                Atuação destacada na implantação de sistemas, automação de rotinas, desenvolvimento de chatbots e agentes de IA.
                Perfil proativo, criativo, com foco em resultados e aprendizado contínuo.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
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
        <div class="glass-card">
            <div class="section-title">Objetivos profissionais</div>
            <div class="section-text">
                Desenvolvedor Python Pleno/Sênior, Especialista em Automação de Processos,
                Desenvolvedor de Chatbots e IA, Arquiteto de Soluções Python e Analista de Sistemas com foco em APIs e IA.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Qualidades</div>
            <div class="section-text">
                Resolução de problemas, criatividade, foco em resultados, proatividade e organização.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b3:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Trabalho voluntário</div>
            <div class="section-text">
                Recepcionista na Comunidade Cristã Recomeçar desde 2014,
                com atuação em atendimento e recepção em cultos e eventos.
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="glass-card">
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
        st.image("perfil/crypto-bot.png", caption="", width=200)
        st.markdown("""
        <div class="project-card">
            <div class="project-title">Cripto Bot</div>
            <div class="project-text">
                Aplicação com proposta de dashboard moderno e navegação interativa,
                reforçando apresentação visual e experiência de uso em Streamlit.
            </div>
            <span class="tag-badge">Streamlit</span>
            <span class="tag-badge">Dashboard</span>
            <span class="tag-badge">Finanças</span>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir projeto", "https://cripto-bot.streamlit.app")

    with p2:
        st.image("perfil/chef-delivery.png",
                 caption="", width=200)
        st.markdown("""
        <div class="project-card">
            <div class="project-title">Chef Delivery</div>
            <div class="project-text">
                Sistema com foco em layout funcional, organização visual e apresentação de produto,
                ideal para destacar domínio de interface com Streamlit.
            </div>
            <span class="tag-badge">UX/UI</span>
            <span class="tag-badge">Produto</span>
            <span class="tag-badge">Layout</span>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir projeto", "https://chef-delivery.streamlit.app")

    with p3:
        st.image("perfil/agente-email.png",
                 caption="", width=200)
        st.markdown("""
        <div class="project-card">
            <div class="project-title">Agente Gmail</div>
            <div class="project-text">
                Projeto orientado à automação com inteligência artificial,
                conectando produtividade, integração e uso prático de agentes.
            </div>
            <span class="tag-badge">IA</span>
            <span class="tag-badge">Automação</span>
            <span class="tag-badge">Integração</span>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Abrir repositório",
                       "https://github.com/oraculosia/agente-gmail")

with tab3:
    st.markdown("""
    <div class="glass-card">
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
        with st.popover("Python 64h"):
            st.write(
                "Programação em Python do básico ao avançado — Geek University — 20/09/2021 a 14/03/2022 — 64 horas")
        with st.popover("Django 35.5h"):
            st.write(
                "Programação Web com Python e Django Framework: Essencial — Geek University — 08/02/2022 a 30/04/2022 — 35.5 horas")

    with c2:
        with st.popover("FastAPI APIs 12h"):
            st.write(
                "FastAPI - APIs Modernas e Assíncronas com Python — Geek University — 28/05/2022 a 17/02/2025 — 12 horas")
        with st.popover("FastAPI Web 14h"):
            st.write(
                "FastAPI - Websites Modernos e Assíncronos com Python — Geek University — 29/01/2024 a 17/02/2024 — 14 horas")

    with c3:
        with st.popover("SQLAlchemy 15h"):
            st.write(
                "SQL Alchemy: Essencial — Geek University — 08/06/2023 a 21/02/2024 — 15 horas")
        with st.popover("AWS 12.5h"):
            st.write(
                "Amazon Web Services: Essencial — Geek University — 30/04/2025 a 22/06/2025 — 12.5 horas")

    with c4:
        with st.popover("Visualização 6h"):
            st.write(
                "Visualização de Dados com Python — Geek University — 20/08/2025 a 25/08/2025 — 6 horas")
        with st.popover("SQL 3.5h + Power Query 5h"):
            st.write(
                "Noções da Linguagem SQL — Empowerdata — 31/12/2021 — 3.5h | Dominando Power Query — Empowerdata — 20/10/2021 — 5h")

with tab4:
    c_left, c_right = st.columns([1, 1.2], gap="large")

    with c_left:
        st.markdown("""
        <div class="contact-card">
            <div class="section-title">Contato profissional</div>
            <div class="contact-line">📧 williamllider@gmail.com</div>
            <div class="contact-line">📱 (31) 99841-7976</div>
            <div class="contact-line">📍 Eldorado, Contagem - MG</div>
            <div class="contact-line">🔗 linkedin.com/in/william-silva-40888223a</div>
        </div>
        """, unsafe_allow_html=True)

    with c_right:
        st.markdown("""
        <div class="glass-card">
            <div class="section-title">Áreas de atuação</div>
            <div class="section-text">
                Desenvolvimento backend com Python, APIs modernas com FastAPI,
                aplicações web com Django e Streamlit, automação de processos,
                integração com IA, chatbots e agentes inteligentes.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        a1, a2, a3 = st.columns(3, gap="medium")
        with a1:
            st.link_button(
                "LinkedIn", "https://linkedin.com/in/william-silva-40888223a")
        with a2:
            st.link_button("Enviar e-mail", "mailto:williamllider@gmail.com")
        with a3:
            st.link_button("WhatsApp", "https://wa.me/5531998417976")

st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)
