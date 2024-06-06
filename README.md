# COA ASSIGNMENT

This repository contains the code for a responsive photo gallery (built using HTML, CSS, and JavaScript) and two challenges tackled using JavaScript. The gallery is designed to adapt to different screen sizes to ensure responsiveness.

# 1. PHOTO GALLERY PROJECT
## Features
    Responsive design that adapts to different screen sizes.
    Smooth transitions and animations.
    Feature for viewing photos in a larger view.
    Photo thumbnail navigation

## Approach

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
## Usage

    Viewing photos: Click on any photo to view it.
    Navigating photos: Use the image thumbnail navigation to navigate through the photos.
    Closing the full screen view: Click Exit button to exit the full screen view.

## Folder Structure
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

# 2. JAVASCRIPT CHALLENGES
    This project includes two challenges done in JavaScript. The first one gives you array of integers and target sum. I've write function to take both parameters and then return true if subarray found or false when not found.

    Scond one transform string based on these instructions:
        ● If the length of the string is divisible by 3, reverse the entire string.
        ● If the length of the string is divisible by 5, replace each character with its ASCII code.
        ● If the length of the string is divisible by both 3 and 5 (i.e., divisible by 15), perform
        both operations in the order specified above
## Folder Structure
```
Challenges/
│
├──arrayMaps.js
├──stringTransformation.js

```