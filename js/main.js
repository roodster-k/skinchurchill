document.addEventListener('DOMContentLoaded', () => {

  /* ── Intersection Observer fade-up ── */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.10 });
  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

  /* ── Mobile menu ── */
  const burgerBtn   = document.querySelector('.burger-btn');
  const mobileMenu  = document.querySelector('.mobile-menu');

  if (burgerBtn && mobileMenu) {
    const overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);

    const openMenu  = () => {
      burgerBtn.classList.add('active');
      mobileMenu.classList.add('active');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    };
    const closeMenu = () => {
      burgerBtn.classList.remove('active');
      mobileMenu.classList.remove('active');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    };
    const toggleMenu = () => mobileMenu.classList.contains('active') ? closeMenu() : openMenu();

    burgerBtn.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', closeMenu);

    // Close on ESC
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
  }

  /* ── FAQ Accordion ── */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (!question) return;

    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all
      faqItems.forEach(f => f.classList.remove('active'));

      // Open clicked (if it wasn't already open)
      if (!isActive) item.classList.add('active');
    });
  });

  /* ── Header scroll shadow ── */
  const header = document.querySelector('.main-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.style.boxShadow = '0 4px 24px rgba(26,43,66,0.10)';
      } else {
        header.style.boxShadow = 'none';
      }
    }, { passive: true });
  }

});
