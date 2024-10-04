let images = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg"
];

let currentSlide = 0;

function showSlide() {
    document.querySelector("#slide-image img").src = images[currentSlide];
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
