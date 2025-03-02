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
