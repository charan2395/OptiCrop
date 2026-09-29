 /* =========================================================
   OPTICROP — SMART AGRICULTURAL INTERACTION ENGINE
   Modern animations + validation + dashboard interactions
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    /* =====================================================
       1. PAGE ENTRANCE ANIMATION
    ===================================================== */

    document.body.classList.add("page-loaded");


    /* =====================================================
       2. INPUT FIELD INTERACTIONS
    ===================================================== */

    const inputs = document.querySelectorAll(
        "input, select, textarea"
    );

    inputs.forEach((input) => {

        // Focus effect
        input.addEventListener("focus", () => {

            input.parentElement?.classList.add(
                "input-active"
            );

        });


        // Remove focus effect
        input.addEventListener("blur", () => {

            input.parentElement?.classList.remove(
                "input-active"
            );

        });


        // Detect value change
        input.addEventListener("input", () => {

            if (input.value.trim() !== "") {

                input.classList.add("has-value");

            } else {

                input.classList.remove("has-value");

            }

        });

    });


    /* =====================================================
       3. FORM SUBMISSION LOADING ANIMATION
    ===================================================== */

    const forms = document.querySelectorAll("form");

    forms.forEach((form) => {

        form.addEventListener("submit", (event) => {

            // Check HTML validation first
            if (!form.checkValidity()) {

                event.preventDefault();

                form.classList.add("form-error-shake");

                setTimeout(() => {

                    form.classList.remove(
                        "form-error-shake"
                    );

                }, 500);

                return;

            }


            const button = form.querySelector(
                "button[type='submit'], button:not([type])"
            );

            if (!button) {
                return;
            }


            // Prevent double clicking
            button.disabled = true;

            button.classList.add("predicting");


            // Store original button text
            button.dataset.originalText =
                button.innerHTML;


            button.innerHTML = `
                <span class="loading-spinner"></span>
                <span>Analyzing Field...</span>
            `;

        });

    });


    /* =====================================================
       4. BUTTON RIPPLE EFFECT
    ===================================================== */

    const buttons = document.querySelectorAll(
        "button, .btn"
    );

    buttons.forEach((button) => {

        button.addEventListener("click", function (event) {

            const rect = this.getBoundingClientRect();

            const ripple = document.createElement("span");

            const size = Math.max(
                rect.width,
                rect.height
            );

            ripple.style.width = `${size}px`;
            ripple.style.height = `${size}px`;

            ripple.style.left =
                `${event.clientX - rect.left - size / 2}px`;

            ripple.style.top =
                `${event.clientY - rect.top - size / 2}px`;

            ripple.classList.add("button-ripple");

            this.appendChild(ripple);


            setTimeout(() => {

                ripple.remove();

            }, 650);

        });

    });


    /* =====================================================
       5. ANIMATE RESULT NUMBERS
    ===================================================== */

    const numberElements = document.querySelectorAll(
        "[data-count]"
    );

    numberElements.forEach((element) => {

        const target = parseFloat(
            element.dataset.count
        );

        if (Number.isNaN(target)) {
            return;
        }

        animateNumber(
            element,
            0,
            target,
            900
        );

    });


    /* =====================================================
       6. ANIMATE PROGRESS BARS
    ===================================================== */

    const progressBars = document.querySelectorAll(
        "[data-progress]"
    );

    progressBars.forEach((bar) => {

        const progress = parseFloat(
            bar.dataset.progress
        );

        if (Number.isNaN(progress)) {
            return;
        }

        const safeProgress = Math.min(
            100,
            Math.max(0, progress)
        );


        bar.style.width = "0%";


        setTimeout(() => {

            bar.style.width =
                `${safeProgress}%`;

        }, 250);

    });


    /* =====================================================
       7. RESULT CARD ANIMATION
    ===================================================== */

    const cropResult = document.querySelector(
        ".crop-result"
    );

    if (cropResult) {

        setTimeout(() => {

            cropResult.classList.add(
                "result-visible"
            );

        }, 150);

    }


    /* =====================================================
       8. DASHBOARD CARDS STAGGER ANIMATION
    ===================================================== */

    const dashboardCards = document.querySelectorAll(
        ".dashboard-card, .metric-card"
    );

    dashboardCards.forEach((card, index) => {

        card.style.animationDelay =
            `${index * 100}ms`;

        card.classList.add(
            "dashboard-card-enter"
        );

    });


    /* =====================================================
       9. INTERACTIVE HOVER TILT
    ===================================================== */

    const tiltCards = document.querySelectorAll(
        ".dashboard-card.tilt-card"
    );


    tiltCards.forEach((card) => {

        card.addEventListener(
            "mousemove",
            (event) => {

                const rect =
                    card.getBoundingClientRect();

                const x =
                    event.clientX - rect.left;

                const y =
                    event.clientY - rect.top;


                const centerX =
                    rect.width / 2;

                const centerY =
                    rect.height / 2;


                const rotateX =
                    ((y - centerY) / centerY) * -2;


                const rotateY =
                    ((x - centerX) / centerX) * 2;


                card.style.transform =
                    `perspective(800px)
                     rotateX(${rotateX}deg)
                     rotateY(${rotateY}deg)
                     translateY(-4px)`;

            }
        );


        card.addEventListener(
            "mouseleave",
            () => {

                card.style.transform = "";

            }
        );

    });


    /* =====================================================
       10. INPUT RANGE / VALUE PREVIEW
    ===================================================== */

    const rangeInputs = document.querySelectorAll(
        "input[type='range']"
    );


    rangeInputs.forEach((range) => {

        const output =
            document.querySelector(
                `[data-for="${range.id}"]`
            );


        range.addEventListener("input", () => {

            if (output) {

                output.textContent =
                    range.value;

            }

        });

    });


    /* =====================================================
       11. TOOLTIP SUPPORT
    ===================================================== */

    const tooltipElements =
        document.querySelectorAll(
            "[data-tooltip]"
        );


    tooltipElements.forEach((element) => {

        element.addEventListener(
            "mouseenter",
            () => {

                element.classList.add(
                    "tooltip-visible"
                );

            }
        );


        element.addEventListener(
            "mouseleave",
            () => {

                element.classList.remove(
                    "tooltip-visible"
                );

            }
        );

    });


    /* =====================================================
       12. AUTO FOCUS FIRST INPUT
    ===================================================== */

    const firstInput =
        document.querySelector(
            "form input:not([type='hidden'])"
        );


    if (
        firstInput &&
        window.innerWidth > 768
    ) {

        setTimeout(() => {

            firstInput.focus();

        }, 600);

    }


    /* =====================================================
       13. CHART.JS DASHBOARD
    ===================================================== */

    initializeCharts();

});


/* =========================================================
   NUMBER ANIMATION FUNCTION
========================================================= */

function animateNumber(
    element,
    start,
    end,
    duration
) {

    const startTime =
        performance.now();


    function update(currentTime) {

        const elapsed =
            currentTime - startTime;


        const progress =
            Math.min(
                elapsed / duration,
                1
            );


        // Smooth easing
        const eased =
            1 -
            Math.pow(
                1 - progress,
                3
            );


        const current =
            start +
            (end - start) *
            eased;


        element.textContent =
            Number.isInteger(end)
                ? Math.round(current)
                : current.toFixed(1);


        if (progress < 1) {

            requestAnimationFrame(update);

        }

    }


    requestAnimationFrame(update);

}


/* =========================================================
   CHART INITIALIZATION
========================================================= */

function initializeCharts() {

    // If Chart.js isn't loaded, simply skip charts
    if (
        typeof Chart === "undefined"
    ) {

        return;

    }


    /* =====================================================
       TOP CROP PREDICTIONS CHART
    ===================================================== */

    const predictionCanvas =
        document.getElementById(
            "predictionChart"
        );


    if (predictionCanvas) {

        const labels =
            JSON.parse(
                predictionCanvas.dataset.labels ||
                "[]"
            );


        const values =
            JSON.parse(
                predictionCanvas.dataset.values ||
                "[]"
            );


        new Chart(
            predictionCanvas,
            {

                type: "doughnut",

                data: {

                    labels: labels,

                    datasets: [
                        {

                            data: values,

                            backgroundColor: [

                                "#168653",

                                "#65b86d",

                                "#9bdc72",

                                "#c9e889",

                                "#e7f4c5"

                            ],

                            borderWidth: 0,

                            hoverOffset: 12

                        }
                    ]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    cutout: "68%",

                    animation: {

                        duration: 1400,

                        easing: "easeOutQuart"

                    },

                    plugins: {

                        legend: {

                            position: "bottom",

                            labels: {

                                padding: 18,

                                usePointStyle: true,

                                font: {

                                    size: 12

                                }

                            }

                        },

                        tooltip: {

                            backgroundColor:
                                "rgba(24, 59, 43, 0.95)",

                            padding: 12,

                            cornerRadius: 10,

                            callbacks: {

                                label:
                                    function(context) {

                                        return (
                                            " " +
                                            context.label +
                                            ": " +
                                            context.parsed +
                                            "%"
                                        );

                                    }

                            }

                        }

                    }

                }

            }
        );

    }


    /* =====================================================
       SOIL NUTRIENT CHART
    ===================================================== */

    const soilCanvas =
        document.getElementById(
            "soilChart"
        );


    if (soilCanvas) {

        const labels =
            JSON.parse(
                soilCanvas.dataset.labels ||
                "[]"
            );


        const values =
            JSON.parse(
                soilCanvas.dataset.values ||
                "[]"
            );


        new Chart(
            soilCanvas,
            {

                type: "bar",

                data: {

                    labels: labels,

                    datasets: [
                        {

                            label:
                                "Soil Nutrient Level",

                            data: values,

                            borderRadius: 10,

                            borderSkipped: false,

                            backgroundColor: [

                                "#168653",

                                "#65b86d",

                                "#9bdc72"

                            ]

                        }
                    ]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    animation: {

                        duration: 1200,

                        easing: "easeOutQuart"

                    },

                    scales: {

                        y: {

                            beginAtZero: true,

                            grid: {

                                color:
                                    "rgba(22,134,83,0.08)"

                            }

                        },

                        x: {

                            grid: {

                                display: false

                            }

                        }

                    },

                    plugins: {

                        legend: {

                            display: false

                        },

                        tooltip: {

                            backgroundColor:
                                "rgba(24, 59, 43, 0.95)",

                            padding: 12,

                            cornerRadius: 10

                        }

                    }

                }

            }
        );

    }


    /* =====================================================
       ENVIRONMENT RADAR CHART
    ===================================================== */

    const environmentCanvas =
        document.getElementById(
            "environmentChart"
        );


    if (environmentCanvas) {

        const labels =
            JSON.parse(
                environmentCanvas.dataset.labels ||
                "[]"
            );


        const values =
            JSON.parse(
                environmentCanvas.dataset.values ||
                "[]"
            );


        new Chart(
            environmentCanvas,
            {

                type: "radar",

                data: {

                    labels: labels,

                    datasets: [
                        {

                            label:
                                "Field Conditions",

                            data: values,

                            borderWidth: 2,

                            pointRadius: 4,

                            pointHoverRadius: 7,

                            backgroundColor:
                                "rgba(22, 134, 83, 0.14)",

                            borderColor:
                                "#168653",

                            pointBackgroundColor:
                                "#168653"

                        }
                    ]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    animation: {

                        duration: 1400,

                        easing: "easeOutQuart"

                    },

                    scales: {

                        r: {

                            beginAtZero: true,

                            grid: {

                                color:
                                    "rgba(22,134,83,0.10)"

                            },

                            angleLines: {

                                color:
                                    "rgba(22,134,83,0.10)"

                            },

                            pointLabels: {

                                font: {

                                    size: 11,

                                    weight: "600"

                                },

                                color:
                                    "#345b43"

                            }

                        }

                    },

                    plugins: {

                        legend: {

                            position: "bottom"

                        }

                    }

                }

            }
        );

    }

}


/* =========================================================
   SCROLL REVEAL
========================================================= */

const observer =
    new IntersectionObserver(

        (entries) => {

            entries.forEach(
                (entry) => {

                    if (
                        entry.isIntersecting
                    ) {

                        entry.target.classList.add(
                            "visible"
                        );

                    }

                }
            );

        },

        {
            threshold: 0.12
        }

    );


document
    .querySelectorAll(
        ".dashboard-card, .metric-card, .crop-result"
    )
    .forEach(
        (element) => {

            observer.observe(element);

        }
    );


/* =========================================================
   ACCESSIBILITY — REDUCED MOTION
========================================================= */

const prefersReducedMotion =
    window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    );


if (
    prefersReducedMotion.matches
) {

    document.documentElement.classList.add(
        "reduce-motion"
    );

}