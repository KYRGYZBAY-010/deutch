const next = document.querySelector(".next")
const sliderLine = document.querySelector(".slider-line")

let left = 0



setInterval(() => {animation()}, 3000);


function animation() {   
    left += 1190
    if (left == 2380) {
        left = 0
        sliderLine.style.left = `-${left}px`
    }
    else{
        sliderLine.style.left = `-${left}px`

    }
}
