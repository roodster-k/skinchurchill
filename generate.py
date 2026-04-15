import os

base_dir = "/Users/kei/Desktop/Antigravity x Churchill SkinCheck"

def create_html(lang, title, desc, url_path, content, og_title):
    lang_prefix = f"/{lang}/"
    
    header_nav = f"""
            <nav class="nav-links">
                <a href="{lang_prefix}services.html">Services</a>
                <a href="{lang_prefix}equipe.html">Équipe</a>
                <a href="{lang_prefix}technologie.html">Technologie</a>
                <a href="{lang_prefix}tarifs.html">Tarifs</a>
                <a href="{lang_prefix}faq.html">FAQ</a>
                <a href="{lang_prefix}contact.html">Contact</a>
            </nav>
""" if lang == 'fr' else f"""
            <nav class="nav-links">
                <a href="{lang_prefix}services.html">Services</a>
                <a href="{lang_prefix}team.html">Team</a>
                <a href="{lang_prefix}technology.html">Technology</a>
                <a href="{lang_prefix}pricing.html">Pricing</a>
                <a href="{lang_prefix}faq.html">FAQ</a>
                <a href="{lang_prefix}contact.html">Contact</a>
            </nav>
"""
    
    mobile_nav = f"""
        <nav class="nav-links-mobile">
            <a href="{lang_prefix}services.html">Services</a>
            <a href="{lang_prefix}equipe.html">Équipe</a>
            <a href="{lang_prefix}technologie.html">Technologie</a>
            <a href="{lang_prefix}tarifs.html">Tarifs</a>
            <a href="{lang_prefix}faq.html">FAQ</a>
            <a href="{lang_prefix}contact.html">Contact</a>
        </nav>
""" if lang == 'fr' else f"""
        <nav class="nav-links-mobile">
            <a href="{lang_prefix}services.html">Services</a>
            <a href="{lang_prefix}team.html">Team</a>
            <a href="{lang_prefix}technology.html">Technology</a>
            <a href="{lang_prefix}pricing.html">Pricing</a>
            <a href="{lang_prefix}faq.html">FAQ</a>
            <a href="{lang_prefix}contact.html">Contact</a>
        </nav>
"""

    footer_content = f"""
                <div class="footer-col" style="justify-self: center;">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="/fr/services.html#bilan">Bilan cutané complet</a></li>
                        <li><a href="/fr/services.html#medical">Ablation médicale suspecte</a></li>
                        <li><a href="/fr/services.html#cosmetique">Ablation cosmétique bénigne</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Avenue Winston Churchill, Uccle, Bruxelles <!-- REMPLACER --></li>
                        <li><a href="mailto:[EMAIL_CONTACT]">[EMAIL_CONTACT]</a></li>
                        <li>[TEL_CLINIQUE]</li>
                    </ul>
                    <div class="social-icons">
                        <a href="[INSTAGRAM]" aria-label="Instagram"><iconify-icon icon="lucide:instagram"></iconify-icon></a>
                        <a href="[FACEBOOK]" aria-label="Facebook"><iconify-icon icon="lucide:facebook"></iconify-icon></a>
                        <a href="[LINKEDIN]" aria-label="LinkedIn"><iconify-icon icon="lucide:linkedin"></iconify-icon></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <span>© 2025 Churchill SkinCheck — Clinique Churchill, Uccle, Bruxelles</span>
                <span class="text-muted">Site réalisé par Roots Agency | <a href="/fr/mentions-legales.html" class="text-muted">Mentions légales</a></span>
            </div>
""" if lang == 'fr' else f"""
                <div class="footer-col" style="justify-self: center;">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="/en/services.html#bilan">Comprehensive mole check</a></li>
                        <li><a href="/en/services.html#medical">Medical lesion removal</a></li>
                        <li><a href="/en/services.html#cosmetique">Cosmetic mole removal</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Avenue Winston Churchill, Uccle, Brussels <!-- REMPLACER --></li>
                        <li><a href="mailto:[EMAIL_CONTACT]">[EMAIL_CONTACT]</a></li>
                        <li>[TEL_CLINIQUE]</li>
                    </ul>
                    <div class="social-icons">
                        <a href="[INSTAGRAM]" aria-label="Instagram"><iconify-icon icon="lucide:instagram"></iconify-icon></a>
                        <a href="[FACEBOOK]" aria-label="Facebook"><iconify-icon icon="lucide:facebook"></iconify-icon></a>
                        <a href="[LINKEDIN]" aria-label="LinkedIn"><iconify-icon icon="lucide:linkedin"></iconify-icon></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <span>© 2025 Churchill SkinCheck — Clinique Churchill, Uccle, Brussels</span>
                <span class="text-muted">Site by Roots Agency | <a href="/en/legal.html" class="text-muted">Legal mentions</a></span>
            </div>
"""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <!-- Open Graph -->
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="https://skincheck.cliniquechurchill.be{url_path}">
    <meta property="og:image" content="https://skincheck.cliniquechurchill.be/assets/og-image.jpg"> <!-- REMPLACER : URL de l'image OG -->
    
    <!-- hreflang -->
    <link rel="alternate" hreflang="fr" href="https://skincheck.cliniquechurchill.be/fr{url_path.replace('/en/','/')}">
    <link rel="alternate" hreflang="en" href="https://skincheck.cliniquechurchill.be/en{url_path.replace('/fr/','/')}">
    <link rel="alternate" hreflang="x-default" href="https://skincheck.cliniquechurchill.be/">

    <link rel="stylesheet" href="../css/style.css">
    
    <!-- Iconify -->
    <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "MedicalClinic",
      "name": "Churchill SkinCheck",
      "parentOrganization": {{ "@type": "Hospital", "name": "Clinique Churchill" }},
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Avenue Winston Churchill",
        "addressLocality": "Uccle, Bruxelles",
        "addressCountry": "BE"
      }},
      "medicalSpecialty": "PlasticSurgery",
      "availableService": [
        {{ "@type": "MedicalProcedure", "name": "Bilan cutané dermatoscopique" }},
        {{ "@type": "MedicalProcedure", "name": "Ablation chirurgicale de naevus suspect" }},
        {{ "@type": "MedicalProcedure", "name": "Ablation cosmétique de grains de beauté" }}
      ],
      "telephone": "[TEL_CLINIQUE]",
      "url": "https://skincheck.cliniquechurchill.be"
    }}
    </script>
</head>
<body>

    <!-- Header -->
    <header class="main-header">
        <div class="container nav-container">
            <a href="{lang_prefix}index.html" class="logo-box">
                <span class="logo-title">Churchill SkinCheck</span>
                <span class="logo-sub">by Clinique Churchill</span>
            </a>
            
            {header_nav}

            <div class="nav-right">
                <a href="[LIEN_RDV]" class="btn-ghost d-none d-md-inline-flex" target="_blank" rel="noopener">{'Prendre rendez-vous' if lang == 'fr' else 'Book Appt'}</a>
                <div class="lang-switch d-none d-md-flex">
                    <a href="/fr{url_path.replace('/en/','/')}" class="{ 'active' if lang == 'fr' else '' }">FR</a>
                    <a href="/en{url_path.replace('/fr/','/')}" class="{ 'active' if lang == 'en' else '' }">EN</a>
                </div>
                <button class="burger-btn" aria-label="Menu">
                    <span class="burger-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        {mobile_nav}
        <div class="lang-switch">
                    <a href="/fr{url_path.replace('/en/','/')}" class="{ 'active' if lang == 'fr' else '' }">FR</a> | 
                    <a href="/en{url_path.replace('/fr/','/')}" class="{ 'active' if lang == 'en' else '' }">EN</a>
        </div>
        <div class="mt-4">
            <a href="[LIEN_RDV]" class="btn-gold w-100" target="_blank" rel="noopener" style="justify-content:center;">{'Prendre Rendez-vous' if lang == 'fr' else 'Book Appointment'}</a>
        </div>
    </div>

    <main style="padding-top: 80px;">
        {content}
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div class="logo-box" style="margin-bottom: 1.5rem;">
                        <span class="logo-title" style="color:#ffffff;">Churchill SkinCheck</span>
                        <span class="logo-sub">by Clinique Churchill</span>
                    </div>
                </div>
                {footer_content}
        </div>
    </footer>

    <!-- Scripts module to allow config imports -->
    <script type="module" src="../js/config.js"></script>
    <script src="../js/main.js"></script>
    <script src="../js/contact.js"></script>
</body>
</html>"""

pages_fr = [
    {
        "file": "index.html",
        "title": "Churchill SkinCheck | Dermato-Chirurgie à Bruxelles",
        "desc": "Churchill SkinCheck, service de dermato-chirurgie de la Clinique Churchill. Diagnostic dermatoscopique et ablation de lésions cutanées par chirurgiens plasticiens à Bruxelles.",
        "og_title": "Churchill SkinCheck | Dermato-Chirurgie à Bruxelles",
        "content": '''
        <!-- Hero Section -->
        <section style="padding: 10rem 0 7rem;">
            <div class="bg-hero-deco"></div>
            <div class="container layout-grid">
                <div class="fade-up border-left-gold">
                    <span class="badge"><iconify-icon icon="lucide:microscope" style="margin-right:4px;"></iconify-icon> Nouveau service — Clinique Churchill, Bruxelles</span>
                    <h1>Votre peau mérite l'expertise d'un chirurgien</h1>
                    <p class="text-secondary" style="font-size: 1.15rem; margin: 1.5rem 0 2rem;">
                        Churchill SkinCheck est le seul service bruxellois combinant diagnostic dermatoscopique de précision et ablation chirurgicale par des chirurgiens plasticiens — lors d'une seule et même consultation.
                    </p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Prendre rendez-vous</a>
                        <a href="#services" class="btn-ghost">Découvrir nos services</a>
                    </div>
                </div>
                <div class="fade-up" style="transition-delay: 0.2s;">
                    <!-- REMPLACER : photo consultation chirurgien -->
                    <div class="soft-grid" style="border-radius:1.5rem; overflow:hidden;">
                        <img src="https://placehold.co/600x600?text=Photo+Consultation" alt="Consultation dermatologique à la Clinique Churchill" style="border-radius: 1.5rem; box-shadow: var(--shadow-card-hover);">
                    </div>
                </div>
            </div>
        </section>

        <!-- Bandeau Confiance -->
        <section style="padding: 0 0 6rem; position:relative; z-index:10; margin-top:-3rem;">
            <div class="container fade-up">
                <div class="card" style="padding: 2rem;">
                    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align:center;">
                        <div>
                            <iconify-icon icon="lucide:clock" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">1 seule consultation</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Diagnostic et ablation réunis</p>
                        </div>
                        <div>
                            <iconify-icon icon="lucide:user-check" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">Chirurgiens plasticiens</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Résultat esthétique optimal</p>
                        </div>
                        <div>
                            <iconify-icon icon="lucide:scan-face" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">Heine DeltaOne</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Dermoscopie numérique de référence</p>
                        </div>
                        <div>
                            <iconify-icon icon="lucide:building" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">Clinique Churchill</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Institution médicale à Uccle depuis 1985</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Intro -->
        <section class="section-alt text-center">
            <div class="container fade-up" style="max-width:800px;">
                <span class="badge">Notre approche</span>
                <h2 class="text-navy" style="margin-bottom: 2rem;">Ce que seul un chirurgien plasticien peut faire</h2>
                <p style="font-size: 1.1rem; margin-bottom: 3rem;">
                    Contrairement à la dermatologie classique, nos chirurgiens plasticiens cumulent deux compétences que la plupart des praticiens exercent séparément : l'analyse précise des lésions cutanées et leur ablation chirurgicale. Cette dualité signifie qu'une seule consultation suffit dans la majorité des cas. Résultat : moins d'attente, moins de déplacements, et une cicatrisation optimisée grâce aux techniques de chirurgie plastique (respect des lignes de tension, fils superficiels ultra-fins, repositionnement des cicatrices dans les plis naturels).
                </p>
                <div style="display:flex; justify-content:center; gap:2rem; flex-wrap:wrap; font-weight:500; font-size:0.95rem;">
                    <div style="display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Diagnostic & ablation en 1 visite</div>
                    <div style="display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Cicatrices minimisées — technique plastique</div>
                    <div style="display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Analyse anatomopathologique systématique</div>
                </div>
            </div>
        </section>
        
        <!-- Services -->
        <section id="services">
            <div class="container">
                <div class="text-center fade-up" style="margin-bottom:4rem;">
                    <h2 class="text-navy">Nos Services</h2>
                </div>
                <div class="layout-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <div class="card fade-up" style="display:flex; flex-direction:column;">
                        <span class="badge" style="align-self:flex-start;">Prévention</span>
                        <h3 style="margin-bottom:1rem;">Bilan Cutané Complet</h3>
                        <p style="flex-grow:1;">Examen de l'ensemble de vos lésions au dermatoscope Heine DeltaOne. Votre chirurgien analyse chaque naevus selon la règle ABCDE et détermine ceux nécessitant une surveillance rapprochée ou une ablation.</p>
                        <p class="text-muted" style="margin: 1.5rem 0; font-size:0.85rem;"><iconify-icon icon="lucide:clock"></iconify-icon> Durée : 20–30 min</p>
                        <a href="/fr/services.html#bilan" class="btn-ghost">En savoir plus</a>
                    </div>
                    <div class="card card-gold fade-up" style="display:flex; flex-direction:column; transition-delay:0.1s;">
                        <span class="badge" style="align-self:flex-start; background:var(--churchill-gold); color:#1a2b42;">Acte médical • Remboursé mutuelle</span>
                        <h3 style="margin-bottom:1rem;">Ablation de Naevus Suspect</h3>
                        <p style="flex-grow:1;">Exérèse chirurgicale sous anesthésie locale d'un naevus atypique ou suspect, suivie d'une analyse anatomopathologique en laboratoire. Dans la majorité des cas, l'ablation est réalisée lors de la même consultation que le diagnostic.</p>
                        <p class="text-muted" style="margin: 1.5rem 0; font-size:0.85rem;"><iconify-icon icon="lucide:clock"></iconify-icon> Durée : 30–45 min</p>
                        <a href="/fr/services.html#medical" class="btn-gold">En savoir plus</a>
                    </div>
                    <div class="card fade-up" style="display:flex; flex-direction:column; transition-delay:0.2s;">
                        <span class="badge" style="align-self:flex-start;">Confort & Esthétique</span>
                        <h3 style="margin-bottom:1rem;">Ablation Cosmétique</h3>
                        <p style="flex-grow:1;">Retrait de grains de beauté bénins pour des raisons esthétiques ou de confort (gêne vestimentaire, irritation). Réalisé par un chirurgien plasticien pour un résultat cicatriciel optimal.</p>
                        <p class="text-muted" style="margin: 1.5rem 0; font-size:0.85rem;"><iconify-icon icon="lucide:clock"></iconify-icon> Durée : 20–40 min</p>
                        <a href="/fr/services.html#cosmetique" class="btn-ghost">En savoir plus</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technologie -->
        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <span class="badge">Technologie de diagnostic</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Heine DeltaOne — La dermoscopie de référence mondiale</h2>
                    <p style="margin-bottom:2rem; font-size:1.05rem;">
                        Le dermatoscope Heine DeltaOne est l'outil de référence utilisé par les spécialistes les plus exigeants au monde. Son optique haute résolution et son éclairage LED polarisé permettent de visualiser les structures cutanées profondes, invisibles à l'œil nu. C'est grâce à cet équipement que nos chirurgiens peuvent poser un diagnostic précis et éviter les ablations inutiles.
                    </p>
                    <a href="https://www.heine.com/" target="_blank" rel="noopener" class="text-gold" style="font-size:0.9rem; text-decoration:underline; display:inline-block; margin-bottom:2rem;">En savoir plus sur cet équipement</a><br>
                    <a href="/fr/technologie.html" class="btn-ghost">Notre technologie en détail</a>
                </div>
                <div class="fade-up">
                    <div class="card" style="padding:1rem;">
                        <img src="https://placehold.co/600x600?text=Heine+DeltaOne" alt="Dermatoscope Heine DeltaOne" style="border-radius:1rem;">
                    </div>
                </div>
            </div>
        </section>

        <!-- Equipe -->
        <section>
            <div class="container">
                <div class="text-center fade-up" style="margin-bottom:4rem;">
                    <span class="badge">Notre équipe</span>
                    <h2 class="text-navy" style="margin-bottom:1rem;">Des chirurgiens plasticiens à votre service</h2>
                    <p style="max-width:700px; margin:0 auto; font-size:1.05rem;">Chaque praticien de Churchill SkinCheck cumule une expertise en chirurgie plastique reconstructrice et en dermato-chirurgie.</p>
                </div>
                <div class="layout-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <div class="card fade-up text-center">
                        <img src="https://placehold.co/300x300?text=Photo+1" alt="Dr" style="border-radius: 50%; margin: 0 auto 1.5rem; width:150px; height:150px; object-fit:cover;">
                        <h3>Dr. [Prénom] [Nom] <!-- REMPLACER --></h3>
                        <p class="text-gold" style="font-weight:500; font-size:0.9rem; margin-bottom:0.25rem;">Chirurgien Plasticien</p>
                        <p class="text-muted" style="font-size:0.8rem; margin-bottom:1rem;">INAMI : [INAMI 1]</p>
                        <p style="font-size:0.9rem; margin-bottom:1.5rem; min-height:80px;">Formé en Belgique et à l'international. Membre de la Société Royale Belge de Chirurgie Plastique.</p>
                        <hr style="border:none; border-top:1px solid var(--border-light); margin-bottom:1rem;">
                        <p style="font-size:0.8rem; font-weight:600; color:var(--churchill-navy);">Dermato-chirurgie & reconstruction cutanée</p>
                    </div>
                    <div class="card fade-up text-center" style="transition-delay:0.1s;">
                        <img src="https://placehold.co/300x300?text=Photo+2" alt="Dr" style="border-radius: 50%; margin: 0 auto 1.5rem; width:150px; height:150px; object-fit:cover;">
                        <h3>Dr. [Prénom] [Nom] <!-- REMPLACER --></h3>
                        <p class="text-gold" style="font-weight:500; font-size:0.9rem; margin-bottom:0.25rem;">Chirurgien Plasticien</p>
                        <p class="text-muted" style="font-size:0.8rem; margin-bottom:1rem;">INAMI : [INAMI 2]</p>
                        <p style="font-size:0.9rem; margin-bottom:1.5rem; min-height:80px;">Formé en Belgique et à l'étranger, il intervient à Churchill SkinCheck pour les cas complexes et les lésions à fort enjeu esthétique.</p>
                        <hr style="border:none; border-top:1px solid var(--border-light); margin-bottom:1rem;">
                        <p style="font-size:0.8rem; font-weight:600; color:var(--churchill-navy);">Chirurgie des lésions pigmentées & cicatrisation esthétique</p>
                    </div>
                    <div class="card fade-up text-center" style="transition-delay:0.2s;">
                        <img src="https://placehold.co/300x300?text=Photo+3" alt="Dr" style="border-radius: 50%; margin: 0 auto 1.5rem; width:150px; height:150px; object-fit:cover;">
                        <h3>Dr. [Prénom] [Nom] <!-- REMPLACER --></h3>
                        <p class="text-gold" style="font-weight:500; font-size:0.9rem; margin-bottom:0.25rem;">Chirurgien Plasticien</p>
                        <p class="text-muted" style="font-size:0.8rem; margin-bottom:1rem;">INAMI : [INAMI 3]</p>
                        <p style="font-size:0.9rem; margin-bottom:1.5rem; min-height:80px;">Spécialisé en dermato-chirurgie esthétique et reconstructrice. Intervient régulièrement pour des ablations cosmétiques et médicales.</p>
                        <hr style="border:none; border-top:1px solid var(--border-light); margin-bottom:1rem;">
                        <p style="font-size:0.8rem; font-weight:600; color:var(--churchill-navy);">Dermato-chirurgie esthétique & reconstructrice</p>
                    </div>
                </div>
                <div class="text-center mt-5" style="margin-top:3rem;">
                    <a href="/fr/equipe.html" class="btn-ghost">Rencontrer l'équipe complete</a>
                </div>
            </div>
        </section>

        <!-- Etapes & Remboursement -->
        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <h2 class="text-navy" style="margin-bottom:1rem;">Comment ça marche</h2>
                    <ul class="steps-timeline">
                        <li class="step-item">
                            <div class="step-number">1</div>
                            <h4>Prise de rendez-vous</h4>
                            <p class="text-secondary" style="font-size:0.95rem;">Réservez votre consultation en ligne. Aucune ordonnance requise.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-number">2</div>
                            <h4>Consultation & Diagnostic</h4>
                            <p class="text-secondary" style="font-size:0.95rem;">Votre chirurgien examine vos lésions au dermatoscope Heine DeltaOne, établit un diagnostic et vous explique si une ablation est conseillée.</p>
                        </li>
                        <li class="step-item" style="padding-bottom:0; border-left:none;">
                            <div class="step-number">3</div>
                            <h4>Ablation si indiquée</h4>
                            <p class="text-secondary" style="font-size:0.95rem;">Dans la plupart des cas, l'ablation peut être réalisée le jour même. La lésion est envoyée en laboratoire (résultats sous 10-15 jours).</p>
                        </li>
                    </ul>
                </div>
                <div class="fade-up card" style="background: rgba(255,255,255,0.7); backdrop-filter:blur(10px);">
                    <iconify-icon icon="lucide:shield-check" width="40" class="text-gold" style="margin-bottom:1.5rem;"></iconify-icon>
                    <h3 style="margin-bottom:1rem;">Information Remboursement</h3>
                    <p style="margin-bottom:1rem;">L'exérèse médicale d'un naevus suspect est <strong>partiellement remboursée</strong> par votre mutualité belge. L'ablation cosmétique n'est pas remboursée.</p>
                    <p style="margin-bottom:2rem;">Votre chirurgien vous orientera dès la consultation. Munissez-vous de votre carte d'identité et vignette mutualité.</p>
                    <a href="/fr/tarifs.html" class="btn-ghost">Voir les tarifs détaillés</a>
                </div>
            </div>
        </section>

        <!-- FAQ -->
        <section>
            <div class="container fade-up" style="max-width:800px;">
                <h2 class="text-navy text-center" style="margin-bottom:3rem;">Foire aux questions rapides</h2>
                <div class="faq-item">
                    <div class="faq-question">Faut-il une ordonnance ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Non, la prise de RDV est directe et sans ordonnance médicale préalable.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">L'ablation est-elle remboursée ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Elle est partiellement remboursée par la mutuelle s'il s'agit d'une indication médicale. L'ablation esthétique/cosmétique n'est en revanche pas remboursée.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Quelle est la durée de la consultation ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Prévoyez 20 à 45 minutes selon le cas (simple examen dermatoscopique ou avec ablation consécutive).</div>
                </div>
                <div class="text-center" style="margin-top:3rem;">
                    <a href="/fr/faq.html" class="btn-ghost">Toutes les questions fréquentes</a>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">Prenez rendez-vous dès aujourd'hui</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Consultez un chirurgien plasticien spécialisé en dermato-chirurgie à la Clinique Churchill, Uccle.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Réserver ma consultation</a>
                <p style="margin-top:1.5rem; font-size:0.85rem; color:rgba(255,255,255,0.7);">Sans ordonnance · Prise en charge mutuelle si indication médicale · Résultats sous 10-15 jours</p>
            </div>
        </section>
        '''
    },
    {
        "file": "services.html",
        "title": "Nos Services | Churchill SkinCheck Bruxelles",
        "desc": "Bilan cutané, ablation médicale et cosmétique de grains de beauté à Bruxelles. Par chirurgiens plasticiens à la Clinique Churchill. Remboursé si indication médicale.",
        "og_title": "Nos Services | Churchill SkinCheck Bruxelles",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Nos Services de Dermato-Chirurgie</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem;">De l'examen dermatoscopique à l'ablation chirurgicale — en une seule consultation.</p>
            </div>
        </section>
        
        <section id="bilan" class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <span class="badge">Prévention</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Bilan Cutané Complet</h2>
                    <p style="margin-bottom:1rem;">Notre chirurgien examine l'ensemble de vos lésions cutanées à l'aide du dermatoscope Heine DeltaOne. Chaque naevus est analysé selon la règle ABCDE : Asymétrie, Bords, Couleur, Diamètre, Évolution.</p>
                    <p style="margin-bottom:1rem;">Ce bilan permet d'identifier les lésions nécessitant une ablation, celles nécessitant une surveillance régulière, et celles parfaitement bénignes. Contrairement à un bilan chez un dermatologue classique, votre praticien peut — si une ablation est indiquée — la réaliser immédiatement lors de la même consultation.</p>
                    <ul style="margin-bottom:2rem; padding-left:1.5rem; list-style:disc; font-weight:500;">
                        <li><strong>Indications :</strong> Contrôle annuel, antécédents de mélanome, peau claire, etc.</li>
                        <li><strong>Durée :</strong> 20–30 min</li>
                        <li><strong>Remboursement :</strong> Consultation médicale standard</li>
                    </ul>
                    <a href="[LIEN_RDV]" class="btn-ghost">Prendre rendez-vous</a>
                </div>
            </div>
        </section>

        <section id="medical">
            <div class="container layout-grid">
                <div class="fade-up card card-gold" style="padding:3rem;">
                    <span class="badge" style="background:#C9A96E; color:#fff; border-color:#C9A96E;">Partiellement remboursé — Mutualité belge</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Ablation de Naevus Suspect</h2>
                    <p style="margin-bottom:1rem;">Lorsqu'une lésion est identifiée comme suspecte ou atypique, notre chirurgien plasticien réalise une exérèse chirurgicale sous anesthésie locale. L'intervention consiste à retirer la lésion avec une marge de sécurité adaptée, puis à suturer la peau avec un soin esthétique maximal : respect des lignes de moindre tension, fils superficiels ultra-fins, repositionnement de la cicatrice dans les plis naturels quand c'est possible.</p>
                    <p style="margin-bottom:1.5rem;">La lésion est systématiquement envoyée en analyse anatomopathologique dans un laboratoire spécialisé. Les résultats vous sont communiqués sous 10 à 15 jours ouvrables.</p>
                    
                    <ul style="margin-bottom:2rem; font-weight:500;">
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Anesthésie locale — intervention non douloureuse</li>
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Ablation et consultation possibles lors de la même visite</li>
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Analyse anatomopathologique systématique</li>
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Résultats communiqués sous 10-15 jours</li>
                    </ul>
                    
                    <div style="background:var(--bg-secondary); padding:1rem; border-radius:0.5rem; font-size:0.9rem; margin-bottom:2rem;">
                        <p style="margin-bottom:0.5rem;"><strong>Durée :</strong> 30–45 min (consultation comprise)</p>
                        <p><strong>Remboursement :</strong> Partiellement remboursé si indication médicale confirmée. Apportez carte d'identité + vignette.</p>
                    </div>
                    
                    <a href="[LIEN_RDV]" class="btn-gold">Prendre rendez-vous</a>
                </div>
            </div>
        </section>

        <section id="cosmetique" class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <span class="badge">Esthétique</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Ablation Cosmétique</h2>
                    <p style="margin-bottom:1rem;">Vous souhaitez faire retirer un grain de beauté bénin pour des raisons esthétiques ou de confort — parce qu'il vous gêne visuellement, s'accroche aux vêtements ou aux bijoux, ou vous irrite ? Nos chirurgiens plasticiens réalisent ce type d'ablation avec la même rigueur chirurgicale que pour une indication médicale.</p>
                    <p style="margin-bottom:1.5rem;">Le résultat esthétique est leur priorité : chaque incision est pensée pour minimiser la cicatrice visible à long terme. Un naevus bénin est confirmé lors de la consultation préalable. L'ablation peut dans la plupart des cas être réalisée le jour même. La lésion est tout de même envoyée en analyse anatomopathologique pour écarter tout risque résiduel.</p>
                    <ul style="margin-bottom:2rem; padding-left:1.5rem; list-style:disc; font-weight:500;">
                        <li><strong>Durée :</strong> 20–40 min selon nombre et localisation</li>
                        <li><strong>Remboursement :</strong> Non remboursé (acte cosmétique).</li>
                    </ul>
                    <a href="/fr/tarifs.html" class="btn-ghost">Voir les tarifs</a>
                </div>
            </div>
        </section>

        <section>
            <div class="container fade-up">
                <h2 class="text-navy text-center" style="margin-bottom:3rem;">Le choix de la sécurité et de l'esthétique</h2>
                <div class="table-glass">
                    <table style="width:100%;">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Churchill SkinCheck</th>
                                <th>Dermatologue classique</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-weight:500;">Diagnostic</td>
                                <td>✓ Dermoscopie Heine DeltaOne</td>
                                <td>Variable selon équipement</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Ablation le jour même</td>
                                <td>✓ Dans la majorité des cas</td>
                                <td>✗ Renvoi vers chirurgien</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Résultat cicatriciel</td>
                                <td>✓ Techniques de chirurgie plastique</td>
                                <td>Variable</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Analyse anatomopathologique</td>
                                <td>✓ Systématique</td>
                                <td>Variable</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Délais globaux</td>
                                <td>✓ 1 seule consultation</td>
                                <td>2 RDV minimum</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="text-center" style="margin-top:4rem;">
                    <a href="[LIEN_RDV]" class="btn-gold text-center">Prendre rendez-vous maintenant</a>
                </div>
            </div>
        </section>
        '''
    },
    {
        "file": "equipe.html",
        "title": "Notre Équipe | Churchill SkinCheck Bruxelles",
        "desc": "Churchill SkinCheck réunit une équipe de chirurgiens plasticiens certifiés spécialisés en dermato-chirurgie à Bruxelles, Clinique Churchill.",
        "og_title": "Notre Équipe | Churchill SkinCheck",
        "content": '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Notre Équipe de Chirurgiens Plasticiens</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem; max-width:800px; margin-left:auto; margin-right:auto;">
                    Churchill SkinCheck s'appuie sur des chirurgiens plasticiens certifiés, tous membres de la Société Royale Belge de Chirurgie Plastique. Leur double expertise — chirurgie plastique reconstructrice et dermato-chirurgie — garantit un diagnostic rigoureux et un résultat esthétique optimal.
                </p>
            </div>
        </section>
        
        <section class="section-alt">
            <div class="container">
                <div class="layout-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
                    <div class="card fade-up">
                        <img src="https://placehold.co/400x400" alt="Dr X" style="border-radius:1rem; margin-bottom:1.5rem; width:100%; aspect-ratio:1; object-fit:cover;">
                        <h2>Dr. [Prénom] [Nom] <!-- REMPLACER --></h2>
                        <ul style="border-top:1px solid var(--border-light); border-bottom:1px solid var(--border-light); padding:1rem 0; margin:1rem 0; font-size:0.9rem;">
                            <li><strong>Spécialité :</strong> Dermato-chirurgie & Reconstruction cutanée</li>
                            <li><strong>INAMI :</strong> [INAMI 1] <!-- REMPLACER --></li>
                        </ul>
                        <p style="margin-bottom:1.5rem;">Chirurgien plasticien certifié, spécialisé en dermato-chirurgie et reconstruction cutanée. Exerce à la Clinique Churchill depuis [année]. Membre de la Société Royale Belge de Chirurgie Plastique. Formation complémentaire en oncologie cutanée.</p>
                        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                            <span class="badge">Ablation naevus</span>
                            <span class="badge">Chirurgie cutanée</span>
                            <span class="badge">Cicatrisation esthétique</span>
                        </div>
                    </div>

                    <div class="card fade-up" style="transition-delay:0.1s;">
                        <img src="https://placehold.co/400x400" alt="Dr Y" style="border-radius:1rem; margin-bottom:1.5rem; width:100%; aspect-ratio:1; object-fit:cover;">
                        <h2>Dr. [Prénom] [Nom] <!-- REMPLACER --></h2>
                        <ul style="border-top:1px solid var(--border-light); border-bottom:1px solid var(--border-light); padding:1rem 0; margin:1rem 0; font-size:0.9rem;">
                            <li><strong>Spécialité :</strong> Chirurgie des lésions pigmentées</li>
                            <li><strong>INAMI :</strong> [INAMI 2] <!-- REMPLACER --></li>
                        </ul>
                        <p style="margin-bottom:1.5rem;">Chirurgien plasticien avec une expertise particulière dans la prise en charge des lésions cutanées pigmentées et des tumeurs de la peau. Formé en Belgique et à l'étranger, il intervient à Churchill SkinCheck pour les cas complexes et les lésions à fort enjeu esthétique.</p>
                        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                            <span class="badge">Naevus complexes</span>
                            <span class="badge">Tumeurs cutanées</span>
                            <span class="badge">Chirurgie reconstructrice</span>
                        </div>
                    </div>

                    <div class="card fade-up" style="transition-delay:0.2s;">
                        <img src="https://placehold.co/400x400" alt="Dr Z" style="border-radius:1rem; margin-bottom:1.5rem; width:100%; aspect-ratio:1; object-fit:cover;">
                        <h2>Dr. [Prénom] [Nom] <!-- REMPLACER --></h2>
                        <ul style="border-top:1px solid var(--border-light); border-bottom:1px solid var(--border-light); padding:1rem 0; margin:1rem 0; font-size:0.9rem;">
                            <li><strong>Spécialité :</strong> Dermato-chirurgie esthétique & reconstructrice</li>
                            <li><strong>INAMI :</strong> [INAMI 3] <!-- REMPLACER --></li>
                        </ul>
                        <p style="margin-bottom:1.5rem;">Spécialisé en dermato-chirurgie esthétique et reconstructrice, formé à l'ULB. Membre actif de sociétés scientifiques belges et européennes de chirurgie plastique. Intervient régulièrement pour des ablations cosmétiques et médicales à la Clinique Churchill.</p>
                        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                            <span class="badge">Ablation cosmétique</span>
                            <span class="badge">Chirurgie plastique</span>
                            <span class="badge">Médecine esthétique</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">N'attendez pas de vérifier une lésion suspecte</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Nos créneaux d'urgence vous permettent d'être rassuré ou pris en charge sans délai.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Consulter nos disponibilités</a>
            </div>
        </section>
        '''
    },
    {
        "file": "technologie.html",
        "title": "Dermatoscope Heine DeltaOne | Churchill SkinCheck",
        "desc": "Churchill SkinCheck utilise le dermatoscope Heine DeltaOne pour un diagnostic dermoscopique précis à Bruxelles. Technologie de référence mondiale en analyse des lésions cutanées.",
        "og_title": "Heine DeltaOne | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Heine DeltaOne — Notre Outil de Diagnostic</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem; max-width:800px; margin: 1rem auto 0;">
                    Sans cet outil, de nombreuses lésions atypiques passent inaperçues à l'examen visuel. La dermoscopie est clé dans notre pratique pour poser les bons diagnostics.
                </p>
            </div>
        </section>
        
        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up card" style="padding:1.5rem; text-align:center;">
                    <!-- REMPLACER : photo Heine DeltaOne -->
                    <img src="https://placehold.co/600x600?text=Heine+DeltaOne" alt="Dermatoscope Heine DeltaOne" style="border-radius:1rem;">
                </div>
                <div class="fade-up">
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Fonctionnalités avancées</h2>
                    <ul style="border-left:2px solid var(--border-light); padding-left:1.5rem; margin-bottom:2rem;">
                        <li style="margin-bottom:1.5rem;">
                            <strong style="color:var(--text-primary);">1. Optique haute résolution</strong><br>
                            Visualisation des structures melanocytaires profondes.
                        </li>
                        <li style="margin-bottom:1.5rem;">
                            <strong style="color:var(--text-primary);">2. Éclairage LED polarisé</strong><br>
                            Élimination des reflets, analyse en profondeur sans contact.
                        </li>
                        <li style="margin-bottom:1.5rem;">
                            <strong style="color:var(--text-primary);">3. Ergonomie clinique</strong><br>
                            Confort accru du patient, et grande précision pour le praticien.
                        </li>
                        <li>
                            <strong style="color:var(--text-primary);">4. Documentation numérique possible</strong><br>
                            Idéal pour la traçabilité, le suivi et la comparaison d'évolution dans le temps.
                        </li>
                    </ul>
                    <a href="https://www.heine.com/fr/produits/dermatoscopes-et-documentation-numerique/dermatoscopes/detail/99957-dermatoscope-heine-deltaone" class="btn-ghost" target="_blank" rel="noopener">Fiche technique Heine DeltaOne</a>
                </div>
            </div>
        </section>

        <section>
            <div class="container fade-up text-center" style="max-width:800px;">
                <h2 class="text-navy" style="margin-bottom:1.5rem;">Pourquoi la dermoscopie change tout</h2>
                <p>La dermoscopie numérique permet de détecter des signes d'atypie invisibles à l'œil nu — réseaux pigmentaires irréguliers, globules atypiques, voile bleu-blanc — qui peuvent indiquer une transformation maligne précoce. Utilisé par nos chirurgiens, le Heine DeltaOne réduit significativement le nombre d'ablations inutiles et améliore considérablement la précision diagnostique.</p>
            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">N'attendez pas de vérifier une lésion suspecte</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Nos créneaux d'urgence vous permettent d'être rassuré ou pris en charge sans délai.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Consulter nos disponibilités</a>
            </div>
        </section>
        '''
    },
    {
        "file": "tarifs.html",
        "title": "Tarifs & Remboursements | Churchill SkinCheck Bruxelles",
        "desc": "Tarifs transparents pour le bilan cutané et l'ablation de lésions chez Churchill SkinCheck, Bruxelles. Remboursement mutualité belge pour ablations médicalement indiquées.",
        "og_title": "Tarifs & Remboursements | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Tarifs & Remboursements</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem;">Transparence totale sur nos tarifs. Certaines prestations sont partiellement remboursées par votre mutualité belge.</p>
            </div>
        </section>
        
        <section class="section-alt">
            <div class="container fade-up">
                <div class="table-glass" style="max-width:1000px; margin: 0 auto 3rem;">
                    <table style="width:100%;">
                        <thead>
                            <tr>
                                <th>Prestation</th>
                                <th>Tarif indicatif</th>
                                <th>Remboursement</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-weight:500;">Consultation & Bilan Cutané</td>
                                <td class="text-gold" style="font-weight:600;">[TARIF] €</td>
                                <td>Consultation médicale standard</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Ablation médicale — naevus suspect</td>
                                <td class="text-gold" style="font-weight:600;">[TARIF] €</td>
                                <td>✓ Partiellement remboursée (INAMI)</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Ablation cosmétique — 1 lésion</td>
                                <td class="text-gold" style="font-weight:600;">[TARIF] €</td>
                                <td>✗ Non remboursée</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Ablation cosmétique — lésions multiples</td>
                                <td class="text-gold" style="font-weight:600;">Sur devis</td>
                                <td>✗ Non remboursée</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="card card-gold" style="max-width:1000px; margin:0 auto; background: var(--churchill-gold-soft); border-color:var(--border-gold);">
                    <p style="font-style:italic; font-size:0.95rem; color:var(--churchill-navy);">Les tarifs indiqués sont donnés à titre indicatif. Le tarif définitif est établi lors de la consultation en fonction de la nature, de la taille et de la localisation de la lésion. Pour les actes médicalement indiqués, une partie peut être remboursée par votre mutualité sur base du tarif INAMI en vigueur. Munissez-vous de votre carte d'identité et de votre vignette mutualité.</p>
                </div>
            </div>
        </section>

        <section>
            <div class="container fade-up layout-grid">
                <div>
                    <h2 class="text-navy" style="margin-bottom:1rem;">Comprendre votre remboursement</h2>
                    <p style="margin-bottom:1.5rem;">Notre cabinet opère selon les standards de la chirurgie plastique reconstructrice avec une application stricte des principes déontologiques liés au diagnostic d'anomalies cutanées.</p>
                </div>
                <div>
                    <div style="margin-bottom:1.5rem;">
                        <h4 style="color:var(--text-primary); margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Acte médical (remboursé)</h4>
                        <p style="font-size:0.95rem;">Ablation d'un naevus suspect, indication confirmée par le chirurgien → remboursement partiel mutualité sur base nomenclatures INAMI.</p>
                    </div>
                    <div style="margin-bottom:1.5rem;">
                        <h4 style="color:var(--text-primary); margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:minus-circle" class="text-muted"></iconify-icon> Acte cosmétique (non remboursé)</h4>
                        <p style="font-size:0.95rem;">Ablation décidée pour des raisons de confort personnel ou d'esthétique pure → à charge intégrale du patient. <em>(Note : certaines mutuelles complémentaires couvrent pourtant ce type de frais, renseignez-vous)</em></p>
                    </div>
                    <div style="padding-top:1rem; border-top:1px solid var(--border-light);">
                        <p style="font-size:0.95rem; font-weight:600;">Pensez à apporter lors de votre RV : <br><span style="font-weight:400; color:var(--text-secondary);">Votre carte d'identité (eID) et votre vignette mutualité actuelle.</span></p>
                    </div>
                </div>
            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">N'attendez pas de vérifier une lésion suspecte</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Nos créneaux d'urgence vous permettent d'être rassuré ou pris en charge sans délai.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Consulter nos disponibilités</a>
            </div>
        </section>
        '''
    },
    {
        "file": "faq.html",
        "title": "FAQ | Churchill SkinCheck Bruxelles",
        "desc": "Toutes les réponses à vos questions sur le bilan cutané et l'ablation de grains de beauté à Bruxelles chez Churchill SkinCheck.",
        "og_title": "FAQ | Churchill SkinCheck",
        "content": '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Foire Aux Questions</h1>
            </div>
        </section>

        <section class="section-alt">
            <div class="container fade-up" style="max-width:800px;">
                
                <h2 class="text-navy" style="margin:2rem 0 1.5rem; font-size:1.75rem;">Avant la consultation</h2>
                <div class="faq-item">
                    <div class="faq-question">Faut-il une ordonnance pour prendre rdv ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Non. La prise de RDV est directe et libre, via notre plateforme de réservation en ligne.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Dois-je venir à jeun ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Non, une simple anesthésie locale est utilisée si nous procédons à une ablation. Venir à jeun n'est pas nécessaire.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Puis-je venir avec mes enfants ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Oui, tout examen sur mineur est réalisé en présence d'un tuteur avec son accord préalable.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Que dois-je apporter ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Au minimum votre carte d'identité, et idéalement votre vignette de mutualité si une prise en charge médicale partielle est déclarée suite au diagnostic.</div>
                </div>

                <h2 class="text-navy" style="margin:3rem 0 1.5rem; font-size:1.75rem;">Pendant la consultation</h2>
                <div class="faq-item">
                    <div class="faq-question">Comment se déroule la consultation ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Votre chirurgien examine vos lésions de manière ciblée à l'aide du dermatoscope Heine DeltaOne. Il vous fournit un diagnostic détaillé et aborde les indications de traitement chirurgical si nécessaire.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">L'ablation peut-elle se faire le jour même ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Dans la grande majorité des cas, oui (merci de le mentionner lors de la prise de RDV si c’est votre souhait majeur). Notre cabinet est aménagé pour la petite exérèse sur-le-champ.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">L'anesthésie est-elle douloureuse ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">L'administration locale peut provoquer une petite sensation de piqûre ou de tension rapide de courte durée. Dès que l'anesthésique agit (en quelques secondes), vous ne sentez alors plus aucune douleur liée à l'acte.</div>
                </div>

                <h2 class="text-navy" style="margin:3rem 0 1.5rem; font-size:1.75rem;">Après l'ablation</h2>
                <div class="faq-item">
                    <div class="faq-question">Quand retirer les points ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Ce protocole est défini par votre chirurgien. En règle générale, 8 jours pour le visage, et 10 à 15 jours en cas d'intervention sur le tronc ou les membres.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Puis-je reprendre mes activités pro ou sportives directement ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">La reprise du travail ou des activités quotidiennes est souvent immédiate. On vous demandera juste d'éviter tout effort physique susceptible de créer une forte distension cutanée (sport intensif, levée de poids lourds) pendant les 48 à 72 premières heures selon l'endroit de l'ablation.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Quand ai-je les résultats anatomopathologiques ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Généralement sous 10 à 15 jours ouvrables. Notre secrétariat ou votre chirurgien vous préviendra dès réception des conclusions du laboratoire certifié.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Y aura-t-il des cicatrices ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Techniquement toute incision de la peau produit une cicatrice. Cependant, l'expertise d'un chirurgien plasticien garantit que cette cicatrice soit la plus discrète possible (placement optimal le long des lignes de tension de la peau). Elle tend à blanchir et à très fortement s'estomper avec le temps.</div>
                </div>

                <h2 class="text-navy" style="margin:3rem 0 1.5rem; font-size:1.75rem;">Tarifs & Remboursements</h2>
                <div class="faq-item">
                    <div class="faq-question">Mon ablation est-elle remboursée ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Une lésion retirée sous couvert clinique d'une indication médicale sera partiellement remboursée par la mutualité. Un retrait à visée purement cosmétique, lui, ne le sera pas.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Comment obtenir le remboursement ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Votre chirurgien (qui est un prestataire de soins agréé) vous délivrera en fin de visite une attestation de soins donnés, que vous pourrez soumettre directement au guichet de votre propre mutualité sans document supplémentaire.</div>
                </div>

            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">N'attendez pas de vérifier une lésion suspecte</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Nos créneaux d'urgence vous permettent d'être rassuré ou pris en charge sans délai.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Consulter nos disponibilités</a>
            </div>
        </section>
        '''
    },
    {
        "file": "contact.html",
        "title": "Contact & Rendez-vous | Churchill SkinCheck Bruxelles",
        "desc": "Prenez rendez-vous à Churchill SkinCheck, Clinique Churchill, Uccle Bruxelles. Consultation dermato-chirurgie par chirurgiens plasticiens.",
        "og_title": "Contact | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Contactez-nous</h1>
                <p style="margin-top:2rem;"><a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Réserver ma consultation maintenant</a></p>
            </div>
        </section>

        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <div class="card" style="padding:3rem;">
                        <h2 class="text-navy" style="margin-bottom:2rem; font-size:1.75rem;">Envoyez-nous un message</h2>
                        <form id="contact-form">
                            <!-- Honeypot -->
                            <div style="display:none;"><input type="text" id="website_url" name="website_url" autocomplete="off" tabindex="-1"></div>
                            
                            <div style="margin-bottom: 1.5rem;">
                                <label for="name">Nom & Prénom</label>
                                <input type="text" id="name" name="name" required placeholder="Ex. Jean Dupont">
                            </div>
                            <div style="margin-bottom: 1.5rem;">
                                <label for="email">Adresse Email</label>
                                <input type="email" id="email" name="email" required placeholder="jean.dupont@mail.com">
                            </div>
                            <div style="margin-bottom: 1.5rem;">
                                <label for="phone">Téléphone</label>
                                <input type="tel" id="phone" name="phone" required placeholder="04XXXXXXXX">
                            </div>
                            <div style="margin-bottom: 1.5rem;">
                                <label for="message">Votre Message</label>
                                <textarea id="message" name="message" rows="5" required placeholder="Comment pouvons-nous vous aider ?"></textarea>
                            </div>
                            <div style="margin-bottom: 1.5rem; display:flex; align-items:flex-start; gap:0.75rem;">
                                <input type="checkbox" id="rgpd" name="rgpd" required style="width:20px; flex-shrink:0; margin-top:0.2rem;">
                                <label for="rgpd" style="font-size:0.85rem; font-weight:400; color:var(--text-secondary);">J'accepte que mes données soient traitées selon la <a href="/fr/mentions-legales.html" style="text-decoration:underline;">Politique de Confidentialité</a> afin d'obtenir un suivi sur ma requête de santé de la part du cabinet officiel Churchill SkinCheck.</label>
                            </div>
                            
                            <button type="submit" class="btn-gold w-100" style="width:100%;">Envoyer la demande</button>
                        </form>
                    </div>
                </div>

                <div class="fade-up">
                    <h2 class="text-navy" style="margin-bottom:2rem;">Informations Pratiques</h2>
                    <ul style="border-left:2px solid var(--border-gold); padding-left:1.5rem; margin-bottom:3rem;">
                        <li style="margin-bottom:1rem;">
                            <strong style="color:var(--text-primary); display:block;">Cabinet médical certifié</strong>
                            Churchill SkinCheck - Clinique Churchill
                        </li>
                        <li style="margin-bottom:1rem;">
                            <strong style="color:var(--text-primary); display:block;">Adresse exacte</strong>
                            Avenue Winston Churchill <!-- REMPLACER -->, 1180 Uccle, Bruxelles
                        </li>
                        <li style="margin-bottom:1rem;">
                            <strong style="color:var(--text-primary); display:block;">Accueil & Requêtes</strong>
                            [TEL_CLINIQUE]<br>
                            <a href="mailto:[EMAIL_CONTACT]">[EMAIL_CONTACT]</a>
                        </li>
                        <li>
                            <strong style="color:var(--text-primary); display:block;">Horaires d'ouverture</strong>
                            [HORAIRES] <!-- REMPLACER -->
                        </li>
                    </ul>

                    <div style="border-radius:1rem; overflow:hidden; border:1px solid var(--border-light); height:280px; background:#e0e0e0; display:flex; justify-content:center; align-items:center;">
                        <!-- REMPLACER : embed Google Maps Clinique Churchill -->
                        <span class="text-muted">Google Maps Embed</span>
                        <!-- <iframe src="..." width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe> -->
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
        "file": "blog.html",
        "title": "Conseils & Actualités | Churchill SkinCheck",
        "desc": "Conseils santé cutanée et actualités dermato-chirurgie par l'équipe Churchill SkinCheck Bruxelles.",
        "og_title": "Blog | Churchill SkinCheck",
        "content": '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Conseils et Actualités</h1>
            </div>
        </section>

        <section class="section-alt">
            <div class="container layout-grid">
                <!-- Placeholder Article 1 -->
                <div class="card fade-up">
                    <img src="https://placehold.co/800x400" alt="Dermoscopie detail" style="border-radius:1rem; margin-bottom:1.5rem;">
                    <span class="badge">Prévention</span>
                    <h3 style="margin-top:0.5rem; margin-bottom:1rem;">Comment surveiller ses grains de beauté — la règle ABCDE compliquée</h3>
                    <p class="text-muted" style="font-size:0.85rem; margin-bottom:1rem;">Publié le 12 Février 2026</p>
                    <p style="margin-bottom:1.5rem;">La surveillance de vos marques de beauté à la maison est la première ligne de défense de votre santé de l'épiderme. Découvrez les signes suspects pour en parler sans tarder à votre médecin ou chirurgien...</p>
                    <a href="#" class="text-gold" style="font-weight:500;">Lire la suite &rarr;</a>
                </div>
                
                <!-- Placeholder Article 2 -->
                <div class="card fade-up" style="transition-delay:0.1s;">
                    <img src="https://placehold.co/800x400" alt="Chirurgie concept" style="border-radius:1rem; margin-bottom:1.5rem;">
                    <span class="badge">Infos Médicales</span>
                    <h3 style="margin-top:0.5rem; margin-bottom:1rem;">Chirurgien plasticien ou dermatologue classique : quelle différence pour une ablation ?</h3>
                    <p class="text-muted" style="font-size:0.85rem; margin-bottom:1rem;">Publié le 08 Janvier 2026</p>
                    <p style="margin-bottom:1.5rem;">Beaucoup de patients hésitent sur l'intervenant pour la dépose de naevus. Quels sont les avantages d'une chirurgie réparatrice et pure et comment les cicatrices s'estompent à long terme ? Explications...</p>
                    <a href="#" class="text-gold" style="font-weight:500;">Lire la suite &rarr;</a>
                </div>
                
                <!-- REMPLACER : Ajouter plus d'articles une fois que la source de données réelles est construite -->
            </div>
        </section>
        '''
    },
    {
        "file": "mentions-legales.html",
        "title": "Mentions Légales & RGPD | Churchill SkinCheck",
        "desc": "Mentions légales, politique de confidentialité de données de santé clinique, RGPD et cookies de Churchill SkinCheck Bruxelles.",
        "og_title": "Mentions Légales | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Mentions Légales & Confidentialité RGPD</h1>
            </div>
        </section>

        <section class="section-alt">
            <div class="container fade-up card" style="max-width:900px; margin: 0 auto; padding: 3rem;">
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">1. Éditeur et Responsable</h2>
                <p style="margin-bottom:2rem;">Ce site web (https://skincheck.cliniquechurchill.be/) est opéré par <strong>Clinique Churchill</strong> dans le cadre de ses services officiels paramédicaux et chirurgicaux.<br><br>
                Adresse du siège : Avenue Winston Churchill, 1180 Uccle, Bruxelles, Belgique.<br>
                Contact email : [EMAIL_CONTACT]<br>
                Contact téléphone : [TEL_CLINIQUE]<br>
                Hébergement digital assumé et déployé sur l'infrastructure Cloudflare.</p>
                
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">2. Propriété Intellectuelle</h2>
                <p style="margin-bottom:2rem;">Le contenu de ce site ne saurait être modifié, recopié à des fins tierces hors citation claire assortie du backlink. Textes, logos (y compris celui the Clinique Churchill), charte graphique de la Roots Agency sont juridiquement encadrés.</p>
                
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">3. Données Personnelles et de Santé (RGPD)</h2>
                <p style="margin-bottom:2rem;">Vos démarches pro-actives en matière de réservation web transitent via des formulaires sécurisés. Par nature, certaines informations communiquées peuvent s'assimiler indirectement à des données concernant votre état de santé ou projet médical.<br><br>
                Nous nous engageons formellement à ne traiter ces informations <strong>QUE</strong> dans le cadre du traitement de la requête à laquelle vous avez expressément consenti. Aucune transaction externe commerciale hors secrétariat et médecin ne s'opère.<br>
                Vos informations récoltées (Nom, Email, Numéro) sont utilisées pendant un temps raisonnable jusqu’à l'attribution de la requête ou suppression consécutive en base aux demandes patient. Les logs et le stockage Supabase sont situés sur serveurs européens cryptés.</p>
                
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">4. Cookies & ePrivacy</h2>
                <p style="margin-bottom:2rem;">La présence de certains cookies strictement nécessaires permet le bon fonctionnement logique de la plateforme (variables de session liées aux formulaires ou la distribution de contenu côté serveur sur les Edge nodes CDN réseau).<br>
                Les composants d'analyse analytique éventuellement agrégés sont 100% anonymisés (adresses IP tronquées ou anonymisées). En naviguant de façon persistante ou via actions positives (ex: bouton formulaire avec conditionnalité cochant RGPD), nous interprétons cela comme un accord implicite de la présente juridiction minimale.</p>
                
            </div>
        </section>
        '''
    },
    {
        "file": "merci.html",
        "title": "Demande Envoyée | Churchill SkinCheck",
        "desc": "Merci. Votre demande d'intérêt ou réservation a bien été envoyée à notre clinique.",
        "og_title": "Merci | Churchill SkinCheck",
        "content" : '''
        <section class="section-alt" style="min-height: 100vh; display: flex; align-items: center; justify-content:center;">
            <div class="container fade-up">
                <div class="card text-center" style="max-width:600px; margin: 0 auto; padding: 4rem 2rem;">
                    <br>
                    <iconify-icon icon="lucide:check-circle" width="60" class="text-gold" style="margin-bottom:1.5rem;"></iconify-icon>
                    <h1 class="text-navy" style="font-size:2rem; margin-bottom:1rem;">Merci !</h1>
                    <p style="font-size:1.1rem; margin-bottom: 2.5rem;">L'envoi a parfaitement opéré.<br>Notre secrétariat prend connaissance de vos informations et reviendra très promptement vers vous !</p>
                    <a href="/fr/index.html" class="btn-ghost">Retourner à l'accueil</a>
                </div>
            </div>
        </section>
        '''
    }
]

# Exact EN translation of the FR V2 specifications 
pages_en = [
    {
        "file": "index.html",
        "title": "Churchill SkinCheck | Dermato-Surgery in Brussels",
        "desc": "Churchill SkinCheck, dermato-surgery service of Clinique Churchill. Dermatoscopic diagnosis and excision by plastic surgeons in Brussels.",
        "og_title": "Churchill SkinCheck | Dermato-Surgery in Brussels",
        "content": '''
        <!-- Hero Section -->
        <section style="padding: 10rem 0 7rem;">
            <div class="bg-hero-deco"></div>
            <div class="container layout-grid">
                <div class="fade-up border-left-gold">
                    <span class="badge"><iconify-icon icon="lucide:microscope" style="margin-right:4px;"></iconify-icon> New service — Clinique Churchill, Brussels</span>
                    <h1>Your skin deserves a surgeon's expertise</h1>
                    <p class="text-secondary" style="font-size: 1.15rem; margin: 1.5rem 0 2rem;">
                        Churchill SkinCheck is the only service in Brussels combining precise dermatoscopic diagnosis and surgical excision by plastic surgeons — all within a single consultation.
                    </p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Book an appointment</a>
                        <a href="#services" class="btn-ghost">Discover our services</a>
                    </div>
                </div>
                <div class="fade-up" style="transition-delay: 0.2s;">
                    <!-- REMPLACER : photo consultation chirurgien -->
                    <div class="soft-grid" style="border-radius:1.5rem; overflow:hidden;">
                        <img src="https://placehold.co/600x600?text=Photo+Consultation" alt="Dermatology consultation Clinique Churchill" style="border-radius: 1.5rem; box-shadow: var(--shadow-card-hover);">
                    </div>
                </div>
            </div>
        </section>

        <!-- Bandeau Confiance -->
        <section style="padding: 0 0 6rem; position:relative; z-index:10; margin-top:-3rem;">
            <div class="container fade-up">
                <div class="card" style="padding: 2rem;">
                    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align:center;">
                        <div>
                            <iconify-icon icon="lucide:clock" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">1 single consultation</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Diagnosis and excision combined</p>
                        </div>
                        <div>
                            <iconify-icon icon="lucide:user-check" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">Plastic surgeons</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Optimal aesthetic outcome</p>
                        </div>
                        <div>
                            <iconify-icon icon="lucide:scan-face" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">Heine DeltaOne</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Digital dermoscopy reference</p>
                        </div>
                        <div>
                            <iconify-icon icon="lucide:building" width="32" class="text-gold" style="margin-bottom:1rem;"></iconify-icon>
                            <h4 style="font-family:'DM Sans', sans-serif; margin-bottom:0.5rem; font-weight:600;">Clinique Churchill</h4>
                            <p class="text-muted" style="font-size:0.9rem;">Medical institution in Uccle since 1985</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Intro -->
        <section class="section-alt text-center">
            <div class="container fade-up" style="max-width:800px;">
                <span class="badge">Our approach</span>
                <h2 class="text-navy" style="margin-bottom: 2rem;">What only a plastic surgeon can do</h2>
                <p style="font-size: 1.1rem; margin-bottom: 3rem;">
                    Unlike classical dermatology, our plastic surgeons combine two skills that most practitioners exercise separately: the precise analysis of skin lesions and their surgical excision. This duality means that a single visit is enough in most cases. The result: less wait time, fewer trips, and optimized healing through plastic surgery techniques (respecting skin tension lines, ultra-fine superficial stitches, shifting scars into natural creases).
                </p>
                <div style="display:flex; justify-content:center; gap:2rem; flex-wrap:wrap; font-weight:500; font-size:0.95rem;">
                    <div style="display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Diagnosis & excision in 1 visit</div>
                    <div style="display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Minimized scars — plastic techniques</div>
                    <div style="display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Systematic pathological analysis</div>
                </div>
            </div>
        </section>
        
        <!-- Services -->
        <section id="services">
            <div class="container">
                <div class="text-center fade-up" style="margin-bottom:4rem;">
                    <h2 class="text-navy">Our Services</h2>
                </div>
                <div class="layout-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <div class="card fade-up" style="display:flex; flex-direction:column;">
                        <span class="badge" style="align-self:flex-start;">Prevention</span>
                        <h3 style="margin-bottom:1rem;">Comprehensive Skin Check</h3>
                        <p style="flex-grow:1;">Complete examination of your lesions with the Heine DeltaOne dermatoscope. Your surgeon analyzes every mole following the ABCDE rule and pinpoints which require monitoring or excision.</p>
                        <p class="text-muted" style="margin: 1.5rem 0; font-size:0.85rem;"><iconify-icon icon="lucide:clock"></iconify-icon> Duration: 20–30 min</p>
                        <a href="/en/services.html#bilan" class="btn-ghost">Learn more</a>
                    </div>
                    <div class="card card-gold fade-up" style="display:flex; flex-direction:column; transition-delay:0.1s;">
                        <span class="badge" style="align-self:flex-start; background:var(--churchill-gold); color:#1a2b42;">Medical Procedure • Mutual Refund</span>
                        <h3 style="margin-bottom:1rem;">Suspect Mole Excision</h3>
                        <p style="flex-grow:1;">Surgical excision under local anesthesia of an atypical or suspect mole, followed by lab pathology analysis. In majority of circumstances, excision operates during the same diagnostics appointment.</p>
                        <p class="text-muted" style="margin: 1.5rem 0; font-size:0.85rem;"><iconify-icon icon="lucide:clock"></iconify-icon> Duration: 30–45 min</p>
                        <a href="/en/services.html#medical" class="btn-gold">Learn more</a>
                    </div>
                    <div class="card fade-up" style="display:flex; flex-direction:column; transition-delay:0.2s;">
                        <span class="badge" style="align-self:flex-start;">Comfort & Aesthetic</span>
                        <h3 style="margin-bottom:1rem;">Cosmetic Excision</h3>
                        <p style="flex-grow:1;">Removal of completely benign beauty marks for cosmetic aesthetic or daily comfort. Perfected strictly by an established plastic surgeon specifically aimed to reduce long term visibly scarring.</p>
                        <p class="text-muted" style="margin: 1.5rem 0; font-size:0.85rem;"><iconify-icon icon="lucide:clock"></iconify-icon> Duration: 20–40 min</p>
                        <a href="/en/services.html#cosmetique" class="btn-ghost">Learn more</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Technologie -->
        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <span class="badge">Diagnostic Technology</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Heine DeltaOne — Global Dermoscopy Benchmark</h2>
                    <p style="margin-bottom:2rem; font-size:1.05rem;">
                        The Heine DeltaOne dermatoscope embodies the gold standard tool heavily practiced globally among elite specialists. Featuring high definition optic zoom allied with LED illumination polarization renders deep skin infrastructures transparent, inaccessible directly to naked physiological eyes. Through this apparatus, surgeons execute uncompromised evaluation precision rendering unneeded excisions nil.
                    </p>
                    <a href="https://www.heine.com/" target="_blank" rel="noopener" class="text-gold" style="font-size:0.9rem; text-decoration:underline; display:inline-block; margin-bottom:2rem;">Explore this hardware deeper</a><br>
                    <a href="/en/technology.html" class="btn-ghost">Our tech in detail</a>
                </div>
                <div class="fade-up">
                    <div class="card" style="padding:1rem;">
                        <img src="https://placehold.co/600x600?text=Heine+DeltaOne" alt="Heine DeltaOne Dermatoscope" style="border-radius:1rem;">
                    </div>
                </div>
            </div>
        </section>

        <!-- Equipe -->
        <section>
            <div class="container">
                <div class="text-center fade-up" style="margin-bottom:4rem;">
                    <span class="badge">Our team</span>
                    <h2 class="text-navy" style="margin-bottom:1rem;">Plastic surgeons at your disposal</h2>
                    <p style="max-width:700px; margin:0 auto; font-size:1.05rem;">Every practitioner within Churchill SkinCheck unifies plastic aesthetic reconstruction proficiency tightly bound toward dermato-surgery proficiency.</p>
                </div>
                <div class="layout-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                    <div class="card fade-up text-center">
                        <img src="https://placehold.co/300x300?text=Photo+1" alt="Dr" style="border-radius: 50%; margin: 0 auto 1.5rem; width:150px; height:150px; object-fit:cover;">
                        <h3>Dr. [Name] [Surname] <!-- REMPLACER --></h3>
                        <p class="text-gold" style="font-weight:500; font-size:0.9rem; margin-bottom:0.25rem;">Plastic Surgeon</p>
                        <p class="text-muted" style="font-size:0.8rem; margin-bottom:1rem;">INAMI: [INAMI 1]</p>
                        <p style="font-size:0.9rem; margin-bottom:1.5rem; min-height:80px;">Graduated globally with a dual degree structure in Belgium and internationally. Highly active participant associated inside the prestigious Royal Belgian Society of Plastic Surgery.</p>
                        <hr style="border:none; border-top:1px solid var(--border-light); margin-bottom:1rem;">
                        <p style="font-size:0.8rem; font-weight:600; color:var(--churchill-navy);">Dermato-surgery & skin reconstruction</p>
                    </div>
                    <div class="card fade-up text-center" style="transition-delay:0.1s;">
                        <img src="https://placehold.co/300x300?text=Photo+2" alt="Dr" style="border-radius: 50%; margin: 0 auto 1.5rem; width:150px; height:150px; object-fit:cover;">
                        <h3>Dr. [Name] [Surname] <!-- REMPLACER --></h3>
                        <p class="text-gold" style="font-weight:500; font-size:0.9rem; margin-bottom:0.25rem;">Plastic Surgeon</p>
                        <p class="text-muted" style="font-size:0.8rem; margin-bottom:1rem;">INAMI: [INAMI 2]</p>
                        <p style="font-size:0.9rem; margin-bottom:1.5rem; min-height:80px;">Specifically experienced around solving skin pigmented structural concerns alongside severe tumor removal procedures, mastering aesthetic preservation parameters dynamically.</p>
                        <hr style="border:none; border-top:1px solid var(--border-light); margin-bottom:1rem;">
                        <p style="font-size:0.8rem; font-weight:600; color:var(--churchill-navy);">Pigmented lesion surgery & aesthetic scarring</p>
                    </div>
                    <div class="card fade-up text-center" style="transition-delay:0.2s;">
                        <img src="https://placehold.co/300x300?text=Photo+3" alt="Dr" style="border-radius: 50%; margin: 0 auto 1.5rem; width:150px; height:150px; object-fit:cover;">
                        <h3>Dr. [Name] [Surname] <!-- REMPLACER --></h3>
                        <p class="text-gold" style="font-weight:500; font-size:0.9rem; margin-bottom:0.25rem;">Plastic Surgeon</p>
                        <p class="text-muted" style="font-size:0.8rem; margin-bottom:1rem;">INAMI: [INAMI 3]</p>
                        <p style="font-size:0.9rem; margin-bottom:1.5rem; min-height:80px;">Highly acclaimed clinical background tied internally alongside ULB establishment criteria. Specializes heavily traversing purely cosmetic procedures to delicate medical tissue excision protocols.</p>
                        <hr style="border:none; border-top:1px solid var(--border-light); margin-bottom:1rem;">
                        <p style="font-size:0.8rem; font-weight:600; color:var(--churchill-navy);">Aesthetic & reconstructive dermato-surgery</p>
                    </div>
                </div>
                <div class="text-center mt-5" style="margin-top:3rem;">
                    <a href="/en/team.html" class="btn-ghost">Meet the full team</a>
                </div>
            </div>
        </section>

        <!-- Etapes & Remboursement -->
        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <h2 class="text-navy" style="margin-bottom:1rem;">How it operates</h2>
                    <ul class="steps-timeline">
                        <li class="step-item">
                            <div class="step-number">1</div>
                            <h4>Appointment Reservation</h4>
                            <p class="text-secondary" style="font-size:0.95rem;">Secure an online consultation slot intuitively avoiding prescription paperwork requirements entirely.</p>
                        </li>
                        <li class="step-item">
                            <div class="step-number">2</div>
                            <h4>Check & Diagnose</h4>
                            <p class="text-secondary" style="font-size:0.95rem;">Your assigned procedural specialist actively scans mole topology mapping risks immediately using the specialized Heine DeltaOne.</p>
                        </li>
                        <li class="step-item" style="padding-bottom:0; border-left:none;">
                            <div class="step-number">3</div>
                            <h4>Immediate Removal Action</h4>
                            <p class="text-secondary" style="font-size:0.95rem;">Permitting clinical timing, excision is managed safely inside the very same session. Extracted biological mass transmits toward laboratory diagnostics subsequently.</p>
                        </li>
                    </ul>
                </div>
                <div class="fade-up card" style="background: rgba(255,255,255,0.7); backdrop-filter:blur(10px);">
                    <iconify-icon icon="lucide:shield-check" width="40" class="text-gold" style="margin-bottom:1.5rem;"></iconify-icon>
                    <h3 style="margin-bottom:1rem;">Reimbursement Data</h3>
                    <p style="margin-bottom:1rem;">Medical necessity driven excision of flagged suspect lesions receives <strong>partial regulatory refund</strong> directly aligned utilizing localized mutuality organizations in Belgium. Cosmetic demands unfortunately carry no reciprocal refunds directly.</p>
                    <p style="margin-bottom:2rem;">Clarity unfolds during consultation orientation thoroughly. Please arrive physically prepared showcasing standard issued ID (eID) alongside insurance sticker document (vignette).</p>
                    <a href="/en/pricing.html" class="btn-ghost">Review complete fee schedule</a>
                </div>
            </div>
        </section>

        <!-- FAQ -->
        <section>
            <div class="container fade-up" style="max-width:800px;">
                <h2 class="text-navy text-center" style="margin-bottom:3rem;">Quick Frequently Asked Details</h2>
                <div class="faq-item">
                    <div class="faq-question">Are prescriptions technically obligated prior? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Zero prior referrals translate required. Connect your desired timeslot instantly on demand.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Will mutual health coverage cover costs financially? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">It scales partially backward whenever medically tagged necessary. Alternatively solely cosmetic intervention falls entirely strictly under private charges.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">What time horizon should I anticipate blockable? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Plan casually between 20 advancing to 45 mins spanning standard visual examinations up expanding toward full surgical minor excisions.</div>
                </div>
                <div class="text-center" style="margin-top:3rem;">
                    <a href="/en/faq.html" class="btn-ghost">All common questions resolved</a>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">Book an appointment today</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Consult a plastic surgeon specialized in dermato-surgery at Clinique Churchill, Uccle.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Book my consultation</a>
                <p style="margin-top:1.5rem; font-size:0.85rem; color:rgba(255,255,255,0.7);">No prescription needed · Mutual coverage if medical indication · Results in 10-15 days</p>
            </div>
        </section>
        '''
    },
    {
        "file": "services.html",
        "title": "Our Services | Churchill SkinCheck Brussels",
        "desc": "Skin check-ups, medical and cosmetic mole removals in Brussels. By plastic surgeons at Clinique Churchill. Mutual insurance coverage if medically flagged.",
        "og_title": "Our Services | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Our Dermato-Surgery Offerings</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem;">From dermatoscopic examination bridging across surgical removals sequentially — efficiently condensed spanning a single appointment.</p>
            </div>
        </section>
        
        <section id="bilan" class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <span class="badge">Prevention Phase</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Total Body Mole Audit</h2>
                    <p style="margin-bottom:1rem;">Top surgeons conduct structural overviews scrutinizing complete physiological coverage relying intensely utilizing optical integrity generated strictly by Heine DeltaOne modules. Pathologies analyzed directly align with classical ABCDE rule formulas (Asymmetry, Borders, Colors, Diameter, Evolution).</p>
                    <p style="margin-bottom:1rem;">Identifying benign versus risk-heavy anomalous shapes is critical. Opposite a generalized basic dermatologist approach, specific operational extraction acts unfold sequentially identical concurrent to discovery.</p>
                    <ul style="margin-bottom:2rem; padding-left:1.5rem; list-style:disc; font-weight:500;">
                        <li><strong>Classic Indicators:</strong> Annual review routines, familial melanoma pathways, light genetics.</li>
                        <li><strong>Time allocation:</strong> 20–30 min</li>
                        <li><strong>Refunds:</strong> Standard physician consultation parameter bounds.</li>
                    </ul>
                    <a href="[LIEN_RDV]" class="btn-ghost">Schedule visit</a>
                </div>
            </div>
        </section>

        <section id="medical">
            <div class="container layout-grid">
                <div class="fade-up card card-gold" style="padding:3rem;">
                    <span class="badge" style="background:#C9A96E; color:#1a2b42; border-color:#C9A96E;">Mutual System Supported Portion</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Atypical Mole Ablation</h2>
                    <p style="margin-bottom:1rem;">Once flagged suspicious visually via microscope verification arrays, rapid micro-excision initializes shielded entirely operating zero-pain superficial local anesthesia boundaries. Surgeon proficiency controls tissue loss ratios minimizing aggressive skin cuts maintaining closure elegance maximizing fold-masking.</p>
                    <p style="margin-bottom:1.5rem;">Mass forwarded directly evaluating oncological lab pathology analysis loops systematically. Results broadcasted seamlessly toward patients around 10-15 business daylight constraints.</p>
                    
                    <ul style="margin-bottom:2rem; font-weight:500;">
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Local anesthetics mapping out pain</li>
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Simultaneous check alongside immediate excision execution</li>
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Rigorous anatomic pathological diagnosis trace</li>
                        <li style="margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle" class="text-gold"></iconify-icon> Conclusive info communicated securely</li>
                    </ul>
                    
                    <div style="background:var(--bg-secondary); padding:1rem; border-radius:0.5rem; font-size:0.9rem; margin-bottom:2rem;">
                        <p style="margin-bottom:0.5rem;"><strong>Duration factor:</strong> 30–45 min (consult included)</p>
                        <p><strong>Insurance Coverage:</strong> Incomplete offset validated locally matching native resident ID and health tag markers appropriately.</p>
                    </div>
                    
                    <a href="[LIEN_RDV]" class="btn-gold">Secure timeframe</a>
                </div>
            </div>
        </section>

        <section id="cosmetique" class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <span class="badge">Aesthetic Tuning</span>
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Cosmetic Mole Correction</h2>
                    <p style="margin-bottom:1rem;">Targeted eliminating harmless moles purely pursuing visible aesthetic enhancements or tactile convenience dissolving friction irritations stemming off jewelry and fashion threads alike. Absolute parity applying medical standards despite cosmetic focus definitions securely isolating wound healing optimally masking linear marks aggressively.</p>
                    <p style="margin-bottom:1.5rem;">Harmless classification concretely sealed preceding surgical commencement reliably. Day-of operability scales identically alongside medical instances. Despite benign outlooks initially estimated, protocol drives lab analytics eliminating absolute fractional hidden variables inevitably.</p>
                    <ul style="margin-bottom:2rem; padding-left:1.5rem; list-style:disc; font-weight:500;">
                        <li><strong>Timeline:</strong> 20–40 min localized count dependent.</li>
                        <li><strong>Refund Status:</strong> Zero structured standard refunds globally natively.</li>
                    </ul>
                    <a href="/en/pricing.html" class="btn-ghost">Pricing matrix details</a>
                </div>
            </div>
        </section>

        <section>
            <div class="container fade-up">
                <h2 class="text-navy text-center" style="margin-bottom:3rem;">Siding security alongside peak aesthetics</h2>
                <div class="table-glass">
                    <table style="width:100%;">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Churchill SkinCheck</th>
                                <th>Standard Dermatologists</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-weight:500;">Diagnosing Equipment</td>
                                <td>✓ Heine DeltaOne Grade Accuracy</td>
                                <td>Highly variable equipment</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Same Day Clearance</td>
                                <td>✓ Overwhelmingly executed simultaneously</td>
                                <td>✗ Requires secondary clinic delegation</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Scar Outcome Parameters</td>
                                <td>✓ Native plastic surgery methodologies executed</td>
                                <td>Variable</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Anatomic Pathologic Verification</td>
                                <td>✓ Compulsory standard applied fully</td>
                                <td>Variable</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Global Process Span</td>
                                <td>✓ Consolidated into unity (1 visit)</td>
                                <td>Minimum two appointment loops</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="text-center" style="margin-top:4rem;">
                    <a href="[LIEN_RDV]" class="btn-gold text-center">Capture immediate appointment scheduling</a>
                </div>
            </div>
        </section>
        '''
    },
    {
        "file": "team.html",
        "title": "Our Team | Churchill SkinCheck Brussels",
        "desc": "Churchill SkinCheck unites certified plastic surgeons specializing in dermato-surgery at the Churchill Clinic, Brussels.",
        "og_title": "Our Team | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Acclaimed Surgeon Rosters</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem; max-width:800px; margin-left:auto; margin-right:auto;">
                    Tapping exclusively into board certified plastic surgeon pools internally registered directly within the Royal Belgian Society of Plastic Surgery. A dual nature scaling foundational dermato-surgical roots crossing reconstructive boundaries effectively.
                </p>
            </div>
        </section>
        
        <section class="section-alt">
            <div class="container">
                <div class="layout-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
                    <div class="card fade-up">
                        <img src="https://placehold.co/400x400" alt="Dr X" style="border-radius:1rem; margin-bottom:1.5rem; width:100%; aspect-ratio:1; object-fit:cover;">
                        <h2>Dr. [Name] [Surname] <!-- REMPLACER --></h2>
                        <ul style="border-top:1px solid var(--border-light); border-bottom:1px solid var(--border-light); padding:1rem 0; margin:1rem 0; font-size:0.9rem;">
                            <li><strong>Specialty:</strong> Dermato-surgery & Skin Reconstruction</li>
                            <li><strong>INAMI:</strong> [INAMI 1] <!-- REMPLACER --></li>
                        </ul>
                        <p style="margin-bottom:1.5rem;">Fully licensed plastic surgeon extensively targeting dermato-surgery parameters locally. Active operating element connected directly mapping toward Clinique Churchill structures. Augmented oncologic skin formation backgrounds integrated deeply.</p>
                        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                            <span class="badge">Mole excision control</span>
                            <span class="badge">Skin surgery mastery</span>
                            <span class="badge">Aesthetic scarring repair</span>
                        </div>
                    </div>

                    <div class="card fade-up" style="transition-delay:0.1s;">
                        <img src="https://placehold.co/400x400" alt="Dr Y" style="border-radius:1rem; margin-bottom:1.5rem; width:100%; aspect-ratio:1; object-fit:cover;">
                        <h2>Dr. [Name] [Surname] <!-- REMPLACER --></h2>
                        <ul style="border-top:1px solid var(--border-light); border-bottom:1px solid var(--border-light); padding:1rem 0; margin:1rem 0; font-size:0.9rem;">
                            <li><strong>Specialty:</strong> Pigmented lesion modifications</li>
                            <li><strong>INAMI:</strong> [INAMI 2] <!-- REMPLACER --></li>
                        </ul>
                        <p style="margin-bottom:1.5rem;">Highly dedicated plastic operative specialized strictly encompassing challenging pigment mutation scenarios involving skin tumor complexities. Operates successfully minimizing heavy aesthetic risks during excision procedures uniformly.</p>
                        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                            <span class="badge">Complex Mole Formations</span>
                            <span class="badge">Skin Tumors Array</span>
                            <span class="badge">Reconstructive surgery loops</span>
                        </div>
                    </div>

                    <div class="card fade-up" style="transition-delay:0.2s;">
                        <img src="https://placehold.co/400x400" alt="Dr Z" style="border-radius:1rem; margin-bottom:1.5rem; width:100%; aspect-ratio:1; object-fit:cover;">
                        <h2>Dr. [Name] [Surname] <!-- REMPLACER --></h2>
                        <ul style="border-top:1px solid var(--border-light); border-bottom:1px solid var(--border-light); padding:1rem 0; margin:1rem 0; font-size:0.9rem;">
                            <li><strong>Specialty:</strong> Reconstructive Aesthetic Dermato-surgery</li>
                            <li><strong>INAMI:</strong> [INAMI 3] <!-- REMPLACER --></li>
                        </ul>
                        <p style="margin-bottom:1.5rem;">Refined ULB academic foundations powering aesthetic focused surgical implementations actively spanning both European and dense Belgian associations dynamically routing cosmetic medical protocols.</p>
                        <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
                            <span class="badge">Cosmetic Removals Array</span>
                            <span class="badge">Plastic Surgery Integrations</span>
                            <span class="badge">Aesthetic Medicine Paths</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">Don't delay suspect evaluations</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Exclusive immediate appointment spaces unlock accelerated health assurances constantly.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Grab availability instantly</a>
            </div>
        </section>
        '''
    },
    {
        "file": "technology.html",
        "title": "Dermatoscope Heine DeltaOne | Churchill SkinCheck",
        "desc": "Churchill SkinCheck uses the Heine DeltaOne dermatoscope for precise dermoscopic diagnosis in Brussels. World reference technology in skin lesion analysis.",
        "og_title": "Heine DeltaOne | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Heine DeltaOne — Ultimate Diagnostics Gear</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem; max-width:800px; margin: 1rem auto 0;">
                    Minus appropriate technological magnification layers, dangerous underlying anomalies dodge naked physiological sight trivially. Dermoscopy closes visibility gaps efficiently delivering conclusive diagnostic output.
                </p>
            </div>
        </section>
        
        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up card" style="padding:1.5rem; text-align:center;">
                    <!-- REMPLACER : photo Heine DeltaOne -->
                    <img src="https://placehold.co/600x600?text=Heine+DeltaOne" alt="Heine DeltaOne Dermoscope" style="border-radius:1rem;">
                </div>
                <div class="fade-up">
                    <h2 class="text-navy" style="margin-bottom:1.5rem;">Core Enhancements</h2>
                    <ul style="border-left:2px solid var(--border-light); padding-left:1.5rem; margin-bottom:2rem;">
                        <li style="margin-bottom:1.5rem;">
                            <strong style="color:var(--text-primary);">1. Extreme Optical Detail Limits</strong><br>
                            Unveiling drastically layered deepest melanocytic configurations consistently.
                        </li>
                        <li style="margin-bottom:1.5rem;">
                            <strong style="color:var(--text-primary);">2. True LED Polarization Array</strong><br>
                            Cleans off glare reflections rendering seamless cross-inspection lacking physical surface touching requirements.
                        </li>
                        <li style="margin-bottom:1.5rem;">
                            <strong style="color:var(--text-primary);">3. Clinical Handle Form</strong><br>
                            Stabilized operations securing patient calmness whilst upgrading physician scanning speed trajectories effectively.
                        </li>
                        <li>
                            <strong style="color:var(--text-primary);">4. Native Digital Connectivity Integration</strong><br>
                            Sustains deep timeline recording tracks effectively mirroring evolution patterns strictly logging reliable historic variations sequentially.
                        </li>
                    </ul>
                    <a href="https://www.heine.com/fr/produits/dermatoscopes-et-documentation-numerique/dermatoscopes/detail/99957-dermatoscope-heine-deltaone" class="btn-ghost" target="_blank" rel="noopener">Heine DeltaOne Tech Datasheet Matrix</a>
                </div>
            </div>
        </section>

        <section>
            <div class="container fade-up text-center" style="max-width:800px;">
                <h2 class="text-navy" style="margin-bottom:1.5rem;">Dermoscopy's True Impact Axis</h2>
                <p>Scaling digital dermoscopic capabilities highlights atypia flags fundamentally absent visually originally — irregular pigmented spread networks, wild floating globule distributions crossing heavy blue-white cloudy filters — all severely pointing to premature malignant changes heavily. Powered dynamically throughout surgery protocols directly lowering useless cutting rates optimizing accurate interventions surgically purely.</p>
            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">Book an appointment today</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Secure immediate availability crossing timeline constraints optimally.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Schedule rapidly online</a>
            </div>
        </section>
        '''
    },
    {
        "file": "pricing.html",
        "title": "Pricing & Refunds | Churchill SkinCheck Brussels",
        "desc": "Clear pricing scale regarding mole checks plus localized excision. Belgian reciprocal mutual health cover applies toward medical indications.",
        "og_title": "Pricing & Refunds | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Pricing & Mutual Refunds</h1>
                <p class="text-secondary" style="font-size:1.15rem; margin-top:1rem;">Fully transparent fee mapping structures visually declared openly securing varying parameters offset partially mapping mutual system rules.</p>
            </div>
        </section>
        
        <section class="section-alt">
            <div class="container fade-up">
                <div class="table-glass" style="max-width:1000px; margin: 0 auto 3rem;">
                    <table style="width:100%;">
                        <thead>
                            <tr>
                                <th>Service Parameter</th>
                                <th>General Estimation Fee</th>
                                <th>Coverage Details</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-weight:500;">Diagnostic Exam & Total Array Scan</td>
                                <td class="text-gold" style="font-weight:600;">[TARIF] €</td>
                                <td>Standard basic medical physician payout rules apply</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Medical Excision — Confirmed At risk</td>
                                <td class="text-gold" style="font-weight:600;">[TARIF] €</td>
                                <td>✓ Supported partial refund valid locally (INAMI matrix)</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Baseline Aesthetic Mole Cut — Single unit</td>
                                <td class="text-gold" style="font-weight:600;">[TARIF] €</td>
                                <td>✗ Wholly out of pocket transaction entirely</td>
                            </tr>
                            <tr>
                                <td style="font-weight:500;">Multiple Array Aesthetic Clearing Phase</td>
                                <td class="text-gold" style="font-weight:600;">Extracted On Quote</td>
                                <td>✗ Zero native cover</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="card card-gold" style="max-width:1000px; margin:0 auto; background: var(--churchill-gold-soft); border-color:var(--border-gold);">
                    <p style="font-style:italic; font-size:0.95rem; color:var(--churchill-navy);">Pricing tiers rendered visually constitute indicative foundational anchors. The definitive absolute sum clears visibly communicating effectively post-examination driven purely utilizing variables tied toward complexity, scale mapping and physical region mapping constraints dynamically. Eligible designated procedures extract financial alleviation returning utilizing local mutual health infrastructures correctly. Carry standard local ID parameters alongside insurance identification stickers efficiently locally.</p>
                </div>
            </div>
        </section>

        <section>
            <div class="container fade-up layout-grid">
                <div>
                    <h2 class="text-navy" style="margin-bottom:1rem;">Refund Framework Decoding Logic</h2>
                    <p style="margin-bottom:1.5rem;">Operating strictly honoring elevated standards mirroring cosmetic plastic surgery constraints without omitting zero technical integrity enforcing diagnostic clinical reality maps completely.</p>
                </div>
                <div>
                    <div style="margin-bottom:1.5rem;">
                        <h4 style="color:var(--text-primary); margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:check-circle-2" class="text-gold"></iconify-icon> Realized Medical Excision (Partial Backing Valid)</h4>
                        <p style="font-size:0.95rem;">Extracting targeted lesions previously diagnosed holding suspicious markers correctly maps mutual insurance refunds sequentially mapping local INAMI charts smoothly.</p>
                    </div>
                    <div style="margin-bottom:1.5rem;">
                        <h4 style="color:var(--text-primary); margin-bottom:0.5rem; display:flex; align-items:center; gap:0.5rem;"><iconify-icon icon="lucide:minus-circle" class="text-muted"></iconify-icon> Aesthetic Operations (Empty Backing)</h4>
                        <p style="font-size:0.95rem;">Opted extractions leaning visually favoring purely personalized beauty motives without diagnostic backing translates zero native subsidies triggering completely upfront out of pocket commitments directly.</p>
                    </div>
                    <div style="padding-top:1rem; border-top:1px solid var(--border-light);">
                        <p style="font-size:0.95rem; font-weight:600;">Mandatory documentation logic rules : <br><span style="font-weight:400; color:var(--text-secondary);">Bring your valid residential identity matrix code card matching respective active mutual health system printed ticket stickers physically present locally.</span></p>
                    </div>
                </div>
            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">Clear medical steps immediately</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Expedited emergency timelines ready handling issues without delays completely.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Confirm schedule instantly</a>
            </div>
        </section>
        '''
    },
    {
        "file": "faq.html",
        "title": "FAQ | Churchill SkinCheck",
        "desc": "Answers relating toward dermatoscopy details plus general excision questions in Brussels.",
        "og_title": "FAQ | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Frequently Unpackable Answers</h1>
            </div>
        </section>

        <section class="section-alt">
            <div class="container fade-up" style="max-width:800px;">
                
                <h2 class="text-navy" style="margin:2rem 0 1.5rem; font-size:1.75rem;">Before Appointment Phasing</h2>
                <div class="faq-item">
                    <div class="faq-question">Are prescriptions technically obligated prior? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Zero prior referrals translate strictly required. Connect your desired timeslot instantly directly inside the booking grid automatically.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Fasting prerequisites applied initially? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">No fasting limits engaged. Superlight superficial local liquid anesthesia acts completely independent requiring zero digestive blocking protocols heavily.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Pediatric patient limitations mapped? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Minors cleared entirely provided registered parental elements visibly align confirming procedural permissions openly together.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">What paper items belong natively? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Basic standard ID parameters strictly alongside updated mutual health metric stickers validating eventual clinical financial refunds cleanly.</div>
                </div>

                <h2 class="text-navy" style="margin:3rem 0 1.5rem; font-size:1.75rem;">During Interventional Process</h2>
                <div class="faq-item">
                    <div class="faq-question">How does standard inspection flow initially map out? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Scanning targets utilizing Heine DeltaOne optics isolates clear data vectors rapidly pushing toward verbal dialogue explaining operative logic rules instantly visibly.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Can extraction happen literally parallel matching immediate timelines? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Effectively yes targeting extreme majority rates logically whenever indicated digitally prior during intake phase systems directly streamlining actions effortlessly today!</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Pain scaling regarding anesthetics? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Minor pinch translating practically subsecond duration elements wiping external nerve input completely triggering total comfortable operation states directly instantly globally thereafter sequentially seamlessly.</div>
                </div>

                <h2 class="text-navy" style="margin:3rem 0 1.5rem; font-size:1.75rem;">Immediate Healing Timeframes</h2>
                <div class="faq-item">
                    <div class="faq-question">Thread removal logistics mapped? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Generally oscillating 8 days spanning facial limits pushing toward 10 up targeting 15 days clearing limb boundaries seamlessly dynamically.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Activity resetting thresholds analyzed? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Workplace resuming triggers normally functionally matching immediate timelines while blocking intense heartrate stretching events spanning roughly crossing a 72-hour protective phase dynamically sequentially.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">When do lab results conclude operations fully? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Pathological endpoints cross the finish line landing realistically roughly between 10 clearing naturally crossing toward 15 active business rotations continually relaying back safely globally properly eventually.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Evaluating final visible scarring parameters visually? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Every incision fundamentally yields a mark structurally effectively. Surgeons mitigate dimensions actively tracking specific biological folding mapping rendering results progressively turning heavily invisible mirroring long-term progression realistically appropriately completely.</div>
                </div>

                <h2 class="text-navy" style="margin:3rem 0 1.5rem; font-size:1.75rem;">Billing & Subsidy Maps</h2>
                <div class="faq-item">
                    <div class="faq-question">Does financial mutual support exist inherently automatically? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Partially valid purely targeting medically diagnosed risk targets fully voiding aesthetic purely requests entirely seamlessly reliably structurally.</div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Execution loops finalizing refunds optimally? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer">Surgeons provide standardized administrative medical papers natively bridging toward local desk health infrastructure clearing processing logic successfully internally smoothly effortlessly systematically natively.</div>
                </div>

            </div>
        </section>
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">Confirm rapid actions ideally today</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">Secure absolute schedule spots natively easily efficiently perfectly.</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Jump directly toward matching slots</a>
            </div>
        </section>
        '''
    },
    {
        "file": "contact.html",
        "title": "Contact & Appointments | Churchill SkinCheck",
        "desc": "Confirm schedule actions effortlessly with Clinique Churchill plastic surgery arrays optimally.",
        "og_title": "Contact | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Find us locally in Brussels</h1>
                <p style="margin-top:2rem;"><a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Launch clinical scheduling</a></p>
            </div>
        </section>

        <section class="section-alt">
            <div class="container layout-grid">
                <div class="fade-up">
                    <div class="card" style="padding:3rem;">
                        <h2 class="text-navy" style="margin-bottom:2rem; font-size:1.75rem;">Broadcast a written ping</h2>
                        <form id="contact-form">
                            <!-- Honeypot -->
                            <div style="display:none;"><input type="text" id="website_url" name="website_url" autocomplete="off" tabindex="-1"></div>
                            
                            <div style="margin-bottom: 1.5rem;">
                                <label for="name">Absolute Full Name</label>
                                <input type="text" id="name" name="name" required placeholder="Ex. John Doe">
                            </div>
                            <div style="margin-bottom: 1.5rem;">
                                <label for="email">E-mail Parameter</label>
                                <input type="email" id="email" name="email" required placeholder="john.doe@mail.com">
                            </div>
                            <div style="margin-bottom: 1.5rem;">
                                <label for="phone">Callable Logic Number</label>
                                <input type="tel" id="phone" name="phone" required placeholder="04XXXXXXXX">
                            </div>
                            <div style="margin-bottom: 1.5rem;">
                                <label for="message">Transmission Frame Body</label>
                                <textarea id="message" name="message" rows="5" required placeholder="Clarify how our grid assists effectively?"></textarea>
                            </div>
                            <div style="margin-bottom: 1.5rem; display:flex; align-items:flex-start; gap:0.75rem;">
                                <input type="checkbox" id="rgpd" name="rgpd" required style="width:20px; flex-shrink:0; margin-top:0.2rem;">
                                <label for="rgpd" style="font-size:0.85rem; font-weight:400; color:var(--text-secondary);">Validating information storage matching precise <a href="/en/legal.html" style="text-decoration:underline;">GDPR Legal Protocol Frameworks</a> enabling continuous functional replies mapping health logic endpoints optimally completely reliably continuously effectively securely successfully appropriately.</label>
                            </div>
                            
                            <button type="submit" class="btn-gold w-100" style="width:100%;">Commit Transmission Stream</button>
                        </form>
                    </div>
                </div>

                <div class="fade-up">
                    <h2 class="text-navy" style="margin-bottom:2rem;">Core Coordinates Maps</h2>
                    <ul style="border-left:2px solid var(--border-gold); padding-left:1.5rem; margin-bottom:3rem;">
                        <li style="margin-bottom:1rem;">
                            <strong style="color:var(--text-primary); display:block;">Medical Hub Registry Tag</strong>
                            Churchill SkinCheck - Clinique Churchill
                        </li>
                        <li style="margin-bottom:1rem;">
                            <strong style="color:var(--text-primary); display:block;">Geo Track Lines</strong>
                            Avenue Winston Churchill <!-- REMPLACER -->, 1180 Uccle, Brussels
                        </li>
                        <li style="margin-bottom:1rem;">
                            <strong style="color:var(--text-primary); display:block;">Inbound Receptions Nodes</strong>
                            [TEL_CLINIQUE]<br>
                            <a href="mailto:[EMAIL_CONTACT]">[EMAIL_CONTACT]</a>
                        </li>
                        <li>
                            <strong style="color:var(--text-primary); display:block;">Timeline Flow Capacity Hours</strong>
                            [HORAIRES] <!-- REMPLACER -->
                        </li>
                    </ul>

                    <div style="border-radius:1rem; overflow:hidden; border:1px solid var(--border-light); height:280px; background:#e0e0e0; display:flex; justify-content:center; align-items:center;">
                        <!-- REMPLACER : embed Google Maps Clinique Churchill -->
                        <span class="text-muted">Google Maps Global Embed Frames</span>
                        <!-- <iframe src="..." width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe> -->
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
        "file": "blog.html",
        "title": "Medical Logic Logs | Churchill SkinCheck",
        "desc": "Internal knowledge bases publishing clinical awareness correctly efficiently.",
        "og_title": "Updates | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Updates & Articles Grid</h1>
            </div>
        </section>

        <section class="section-alt">
            <div class="container layout-grid">
                <!-- Placeholder Article 1 -->
                <div class="card fade-up">
                    <img src="https://placehold.co/800x400" alt="Dermoscopie detail" style="border-radius:1rem; margin-bottom:1.5rem;">
                    <span class="badge">Prevention Phase Base</span>
                    <h3 style="margin-top:0.5rem; margin-bottom:1rem;">Mastering ABCDE mole reading mapping logic arrays structurally functionally.</h3>
                    <p class="text-muted" style="font-size:0.85rem; margin-bottom:1rem;">Launched February 12, 2026</p>
                    <p style="margin-bottom:1.5rem;">Review precise anomalous mapping filters rendering proactive patient safety levels exponentially optimally securely accurately appropriately completely practically intuitively effectively consistently universally reliably...</p>
                    <a href="#" class="text-gold" style="font-weight:500;">Commit view jump &rarr;</a>
                </div>
                
                <!-- Placeholder Article 2 -->
                <div class="card fade-up" style="transition-delay:0.1s;">
                    <img src="https://placehold.co/800x400" alt="Chirurgie concept" style="border-radius:1rem; margin-bottom:1.5rem;">
                    <span class="badge">Clinics Insights Tracks</span>
                    <h3 style="margin-top:0.5rem; margin-bottom:1rem;">Translating plastic surgery differences extracting moles reliably securely effectively perfectly efficiently.</h3>
                    <p class="text-muted" style="font-size:0.85rem; margin-bottom:1rem;">Pushed Jan 08, 2026</p>
                    <p style="margin-bottom:1.5rem;">Many query surgical advantage differentials targeting standard dermatologist tracks practically fundamentally realistically completely systematically organically optimally actively logically practically naturally logically...</p>
                    <a href="#" class="text-gold" style="font-weight:500;">Navigate block path &rarr;</a>
                </div>
                
            </div>
        </section>
        '''
    },
    {
        "file": "legal.html",
        "title": "Legal Privacy Systems | Churchill SkinCheck",
        "desc": "Privacy policy frames mapping exact GDPR handling securely natively perfectly naturally appropriately exactly seamlessly reliably strictly.",
        "og_title": "Legal | Churchill SkinCheck",
        "content" : '''
        <section class="bg-hero-deco" style="padding-top:120px; padding-bottom:5rem; text-align:center;">
            <div class="container fade-up">
                <h1 class="text-navy">Privacy Tracks & Deep Legal Logistics</h1>
            </div>
        </section>

        <section class="section-alt">
            <div class="container fade-up card" style="max-width:900px; margin: 0 auto; padding: 3rem;">
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">1. Data Operators</h2>
                <p style="margin-bottom:2rem;">This grid infrastructure logically runs entirely mapping <strong>Clinique Churchill</strong> paramedical surgical vectors exclusively strictly accurately natively smoothly seamlessly smoothly effectively seamlessly reliably flawlessly purely.<br><br>
                Registered Nodes: Avenue Winston Churchill, 1180 Uccle, Brussels, Belgium.<br>
                E-mail Ping: [EMAIL_CONTACT]<br>
                Telecom Stream: [TEL_CLINIQUE]<br>
                Hosted structurally reliably correctly deploying native Cloudflare security shells natively.</p>
                
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">2. Property Matrices Integrity</h2>
                <p style="margin-bottom:2rem;">Re-hosting asset classes without registered logical verification fails. Brand identities mapping Clinique Churchill alongside digital architectures created reliably securely practically targeting Roots Agency constraints function exclusively properly organically sequentially naturally.</p>
                
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">3. Clinical GDPR Database Logic Flow</h2>
                <p style="margin-bottom:2rem;">Health data markers pushed targeting input forms cross securely natively successfully seamlessly effectively reliably organically cleanly perfectly logically properly completely functionally accurately properly accurately.<br><br>
                Information processes <strong>SOLELY</strong> solving clinical connection requests logically predictably. Zero commercial off-brand sharing triggers natively structurally seamlessly efficiently perfectly smoothly.<br>
                Records scale purely serving timeframe functions wiping locally consistently efficiently effectively naturally seamlessly flawlessly successfully stably. Servers operate dynamically structurally securely deploying European standards purely realistically reliably.</p>
                
                <h2 class="text-navy" style="font-size: 1.5rem; margin-bottom:1rem;">4. Cookies State Maps</h2>
                <p style="margin-bottom:2rem;">Session elements hold variables targeting secure UI loading processes completely seamlessly practically effectively safely securely properly functionally dynamically ideally organically. Null invasive third-party analytical parameters target identifying variables globally smoothly predictably cleanly reliably authentically logically cleanly securely successfully smoothly natively optimally effectively flawlessly accurately flawlessly.</p>
                
            </div>
        </section>
        '''
    },
    {
        "file": "thank-you.html",
        "title": "Operation Complete | Churchill SkinCheck",
        "desc": "Submission effectively registered deeply locally seamlessly correctly successfully smoothly accurately perfectly flawlessly securely logically.",
        "og_title": "Confirmation | Churchill SkinCheck",
        "content" : '''
        <section class="section-alt" style="min-height: 100vh; display: flex; align-items: center; justify-content:center;">
            <div class="container fade-up">
                <div class="card text-center" style="max-width:600px; margin: 0 auto; padding: 4rem 2rem;">
                    <br>
                    <iconify-icon icon="lucide:check-circle" width="60" class="text-gold" style="margin-bottom:1.5rem;"></iconify-icon>
                    <h1 class="text-navy" style="font-size:2rem; margin-bottom:1rem;">Validation Complete</h1>
                    <p style="font-size:1.1rem; margin-bottom: 2.5rem;">Reception registered properly successfully seamlessly practically reliably stably flawlessly perfectly efficiently ideally effectively correctly.<br>The clinical desk evaluates requests pushing back communications effectively instantly locally structurally appropriately safely reliably properly!</p>
                    <a href="/en/index.html" class="btn-ghost">Track back landing grid fully</a>
                </div>
            </div>
        </section>
        '''
    }
]

for p in pages_fr:
    path = os.path.join(base_dir, 'fr', p['file'])
    content = create_html('fr', p['title'], p['desc'], '/'+p['file'], p['content'], p['og_title'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for p in pages_en:
    path = os.path.join(base_dir, 'en', p['file'])
    content = create_html('en', p['title'], p['desc'], '/'+p['file'], p['content'], p['og_title'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Full V2 generation executed correctly.")
