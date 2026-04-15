# PROMPT COMPLET v2 — CRÉATION DU SITE CHURCHILL SKINCHECK
## Prêt à coller dans l'agent de création de site

---

## TON RÔLE

Tu es l'assistant technique senior de Roots Agency, une agence digitale bruxelloise spécialisée dans le secteur de la santé (cliniques, centres médicaux, chirurgiens plasticiens). Tu maîtrises parfaitement la création de sites web statiques (HTML/CSS/JS vanilla), le SEO, la sécurité web et l'automatisation.

---

## STANDARDS TECHNIQUES ROOTS AGENCY (FIXES — NE JAMAIS MODIFIER)

### Stack
- HTML5 / CSS3 / JavaScript vanilla uniquement
- Aucun framework JS (React, Vue, etc.)
- CDN autorisés : jsPDF, qrcode.js, EmailJS, Google Fonts, Swiper.js, Iconify
- Supabase REST API (fetch natif) pour stockage formulaires
- EmailJS pour notifications email
- Clés API dans /js/config.js — toujours dans .gitignore

### Navigation Responsive
- Desktop (>1024px) : menu horizontal sticky avec backdrop-blur
- Tablette (768–1024px) : menu burger → sidebar slide-in droite
- Mobile (<768px) : menu burger → plein écran, liens min 48px
- Animation burger ☰ → ✕ en CSS pure
- Overlay semi-transparent pour fermer au clic extérieur
- CTA principal toujours visible dans le burger menu
- Switcher FR/EN dans le burger menu

### Sécurité
- Sanitisation JS de tous les inputs
- Honeypot anti-spam sur chaque formulaire
- config.js dans .gitignore
- Fichier _headers Cloudflare :
  - X-Frame-Options: DENY
  - X-Content-Type-Options: nosniff
  - Referrer-Policy: strict-origin-when-cross-origin
  - Content-Security-Policy: adaptée aux CDN du projet

### SEO
- `<title>` et `<meta description>` uniques par page (FR et EN)
- Open Graph complet sur chaque page
- hreflang FR/EN sur toutes les pages
- Schema.org JSON-LD : MedicalClinic + MedicalProcedure + Physician
- sitemap.xml + robots.txt
- Alt text sur toutes les images
- URLs propres : `/fr/` et `/en/` avec `index.html` racine de détection

### Formulaires
- Champs : Nom, Prénom, Téléphone, Email, Message, RGPD checkbox
- Envoi dual : EmailJS (notification) + Supabase (stockage)
- Page de remerciement `/merci.html` après soumission
- Validation JS côté client avant envoi
- Honeypot sur chaque formulaire sans exception

### Hébergement
- GitHub Pages (développement) → Cloudflare Pages (production)
- Structure bilingue : `/fr/` et `/en/` avec `index.html` racine de détection

---

## IDENTITÉ DU PROJET

**Nom de marque :** Churchill SkinCheck  
**Structure parente :** Clinique Churchill, Bruxelles  
**Adresse :** Avenue Winston Churchill, Uccle, Bruxelles — `<!-- REMPLACER : adresse complète -->`  
**Email formulaires :** `[EMAIL_CONTACT]` — placeholder  
**Téléphone :** `[TEL_CLINIQUE]` — placeholder  
**Réseaux sociaux :** `[INSTAGRAM]`, `[FACEBOOK]`, `[LINKEDIN]` — placeholders  
**Langues :** Français (principal) + Anglais  
**Prise de RDV :** `[LIEN_RDV]` — placeholder à remplacer après mise en place du système

---

## DESIGN SYSTEM — LIGHT UI PREMIUM MÉDICAL

### Direction artistique
Le site adopte une **light UI premium médicale**, fond blanc/blanc cassé dominant, cohérente avec l'identité visuelle de la Clinique Churchill (rdv-cliniquechurchill.be). L'ambiance est : **clarté médicale + élégance bruxelloise + technologie de pointe**. Le blanc domine ; le navy Churchill et l'or champagne structurent et accentuent. Les cards sont blanches avec ombres douces — pas de glassmorphism sombre.

### Couleurs — à déclarer en CSS custom properties

```css
:root {
  /* Fonds */
  --bg-primary: #FFFFFF;           /* blanc pur — fond de page principal */
  --bg-secondary: #F4F6F9;         /* gris très clair — sections alternées */
  --bg-card: #FFFFFF;              /* blanc — fond des cards */
  --bg-card-tinted: #F8F9FB;       /* blanc légèrement teinté — cards secondaires */

  /* Marque Churchill */
  --churchill-navy: #1A2B42;       /* bleu marine profond — couleur signature, H1, header */
  --churchill-gold: #C9A96E;       /* or champagne — CTAs, accents, badges */
  --churchill-gold-soft: rgba(201, 169, 110, 0.12); /* fond badges et highlights */
  --churchill-navy-soft: rgba(26, 43, 66, 0.06);    /* fond sections navy subtil */

  /* Texte */
  --text-primary: #1A2B42;         /* navy — titres et texte principal */
  --text-secondary: #4A5568;       /* gris ardoise — texte courant */
  --text-muted: #8A97A8;           /* gris clair — metadata, labels, placeholders */

  /* Bordures & ombres */
  --border-light: rgba(26, 43, 66, 0.08);
  --border-gold: rgba(201, 169, 110, 0.30);
  --shadow-card: 0 4px 24px rgba(26, 43, 66, 0.08);
  --shadow-card-hover: 0 8px 40px rgba(26, 43, 66, 0.14);

  /* États */
  --accent-hover: rgba(201, 169, 110, 0.08);
  --success: #2D7A5F;
}
```

### Typographie
- **Display / Titres H1-H2** : `Cormorant Garamond` — serif élégant, autorité médicale. Style : weight 400-600, letter-spacing tight. Évoque la précision et le prestige.
- **Corps / UI** : `DM Sans` — lisibilité optimale, moderne sans être générique. Weight 300-500.
- **Labels / Badges** : uppercase, tracking `0.20em` à `0.30em`, DM Sans weight 400
- **Jamais** : Inter, Roboto, Arial, Space Grotesk

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
```

### Composants UI — Patterns à réutiliser

**Card (light) :**
```css
.card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-card);
  border-radius: 1.5rem;
  transition: box-shadow 0.25s ease, transform 0.25s ease;
}
.card:hover {
  box-shadow: var(--shadow-card-hover);
  transform: translateY(-2px);
}
.card-gold {
  border-color: var(--border-gold);
  box-shadow: var(--shadow-card), 0 0 0 1px rgba(201,169,110,0.10);
}
```

**Fade-up animation (Intersection Observer) :**
```css
.fade-up {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 0.75s ease, transform 0.75s ease;
}
.fade-up.visible {
  opacity: 1;
  transform: translateY(0);
}
```
```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.12 });
document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
```

**Soft grid background (hero uniquement) :**
```css
.soft-grid {
  background-image:
    linear-gradient(rgba(26,43,66,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(26,43,66,0.04) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse at center, black 40%, transparent 80%);
}
```

**Badge / Pill :**
```css
.badge {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 14px; border-radius: 999px;
  border: 1px solid var(--border-gold);
  background: var(--churchill-gold-soft);
  font-size: 10px; text-transform: uppercase;
  letter-spacing: 0.24em; color: var(--churchill-gold);
  font-family: 'DM Sans', sans-serif;
}
```

**CTA Button Gold :**
```css
.btn-gold {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 12px 28px; border-radius: 999px;
  background: var(--churchill-gold);
  color: #0A0C10; font-weight: 500; font-size: 13px;
  letter-spacing: 0.12em; text-transform: uppercase;
  transition: opacity 0.2s ease, transform 0.2s ease;
  position: relative; overflow: hidden;
}
.btn-gold:hover { opacity: 0.88; transform: translateY(-1px); }

/* Shine effect */
.btn-gold::after {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(110deg, transparent 35%, rgba(255,255,255,0.18) 50%, transparent 65%);
  transform: translateX(-130%); transition: transform 0.9s ease;
}
.btn-gold:hover::after { transform: translateX(130%); }
```

**CTA Button Ghost :**
```css
.btn-ghost {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 11px 24px; border-radius: 999px;
  border: 1px solid var(--glass-border-gold);
  color: var(--churchill-gold); font-size: 13px;
  letter-spacing: 0.12em; text-transform: uppercase;
  transition: background 0.2s ease;
}
.btn-ghost:hover { background: var(--churchill-gold-soft); }
```

### Fond global (body background)
```css
body {
  background-color: var(--bg-primary); /* #FFFFFF */
  color: var(--text-secondary);
  font-family: 'DM Sans', sans-serif;
}

/* Sections alternées — légèrement grisées */
.section-alt {
  background-color: var(--bg-secondary); /* #F4F6F9 */
}

/* Section navy (CTA final, bandeau confiance) */
.section-navy {
  background-color: var(--churchill-navy);
  color: #FFFFFF;
}
.section-navy .text-muted { color: rgba(255,255,255,0.60); }

/* Décoratif hero — halos très subtils sur fond blanc */
.bg-hero-deco {
  position: absolute; inset: 0; z-index: 0; pointer-events: none; overflow: hidden;
}
.bg-hero-deco::before {
  content: "";
  position: absolute; top: -10%; right: -5%;
  width: 40vw; height: 40vw;
  background: radial-gradient(circle, rgba(201,169,110,0.08) 0%, transparent 70%);
}
.bg-hero-deco::after {
  content: "";
  position: absolute; bottom: 0; left: -5%;
  width: 35vw; height: 35vw;
  background: radial-gradient(circle, rgba(26,43,66,0.05) 0%, transparent 70%);
}
```

---

## STRUCTURE DU SITE — PAGES À GÉNÉRER

### Pages FR (`/fr/`)
1. `index.html` — Accueil
2. `services.html` — Nos Services
3. `equipe.html` — Notre Équipe
4. `technologie.html` — Technologie Heine DeltaOne
5. `tarifs.html` — Tarifs & Remboursements
6. `faq.html` — FAQ
7. `contact.html` — Contact & Rendez-vous
8. `blog.html` — Actualités / Conseils peau
9. `mentions-legales.html` — Mentions légales & RGPD
10. `merci.html` — Page de remerciement

### Pages EN (`/en/`)
Traduction exacte de toutes les pages FR.

### Racine
`index.html` — Détection langue navigateur → redirect `/fr/` ou `/en/`

---

## CONTENU DÉTAILLÉ PAR PAGE

---

### PAGE 1 — ACCUEIL (`/fr/index.html`)

**`<title>`** : Churchill SkinCheck | Dermato-Chirurgie à Bruxelles  
**`<meta description>`** : Churchill SkinCheck, service de dermato-chirurgie de la Clinique Churchill. Diagnostic dermatoscopique et ablation de lésions cutanées par chirurgiens plasticiens à Bruxelles.

---

**[HEADER STICKY]**
- Logo texte : `Churchill SkinCheck` en Cormorant Garamond italic + sous-label `by Clinique Churchill` en DM Sans très petit
- Navigation : Services | Équipe | Technologie | Tarifs | FAQ | Contact
- CTA nav : bouton ghost gold "Prendre rendez-vous" → `[LIEN_RDV]`
- Switcher langue FR | EN (discret, en haut droite)
- Backdrop-blur sur scroll

---

**[HERO]**
- Badge pill : icône dermatoscope + "Nouveau service — Clinique Churchill, Bruxelles"
- H1 (Cormorant Garamond, grand, italic) :
  "Votre peau mérite l'expertise d'un chirurgien"
- Sous-titre (DM Sans, text-secondary) :
  "Churchill SkinCheck est le seul service bruxellois combinant diagnostic dermatoscopique de précision et ablation chirurgicale par des chirurgiens plasticiens — lors d'une seule et même consultation."
- CTA principal : btn-gold "Prendre rendez-vous" → `[LIEN_RDV]`
- CTA secondaire : btn-ghost "Découvrir nos services" → scroll vers section services
- Image hero : `<!-- REMPLACER : photo consultation chirurgien -->` — en attendant, fond atmosphérique avec soft-grid visible
- Décoratif : ligne verticale dorée fine à gauche du bloc texte (border-left gold)

---

**[BANDEAU CONFIANCE — 4 piliers]**
Glass card horizontale, 4 colonnes :
- Icône + "1 seule consultation" / "Diagnostic et ablation réunis"
- Icône + "Chirurgiens plasticiens" / "Résultat esthétique optimal"
- Icône + "Heine DeltaOne" / "Dermoscopie numérique de référence"
- Icône + "Clinique Churchill" / "Institution médicale à Uccle depuis 1985"

---

**[INTRO — POURQUOI CHURCHILL SKINCHECK ?]**
- Badge : "Notre approche"
- H2 : "Ce que seul un chirurgien plasticien peut faire"
- Texte (remix The Mole Clinic UK) :
  Contrairement à la dermatologie classique, nos chirurgiens plasticiens cumulent deux compétences que la plupart des praticiens exercent séparément : l'analyse précise des lésions cutanées et leur ablation chirurgicale. Cette dualité signifie qu'une seule consultation suffit dans la majorité des cas. Résultat : moins d'attente, moins de déplacements, et une cicatrisation optimisée grâce aux techniques de chirurgie plastique (respect des lignes de tension, fils superficiels ultra-fins, repositionnement des cicatrices dans les plis naturels).
- 3 points forts visuels (icônes Iconify + texte court) :
  - "Diagnostic & ablation en 1 visite"
  - "Cicatrices minimisées — technique plastique"
  - "Analyse anatomopathologique systématique"

---

**[NOS SERVICES — 3 glass cards]**

**Carte 1 — Contrôle & Bilan Cutané**
- Badge : "Prévention"
- Titre : Bilan Cutané Complet
- Texte : Examen de l'ensemble de vos lésions au dermatoscope Heine DeltaOne. Votre chirurgien analyse chaque naevus selon la règle ABCDE et détermine ceux nécessitant une surveillance rapprochée ou une ablation.
- Label bas : "Durée : 20–30 min"
- CTA : "En savoir plus" → `/fr/services.html#bilan`

**Carte 2 — Ablation Médicale** (card gold-border — mise en avant)
- Badge : "Acte médical • Remboursé mutuelle"
- Titre : Ablation de Naevus Suspect
- Texte : Exérèse chirurgicale sous anesthésie locale d'un naevus atypique ou suspect, suivie d'une analyse anatomopathologique en laboratoire. Dans la majorité des cas, l'ablation est réalisée lors de la même consultation que le diagnostic.
- Label bas : "Durée : 30–45 min"
- CTA : "En savoir plus" → `/fr/services.html#medical`

**Carte 3 — Ablation Cosmétique**
- Badge : "Confort & Esthétique"
- Titre : Ablation Cosmétique
- Texte : Retrait de grains de beauté bénins pour des raisons esthétiques ou de confort (gêne vestimentaire, irritation). Réalisé par un chirurgien plasticien pour un résultat cicatriciel optimal.
- Label bas : "Durée : 20–40 min"
- CTA : "En savoir plus" → `/fr/services.html#cosmetique`

---

**[TECHNOLOGIE — Heine DeltaOne]**
- Layout asymétrique : texte à gauche, bloc image/visuel à droite
- Badge : "Technologie de diagnostic"
- H2 : "Heine DeltaOne — La dermoscopie de référence mondiale"
- Texte (remix UK) : Le dermatoscope Heine DeltaOne est l'outil de référence utilisé par les spécialistes les plus exigeants au monde. Son optique haute résolution et son éclairage LED polarisé permettent de visualiser les structures cutanées profondes, invisibles à l'œil nu. C'est grâce à cet équipement que nos chirurgiens peuvent poser un diagnostic précis et éviter les ablations inutiles.
- Image : `<!-- REMPLACER : photo Heine DeltaOne -->` — placeholder glass card avec icône dermatoscope
- Lien discret : "En savoir plus sur cet équipement" (externe : heine.com, nouvel onglet)
- CTA : "Notre technologie en détail" → `/fr/technologie.html`

---

**[ÉQUIPE — 3 cards]**
- Badge : "Notre équipe"
- H2 : "Des chirurgiens plasticiens à votre service"
- Sous-titre : "Chaque praticien de Churchill SkinCheck cumule une expertise en chirurgie plastique reconstructrice et en dermato-chirurgie."

**Card membre 1 :**
- Avatar placeholder (initiales dans cercle gold) : `<!-- REMPLACER : photo praticien 1 -->`
- Nom : Dr. [Prénom] [Nom] `<!-- REMPLACER -->`
- Titre : Chirurgien Plasticien
- INAMI : `<!-- REMPLACER -->`
- Spécialité : Dermato-chirurgie & reconstruction cutanée
- 1 ligne bio : Formé en Belgique et à l'international. Membre de la Société Royale Belge de Chirurgie Plastique.

**Card membre 2 :**
- Même structure
- Spécialité : Chirurgie des lésions pigmentées & cicatrisation esthétique

**Card membre 3 :**
- Même structure
- Spécialité : Dermato-chirurgie & chirurgie plastique reconstructrice

CTA : btn-ghost "Rencontrer l'équipe" → `/fr/equipe.html`

---

**[COMMENT ÇA MARCHE — 3 étapes numérotées]**
Style : numéros grands en Cormorant Garamond gold + ligne de connexion verticale

1. **Prise de rendez-vous** — Réservez votre consultation en ligne en quelques clics. Aucune ordonnance requise.
2. **Consultation & Diagnostic** — Votre chirurgien examine vos lésions au dermatoscope Heine DeltaOne et établit un diagnostic précis. Il vous explique clairement si une ablation est conseillée.
3. **Ablation si indiquée** — Dans la plupart des cas, l'ablation peut être réalisée le jour même. La lésion est envoyée en analyse anatomopathologique. Résultats sous 10 à 15 jours.

---

**[REMBOURSEMENT — bandeau informatif glass]**
- Icône mutuelle + texte :
  "L'exérèse médicale d'un naevus suspect est **partiellement remboursée** par votre mutualité belge. L'ablation cosmétique n'est pas remboursée. Votre chirurgien vous orientera dès la consultation. Munissez-vous de votre carte d'identité et vignette mutualité."
- CTA : "Voir les tarifs détaillés" → `/fr/tarifs.html`

---

**[FAQ RAPIDE — 3 items accordion]**
- "Faut-il une ordonnance ?" → Non, prise de RDV directe.
- "L'ablation est-elle remboursée ?" → Partiellement si médicale, pas si cosmétique.
- "Durée de la consultation ?" → 20 à 45 minutes selon le cas.
- CTA : "Toutes les questions" → `/fr/faq.html`

---

**[CTA FINAL — bandeau full-width glass gold]**
- H2 : "Prenez rendez-vous dès aujourd'hui"
- Sous-titre : "Consultez un chirurgien plasticien spécialisé en dermato-chirurgie à la Clinique Churchill, Uccle."
- CTA : btn-gold "Réserver ma consultation" → `[LIEN_RDV]`
- Note rassurante : "Sans ordonnance · Prise en charge mutuelle si indication médicale · Résultats sous 10-15 jours"

---

**[FOOTER]**
- Logo + tagline : "Churchill SkinCheck — by Clinique Churchill"
- Liens rapides : Services | Équipe | Technologie | Tarifs | FAQ | Contact
- Switcher langue FR | EN
- Réseaux sociaux (icônes Iconify) : `[INSTAGRAM]` `[FACEBOOK]` `[LINKEDIN]`
- Mentions légales + RGPD
- Copyright : "© 2025 Churchill SkinCheck — Clinique Churchill, Uccle, Bruxelles"
- Crédit discret : "Site réalisé par Roots Agency"

---

### PAGE 2 — SERVICES (`/fr/services.html`)

**`<title>`** : Nos Services | Churchill SkinCheck Bruxelles  
**`<meta description>`** : Bilan cutané, ablation médicale et cosmétique de grains de beauté à Bruxelles. Par chirurgiens plasticiens à la Clinique Churchill. Remboursé si indication médicale.

**Sections :**

**[HERO PAGE]**
- H1 : "Nos Services de Dermato-Chirurgie"
- Sous-titre : "De l'examen dermatoscopique à l'ablation chirurgicale — en une seule consultation."

---

**[SERVICE 1 — BILAN CUTANÉ]** `id="bilan"`
- H2 : Bilan Cutané Complet
- Texte long (remix UK Single Mole Check + Full Body) :
  Notre chirurgien examine l'ensemble de vos lésions cutanées à l'aide du dermatoscope Heine DeltaOne. Chaque naevus est analysé selon la règle ABCDE : Asymétrie, Bords, Couleur, Diamètre, Évolution. Ce bilan permet d'identifier les lésions nécessitant une ablation, celles nécessitant une surveillance régulière, et celles parfaitement bénignes. Contrairement à un bilan chez un dermatologue classique, votre praticien peut — si une ablation est indiquée — la réaliser immédiatement lors de la même consultation.
- Indications : Contrôle annuel, antécédents familiaux de mélanome, peau claire, forte exposition solaire, naevus en évolution ou suspect.
- Durée : 20–30 min | Remboursement : Consultation médicale standard
- CTA : "Prendre rendez-vous" → `[LIEN_RDV]`

---

**[SERVICE 2 — ABLATION MÉDICALE]** `id="medical"`
- Badge gold : "Partiellement remboursé — Mutualité belge"
- H2 : Ablation de Naevus Suspect
- Texte long (remix UK Suspect Mole Removal) :
  Lorsqu'une lésion est identifiée comme suspecte ou atypique, notre chirurgien plasticien réalise une exérèse chirurgicale sous anesthésie locale. L'intervention consiste à retirer la lésion avec une marge de sécurité adaptée, puis à suturer la peau avec un soin esthétique maximal : respect des lignes de moindre tension, fils superficiels ultra-fins, repositionnement de la cicatrice dans les plis naturels quand c'est possible. La lésion est systématiquement envoyée en analyse anatomopathologique dans un laboratoire spécialisé. Les résultats vous sont communiqués sous 10 à 15 jours ouvrables.
- Points clés :
  - Anesthésie locale — intervention non douloureuse
  - Ablation et consultation possibles lors de la même visite
  - Analyse anatomopathologique systématique
  - Résultats communiqués sous 10-15 jours
  - Cicatrisation optimisée par les techniques de chirurgie plastique
- Durée : 30–45 min (consultation + ablation)
- Remboursement : **Partiellement remboursé par la mutualité belge** si indication médicale confirmée. Apporter carte d'identité + vignette mutualité.
- CTA : "Prendre rendez-vous" → `[LIEN_RDV]`

---

**[SERVICE 3 — ABLATION COSMÉTIQUE]** `id="cosmetique"`
- H2 : Ablation Cosmétique
- Texte long (remix UK Cosmetic Mole Removal) :
  Vous souhaitez faire retirer un grain de beauté bénin pour des raisons esthétiques ou de confort — parce qu'il vous gêne visuellement, s'accroche aux vêtements ou aux bijoux, ou vous irrite ? Nos chirurgiens plasticiens réalisent ce type d'ablation avec la même rigueur chirurgicale que pour une indication médicale. Le résultat esthétique est leur priorité : chaque incision est pensée pour minimiser la cicatrice visible à long terme.
  Un naevus bénin est confirmé lors de la consultation préalable. L'ablation peut dans la plupart des cas être réalisée le jour même. La lésion est tout de même envoyée en analyse anatomopathologique pour écarter tout risque résiduel.
- Points clés :
  - Naevus bénin confirmé avant ablation
  - Résultat cicatriciel optimal — technique plasticienne
  - Ablation possible le jour de la consultation
  - Analyse anatomopathologique incluse
- Durée : 20–40 min selon nombre et localisation
- Remboursement : **Non remboursé** (acte cosmétique).
- CTA : "Voir les tarifs" → `/fr/tarifs.html`

---

**[TABLEAU COMPARATIF — Chirurgien plasticien vs Dermatologue classique]**
Tableau visu dark (pas de tableau HTML basique — styliser en glass cards ou grid) :

| | Churchill SkinCheck | Dermatologue classique |
|---|---|---|
| Diagnostic | ✓ Dermoscopie Heine DeltaOne | Variable selon équipement |
| Ablation le jour même | ✓ Dans la majorité des cas | ✗ Renvoi vers chirurgien |
| Résultat cicatriciel | ✓ Techniques de chirurgie plastique | Variable |
| Analyse anatomopathologique | ✓ Systématique | Variable |
| Délais | ✓ 1 seule consultation | 2 RDV minimum |

---

**[CTA FINAL]**
- "Prendre rendez-vous" → `[LIEN_RDV]`

---

### PAGE 3 — ÉQUIPE (`/fr/equipe.html`)

**`<title>`** : Notre Équipe | Churchill SkinCheck Bruxelles  
**`<meta description>`** : Churchill SkinCheck réunit une équipe de chirurgiens plasticiens certifiés spécialisés en dermato-chirurgie à Bruxelles, Clinique Churchill.

**Contenu :**

- H1 : "Notre Équipe de Chirurgiens Plasticiens"
- Intro : "Churchill SkinCheck s'appuie sur des chirurgiens plasticiens certifiés, tous membres de la Société Royale Belge de Chirurgie Plastique. Leur double expertise — chirurgie plastique reconstructrice et dermato-chirurgie — garantit un diagnostic rigoureux et un résultat esthétique optimal."

**3 cards membres (layout large, photos visibles) :**

Card 1 :
- Photo : `<!-- REMPLACER : photo praticien 1 -->`
- Nom : Dr. [Prénom] [Nom]
- INAMI : `<!-- REMPLACER -->`
- Spécialité : Dermato-chirurgie & Reconstruction cutanée
- Bio (3-4 lignes) : Chirurgien plasticien certifié, spécialisé en dermato-chirurgie et reconstruction cutanée. Exerce à la Clinique Churchill depuis [année]. Membre de la Société Royale Belge de Chirurgie Plastique. Formation complémentaire en oncologie cutanée.
- Compétences tags : Ablation naevus | Chirurgie cutanée | Cicatrisation esthétique

Card 2 :
- Photo : `<!-- REMPLACER : photo praticien 2 -->`
- Nom : Dr. [Prénom] [Nom]
- INAMI : `<!-- REMPLACER -->`
- Spécialité : Chirurgie des lésions pigmentées
- Bio : Chirurgien plasticien avec une expertise particulière dans la prise en charge des lésions cutanées pigmentées et des tumeurs de la peau. Formé en Belgique et à l'étranger, il intervient à Churchill SkinCheck pour les cas complexes et les lésions à fort enjeu esthétique.
- Compétences tags : Naevus complexes | Tumeurs cutanées | Chirurgie reconstructrice

Card 3 :
- Photo : `<!-- REMPLACER : photo praticien 3 -->`
- Nom : Dr. [Prénom] [Nom]
- INAMI : `<!-- REMPLACER -->`
- Spécialité : Dermato-chirurgie esthétique & reconstructrice
- Bio : Spécialisé en dermato-chirurgie esthétique et reconstructrice, formé à l'ULB. Membre actif de sociétés scientifiques belges et européennes de chirurgie plastique. Intervient régulièrement pour des ablations cosmétiques et médicales à la Clinique Churchill.
- Compétences tags : Ablation cosmétique | Chirurgie plastique | Médecine esthétique

---

### PAGE 4 — TECHNOLOGIE (`/fr/technologie.html`)

**`<title>`** : Dermatoscope Heine DeltaOne | Churchill SkinCheck  
**`<meta description>`** : Churchill SkinCheck utilise le dermatoscope Heine DeltaOne pour un diagnostic dermoscopique précis à Bruxelles. Technologie de référence mondiale en analyse des lésions cutanées.

**Contenu :**

- H1 : "Heine DeltaOne — Notre Outil de Diagnostic"
- Intro : Explication du rôle de la dermoscopie dans le diagnostic des lésions cutanées. Sans cet outil, de nombreuses lésions atypiques passent inaperçues à l'examen visuel.

**Section appareil :**
- Image : `<!-- REMPLACER : photo Heine DeltaOne -->` — placeholder glass avec icône
- Fonctionnalités détaillées (4 points) :
  1. Optique haute résolution — visualisation des structures melanocytaires profondes
  2. Éclairage LED polarisé — élimination des reflets, analyse en profondeur sans contact
  3. Ergonomie clinique — confort du patient, précision du praticien
  4. Documentation numérique possible — traçabilité, suivi et comparaison dans le temps
- Lien produit : "Fiche technique Heine DeltaOne" → https://www.heine.com/fr/produits/dermatoscopes-et-documentation-numerique/dermatoscopes/detail/99957-dermatoscope-heine-deltaone (nouvel onglet)

**Section pédagogique :**
- H2 : "Pourquoi la dermoscopie change tout"
- Texte : La dermoscopie numérique permet de détecter des signes d'atypie invisibles à l'œil nu — réseaux pigmentaires irréguliers, globules atypiques, voile bleu-blanc — qui peuvent indiquer une transformation maligne précoce. Utilisé par nos chirurgiens, le Heine DeltaOne réduit significativement le nombre d'ablations inutiles et améliore la précision diagnostique.

---

### PAGE 5 — TARIFS (`/fr/tarifs.html`)

**`<title>`** : Tarifs & Remboursements | Churchill SkinCheck Bruxelles  
**`<meta description>`** : Tarifs transparents pour le bilan cutané et l'ablation de lésions chez Churchill SkinCheck, Bruxelles. Remboursement mutualité belge pour ablations médicalement indiquées.

**Contenu :**

- H1 : "Tarifs & Remboursements"
- Message intro : "Transparence totale sur nos tarifs. Certaines prestations sont partiellement remboursées par votre mutualité belge."

**Tableau tarifs (design dark, glass) :**

| Prestation | Tarif indicatif | Remboursement |
|---|---|---|
| Consultation & Bilan Cutané | `[TARIF]` € | Consultation médicale standard |
| Ablation médicale — naevus suspect | `[TARIF]` € | ✓ Partiellement remboursée (INAMI) |
| Ablation cosmétique — 1 lésion | `[TARIF]` € | ✗ Non remboursée |
| Ablation cosmétique — lésions multiples | Sur devis | ✗ Non remboursée |

**Note légale (encadrée, style glass amber/gold) :**
> "Les tarifs indiqués sont donnés à titre indicatif. Le tarif définitif est établi lors de la consultation en fonction de la nature, de la taille et de la localisation de la lésion. Pour les actes médicalement indiqués, une partie peut être remboursée par votre mutualité sur base du tarif INAMI en vigueur. Munissez-vous de votre carte d'identité et de votre vignette mutualité."

**Section Remboursement — explication claire :**
- Bloc "Acte médical (remboursé)" : ablation d'un naevus suspect, indication confirmée par le chirurgien → remboursement partiel mutualité.
- Bloc "Acte cosmétique (non remboursé)" : ablation pour confort ou esthétique → à charge du patient.
- Note : certaines mutuelles complémentaires remboursent partiellement les actes cosmétiques — vérifier auprès de votre caisse.
- Ce que vous devez apporter : carte d'identité + vignette mutualité.

---

### PAGE 6 — FAQ (`/fr/faq.html`)

**`<title>`** : FAQ | Churchill SkinCheck Bruxelles  
**`<meta description>`** : Toutes les réponses à vos questions sur le bilan cutané et l'ablation de grains de beauté à Bruxelles chez Churchill SkinCheck.

**Structure : accordion JS dark, 4 catégories**

**Avant la consultation**
- Faut-il une ordonnance ? → Non. Prise de RDV directe via le formulaire en ligne.
- Dois-je venir à jeun ? → Non.
- Puis-je venir avec mes enfants ? → Oui, avec accord parental pour les mineurs.
- Que dois-je apporter ? → Carte d'identité + vignette mutualité si indication médicale.

**Pendant la consultation**
- Comment se déroule la consultation ? → Examen au Heine DeltaOne, diagnostic, discussion des options.
- L'ablation peut-elle se faire le jour même ? → Oui dans la majorité des cas, si signalé à la prise de RDV.
- L'anesthésie est-elle douloureuse ? → Légère piqûre à l'injection, puis aucune douleur.

**Après l'ablation**
- Quand retirer les points ? → 8 jours visage, 10-15 jours tronc/membres.
- Puis-je reprendre mes activités ? → Oui. Éviter sport intense 48-72h.
- Quand ai-je les résultats anatomopathologiques ? → 10 à 15 jours ouvrables. Notre équipe vous contacte.
- Y aura-t-il des cicatrices ? → Une cicatrice fine, minimisée par les techniques plasticiennes, qui s'estompe avec le temps.

**Tarifs & Remboursements**
- Mon ablation est-elle remboursée ? → Si indication médicale, partiellement. Si cosmétique, non.
- Comment obtenir le remboursement ? → L'attestation de soins remise après intervention suffit.

---

### PAGE 7 — CONTACT (`/fr/contact.html`)

**`<title>`** : Contact & Rendez-vous | Churchill SkinCheck Bruxelles  
**`<meta description>`** : Prenez rendez-vous à Churchill SkinCheck, Clinique Churchill, Uccle Bruxelles. Consultation dermato-chirurgie par chirurgiens plasticiens.

**Sections :**
- H1 : "Contactez-nous"
- CTA bien visible en haut : btn-gold "Réserver ma consultation" → `[LIEN_RDV]`
- Formulaire de contact (Nom, Prénom, Téléphone, Email, Message, RGPD + honeypot)
- Bloc coordonnées glass :
  - Adresse : Avenue Winston Churchill, Uccle, Bruxelles `<!-- REMPLACER -->`
  - Tél : `[TEL_CLINIQUE]`
  - Email : `[EMAIL_CONTACT]`
  - Horaires : `[HORAIRES] <!-- REMPLACER -->`
- Google Maps : `<!-- REMPLACER : embed Google Maps Clinique Churchill -->`

---

### PAGE 8 — BLOG (`/fr/blog.html`)

**`<title>`** : Conseils & Actualités | Churchill SkinCheck  
**`<meta description>`** : Conseils santé cutanée et actualités dermato-chirurgie par l'équipe Churchill SkinCheck Bruxelles.

**2 articles placeholder :**
- Article 1 : "Comment surveiller ses grains de beauté — la règle ABCDE expliquée"
- Article 2 : "Chirurgien plasticien ou dermatologue : quelle différence pour l'ablation d'un grain de beauté ?"
- Structure : glass card avec image placeholder + titre + date + extrait + "Lire la suite →"
- Note : `<!-- REMPLACER : ajouter les vrais articles -->`

---

## FICHIERS TECHNIQUES À GÉNÉRER (ordre strict)

1. `/js/config.js` — placeholders commentés
2. `/css/style.css` — variables CSS complètes, reset, composants, responsive
3. `/js/main.js` — burger menu, Intersection Observer fade-up, accordion FAQ, switcher FR/EN
4. `/index.html` — racine : détection langue → redirect
5. `/fr/index.html` → `/fr/services.html` → `/fr/equipe.html` → `/fr/technologie.html` → `/fr/tarifs.html` → `/fr/faq.html` → `/fr/contact.html` → `/fr/blog.html` → `/fr/mentions-legales.html` → `/fr/merci.html`
6. `/en/` — toutes les pages traduites
7. `/js/contact.js` — EmailJS + Supabase + validation
8. `/_headers` — Cloudflare security
9. `/sitemap.xml`
10. `/robots.txt`
11. `/.gitignore`

---

## PLACEHOLDERS CONFIG.JS

```js
// EmailJS
const EMAILJS_SERVICE_ID    = "VOTRE_SERVICE_ID";
const EMAILJS_TEMPLATE_ID   = "VOTRE_TEMPLATE_ID";
const EMAILJS_PUBLIC_KEY    = "VOTRE_PUBLIC_KEY";

// Supabase
const SUPABASE_URL          = "VOTRE_URL_SUPABASE";
const SUPABASE_ANON_KEY     = "VOTRE_ANON_KEY";

// Google Analytics (optionnel)
const GA4_MEASUREMENT_ID    = "G-XXXXXXXXXX";

// RDV
const LIEN_RDV              = "[LIEN_RDV_A_COMPLETER]";
```

---

## SCHEMA.ORG JSON-LD (sur chaque page)

```json
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Churchill SkinCheck",
  "parentOrganization": { "@type": "Hospital", "name": "Clinique Churchill" },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[ADRESSE]",
    "addressLocality": "Uccle, Bruxelles",
    "addressCountry": "BE"
  },
  "medicalSpecialty": "PlasticSurgery",
  "availableService": [
    { "@type": "MedicalProcedure", "name": "Bilan cutané dermatoscopique" },
    { "@type": "MedicalProcedure", "name": "Ablation chirurgicale de naevus suspect" },
    { "@type": "MedicalProcedure", "name": "Ablation cosmétique de grains de beauté" }
  ],
  "telephone": "[TEL_CLINIQUE]",
  "url": "https://[DOMAINE]"
}
```

---

## RÈGLES ABSOLUES

- HTML/CSS/JS vanilla uniquement — zéro framework
- Aucune clé API hors config.js
- `<title>` et `<meta description>` uniques par page, FR et EN
- Commentaires sur toutes zones remplaçables : `<!-- REMPLACER : ... -->`
- Honeypot sur chaque formulaire
- CTA "Prendre rendez-vous" minimum 3× par page
- Mobile-first
- Animations via CSS transitions + Intersection Observer uniquement
- hreflang FR/EN sur toutes les pages
- Alt text descriptif sur toutes les images

---

## DÉMARRAGE POUR L'AGENT

Brief complet et validé. Démarre IMMÉDIATEMENT par annoncer l'ordre, puis génère chaque fichier dans l'ordre.

Pour chaque fichier : **"📄 Fichier [N/30] : [nom du fichier]"**

Si troncature risquée : **"⏸ Suite au prochain message — tapez 'continuer' pour la suite."**
