document.addEventListener('DOMContentLoaded', () => {
  // Intersection Observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  
  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

  // Mobile menu logic
  const burgerBtn = document.querySelector('.burger-btn');
  const mobileMenu = document.querySelector('.mobile-menu');
  
  if (burgerBtn && mobileMenu) {
    const overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);

    const toggleMenu = () => {
      burgerBtn.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      overlay.classList.toggle('active');
      document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : 'auto';
    };

    burgerBtn.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', toggleMenu);
  }

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close others
        faqItems.forEach(faq => {
            faq.classList.remove('active');
            const icon = faq.querySelector('iconify-icon');
            if(icon) icon.style.transform = 'rotate(0deg)';
        });
        
        if(!isActive) {
            item.classList.add('active');
            const icon = question.querySelector('iconify-icon');
            if(icon) icon.style.transform = 'rotate(180deg)';
        }
      });
    }
  });
});
