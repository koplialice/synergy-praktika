let images = [
    "url('image1.jpg')",
    "url('image2.jpg')",
    "url('image3.jpg')"
];
let currentSlide = 0;

function showSlide() {
    document.getElementById("slide-image").style.backgroundImage = images[currentSlide];
    document.getElementById("slide-info").textContent = `Изображение ${currentSlide + 1} из ${images.length}`;
}

document.getElementById("prev-btn").addEventListener("click", () => {
    currentSlide = (currentSlide + images.length - 1) % images.length;
    showSlide();
});

document.getElementById("next-btn").addEventListener("click", () => {
    currentSlide = (currentSlide + 1) % images.length;
    showSlide();
});

showSlide();
