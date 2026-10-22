document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menuToggleBtn');
    const closeButton = document.getElementById('menuCloseBtn');
    const menu = document.getElementById('sideMenu');
    const overlay = document.getElementById('menuOverlay');
    const mainPanel = document.getElementById('mainPanel');
    const panels = document.querySelectorAll('.menu-panel');

    if (!menu || !overlay || !mainPanel) return;

    const openMenu = () => {
        menu.classList.add('open');
        overlay.classList.add('active');
        menu.setAttribute('aria-hidden', 'false');
        menuToggle?.setAttribute('aria-expanded', 'true');
        document.body.classList.add('menu-open');
    };

    const closeMenu = () => {
        menu.classList.remove('open');
        overlay.classList.remove('active');
        menu.setAttribute('aria-hidden', 'true');
        menuToggle?.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('menu-open');
        panels.forEach(panel => panel.classList.remove('active'));
        mainPanel.classList.add('active');
    };

    menuToggle?.addEventListener('click', openMenu);
    closeButton?.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape') closeMenu();
    });

    document.querySelectorAll('.submenu-trigger').forEach(trigger => {
        trigger.addEventListener('click', () => {
            const target = document.getElementById(trigger.dataset.target);
            if (!target) return;
            panels.forEach(panel => panel.classList.remove('active'));
            target.classList.add('active');
        });
    });

    document.querySelectorAll('.submenu-back').forEach(button => {
        button.addEventListener('click', () => {
            panels.forEach(panel => panel.classList.remove('active'));
            mainPanel.classList.add('active');
        });
    });
});
