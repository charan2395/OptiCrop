// OptiCrop Frontend JavaScript

// 1. Input validation before form submit
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (event) {

            const inputs = form.querySelectorAll("input");
            let valid = true;

            inputs.forEach(input => {
                if (input.value.trim() === "") {
                    valid = false;
                    input.style.border = "2px solid red";
                } else {
                    input.style.border = "1px solid #ccc";
                }
            });

            if (!valid) {
                alert("❌ Please fill all fields before prediction!");
                event.preventDefault();
            }

        });
    }
});


// 2. Auto smooth scroll (optional UX improvement)
function scrollToResult() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}