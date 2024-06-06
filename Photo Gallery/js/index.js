const images = [
  {
    id: 1,
    src: "./images/fox.jpg",
    h1: "FENNEC",
    h2: "FOX",
    origin: "India",
  },
  {
    id: 2,
    src: "./images/humpback-whale.jpg",
    h1: "HUMPBACK",
    h2: "WHALE",
    origin: "South Africa",
  },
  {
    id: 3,
    src: "./images/baboons_thumb.avif",
    h1: "COMMON BROWN",
    h2: "BOBOON",
    origin: "South Africa",
  },
  {
    id: 4,
    src: "./images/indian-spot-deer.jpg",

    h1: "SPOTTED",
    h2: "DEER",
    origin: "Amazon",
  },
];

const container = document.querySelector(".container")
const fullSizeModel = document.querySelector(".full-size-model")
const closeBtn = document.querySelector(".close-btn");
const thumbnailImgs = document.querySelector(".thumbnail_imgs");

container.innerHTML = ""
images.forEach((image) => {
    container.innerHTML += `
      <div class="single-image">
        <div class="image">
          <small class="tooltip-content">View this image</small>
          <img src=${image.src} data-id = ${image.id} alt="">
        </div>
        <div class="description">
          <h1>${image.h1}</h1>
          <h1>${image.h2}</h1>
          <p>${image.origin}</p>
        </div>
      </div>
    `;
    thumbnailImgs.innerHTML += `
      <img src=${image.src} data-id = ${image.id} alt="">
    `;
})


const imageArea = document.querySelectorAll(".single-image img");
let imageEl = document.createElement('img')

imageArea.forEach((img) => {
    img.addEventListener("click", (e) => {
        fullSizeModel.style.display = "block";
        imageEl.src = e.target.src
        imageEl.width = window.innerWidth;
        imageEl.height = window.innerHeight;
        imageEl.style.objectFit = "contain";
        fullSizeModel.append(imageEl)
    });
})


thumbnailImgs.addEventListener("click", (e) => {
  imageEl.src = e.target.src
  console.log(imageEl.src)
})
closeBtn.addEventListener("click", () => {
    fullSizeModel.removeChild(imageEl);
    fullSizeModel.style.display = "none";
});

