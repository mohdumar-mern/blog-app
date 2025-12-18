function showReplyForm(id) {
    const form = document.getElementById(`reply-form-${id}`);
    form.style.display = form.style.display === "none" ? "block" : "none";
}


document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".toggle-replies").forEach(btn => {

        const targetId = btn.dataset.target;
        const count = btn.dataset.count;
        const targetDiv = document.getElementById(targetId);

        btn.addEventListener("click", () => {
            if (targetDiv.style.display === "none") {
                targetDiv.style.display = "block";
                btn.textContent = `Hide Replies (${count})`;
            } else {
                targetDiv.style.display = "none";
                btn.textContent = `Show Replies (${count})`;
            }
        });

    });
});
