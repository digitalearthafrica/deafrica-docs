document.addEventListener("DOMContentLoaded", function () {
    const pageId =
        document.querySelector('meta[name="page-id"]')?.content || "";

    const links = document.querySelectorAll(
        ".bd-header .navbar-nav a"
    );

    links.forEach(function (link) {
        const label = link.textContent.trim().toLowerCase();
        const parent = link.closest("li");

        link.classList.remove("de-nav-active");
        link.removeAttribute("aria-current");

        if (parent) {
            parent.classList.remove("de-nav-active");
        }

        let shouldActivate = false;

        if (pageId === "home" && label === "home") {
            shouldActivate = true;
        }

        if (pageId === "data" && label === "data") {
            shouldActivate = true;
        }

        if (pageId === "platforms" && label === "platforms") {
            shouldActivate = true;
        }

        if (
            pageId === "direct-access" &&
            label === "direct access"
        ) {
            shouldActivate = true;
        }

        if (
            pageId === "service-status" &&
            label === "service status"
        ) {
            shouldActivate = true;
        }

        if (pageId === "about" && label === "about") {
            shouldActivate = true;
        }

        if (shouldActivate) {
            link.classList.add("de-nav-active");
            link.setAttribute("aria-current", "page");

            if (parent) {
                parent.classList.add("de-nav-active");
            }
        }
    });
});