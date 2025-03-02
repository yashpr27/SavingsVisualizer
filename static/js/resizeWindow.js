// This script does not work for some reason
// goal was/is to specify min height and min width for window
// (i.e.) window cannot be resized smaller than the min width or min height

const minWidth = 120;
const minHeight = 520;

window.addEventListener("resize", function () {
    if (window.innerWidth < minWidth || window.innerHeight < minHeight) {
        window.resizeTo(
            Math.max(window.innerWidth, minWidth),
            Math.max(window.innerHeight, minHeight)
        );
    }
});
