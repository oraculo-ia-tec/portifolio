import base64
from html import escape
from pathlib import Path

import streamlit as st

# =============================================================================
# CONFIG
# =============================================================================
st.set_page_config(
    page_title="William Eustáquio | Desenvolvedor Python & IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "Portfólio profissional de William Eustáquio — Desenvolvedor Python, "
                 "Automação e Inteligência Artificial."
    }
)

# =============================================================================
# DADOS
# =============================================================================
NOME = "William Eustáquio"
CARGO = "Desenvolvedor Python • Automação & IA"
TAGLINE = (
    "Construo sistemas, APIs e agentes de IA que automatizam processos, "
    "reduzem custos operacionais e aceleram a tomada de decisão das empresas."
    "Estou cursando Inteligência Artificial e Machine Learning na Faculdade Uniasselvi."
)

EMAIL = "williamllider@gmail.com"
TELEFONE_DISPLAY = "(31) 99841-7976"
WHATSAPP_URL = "https://wa.me/5531998417976"
LINKEDIN_URL = "https://linkedin.com/in/william-silva-40888223a"
LOCALIZACAO = "Eldorado, Contagem — MG"

METRICAS = [
    ("4+", "Anos de experiência"),
    ("10+", "Projetos entregues"),
    ("8+", "Certificações técnicas"),
    ("100%", "Foco em resultado"),
]

SERVICOS = [
    {
        "icone": "⚙️",
        "titulo": "Automação de Processos",
        "desc": "Robôs e integrações que eliminam tarefas repetitivas, "
                "reduzem erros e liberam o time para o que importa.",
        "tags": ["Python", "Make", "APIs", "RPA"],
    },
    {
        "icone": "🚀",
        "titulo": "APIs & Backend Escalável",
        "desc": "APIs modernas com FastAPI/Django, banco de dados otimizado "
                "e arquitetura pronta para crescer com seu negócio.",
        "tags": ["FastAPI", "Django", "PostgreSQL", "SQLAlchemy"],
    },
    {
        "icone": "🤖",
        "titulo": "Agentes de IA & Chatbots",
        "desc": "Atendimento, vendas e análise 24/7 com agentes inteligentes "
                "integrados ao WhatsApp, web e sistemas internos.",
        "tags": ["LLMs", "MCP", "RAG", "Streamlit"],
    },
    {
        "icone": "📊",
        "titulo": "Dashboards & Análise de Dados",
        "desc": "Visualização de dados clara e acionável para diretores "
                "tomarem decisões com base em informação, não em achismo.",
        "tags": ["Streamlit", "Pandas", "SQL", "Power Query"],
    },
]

PROJETOS = [
    {
        "titulo": "Cripto Bot",
        "desc": "Analista sênior de criptoativos com IA — DeFi, pools de liquidez "
                "e estratégias de Day Trade com recomendações personalizadas.",
        "tags": ["Streamlit", "IA", "Finanças", "Análise"],
        "url": "https://cripto-bolt.streamlit.app/",
        "imagem": "perfil/crypto-bot.png",
        "categoria": "Fintech / IA",
    },
    {
        "titulo": "Chef Delivery",
        "desc": "Agente de IA para vendas online de carnes — sustenta centenas de "
                "atendimentos simultâneos 24/7 sem pausas humanas.",
        "tags": ["Agente IA", "Vendas", "WhatsApp", "Atendimento"],
        "url": "https://chef-delivery-oraculo-ia-tec.streamlit.app/",
        "imagem": "perfil/chef-delivery.png",
        "categoria": "Vendas / Conversacional",
    },
    {
        "titulo": "Oráculo Analista",
        "desc": "Especialista em análise de dados via IA — upload de arquivos, "
                "perguntas em linguagem natural e diagnósticos objetivos.",
        "tags": ["IA", "Dados", "RAG", "Streamlit"],
        "url": "https://docs-ia.streamlit.app/",
        "imagem": "perfil/oraculo-analista-home1.png",
        "categoria": "Data / IA",
    },
    {
        "titulo": "Agente de E-mail",
        "desc": "Automação inteligente de e-mails — leitura, classificação, "
                "resposta e roteamento de mensagens com IA aplicada.",
        "tags": ["Automação", "IA", "Produtividade", "Integração"],
        "url": "#",
        "imagem": "perfil/agente-email.png",
        "categoria": "Automação / IA",
    },
]

EXPERIENCIAS = [
    {
        "cargo": "Programador de Sistema de Gestão (MarketUp)",
        "empresa": "Brasil Ferro e Aço",
        "periodo": "09/2021 — 09/2023",
        "desc": "Implantação e configuração do sistema MarketUp; gestão dos módulos "
                "de clientes, produtos, estoque, financeiro, NF-e e RH; treinamento "
                "e suporte remoto. Resultado: redução de erros operacionais e "
                "aumento de produtividade do time.",
    },
    {
        "cargo": "Inspetor de Qualidade",
        "empresa": "Vallourec — Soluções Tubulares do Brasil",
        "periodo": "09/2017 — 09/2019",
        "desc": "Inspeção técnica de tubos, testes de conformidade, medições com "
                "instrumentos de metrologia e apoio à melhoria contínua na produção.",
    },
]

CERTIFICADOS = [
    # Backend & APIs (Geek University)
    ("Programação em Python — do básico ao avançado",
     "Geek University", "20/09/2021 — 14/03/2022", "64h"),
    ("Programação Web com Python e Django Framework",
     "Geek University", "08/02/2022 — 30/04/2022", "35,5h"),
    ("FastAPI — APIs Modernas e Assíncronas com Python",
     "Geek University", "28/05/2022 — 17/02/2025", "12h"),
    ("FastAPI — Websites Modernos e Assíncronos com Python",
     "Geek University", "29/01/2024 — 17/02/2024", "14h"),
    ("SQLAlchemy: Essencial", "Geek University",
     "08/06/2023 — 21/02/2024", "15h"),
    # Cloud
    ("Amazon Web Services: Essencial", "Geek University",
     "30/04/2025 — 22/06/2025", "12,5h"),
    ("AWS Cloud — Fundamentos", "Amazon Web Services", "Concluído", "—"),
    # Visualização de Dados
    ("Visualização de Dados com Python",
     "Geek University", "20/08/2025 — 25/08/2025", "6h"),
    ("Visualização de Dados", "Udemy", "Concluído", "—"),
    # Power BI / DAX / Power Query (Empowerdata)
    ("Fundamentos de Power BI", "Empowerdata", "Concluído", "8h"),
    ("Fundamentos de DAX", "Empowerdata", "Concluído", "9h"),
    ("Dominando o DAX", "Empowerdata", "Concluído", "—"),
    ("Dominando Power Query", "Empowerdata", "Concluído", "5h"),
    ("Design de Dashboards", "Empowerdata", "Concluído", "5h"),
    ("Publicando Dashboards", "Empowerdata", "Concluído", "—"),
    # SQL & Soft Skills
    ("Noções de SQL", "Empowerdata", "Concluído", "—"),
    ("Apresentações Corporativas", "Empowerdata", "Concluído", "—"),
]

STACK = {
    "Linguagens": ["Python", "SQL", "JavaScript", "HTML/CSS"],
    "Backend & APIs": ["FastAPI", "Django", "SQLAlchemy", "REST"],
    "IA & Automação": ["Agentes de IA", "MCP Server", "Chatbots", "Make"],
    "Dados & Cloud": ["PostgreSQL", "MySQL", "AWS", "Streamlit"],
    "Ferramentas": ["Git", "SAP", "MarketUp", "Trello"],
}

# =============================================================================
# UTILS
# =============================================================================
pdf_path = Path("Curriculo_Moderno_William_Eustaquio.pdf")
pdf_bytes = pdf_path.read_bytes() if pdf_path.exists() else None


def image_to_data_uri(path: str) -> str | None:
    image_path = Path(path)
    if not image_path.exists():
        return None
    mimes = {".png": "image/png", ".jpg": "image/jpeg",
             ".jpeg": "image/jpeg", ".webp": "image/webp"}
    mime = mimes.get(image_path.suffix.lower())
    if not mime:
        return None
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def badges(items: list[str], cls: str = "tag-badge") -> str:
    return "".join(f'<span class="{cls}">{escape(i)}</span>' for i in items)


def project_card(p: dict) -> str:
    uri = image_to_data_uri(p["imagem"])
    media = (
        f'<div class="project-media"><img src="{uri}" alt="{escape(p["titulo"])}" loading="lazy"></div>'
        if uri else
        '<div class="project-media project-media-fallback">Preview indisponível</div>'
    )
    has_link = bool(p["url"]) and p["url"] != "#"
    btn_label = "Acessar projeto ↗" if has_link else "Em breve"
    btn_attrs = (
        f'href="{escape(p["url"])}" target="_blank" rel="noopener"'
        if has_link else 'href="#" aria-disabled="true"'
    )
    btn_class = "action-button" if has_link else "action-button action-button-disabled"
    return f"""
    <article class="project-card">
        {media}
        <div class="project-meta-top">
            <span class="project-category">{escape(p["categoria"])}</span>
        </div>
        <h3 class="project-title">{escape(p["titulo"])}</h3>
        <p class="project-text">{escape(p["desc"])}</p>
        <div class="badge-row">{badges(p["tags"])}</div>
        <div class="button-row">
            <a class="{btn_class}" {btn_attrs}>{btn_label}</a>
        </div>
    </article>
    """


def cert_card(title: str, provider: str, period: str, hours: str) -> str:
    return f"""
    <article class="certificate-card">
        <div class="cert-icon">🎓</div>
        <div class="cert-body">
            <div class="section-kicker">Certificado · {escape(hours)}</div>
            <div class="cert-title">{escape(title)}</div>
            <div class="cert-meta">{escape(provider)} · {escape(period)}</div>
        </div>
    </article>
    """


def service_card(s: dict) -> str:
    return f"""
    <article class="service-card">
        <div class="service-icon">{s["icone"]}</div>
        <h3 class="service-title">{escape(s["titulo"])}</h3>
        <p class="service-text">{escape(s["desc"])}</p>
        <div class="badge-row">{badges(s["tags"])}</div>
    </article>
    """


def experience_item(e: dict) -> str:
    return f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
            <div class="timeline-period">{escape(e["periodo"])}</div>
            <div class="timeline-role">{escape(e["cargo"])}</div>
            <div class="timeline-company">{escape(e["empresa"])}</div>
            <p class="timeline-text">{escape(e["desc"])}</p>
        </div>
    </div>
    """


def stack_block(titulo: str, itens: list[str]) -> str:
    return f"""
    <div class="stack-block">
        <div class="stack-title">{escape(titulo)}</div>
        <div class="badge-row">{badges(itens)}</div>
    </div>
    """


def metric_box(value: str, label: str) -> str:
    return f"""
    <div class="metric-box">
        <div class="metric-value">{escape(value)}</div>
        <div class="metric-label">{escape(label)}</div>
    </div>
    """


profile_uri = image_to_data_uri("perfil/imagem-oculos1.jpg")

# =============================================================================
# CSS
# =============================================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg-0: #05060a;
    --bg-1: #0a0d14;
    --bg-2: #0f1320;
    --surface: rgba(255,255,255,0.04);
    --surface-hover: rgba(255,255,255,0.06);
    --border: rgba(148,163,184,0.12);
    --border-strong: rgba(56,189,248,0.32);
    --text: #e5e7eb;
    --text-soft: #cbd5e1;
    --text-muted: #94a3b8;
    --accent: #22d3ee;
    --accent-2: #3b82f6;
    --accent-3: #a855f7;
    --gradient: linear-gradient(135deg, #22d3ee 0%, #3b82f6 50%, #a855f7 100%);
}

*, *::before, *::after {
    font-family: 'Inter', -apple-system, system-ui, sans-serif;
    box-sizing: border-box;
}

html, body, [class*="css"] {
    color: var(--text);
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(1200px 600px at 10% -10%, rgba(34,211,238,0.10), transparent 60%),
        radial-gradient(1000px 500px at 90% 0%, rgba(168,85,247,0.10), transparent 60%),
        radial-gradient(800px 400px at 50% 100%, rgba(59,130,246,0.08), transparent 60%),
        linear-gradient(180deg, #05060a 0%, #0a0d14 50%, #05060a 100%);
}

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }

.block-container {
    max-width: 1280px;
    padding: 1.4rem 1.6rem 3rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #06080d, #0a0d14);
    border-right: 1px solid var(--border);
}

/* ---------- HERO ---------- */
.hero {
    position: relative;
    padding: 56px 48px;
    border-radius: 32px;
    background:
        radial-gradient(600px 300px at 100% 0%, rgba(168,85,247,0.18), transparent 60%),
        radial-gradient(500px 250px at 0% 100%, rgba(34,211,238,0.16), transparent 60%),
        linear-gradient(135deg, rgba(255,255,255,0.04), rgba(15,19,32,0.85));
    border: 1px solid var(--border);
    overflow: hidden;
    margin-bottom: 28px;
}

.hero::before {
    content: "";
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(148,163,184,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(148,163,184,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 75%);
            mask-image: radial-gradient(ellipse at center, black 30%, transparent 75%);
    pointer-events: none;
}

.hero-grid {
    position: relative;
    display: grid;
    grid-template-columns: 1.7fr 1fr;
    gap: 48px;
    align-items: center;
}

.hero-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 14px;
    border-radius: 999px;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.28);
    color: #86efac;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    margin-bottom: 18px;
}

.hero-status .dot {
    width: 8px; height: 8px; border-radius: 999px;
    background: #22c55e;
    box-shadow: 0 0 0 3px rgba(34,197,94,0.25);
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.55; }
}

.hero-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.2rem, 4.6vw, 3.6rem);
    line-height: 1.05;
    font-weight: 700;
    color: #f8fafc;
    margin: 0 0 8px;
    letter-spacing: -0.02em;
}

.hero-role {
    font-size: 1.02rem;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 18px;
    letter-spacing: 0.02em;
}

.hero-tagline {
    font-size: 1.08rem;
    line-height: 1.75;
    color: var(--text-soft);
    max-width: 60ch;
    margin: 0 0 28px;
}

.hero-gradient {
    background: var(--gradient);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 28px;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 14px 22px;
    border-radius: 14px;
    font-weight: 700;
    font-size: 0.95rem;
    text-decoration: none;
    border: 1px solid transparent;
    cursor: pointer;
    transition: all 0.22s ease;
    white-space: nowrap;
}

.btn-primary {
    background: var(--gradient);
    color: white;
    box-shadow: 0 12px 28px rgba(59,130,246,0.32);
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 36px rgba(59,130,246,0.42);
}

.btn-ghost {
    background: rgba(255,255,255,0.04);
    border-color: var(--border);
    color: var(--text);
}
.btn-ghost:hover {
    background: rgba(255,255,255,0.08);
    border-color: var(--border-strong);
    transform: translateY(-2px);
}

.hero-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

.metric-box {
    padding: 16px;
    border-radius: 16px;
    background: rgba(2,6,23,0.42);
    border: 1px solid var(--border);
    text-align: left;
    transition: border-color 0.2s ease, transform 0.2s ease;
}
.metric-box:hover {
    border-color: var(--border-strong);
    transform: translateY(-2px);
}
.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    background: var(--gradient);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
    margin-bottom: 6px;
}
.metric-label {
    color: var(--text-muted);
    font-size: 0.8rem;
    font-weight: 500;
}

/* ---------- HERO PHOTO ---------- */
.hero-photo-wrap {
    position: relative;
    display: flex;
    justify-content: center;
}
.hero-photo-frame {
    position: relative;
    width: min(100%, 320px);
    aspect-ratio: 4/5;
    border-radius: 28px;
    padding: 4px;
    background: var(--gradient);
    box-shadow: 0 30px 80px rgba(34,211,238,0.22);
}
.hero-photo {
    width: 100%; height: 100%;
    object-fit: cover;
    border-radius: 24px;
    display: block;
}
.hero-photo-tag {
    position: absolute;
    bottom: -14px; left: 50%;
    transform: translateX(-50%);
    padding: 8px 16px;
    border-radius: 999px;
    background: #0a0d14;
    border: 1px solid var(--border-strong);
    color: var(--text);
    font-size: 0.82rem;
    font-weight: 700;
    white-space: nowrap;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

/* ---------- SEÇÕES ---------- */
.section-header {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin: 56px 0 24px;
}
.section-eyebrow {
    color: var(--accent);
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.18em;
    text-transform: uppercase;
}
.section-headline {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.6rem, 2.6vw, 2.1rem);
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: -0.01em;
    margin: 0;
}
.section-sub {
    color: var(--text-muted);
    font-size: 1rem;
    max-width: 70ch;
}

/* ---------- CARDS BASE ---------- */
.glass-card, .service-card, .project-card, .certificate-card, .contact-card {
    position: relative;
    background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(10,13,20,0.72));
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 24px;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}
.glass-card:hover, .service-card:hover, .project-card:hover, .certificate-card:hover, .contact-card:hover {
    transform: translateY(-4px);
    border-color: var(--border-strong);
    box-shadow: 0 22px 50px rgba(0,0,0,0.32);
}

/* ---------- SERVIÇOS ---------- */
.service-card {
    display: flex;
    flex-direction: column;
    gap: 14px;
    height: 100%;
    min-height: 280px;
}
.service-icon {
    width: 52px; height: 52px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    background: linear-gradient(135deg, rgba(34,211,238,0.18), rgba(59,130,246,0.18));
    border: 1px solid var(--border-strong);
}
.service-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #f8fafc;
    margin: 0;
}
.service-text {
    color: var(--text-soft);
    font-size: 0.94rem;
    line-height: 1.7;
    margin: 0;
    flex: 1;
}

/* ---------- PROJETOS ---------- */
.project-card {
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow: hidden;
    padding: 0;
}
.project-media {
    width: 100%;
    aspect-ratio: 16/10;
    overflow: hidden;
    border-bottom: 1px solid var(--border);
    background: linear-gradient(135deg, rgba(34,211,238,0.10), rgba(59,130,246,0.14));
}
.project-media img {
    width: 100%; height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.5s ease;
}
.project-card:hover .project-media img { transform: scale(1.04); }
.project-media-fallback {
    display: flex; align-items: center; justify-content: center;
    color: var(--text-muted);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    aspect-ratio: 16/10;
}
.project-meta-top {
    padding: 18px 22px 0;
}
.project-category {
    display: inline-block;
    padding: 5px 11px;
    border-radius: 999px;
    background: rgba(168,85,247,0.10);
    border: 1px solid rgba(168,85,247,0.28);
    color: #d8b4fe;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.project-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.22rem;
    font-weight: 700;
    color: #f8fafc;
    margin: 12px 22px 8px;
}
.project-text {
    color: var(--text-soft);
    font-size: 0.94rem;
    line-height: 1.7;
    margin: 0 22px 16px;
    flex: 1;
}
.project-card .badge-row { padding: 0 22px; }
.button-row {
    margin-top: auto;
    padding: 18px 22px 22px;
}

/* ---------- BADGES ---------- */
.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.tag-badge, .tech-badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.01em;
}
.tag-badge {
    background: rgba(56,189,248,0.08);
    border: 1px solid rgba(56,189,248,0.20);
    color: #7dd3fc;
}
.tech-badge {
    background: var(--gradient);
    color: white;
    border: none;
}

/* ---------- BOTÃO PROJETO ---------- */
.action-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 48px;
    padding: 12px 18px;
    border-radius: 12px;
    border: 1px solid var(--border-strong);
    background: linear-gradient(135deg, rgba(34,211,238,0.14), rgba(59,130,246,0.14));
    color: #f8fafc;
    text-decoration: none;
    font-weight: 700;
    font-size: 0.92rem;
    transition: all 0.22s ease;
}
.action-button:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, rgba(34,211,238,0.28), rgba(59,130,246,0.28));
    box-shadow: 0 12px 28px rgba(34,211,238,0.18);
}
.action-button-disabled {
    opacity: 0.55;
    pointer-events: none;
    background: rgba(148,163,184,0.08);
    border-color: var(--border);
}

/* ---------- TIMELINE ---------- */
.timeline {
    position: relative;
    padding-left: 28px;
}
.timeline::before {
    content: "";
    position: absolute;
    left: 8px; top: 6px; bottom: 6px;
    width: 2px;
    background: linear-gradient(180deg, var(--accent), transparent);
    opacity: 0.4;
}
.timeline-item {
    position: relative;
    padding-bottom: 28px;
}
.timeline-item:last-child { padding-bottom: 0; }
.timeline-dot {
    position: absolute;
    left: -28px; top: 6px;
    width: 18px; height: 18px;
    border-radius: 999px;
    background: var(--gradient);
    border: 3px solid var(--bg-1);
    box-shadow: 0 0 0 2px var(--border-strong);
}
.timeline-period {
    color: var(--accent);
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.timeline-role {
    font-family: 'Space Grotesk', sans-serif;
    color: #f8fafc;
    font-size: 1.08rem;
    font-weight: 700;
    margin-bottom: 2px;
}
.timeline-company {
    color: var(--text-muted);
    font-size: 0.92rem;
    font-weight: 600;
    margin-bottom: 10px;
}
.timeline-text {
    color: var(--text-soft);
    line-height: 1.75;
    font-size: 0.94rem;
    margin: 0;
}

/* ---------- STACK ---------- */
.stack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 14px;
}
.stack-block {
    padding: 18px;
    background: rgba(2,6,23,0.42);
    border: 1px solid var(--border);
    border-radius: 16px;
    transition: border-color 0.2s ease;
}
.stack-block:hover { border-color: var(--border-strong); }
.stack-title {
    color: #f8fafc;
    font-weight: 700;
    font-size: 0.92rem;
    margin-bottom: 12px;
    letter-spacing: 0.02em;
}

/* ---------- CERTIFICADOS ---------- */
.certificate-card {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 20px;
}
.cert-icon {
    width: 44px; height: 44px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, rgba(34,211,238,0.16), rgba(59,130,246,0.16));
    border: 1px solid var(--border-strong);
    font-size: 1.2rem;
    flex: 0 0 auto;
}
.cert-body { min-width: 0; }
.section-kicker {
    color: var(--accent);
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.cert-title {
    color: #f8fafc;
    font-weight: 700;
    font-size: 0.98rem;
    line-height: 1.4;
    margin-bottom: 6px;
}
.cert-meta {
    color: var(--text-muted);
    font-size: 0.84rem;
}

/* ---------- CTA / CONTATO ---------- */
.cta-banner {
    margin-top: 56px;
    padding: 44px 40px;
    border-radius: 28px;
    background:
        radial-gradient(600px 300px at 0% 0%, rgba(34,211,238,0.18), transparent 60%),
        radial-gradient(600px 300px at 100% 100%, rgba(168,85,247,0.18), transparent 60%),
        linear-gradient(135deg, rgba(255,255,255,0.04), rgba(15,19,32,0.85));
    border: 1px solid var(--border-strong);
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 32px;
    align-items: center;
}
.cta-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.6rem, 2.4vw, 2rem);
    font-weight: 700;
    color: #f8fafc;
    margin: 0 0 10px;
    line-height: 1.2;
}
.cta-text {
    color: var(--text-soft);
    font-size: 1rem;
    line-height: 1.7;
    margin: 0;
}
.cta-actions {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.contact-card {
    display: flex; flex-direction: column; gap: 6px;
}
.contact-line {
    display: flex; align-items: center; gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    font-size: 0.95rem;
}
.contact-line:last-child { border-bottom: none; }
.contact-icon {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    background: rgba(56,189,248,0.10);
    border: 1px solid rgba(56,189,248,0.22);
    flex: 0 0 auto;
    font-size: 1rem;
}
.contact-anchor {
    color: var(--text);
    text-decoration: none;
    word-break: break-word;
}
.contact-anchor:hover { color: var(--accent); }

/* ---------- FOOTER ---------- */
.site-footer {
    margin-top: 48px;
    padding: 24px 0 8px;
    border-top: 1px solid var(--border);
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    color: var(--text-muted);
    font-size: 0.86rem;
}
.site-footer a { color: var(--text-muted); text-decoration: none; margin-left: 16px; }
.site-footer a:hover { color: var(--accent); }

/* ---------- TABS ---------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    margin-bottom: 8px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    border-radius: 0;
    color: var(--text-muted);
    padding: 14px 18px;
    font-weight: 600;
    transition: all 0.2s ease;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--text); }
.stTabs [aria-selected="true"] {
    background: transparent;
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent);
}

/* Streamlit native buttons */
.stButton > button,
a[data-testid="stLinkButton"],
div[data-testid="stDownloadButton"] button {
    width: 100%;
    border-radius: 12px !important;
    min-height: 48px;
    border: 1px solid var(--border-strong) !important;
    background: linear-gradient(135deg, rgba(34,211,238,0.14), rgba(59,130,246,0.14)) !important;
    color: #f8fafc !important;
    font-weight: 700 !important;
    transition: all 0.22s ease !important;
}
.stButton > button:hover,
a[data-testid="stLinkButton"]:hover,
div[data-testid="stDownloadButton"] button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(34,211,238,0.18) !important;
}

/* ---------- RESPONSIVO ---------- */
@media (max-width: 980px) {
    .hero { padding: 36px 24px; }
    .hero-grid { grid-template-columns: 1fr; gap: 32px; }
    .hero-stats { grid-template-columns: repeat(2, 1fr); }
    .cta-banner { grid-template-columns: 1fr; padding: 32px 24px; }
    .hero-photo-frame { max-width: 260px; margin: 0 auto; }
}

@media (max-width: 640px) {
    .block-container { padding: 1rem 0.9rem 2rem; }
    .hero-stats { grid-template-columns: 1fr 1fr; }
    .section-header { margin: 40px 0 20px; }
}
</style>
"""

# =============================================================================
# WHATSAPP FLUTUANTE
# =============================================================================
WHATSAPP_FLOAT = """
<a href="https://wa.me/5531998417976" target="_blank" rel="noopener"
   aria-label="Conversar no WhatsApp"
   style="position:fixed;right:22px;bottom:22px;z-index:9999;
          display:flex;align-items:center;gap:10px;padding:12px 18px 12px 14px;
          border-radius:999px;background:linear-gradient(135deg,#25d366,#128c7e);
          color:white;text-decoration:none;font-weight:700;font-size:0.92rem;
          box-shadow:0 14px 32px rgba(18,140,126,0.42);
          border:1px solid rgba(255,255,255,0.18);
          transition:transform 0.22s ease, box-shadow 0.22s ease;"
   onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 18px 40px rgba(18,140,126,0.55)'"
   onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 14px 32px rgba(18,140,126,0.42)'">
   <span style="width:30px;height:30px;border-radius:999px;background:rgba(255,255,255,0.18);
                display:flex;align-items:center;justify-content:center;flex:0 0 auto;">
      <svg width="16" height="16" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
         <path d="M27.281 4.695A15.84 15.84 0 0016.04 0C7.308 0 .192 7.114.188 15.858c0 2.772.724 5.48 2.1 7.87L0 32l8.482-2.224a15.796 15.796 0 007.554 1.924h.006c8.73 0 15.846-7.114 15.85-15.858A15.75 15.75 0 0027.28 4.695zm-11.24 24.33h-.005a13.14 13.14 0 01-6.69-1.828l-.48-.285-5.033 1.32 1.344-4.905-.313-.502a13.097 13.097 0 01-2.02-6.97C2.848 8.58 8.77 2.67 16.04 2.67c3.513.001 6.815 1.37 9.296 3.854a13.07 13.07 0 013.848 9.31c-.003 7.274-5.926 13.19-13.143 13.19zm7.208-9.83c-.394-.197-2.33-1.15-2.693-1.28-.362-.132-.626-.198-.89.197-.263.394-1.02 1.28-1.25 1.543-.23.263-.46.296-.854.099-.394-.197-1.664-.613-3.17-1.955-1.17-1.042-1.96-2.33-2.19-2.724-.23-.394-.024-.607.173-.803.177-.176.394-.46.592-.69.197-.23.263-.394.394-.657.132-.263.066-.493-.033-.69-.099-.197-.89-2.144-1.22-2.935-.322-.773-.65-.668-.89-.68-.23-.011-.493-.014-.756-.014-.263 0-.69.099-1.052.493-.362.394-1.38 1.35-1.38 3.29 0 1.94 1.413 3.814 1.61 4.077.197.263 2.78 4.245 6.735 5.95.94.406 1.674.648 2.246.83.944.3 1.803.258 2.482.157.758-.113 2.33-.952 2.66-1.872.329-.92.329-1.708.23-1.872-.099-.164-.362-.263-.756-.46z" fill="white"/>
      </svg>
   </span>
   <span>WhatsApp</span>
</a>
"""

st.html(CSS)
st.html(WHATSAPP_FLOAT)

# =============================================================================
# SIDEBAR — apenas identidade + download do currículo
# (Contato, links e métricas já aparecem no Hero/CTA/aba Contato)
# =============================================================================
with st.sidebar:
    st.markdown(f"### {NOME}")
    st.caption(CARGO)
    st.markdown("---")
    st.markdown("**Navegação**")
    st.caption(
        "Use as abas no topo para explorar Serviços, Projetos, Experiência e Certificações.")
    st.markdown("---")
    if pdf_bytes:
        st.download_button(
            "⬇️ Baixar Currículo (PDF)",
            data=pdf_bytes,
            file_name="William_Eustaquio_Curriculo.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

# =============================================================================
# HERO
# =============================================================================
photo_block = (
    f"""
    <div class="hero-photo-wrap">
        <div class="hero-photo-frame">
            <img class="hero-photo" src="{profile_uri}" alt="{escape(NOME)}">
        </div>
        <div class="hero-photo-tag">✨ Disponível para projetos</div>
    </div>
    """ if profile_uri else ""
)

metric_html = "".join(metric_box(v, l) for v, l in METRICAS)

primeiro_nome = escape(NOME.split()[0])
ultimo_nome = escape(" ".join(NOME.split()[1:]))

hero_html = f"""
<section class="hero">
  <div class="hero-grid">
    <div>
      <div class="hero-status"><span class="dot"></span> Aberto a novas oportunidades</div>
      <h1 class="hero-name">Olá, sou {primeiro_nome} <span class="hero-gradient">{ultimo_nome}</span></h1>
      <div class="hero-role">{escape(CARGO)}</div>
      <p class="hero-tagline">{escape(TAGLINE)}</p>
      <div class="hero-cta-row">
        <a class="btn btn-primary" href="{escape(WHATSAPP_URL)}" target="_blank" rel="noopener">💬 Iniciar conversa</a>
        <a class="btn btn-ghost" href="mailto:{escape(EMAIL)}">📧 Enviar e-mail</a>
        <a class="btn btn-ghost" href="{escape(LINKEDIN_URL)}" target="_blank" rel="noopener">💼 LinkedIn</a>
      </div>
      <div class="hero-stats">{metric_html}</div>
    </div>
    {photo_block}
  </div>
</section>
"""
st.html(hero_html)

# =============================================================================
# TABS
# =============================================================================
tab_visao, tab_servicos, tab_projetos, tab_experiencia, tab_certs, tab_contato = st.tabs(
    ["🏠 Visão geral", "💼 Serviços", "🚀 Projetos",
     "📈 Experiência", "🎓 Certificações", "✉️ Contato"]
)

# ----- VISÃO GERAL -----
with tab_visao:
    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">Sobre mim</span>
            <h2 class="section-headline">Tecnologia que <span class="hero-gradient">gera resultado</span></h2>
            <p class="section-sub">
                Desenvolvedor Python com experiência sólida em automação, suporte técnico e qualidade.
                Construo APIs modernas, agentes de IA e dashboards para empresas que querem operar
                com mais eficiência e menos retrabalho.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_a, col_b = st.columns([1.4, 1], gap="large")

    with col_a:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-kicker">Resumo profissional</div>
                <p class="timeline-text" style="margin-bottom:14px">
                    Profissional com sólida experiência nas áreas de qualidade, suporte técnico
                    e automação de processos. Especializado em desenvolvimento de sistemas com
                    Python, APIs modernas e soluções com inteligência artificial.
                </p>
                <p class="timeline-text" style="margin:0">
                    Atuação destacada em implantação de sistemas, automação de rotinas,
                    desenvolvimento de chatbots e agentes de IA. Perfil proativo, criativo,
                    com foco em resultados e aprendizado contínuo.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-kicker">Diferenciais</div>
                <div style="display:flex;flex-direction:column;gap:10px;margin-top:6px">
                    <div style="display:flex;gap:10px;align-items:flex-start">
                        <span style="color:#22d3ee;font-size:1.1rem">▸</span>
                        <div><strong>Foco em ROI:</strong> entregas que impactam o financeiro do cliente.</div>
                    </div>
                    <div style="display:flex;gap:10px;align-items:flex-start">
                        <span style="color:#22d3ee;font-size:1.1rem">▸</span>
                        <div><strong>Comunicação clara:</strong> sem jargão técnico desnecessário.</div>
                    </div>
                    <div style="display:flex;gap:10px;align-items:flex-start">
                        <span style="color:#22d3ee;font-size:1.1rem">▸</span>
                        <div><strong>Visão de produto:</strong> resolvo o problema, não só o código.</div>
                    </div>
                    <div style="display:flex;gap:10px;align-items:flex-start">
                        <span style="color:#22d3ee;font-size:1.1rem">▸</span>
                        <div><strong>Aprendizado contínuo:</strong> stack sempre atualizada com IA.</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">Stack técnica</span>
            <h2 class="section-headline">Tecnologias que domino</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    stack_html = '<div class="stack-grid">' + "".join(
        stack_block(k, v) for k, v in STACK.items()
    ) + "</div>"
    st.html(stack_html)

# ----- SERVIÇOS -----
with tab_servicos:
    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">O que entrego</span>
            <h2 class="section-headline">Serviços para <span class="hero-gradient">empresas</span></h2>
            <p class="section-sub">
                Soluções sob medida que economizam tempo, reduzem custos e geram dados
                acionáveis para o seu time tomar decisões melhores.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(2, gap="large")
    for i, s in enumerate(SERVICOS):
        with cols[i % 2]:
            st.html(service_card(s))

# ----- PROJETOS -----
with tab_projetos:
    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">Portfólio</span>
            <h2 class="section-headline">Projetos em <span class="hero-gradient">destaque</span></h2>
            <p class="section-sub">
                Aplicações reais publicadas em produção — de bots financeiros a agentes
                de vendas e plataformas de análise de dados com IA.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(2, gap="large")
    for i, p in enumerate(PROJETOS):
        with cols[i % 2]:
            st.html(project_card(p))

# ----- EXPERIÊNCIA -----
with tab_experiencia:
    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">Trajetória</span>
            <h2 class="section-headline">Experiência profissional</h2>
            <p class="section-sub">
                Mais de 6 anos atuando entre qualidade, suporte técnico e desenvolvimento,
                sempre conectando processo, pessoas e tecnologia.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    timeline_html = '<div class="glass-card"><div class="timeline">' + "".join(
        experience_item(e) for e in EXPERIENCIAS
    ) + "</div></div>"
    st.html(timeline_html)

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-kicker">Formação acadêmica</div>
                <div class="cert-title" style="margin-top:6px">Inteligência Artificial e Machine Learning</div>
                <div class="cert-meta">Uniasselvi · Em andamento</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-kicker">Trabalho voluntário</div>
                <div class="cert-title" style="margin-top:6px">Recepcionista — Comunidade Cristã Recomeçar</div>
                <div class="cert-meta">Desde 2014 · Atendimento e recepção em cultos e eventos</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ----- CERTIFICAÇÕES -----
with tab_certs:
    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">Educação contínua</span>
            <h2 class="section-headline">Certificações</h2>
            <p class="section-sub">
                Formação complementar focada em backend Python, APIs modernas, banco de dados,
                cloud, visualização de dados e Inteligência Artificial.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(2, gap="medium")
    for i, c in enumerate(CERTIFICADOS):
        with cols[i % 2]:
            st.html(cert_card(*c))

# ----- CONTATO -----
with tab_contato:
    st.markdown(
        """
        <div class="section-header">
            <span class="section-eyebrow">Vamos conversar</span>
            <h2 class="section-headline">Pronto para o próximo <span class="hero-gradient">projeto</span>?</h2>
            <p class="section-sub">
                Conte sobre o seu desafio. Respondo em até 24h em dias úteis.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_l, col_r = st.columns([1, 1.1], gap="large")
    with col_l:
        st.markdown(
            f"""
            <div class="contact-card">
                <div class="section-kicker">Canais diretos</div>
                <div class="contact-line">
                    <div class="contact-icon">📧</div>
                    <a class="contact-anchor" href="mailto:{escape(EMAIL)}">{escape(EMAIL)}</a>
                </div>
                <div class="contact-line">
                    <div class="contact-icon">📱</div>
                    <a class="contact-anchor" href="{escape(WHATSAPP_URL)}" target="_blank" rel="noopener">{escape(TELEFONE_DISPLAY)}</a>
                </div>
                <div class="contact-line">
                    <div class="contact-icon">💼</div>
                    <a class="contact-anchor" href="{escape(LINKEDIN_URL)}" target="_blank" rel="noopener">LinkedIn — William Silva</a>
                </div>
                <div class="contact-line">
                    <div class="contact-icon">📍</div>
                    <span>{escape(LOCALIZACAO)}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_r:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-kicker">Áreas de atuação</div>
                <p class="timeline-text" style="margin:6px 0 14px">
                    Desenvolvimento backend com Python, APIs modernas com FastAPI,
                    aplicações web com Django e Streamlit, automação de processos,
                    integração com IA, chatbots e agentes inteligentes.
                </p>
                <div class="badge-row">
                    <span class="tag-badge">Backend Python</span>
                    <span class="tag-badge">FastAPI</span>
                    <span class="tag-badge">Django</span>
                    <span class="tag-badge">Streamlit</span>
                    <span class="tag-badge">Automação</span>
                    <span class="tag-badge">IA aplicada</span>
                    <span class="tag-badge">Chatbots</span>
                    <span class="tag-badge">Dashboards</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =============================================================================
# CTA + FOOTER
# =============================================================================
st.html(
    f"""
    <section class="cta-banner">
        <div>
            <h3 class="cta-title">Vamos transformar seu processo em <span class="hero-gradient">software inteligente</span>?</h3>
            <p class="cta-text">
                Diga qual o desafio do seu time e em poucos dias entrego uma proposta
                clara com escopo, prazo e ROI esperado. Sem enrolação, foco no resultado.
            </p>
        </div>
        <div class="cta-actions">
            <a class="btn btn-primary" href="{escape(WHATSAPP_URL)}" target="_blank" rel="noopener">💬 Falar no WhatsApp</a>
            <a class="btn btn-ghost" href="mailto:{escape(EMAIL)}">📧 Enviar briefing por e-mail</a>
        </div>
    </section>

    <footer class="site-footer">
        <div>© 2026 {escape(NOME)} — Todos os direitos reservados.</div>
        <div>
            <a href="{escape(LINKEDIN_URL)}" target="_blank" rel="noopener">LinkedIn</a>
            <a href="mailto:{escape(EMAIL)}">E-mail</a>
            <a href="{escape(WHATSAPP_URL)}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
    </footer>
    """
)
