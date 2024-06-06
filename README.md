# COA ASSIGNMENT

This repository contains the code for a responsive photo gallery (built using HTML, CSS, and JavaScript) and two challenges tackled using JavaScript. The gallery is designed to adapt to different screen sizes to ensure responsiveness.

1. ## Features
    Responsive design that adapts to different screen sizes.
    Smooth transitions and animations.
    Feature for viewing photos in a larger view.
    Photo thumbnail navigation

2. ## Approach

    The HTML structure is kept simple. Only two parent divs in HTML `<div class="container"></div` and `<div class="full-size-model"></div>`. Images are rendered from JavaScript. JavaScript holds images in an array and by using looping technique, each image is wrappred in its own div to be rendered on the screen.
    Here is a snippet of the HTML:

    ```
    <body>
        <div class="container"></div>
        <div class="full-size-model">
            <div class="thumbnail_imgs"></div>
            <h1 class="close-btn">&cross; Exit</h1>
        </div>
        <script type="text/javascript" src="./js/index.js"></script>
    </body>
    ```
3. ## Usage

    Viewing photos: Click on any photo to view it.
    Navigating photos: Use the image thumbnail navigation to navigate through the photos.
    Closing the full screen view: Click Exit button to exit the full screen view.

4. ## Folder Structure
```
photo-gallery/
│
├── css/
│   ├── styles.css
│
├── images/             
│
├── js/
│   ├── index.js
│
├── index.html             # Main HTML file
└── README.md              # Project documentation
```