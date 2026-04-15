# Churchill SkinCheck — Contexte Projet & Marche à Suivre

**Agence :** Roots Agency  
**Client :** Clinique Churchill (Uccle, Bruxelles)  
**Produit :** Churchill SkinCheck — service de dermato-chirurgie  
**Date de démarrage :** 2026-04-15  
**Source :** `churchill-skincheck-prompt-v2.md`

---

## 1. Vue d'ensemble du projet

Site web statique bilingue (FR/EN) pour Churchill SkinCheck, un service de dermato-chirurgie de la Clinique Churchill à Bruxelles. Le site positionne l'offre autour de la différenciation clé : **diagnostic dermatoscopique + ablation chirurgicale en une seule consultation**, réalisés par des chirurgiens plasticiens.

### Stack technique
- HTML5 / CSS3 / JavaScript vanilla (zéro framework)
- CDN : Google Fonts, Iconify, EmailJS, jsPDF, qrcode.js, Swiper.js
- Backend : Supabase REST API (formulaires) + EmailJS (notifications)
- Hébergement : GitHub Pages (dev) → Cloudflare Pages (prod)

---

## 2. Structure de fichiers à générer (30 fichiers)

### Fichiers techniques (racine)
| # | Fichier | Statut |
|---|---------|--------|
| 1 | `/js/config.js` | ⬜ À faire |
| 2 | `/css/style.css` | ⬜ À faire |
| 3 | `/js/main.js` | ⬜ À faire |
| 4 | `/js/contact.js` | ⬜ À faire |
| 5 | `/index.html` (redirect racine) | ⬜ À faire |
| 6 | `/_headers` (Cloudflare) | ⬜ À faire |
| 7 | `/sitemap.xml` | ⬜ À faire |
| 8 | `/robots.txt` | ⬜ À faire |
| 9 | `/.gitignore` | ⬜ À faire |

### Pages FR (`/fr/`)
| # | Fichier | Statut |
|---|---------|--------|
| 10 | `/fr/index.html` — Accueil | ⬜ À faire |
| 11 | `/fr/services.html` — Services | ⬜ À faire |
| 12 | `/fr/equipe.html` — Équipe | ⬜ À faire |
| 13 | `/fr/technologie.html` — Heine DeltaOne | ⬜ À faire |
| 14 | `/fr/tarifs.html` — Tarifs & Remboursements | ⬜ À faire |
| 15 | `/fr/faq.html` — FAQ | ⬜ À faire |
| 16 | `/fr/contact.html` — Contact & RDV | ⬜ À faire |
| 17 | `/fr/blog.html` — Actualités | ⬜ À faire |
| 18 | `/fr/mentions-legales.html` — RGPD | ⬜ À faire |
| 19 | `/fr/merci.html` — Page de remerciement | ⬜ À faire |

### Pages EN (`/en/`)
| # | Fichier | Statut |
|---|---------|--------|
| 20 | `/en/index.html` — Home | ⬜ À faire |
| 21 | `/en/services.html` — Services | ⬜ À faire |
| 22 | `/en/team.html` — Team | ⬜ À faire |
| 23 | `/en/technology.html` — Heine DeltaOne | ⬜ À faire |
| 24 | `/en/pricing.html` — Pricing | ⬜ À faire |
| 25 | `/en/faq.html` — FAQ | ⬜ À faire |
| 26 | `/en/contact.html` — Contact | ⬜ À faire |
| 27 | `/en/blog.html` — News | ⬜ À faire |
| 28 | `/en/legal.html` — Legal & GDPR | ⬜ À faire |
| 29 | `/en/thank-you.html` — Thank you | ⬜ À faire |

---

## 3. Marche à suivre — Ordre de génération recommandé

### Phase 1 — Fondations (fichiers partagés)
1. **`/js/config.js`** — Placeholders API (EmailJS, Supabase, GA4, LIEN_RDV)
2. **`/css/style.css`** — Variables CSS, reset, tous les composants (cards, buttons, badges, animations, responsive)
3. **`/js/main.js`** — Burger menu, Intersection Observer, accordion FAQ, switcher FR/EN
4. **`/js/contact.js`** — Validation, honeypot, envoi EmailJS + Supabase

### Phase 2 — Structure racine
5. **`/index.html`** — Détection langue navigateur → redirect `/fr/` ou `/en/`
6. **`/.gitignore`** — Inclut `config.js`
7. **`/_headers`** — CSP Cloudflare + headers sécurité

### Phase 3 — Pages FR (dans l'ordre)
8. `/fr/index.html` — Accueil (page la plus complexe, référence pour les autres)
9. `/fr/services.html`
10. `/fr/equipe.html`
11. `/fr/technologie.html`
12. `/fr/tarifs.html`
13. `/fr/faq.html`
14. `/fr/contact.html`
15. `/fr/blog.html`
16. `/fr/mentions-legales.html`
17. `/fr/merci.html`

### Phase 4 — Pages EN (traductions)
18–27. Toutes les pages `/en/` — traduction fidèle avec adaptation `<title>`, `<meta>`, hreflang

### Phase 5 — SEO & déploiement
28. `/sitemap.xml` — Toutes les URLs FR + EN
29. `/robots.txt`

---

## 4. Design System — Rappel clés

### Couleurs principales
| Variable | Valeur | Usage |
|----------|--------|-------|
| `--churchill-navy` | `#1A2B42` | Titres, header, H1 |
| `--churchill-gold` | `#C9A96E` | CTAs, accents, badges |
| `--bg-primary` | `#FFFFFF` | Fond de page |
| `--bg-secondary` | `#F4F6F9` | Sections alternées |
| `--text-secondary` | `#4A5568` | Corps de texte |

### Typographie
- **Titres** : `Cormorant Garamond` (serif, 400–600)
- **Corps/UI** : `DM Sans` (sans-serif, 300–500)
- Jamais : Inter, Roboto, Arial, Space Grotesk

### Composants obligatoires
- Cards light avec ombre douce + hover lift
- `.fade-up` via Intersection Observer
- `.soft-grid` (hero uniquement)
- `.badge` pill gold
- `.btn-gold` avec shine effect
- `.btn-ghost` contour gold
- `section-navy` pour CTA finaux
- Halos décoratifs hero (`.bg-hero-deco`)

### Navigation responsive
- Desktop >1024px : menu horizontal sticky + backdrop-blur
- Tablette 768–1024px : burger → sidebar droite
- Mobile <768px : burger → plein écran, liens 48px min
- Switcher FR/EN dans burger menu
- CTA RDV toujours visible

---

## 5. Standards qualité — Checklist par page

Chaque page HTML doit avoir :
- [ ] `<title>` unique (FR ou EN)
- [ ] `<meta description>` unique
- [ ] Open Graph complet (og:title, og:description, og:url, og:image)
- [ ] hreflang FR/EN
- [ ] Schema.org JSON-LD (MedicalClinic)
- [ ] Alt text sur toutes les images
- [ ] CTA "Prendre rendez-vous" ≥ 3× par page
- [ ] Honeypot sur tout formulaire
- [ ] Commentaires `<!-- REMPLACER : ... -->` sur les zones à compléter

---

## 6. Placeholders à remplacer par le client

| Placeholder | Description |
|-------------|-------------|
| `[LIEN_RDV]` | URL du système de réservation en ligne |
| `[EMAIL_CONTACT]` | Email de contact du service |
| `[TEL_CLINIQUE]` | Numéro de téléphone |
| `[INSTAGRAM]` | URL profil Instagram |
| `[FACEBOOK]` | URL page Facebook |
| `[LINKEDIN]` | URL page LinkedIn |
| `[TARIF]` | Tarifs des prestations (consultation, ablations) |
| `[HORAIRES]` | Horaires d'ouverture |
| Adresse complète | Avenue Winston Churchill, Uccle (numéro exact) |
| Photos praticiens | 3 photos des chirurgiens (Dr. 1, 2, 3) |
| Noms & INAMI | Noms complets et numéros INAMI des praticiens |
| Photo Heine DeltaOne | Photo du dermatoscope |
| Photo consultation | Photo hero page d'accueil |
| Google Maps embed | Code d'intégration Google Maps |

---

## 7. Journal des actions

| Date | Action | Statut |
|------|--------|--------|
| 2026-04-15 | Lecture et analyse du prompt `churchill-skincheck-prompt-v2.md` | ✅ Fait |
| 2026-04-15 | Création de `context.md` — plan de marche et récapitulatif | ✅ Fait |

> Mettre à jour ce journal à chaque session de travail.

---

## 8. Notes importantes

- **Aucun framework JS** — vanilla uniquement, sans exception
- **config.js toujours dans .gitignore** — ne jamais committer les clés API
- **Mobile-first** — toutes les pages conçues d'abord pour mobile
- **Mentions légales** — inclure RGPD belge + ePrivacy cookie notice
- **Analyse anatomopathologique** — mentionner systématiquement (obligation déontologique)
- **Remboursement INAMI** — ne jamais affirmer un montant exact de remboursement (variable)
- Le site est **en cours de lancement** — tous les médias sont des placeholders à ce stade
