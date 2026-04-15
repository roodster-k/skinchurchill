import os
import json

base_dir = "/Users/kei/Desktop/Antigravity x Churchill SkinCheck"

def create_html(lang, title, desc, url_path, content, og_title, og_desc):
    lang_prefix = f"/{lang}/"
    header_nav = f"""
            <nav class="nav-links">
                <a href="{lang_prefix}services.html">Services</a>
                <a href="{lang_prefix}equipe.html">Équipe</a>
                <a href="{lang_prefix}technologie.html">Technologie</a>
                <a href="{lang_prefix}tarifs.html">Tarifs</a>
                <a href="{lang_prefix}faq.html">FAQ</a>
            </nav>
""" if lang == 'fr' else f"""
            <nav class="nav-links">
                <a href="{lang_prefix}services.html">Services</a>
                <a href="{lang_prefix}team.html">Team</a>
                <a href="{lang_prefix}technology.html">Technology</a>
                <a href="{lang_prefix}pricing.html">Pricing</a>
                <a href="{lang_prefix}faq.html">FAQ</a>
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
                        <li><a href="/fr/services.html">Lésions suspectes</a></li>
                        <li><a href="/fr/technologie.html">Le Dermatoscope</a></li>
                        <li><a href="/fr/tarifs.html">Honoraires & Remboursement</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Avenue Winston Churchill [NUMERO]</li>
                        <li>1180 Uccle, Bruxelles</li>
                        <li><a href="mailto:[EMAIL_CONTACT]">[EMAIL_CONTACT]</a></li>
                        <li>[TEL_CLINIQUE]</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; <script>document.write(new Date().getFullYear())</script> Churchill SkinCheck. Tous droits réservés. | <a href="/fr/mentions-legales.html">Mentions légales</a>
            </div>
""" if lang == 'fr' else f"""
                <div class="footer-col" style="justify-self: center;">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="/en/services.html">Suspect Lesions</a></li>
                        <li><a href="/en/technology.html">Dermatoscope</a></li>
                        <li><a href="/en/pricing.html">Fees & Reimbursement</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Avenue Winston Churchill [NUMERO]</li>
                        <li>1180 Uccle, Brussels</li>
                        <li><a href="mailto:[EMAIL_CONTACT]">[EMAIL_CONTACT]</a></li>
                        <li>[TEL_CLINIQUE]</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; <script>document.write(new Date().getFullYear())</script> Churchill SkinCheck. All rights reserved. | <a href="/en/legal.html">Legal Mentions</a>
            </div>
"""

    cta_title = "N'attendez pas de vérifier une lésion suspecte" if lang == 'fr' else "Do not wait to check a suspicious lesion"
    cta_desc = "Nos créneaux d'urgence vous permettent d'être rassuré ou pris en charge sans délai." if lang == 'fr' else "Our emergency slots allow you to be reassured or treated without delay."
    cta_btn = "Consulter nos disponibilités" if lang == 'fr' else "Check availabilities"
    
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
      "image": "https://skincheck.cliniquechurchill.be/assets/logo.png",
      "@id": "",
      "url": "https://skincheck.cliniquechurchill.be",
      "telephone": "[TEL_CLINIQUE]", 
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Avenue Winston Churchill",
        "addressLocality": "Uccle",
        "postalCode": "1180",
        "addressCountry": "BE"
      }}
    }}
    </script>
</head>
<body>

    <!-- Header -->
    <header class="main-header">
        <div class="container nav-container">
            <a href="{lang_prefix}index.html" class="logo">
                <!-- REMPLACER : Logo -->
                <img src="https://placehold.co/150x40?text=Churchill+SkinCheck" alt="Churchill SkinCheck Logo">
            </a>
            
            {header_nav}

            <div class="nav-right">
                <div class="lang-switch">
                    <a href="/fr{url_path.replace('/en/','/')}" class="{ 'active' if lang == 'fr' else '' }">FR</a> | 
                    <a href="/en{url_path.replace('/fr/','/')}" class="{ 'active' if lang == 'en' else '' }">EN</a>
                </div>
                <a href="[LIEN_RDV]" class="btn-gold d-none d-md-inline-flex" target="_blank" rel="noopener">{'RDV Rapide' if lang == 'fr' else 'Quick Appt'}</a>
                <button class="burger-btn" aria-label="Menu">
                    <span class="burger-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        {mobile_nav}
        <div class="mt-4" style="margin-top: 2rem;">
            <a href="[LIEN_RDV]" class="btn-gold w-100" target="_blank" rel="noopener">{'Prendre Rendez-vous' if lang == 'fr' else 'Book Appointment'}</a>
        </div>
    </div>

    <main style="padding-top: 80px;">
        {content}
        
        <!-- CTA Section -->
        <section class="section-navy text-center">
            <div class="container fade-up">
                <h2 style="margin-bottom: 1rem;">{cta_title}</h2>
                <p style="margin-bottom: 2.5rem; font-size: 1.125rem; opacity: 0.9;">{cta_desc}</p>
                <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">{cta_btn}</a>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <img src="https://placehold.co/150x40?text=Logo+White" alt="Churchill SkinCheck" class="footer-logo">
                    <p style="font-size: 0.9rem;">
                        {'Expertise en dermato-chirurgie et diagnostic rapide. Encadré par la Clinique Churchill, Uccle.' if lang == 'fr' else 'Expertise in dermato-surgery and quick diagnosis. Embedded in Clinique Churchill, Uccle.'}
                    </p>
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

def ensure_dir(d):
    path = os.path.join(base_dir, d)
    if not os.path.exists(path):
        os.makedirs(path)

ensure_dir('fr')
ensure_dir('en')

# We'll create the HTML pages for Phase 3 and Phase 4.

pages_fr = [
    {
        "file": "services.html",
        "title": "Nos Services - Churchill SkinCheck",
        "desc": "Découvrez nos services d'évaluation dermatoscopique et d'ablation de lésions suspectes à la Clinique Churchill.",
        "og_title": "Services - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up">
                <h1 class="text-navy" style="margin-bottom: 1rem;">Nos Services</h1>
                <p class="text-secondary" style="font-size: 1.125rem;">Un diagnostic ultra précis et une prise en charge chirurgicale immédiate.</p>
            </div>
        </section>
        <section>
            <div class="container fade-up">
                <div class="soft-grid">
                    <div class="card">
                        <h3>Diagnostic Dermatoscopique</h3>
                        <p>Examen de toute lésion grâce à une optique de très haute résolution.</p>
                        <a href="[LIEN_RDV]" class="btn-ghost" style="margin-top: 1rem;">Prendre RDV</a>
                    </div>
                    <div class="card">
                        <h3>Ablation par Exérèse Chirurgicale</h3>
                        <p>Intervention réalisée sur-le-champ par un chirurgien plasticien en salle dédiée.</p>
                        <a href="[LIEN_RDV]" class="btn-ghost" style="margin-top: 1rem;">Prendre RDV</a>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "equipe.html",
        "title": "L'Équipe - Churchill SkinCheck",
        "desc": "Rencontrez nos chirurgiens plasticiens spécialisés dans le diagnostic et l'exérèse.",
        "og_title": "Équipe - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Notre Équipe Médicale</h1></div>
        </section>
        <section>
            <div class="container fade-up soft-grid">
                <!-- REMPLACER : Photos et infos praticiens -->
                <div class="card text-center">
                    <img src="https://placehold.co/400x400" alt="Dr X" style="border-radius: 50%; margin: 0 auto 1.5rem;">
                    <h3>Dr. [NOM 1]</h3>
                    <p class="badge">Chirurgien Plasticien</p>
                    <p>INAMI : [INAMI 1]</p>
                </div>
                <div class="card text-center">
                    <img src="https://placehold.co/400x400" alt="Dr Y" style="border-radius: 50%; margin: 0 auto 1.5rem;">
                    <h3>Dr. [NOM 2]</h3>
                    <p class="badge">Chirurgien Plasticien</p>
                    <p>INAMI : [INAMI 2]</p>
                </div>
                <div class="card text-center">
                    <img src="https://placehold.co/400x400" alt="Dr Z" style="border-radius: 50%; margin: 0 auto 1.5rem;">
                    <h3>Dr. [NOM 3]</h3>
                    <p class="badge">Chirurgien Plasticien</p>
                    <p>INAMI : [INAMI 3]</p>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "technologie.html",
        "title": "Technologie Heine DeltaOne - Churchill SkinCheck",
        "desc": "L’excellence diagnostique grâce à la technologie Heine DeltaOne.",
        "og_title": "Heine DeltaOne - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Le Dermatoscope Heine DeltaOne</h1></div>
        </section>
        <section>
            <div class="container fade-up soft-grid">
                <div>
                    <!-- REMPLACER : Photo Heine DeltaOne -->
                    <img src="https://placehold.co/500x500" alt="Dermatoscope Heine DeltaOne" style="border-radius: var(--border-radius-md);">
                </div>
                <div>
                    <h2>Une précision optique médicale</h2>
                    <p>Cet outil de diagnostic cutané offre une illumination LED HQ assurant un rendu des couleurs optimal.</p>
                </div>
            </div>
        </section>
        '''
    },
    {
        "file": "tarifs.html",
        "title": "Tarifs & Remboursements - Churchill SkinCheck",
        "desc": "Consultez les informations sur nos honoraires, les actes posés et le potentiel de remboursement par l'INAMI.",
        "og_title": "Tarifs - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Tarifs & Remboursements</h1></div>
        </section>
        <section>
            <div class="container fade-up text-center">
                <h2>Actes posés par des chirurgiens plasticiens</h2>
                <div class="card" style="max-width: 600px; margin: 2rem auto;">
                    <h3>Consultation & Diagnostic</h3>
                    <p class="text-gold" style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">[TARIF]</p>
                    <p class="text-secondary">Des remboursements INAMI et assurances complémentaires peuvent s'appliquer. Ces montants sont indicatifs et dépendent de l'acte précis.</p>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "faq.html",
        "title": "Questions Fréquentes - Churchill SkinCheck",
        "desc": "Découvrez les réponses aux questions fréquentes concernant Churchill SkinCheck.",
        "og_title": "FAQ - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Questions Fréquentes</h1></div>
        </section>
        <section>
            <div class="container fade-up" style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item">
                    <div class="faq-question">Comment se déroule la consultation ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer"><p>Le médecin examine d'abord la lésion avec le dermatoscope. Si l'indication chirurgicale est posée, l'ablation est possible directement.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Est-ce remboursé ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer"><p>Une partie des actes est généralement remboursée par la mutuelle/INAMI selon les tarifs en vigueur.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Qu'est-ce qu'une analyse anatomopathologique ? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer"><p>Toute lésion retirée est envoyée en laboratoire pour une analyse microscopique. C'est une obligation déontologique assurant un diagnostic définitif.</p></div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "contact.html",
        "title": "Contact & Rendez-vous - Churchill SkinCheck",
        "desc": "Prenez contact avec la Clinique Churchill pour un SkinCheck.",
        "og_title": "Contact - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Contactez Churchill SkinCheck</h1></div>
        </section>
        <section>
            <div class="container fade-up soft-grid">
                <div>
                    <h2>Envoyez-nous un message</h2>
                    <form id="contact-form" class="card" style="margin-top: 1.5rem;">
                        <input type="text" id="website_url" name="website_url" style="display:none" tabindex="-1" autocomplete="off">
                        
                        <div style="margin-bottom: 1rem; text-align: left;">
                            <label style="display:block; margin-bottom: 0.5rem; font-weight: 500;">Nom & Prénom</label>
                            <input type="text" name="name" required style="width:100%; padding: 0.8rem; border: 1px solid #ccc; border-radius: 8px;">
                        </div>
                        <div style="margin-bottom: 1rem; text-align: left;">
                            <label style="display:block; margin-bottom: 0.5rem; font-weight: 500;">Email</label>
                            <input type="email" name="email" required style="width:100%; padding: 0.8rem; border: 1px solid #ccc; border-radius: 8px;">
                        </div>
                        <div style="margin-bottom: 1rem; text-align: left;">
                            <label style="display:block; margin-bottom: 0.5rem; font-weight: 500;">Message</label>
                            <textarea name="message" rows="4" required style="width:100%; padding: 0.8rem; border: 1px solid #ccc; border-radius: 8px;"></textarea>
                        </div>
                        <button type="submit" class="btn-gold">Envoyer la demande</button>
                    </form>
                </div>
                <div>
                    <h2>Informations Pratiques</h2>
                    <ul style="list-style:none; line-height:2; margin-top:1.5rem; text-align: left;">
                        <li><strong>Clinique:</strong> Churchill SkinCheck</li>
                        <li><strong>Adresse:</strong> Avenue Winston Churchill [NUMERO], 1180 Uccle, Bruxelles</li>
                        <li><strong>Téléphone:</strong> [TEL_CLINIQUE]</li>
                        <li><strong>Email:</strong> [EMAIL_CONTACT]</li>
                        <li><strong>Horaires:</strong> [HORAIRES]</li>
                    </ul>
                    <!-- REMPLACER : Google Maps -->
                    <div style="margin-top: 2rem; background: #eee; height: 250px; display:flex; align-items:center; justify-content:center; border-radius:12px;">
                        [Google Maps Embed]
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "blog.html",
        "title": "Actualités Médicales - Churchill SkinCheck",
        "desc": "Suivez les actualités médicales et annonces de Churchill SkinCheck.",
        "og_title": "Blog - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Actualités & L'Essentiel</h1></div>
        </section>
        <section>
            <div class="container fade-up text-center">
                <p>Aucun article publié pour le moment. Revenez bientôt !</p>
            </div>
        </section>
        '''
    },
    {
         "file": "mentions-legales.html",
        "title": "Mentions Légales - Churchill SkinCheck",
        "desc": "Mentions légales, politique de confidentialité, RGPD et cookies de Churchill SkinCheck.",
        "og_title": "Mentions Légales - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Mentions Légales & RGPD</h1></div>
        </section>
        <section>
            <div class="container fade-up" style="max-width: 800px; margin: 0 auto; text-align: left;">
                <h2>1. Responsable du traitement</h2>
                <p>La Clinique Churchill, Avenue Winston Churchill, 1180 Uccle, Belgique.</p>
                <h2 style="margin-top: 2rem;">2. Cookies & ePrivacy</h2>
                <p>Ce site n'utilise que des cookies strictement nécessaires et des outils d'analyse anonymisés.</p>
                <h2 style="margin-top: 2rem;">3. Données de santé</h2>
                <p>Vos données envoyées via le formulaire sont traitées en toute confidentialité.</p>
            </div>
        </section>
        '''
    },
    {
         "file": "merci.html",
        "title": "Merci ! - Churchill SkinCheck",
        "desc": "Merci pour votre demande.",
        "og_title": "Merci - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center" style="min-height: 50vh; display: flex; align-items: center;">
            <div class="container fade-up">
                <iconify-icon icon="lucide:check-circle" width="64" class="text-gold" style="margin-bottom: 1rem;"></iconify-icon>
                <h1 class="text-navy">Merci de nous avoir contacté</h1>
                <p class="text-secondary" style="font-size: 1.125rem;">Nous avons bien reçu votre demande et vous répondrons très rapidement.</p>
                <br>
                <a href="/fr/index.html" class="btn-ghost" style="margin-top: 1rem;">Retourner à l'accueil</a>
            </div>
        </section>
        '''
    }
]

pages_en = [
    {
         "file": "index.html",
        "title": "Churchill SkinCheck - Excision & Dermato-surgery in Brussels",
        "desc": "Quick treatment of your skin lesions in Brussels. Dermatoscopic diagnosis and surgical excision in one consultation by plastic surgeons.",
        "og_title": "Churchill SkinCheck - One-stop Dermato-surgery",
        "content": '''
        <!-- Hero Section -->
        <section class="bg-hero-deco" style="padding-top: 70px;">
            <div class="container soft-grid">
                <div class="fade-up">
                    <span class="badge">Quick Consultation</span>
                    <h1>Diagnosis & excision in one single step</h1>
                    <p class="text-secondary" style="font-size: 1.125rem; margin: 1.5rem 0 2rem;">
                        Our center, supervised by plastic surgeons, offers you a dermatoscopic evaluation followed by the immediate removal of your suspicious lesion, if necessary.
                    </p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="[LIEN_RDV]" class="btn-gold" target="_blank" rel="noopener">Book an appointment</a>
                        <a href="#concept" class="btn-ghost">Discover the concept</a>
                    </div>
                </div>
                <div class="fade-up" style="transition-delay: 0.2s;">
                    <!-- REMPLACER : Photo consultation hero -->
                    <img src="https://placehold.co/600x600?text=Consultation+Photo" alt="Dermatology consultation Clinique Churchill" style="border-radius: var(--border-radius-md); box-shadow: var(--shadow-hover);">
                </div>
            </div>
        </section>

        <!-- Concept Section -->
        <section id="concept" class="bg-secondary">
            <div class="container text-center fade-up">
                <h2 class="text-navy" style="margin-bottom: 3rem;">The Churchill SkinCheck Advantage</h2>
                <div class="soft-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; text-align: left;">
                    <div class="card">
                        <iconify-icon icon="lucide:check-circle" width="32" class="text-gold" style="margin-bottom: 1rem;"></iconify-icon>
                        <h3>One-Stop Service</h3>
                        <p>No more endless delays between diagnosis and intervention. We perform the assessment and excision during the same visit.</p>
                    </div>
                    <div class="card">
                        <iconify-icon icon="lucide:microscope" width="32" class="text-gold" style="margin-bottom: 1rem;"></iconify-icon>
                        <h3>Heine Technology</h3>
                        <p>We use the cutting-edge Heine DeltaOne dermatoscope, ensuring exceptional diagnostic accuracy.</p>
                    </div>
                    <div class="card">
                        <iconify-icon icon="lucide:shield" width="32" class="text-gold" style="margin-bottom: 1rem;"></iconify-icon>
                        <h3>Surgical Expertise</h3>
                        <p>Excisions are performed by plastic surgeons, ensuring a safe procedure and optimizing scar quality.</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "services.html",
        "title": "Our Services - Churchill SkinCheck",
        "desc": "Discover our dermatoscopic evaluation and suspicious lesion excision services at Clinique Churchill.",
        "og_title": "Services - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up">
                <h1 class="text-navy" style="margin-bottom: 1rem;">Our Services</h1>
                <p class="text-secondary" style="font-size: 1.125rem;">Ultra-precise diagnosis and immediate surgical care.</p>
            </div>
        </section>
        <section>
            <div class="container fade-up">
                <div class="soft-grid">
                    <div class="card">
                        <h3>Dermatoscopic Diagnosis</h3>
                        <p>Examination of any lesion with high-resolution optics.</p>
                        <a href="[LIEN_RDV]" class="btn-ghost" style="margin-top: 1rem;">Book Appt</a>
                    </div>
                    <div class="card">
                        <h3>Surgical Excision</h3>
                        <p>Intervention performed on the spot by a plastic surgeon in a dedicated room.</p>
                        <a href="[LIEN_RDV]" class="btn-ghost" style="margin-top: 1rem;">Book Appt</a>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "team.html",
        "title": "The Team - Churchill SkinCheck",
        "desc": "Meet our plastic surgeons specializing in diagnosis and excision.",
        "og_title": "Team - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Our Medical Team</h1></div>
        </section>
        <section>
            <div class="container fade-up soft-grid">
                <!-- REMPLACER : Photos et infos praticiens -->
                <div class="card text-center">
                    <img src="https://placehold.co/400x400" alt="Dr X" style="border-radius: 50%; margin: 0 auto 1.5rem;">
                    <h3>Dr. [NAME 1]</h3>
                    <p class="badge">Plastic Surgeon</p>
                    <p>INAMI: [INAMI 1]</p>
                </div>
                <div class="card text-center">
                    <img src="https://placehold.co/400x400" alt="Dr Y" style="border-radius: 50%; margin: 0 auto 1.5rem;">
                    <h3>Dr. [NAME 2]</h3>
                    <p class="badge">Plastic Surgeon</p>
                    <p>INAMI: [INAMI 2]</p>
                </div>
                <div class="card text-center">
                    <img src="https://placehold.co/400x400" alt="Dr Z" style="border-radius: 50%; margin: 0 auto 1.5rem;">
                    <h3>Dr. [NAME 3]</h3>
                    <p class="badge">Plastic Surgeon</p>
                    <p>INAMI: [INAMI 3]</p>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "technology.html",
        "title": "Heine DeltaOne Technology - Churchill SkinCheck",
        "desc": "Diagnostic excellence thanks to the Heine DeltaOne technology.",
        "og_title": "Heine DeltaOne - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>The Heine DeltaOne Dermatoscope</h1></div>
        </section>
        <section>
            <div class="container fade-up soft-grid">
                <div>
                    <!-- REMPLACER : Photo Heine DeltaOne -->
                    <img src="https://placehold.co/500x500" alt="Dermatoscope Heine DeltaOne" style="border-radius: var(--border-radius-md);">
                </div>
                <div>
                    <h2>Medical optical precision</h2>
                    <p>This diagnostic tool offers LED HQ illumination ensuring optimal color rendering.</p>
                </div>
            </div>
        </section>
        '''
    },
    {
        "file": "pricing.html",
        "title": "Pricing & Reimbursement - Churchill SkinCheck",
        "desc": "Check information on our fees, acts performed, and INAMI reimbursement details.",
        "og_title": "Pricing - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Pricing & Reimbursement</h1></div>
        </section>
        <section>
            <div class="container fade-up text-center">
                <h2>Procedures by plastic surgeons</h2>
                <div class="card" style="max-width: 600px; margin: 2rem auto;">
                    <h3>Consultation & Diagnosis</h3>
                    <p class="text-gold" style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">[PRICING]</p>
                    <p class="text-secondary">INAMI reimbursements and complementary insurances may apply. These amounts are indicative.</p>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "faq.html",
        "title": "Frequently Asked Questions - Churchill SkinCheck",
        "desc": "Discover answers to frequently asked questions about Churchill SkinCheck.",
        "og_title": "FAQ - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Frequently Asked Questions</h1></div>
        </section>
        <section>
            <div class="container fade-up" style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item">
                    <div class="faq-question">How does the consultation work? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer"><p>The doctor examines the lesion. If there is a surgical indication, removal can be done directly.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">Is it reimbursed? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer"><p>A portion of the fees is generally reimbursed by mutual insurance according to rates in force.</p></div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">What is a pathological analysis? <iconify-icon icon="lucide:chevron-down"></iconify-icon></div>
                    <div class="faq-answer"><p>Any removed lesion is sent to a laboratory for microscopic analysis to ensure a definitive diagnosis.</p></div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "contact.html",
        "title": "Contact & Appointment - Churchill SkinCheck",
        "desc": "Get in touch with Clinique Churchill for a SkinCheck.",
        "og_title": "Contact - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Contact Churchill SkinCheck</h1></div>
        </section>
        <section>
            <div class="container fade-up soft-grid">
                <div>
                    <h2>Send us a message</h2>
                    <form id="contact-form" class="card" style="margin-top: 1.5rem;">
                        <input type="text" id="website_url" name="website_url" style="display:none" tabindex="-1" autocomplete="off">
                        
                        <div style="margin-bottom: 1rem; text-align: left;">
                            <label style="display:block; margin-bottom: 0.5rem; font-weight: 500;">Full Name</label>
                            <input type="text" name="name" required style="width:100%; padding: 0.8rem; border: 1px solid #ccc; border-radius: 8px;">
                        </div>
                        <div style="margin-bottom: 1rem; text-align: left;">
                            <label style="display:block; margin-bottom: 0.5rem; font-weight: 500;">Email</label>
                            <input type="email" name="email" required style="width:100%; padding: 0.8rem; border: 1px solid #ccc; border-radius: 8px;">
                        </div>
                        <div style="margin-bottom: 1rem; text-align: left;">
                            <label style="display:block; margin-bottom: 0.5rem; font-weight: 500;">Message</label>
                            <textarea name="message" rows="4" required style="width:100%; padding: 0.8rem; border: 1px solid #ccc; border-radius: 8px;"></textarea>
                        </div>
                        <button type="submit" class="btn-gold">Send request</button>
                    </form>
                </div>
                <div>
                    <h2>Practical Information</h2>
                    <ul style="list-style:none; line-height:2; margin-top:1.5rem; text-align: left;">
                        <li><strong>Clinic:</strong> Churchill SkinCheck</li>
                        <li><strong>Address:</strong> Avenue Winston Churchill [NUMERO], 1180 Uccle, Brussels</li>
                        <li><strong>Phone:</strong> [TEL_CLINIQUE]</li>
                        <li><strong>Email:</strong> [EMAIL_CONTACT]</li>
                        <li><strong>Hours:</strong> [HORAIRES]</li>
                    </ul>
                    <!-- REMPLACER : Google Maps -->
                    <div style="margin-top: 2rem; background: #eee; height: 250px; display:flex; align-items:center; justify-content:center; border-radius:12px;">
                        [Google Maps Embed]
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    {
         "file": "blog.html",
        "title": "Medical News - Churchill SkinCheck",
        "desc": "Follow medical news and announcements from Churchill SkinCheck.",
        "og_title": "Blog - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>News & Updates</h1></div>
        </section>
        <section>
            <div class="container fade-up text-center">
                <p>No articles published yet. Check back soon!</p>
            </div>
        </section>
        '''
    },
    {
         "file": "legal.html",
        "title": "Legal Mentions - Churchill SkinCheck",
        "desc": "Legal mentions, privacy policy, GDPR and cookies of Churchill SkinCheck.",
        "og_title": "Legal - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center">
            <div class="container fade-up"><h1>Legal & Privacy Policy</h1></div>
        </section>
        <section>
            <div class="container fade-up" style="max-width: 800px; margin: 0 auto; text-align: left;">
                <h2>1. Data Controller</h2>
                <p>Clinique Churchill, Avenue Winston Churchill, 1180 Uccle, Belgium.</p>
                <h2 style="margin-top: 2rem;">2. Cookies & ePrivacy</h2>
                <p>This site only uses strictly necessary cookies and anonymized analytics tools.</p>
                <h2 style="margin-top: 2rem;">3. Health Data</h2>
                <p>Your data sent via the form is treated with strict confidentiality.</p>
            </div>
        </section>
        '''
    },
    {
         "file": "thank-you.html",
        "title": "Thank You ! - Churchill SkinCheck",
        "desc": "Thank you for your request.",
        "og_title": "Thank You - Churchill SkinCheck",
        "content": '''
        <section class="bg-secondary text-center" style="min-height: 50vh; display: flex; align-items: center;">
            <div class="container fade-up">
                <iconify-icon icon="lucide:check-circle" width="64" class="text-gold" style="margin-bottom: 1rem;"></iconify-icon>
                <h1 class="text-navy">Thank You for Contacting Us</h1>
                <p class="text-secondary" style="font-size: 1.125rem;">We have received your request and will reply shortly.</p>
                <br>
                <a href="/en/index.html" class="btn-ghost" style="margin-top: 1rem;">Return Home</a>
            </div>
        </section>
        '''
    }
]

for p in pages_fr:
    path = os.path.join(base_dir, 'fr', p['file'])
    content = create_html('fr', p['title'], p['desc'], '/'+p['file'], p['content'], p['og_title'], p['desc'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for p in pages_en:
    path = os.path.join(base_dir, 'en', p['file'])
    content = create_html('en', p['title'], p['desc'], '/'+p['file'], p['content'], p['og_title'], p['desc'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Files generated successfully.")
