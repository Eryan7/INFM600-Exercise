let position = 0;
const list = carousel.querySelector("ul");
const list2 = carousel.querySelectorAll("li");

const array = Array.from(list2);

function array_right() {
  array.forEach(() => {
    position += 44;
    list.style.marginLeft = position + "px";
    unhide_arrow(".left");
    hide_arrow(".right");
  });
}

function array_left() {
  array.forEach(() => {
    position -= 44;
    list.style.marginLeft = position + "px";
    unhide_arrow(".right");
    hide_arrow(".left");
  });
}

left.addEventListener("click", () => {
  array_left();
});

right.addEventListener("click", () => {
  array_right();
});

let hide_arrow = (arrow) => {
  carousel.querySelector(arrow).style.visibility = "hidden";
};

let unhide_arrow = (arrow) => {
  carousel.querySelector(arrow).style.visibility = "visible";
};