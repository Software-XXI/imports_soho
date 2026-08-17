const lightbox = document.getElementById("lightbox");
const stage = document.getElementById("lightbox-stage");
const lightboxImg = document.getElementById("lightbox-img");
const closeBtn = document.getElementById("lightbox-close");

const open = (src) => {
    lightboxImg.src = src;
    lightboxImg.style.transform = "scale(1.08)";
    lightbox.classList.add("is-open");
    document.body.classList.add("no-scroll");
};

const close = () => {
    lightbox.classList.remove("is-open");
    document.body.classList.remove("no-scroll");
};

document.querySelectorAll(".card-img[data-full]").forEach((img) => {
    img.addEventListener("click", () => open(img.dataset.full));
});

stage.addEventListener("mousemove", (e) => {
    const rect = stage.getBoundingClientRect();
    const x = e.clientX / rect.width - 0.5;
    const y = e.clientY / rect.height - 0.5;
    lightboxImg.style.transform =
        `translate(${x * 40}px, ${y * 26}px) scale(1.14)`;
});

stage.addEventListener("mouseleave", () => {
    lightboxImg.style.transform = "scale(1.08)";
});

closeBtn.addEventListener("click", close);
lightbox.addEventListener("click", (e) => {
    if (
        e.target === lightbox ||
        e.target === stage ||
        e.target === lightboxImg
    ) {
        close();
    }
});
document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
});