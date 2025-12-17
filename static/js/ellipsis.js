document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.post-body').forEach(el => {
        let lineHeight = parseFloat(getComputedStyle(el).lineHeight);
        if (isNaN(lineHeight)) lineHeight = 24; // fallback in px
        const maxHeight = lineHeight * 3;

        if (el.scrollHeight > maxHeight) {
            let text = el.innerText;
            while(el.scrollHeight > maxHeight) {
                text = text.slice(0, -1);
                el.innerText = text + '...';
            }
        }
    });
});
