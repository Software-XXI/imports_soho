const hamburger = document.getElementById("hamburger");
const navMenu = document.getElementById("nav-menu");

const openMenu = () => {
    navMenu.classList.add("is-open");
    navMenu.setAttribute("aria-hidden", "false");
    hamburger.setAttribute("aria-expanded", "true");
    hamburger.classList.add("is-active");
    document.body.classList.add("no-scroll");
};

const closeMenu = () => {
    navMenu.classList.remove("is-open");
    navMenu.setAttribute("aria-hidden", "true");
    hamburger.setAttribute("aria-expanded", "false");
    hamburger.classList.remove("is-active");
    document.body.classList.remove("no-scroll");
};

hamburger.addEventListener("click", () => {
    navMenu.classList.contains("is-open") ? closeMenu() : openMenu();
});

navMenu.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", closeMenu);
});

document.addEventListener("click", (e) => {
    if (!e.target.closest(".header") && navMenu.classList.contains("is-open")) {
        closeMenu();
    }
});

document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
});