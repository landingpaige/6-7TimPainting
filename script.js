/* Tim MacDonough Painting Company — script.js v2.0 */

/* ─── Header: transparent → glass on scroll ──────────────── */
const header = document.querySelector('.site-header');
if (header) {
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 24);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ─── Mobile nav ─────────────────────────────────────────── */
const navToggle = document.getElementById('navToggle');
const mobileNav = document.getElementById('mobileNav');

if (navToggle && mobileNav) {
  navToggle.addEventListener('click', () => {
    const open = mobileNav.classList.toggle('open');
    navToggle.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', open);
    mobileNav.setAttribute('aria-hidden', !open);
    document.body.style.overflow = open ? 'hidden' : '';
  });

  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      navToggle.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      mobileNav.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    });
  });

  /* Close on Escape */
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
      mobileNav.classList.remove('open');
      navToggle.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      mobileNav.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  });
}

/* ─── Smooth scroll (offset for sticky header) ───────────── */
function scrollToAnchor(id) {
  const target = document.querySelector(id);
  if (!target) return;
  const h = parseInt(
    getComputedStyle(document.documentElement).getPropertyValue('--header-h')
  ) || 80;
  const top = target.getBoundingClientRect().top + window.scrollY - h;
  window.scrollTo({ top, behavior: 'smooth' });
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const id = anchor.getAttribute('href');
    if (id === '#' || id === '#top') return;
    if (!document.querySelector(id)) return;
    e.preventDefault();
    scrollToAnchor(id);
  });
});

/* Landing on a page with a hash (eg. contact.html#contact) — browser jumps
   there instantly before layout/fonts settle, and ignores the sticky header
   offset. Re-run the offset scroll once the page has loaded. */
if (window.location.hash && window.location.hash !== '#top') {
  window.addEventListener('load', () => scrollToAnchor(window.location.hash));
}

/* ─── Scroll reveal ──────────────────────────────────────── */
if ('IntersectionObserver' in window) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
}

/* ─── Animated counters ──────────────────────────────────── */
function animateCounter(el, target, duration = 1800) {
  const start = performance.now();
  const tick = now => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.round(eased * target);
    if (progress < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

const statEls = document.querySelectorAll('.stat-count[data-target]');
if (statEls.length && 'IntersectionObserver' in window) {
  const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.dataset.target, 10);
        if (target === 0) {
          entry.target.textContent = '0';
        } else {
          animateCounter(entry.target, target);
        }
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  statEls.forEach(el => counterObserver.observe(el));
}

/* ─── Hero parallax (desktop only, reduced-motion safe) ─── */
const heroContent = document.querySelector('.hero-content');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (heroContent && !prefersReducedMotion) {
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (ticking) return;
    requestAnimationFrame(() => {
      const y = window.scrollY;
      if (y < window.innerHeight) {
        heroContent.style.transform = `translateY(${y * 0.1}px)`;
      }
      ticking = false;
    });
    ticking = true;
  }, { passive: true });
}

/* ─── Contact / estimate form ────────────────────────────── */
function initForm(formId, successId) {
  const form    = document.getElementById(formId);
  const success = document.getElementById(successId);
  if (!form || !success) return;

  form.addEventListener('submit', e => {
    e.preventDefault();
    let valid = true;

    form.querySelectorAll('[required]').forEach(field => {
      field.classList.remove('error');
      if (!field.value.trim()) {
        field.classList.add('error');
        valid = false;
      }
    });

    if (!valid) {
      form.querySelector('.error')?.focus();
      return;
    }

    const btn  = form.querySelector('[type="submit"]');
    const orig = btn.textContent;
    btn.disabled    = true;
    btn.textContent = 'Sending…';

    const payload = new URLSearchParams(new FormData(form)).toString();
    fetch('/', {
      method:  'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body:    payload
    })
    .then(() => {
      form.reset();
      success.hidden = false;
      success.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    })
    .catch(() => {
      alert('Something went wrong. Please call us directly at (248) 978-2946.');
    })
    .finally(() => {
      btn.disabled    = false;
      btn.textContent = orig;
    });
  });

  form.querySelectorAll('input, select, textarea').forEach(field => {
    field.addEventListener('input', () => field.classList.remove('error'));
  });
}

initForm('contactForm',  'formSuccess');
initForm('estimateForm', 'estimateSuccess');

/* ─── FAQ accordion ──────────────────────────────────────── */
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(item => {
  const btn = item.querySelector('.faq-question');
  const answer = item.querySelector('.faq-answer');
  const inner = item.querySelector('.faq-answer-inner');
  if (!btn || !answer || !inner) return;

  btn.addEventListener('click', () => {
    const isOpen = btn.getAttribute('aria-expanded') === 'true';

    faqItems.forEach(other => {
      const otherBtn = other.querySelector('.faq-question');
      const otherAnswer = other.querySelector('.faq-answer');
      if (otherBtn && otherAnswer) {
        otherBtn.setAttribute('aria-expanded', 'false');
        otherAnswer.style.maxHeight = '0';
      }
    });

    if (!isOpen) {
      btn.setAttribute('aria-expanded', 'true');
      answer.style.maxHeight = inner.scrollHeight + 32 + 'px';
    }
  });
});

/* ─── Mobile CTA bar: hide when nav is open ─────────────── */
const mobileCta = document.getElementById('mobileCta');
if (mobileCta && navToggle && mobileNav) {
  const updateCtaVisibility = () => {
    const navOpen = mobileNav.classList.contains('open');
    mobileCta.classList.toggle('nav-open', navOpen);
  };
  navToggle.addEventListener('click', updateCtaVisibility);
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', updateCtaVisibility);
  });
}

/* ─── Footer year ────────────────────────────────────────── */
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

/* ─── Active nav link ────────────────────────────────────── */
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-list a').forEach(a => {
  const href = a.getAttribute('href');
  if (href === currentPage || (currentPage === '' && href === 'index.html')) {
    a.classList.add('active');
  }
});
