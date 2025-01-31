document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu functionality
    const menuToggle = document.querySelector('.menu-toggle');
    const navContent = document.querySelector('.nav-content');

    menuToggle.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent event bubbling
        navContent.classList.toggle('active');
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            navContent.classList.remove('active');
            const section = document.querySelector(this.getAttribute('href'));
            section.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('nav')) {
            navContent.classList.remove('active');
        }
    });

    // Add scroll animation for elements
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });

    // Observe all sections
    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = 0;
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'all 0.5s ease-in-out';
        observer.observe(section);
    });
});
