document.addEventListener("DOMContentLoaded", function () {
    const navbarLinks = document.querySelectorAll(
        ".bd-header .navbar-nav a"
    );

    if (!navbarLinks.length) {
        return;
    }

    const pageName =
        window.DOCUMENTATION_OPTIONS?.pagename || "";

    navbarLinks.forEach(function (link) {
        const label = link.textContent.trim().toLowerCase();
        const parent = link.closest("li");

        link.classList.remove("de-nav-active");
        link.removeAttribute("aria-current");

        if (parent) {
            parent.classList.remove("de-nav-active");
        }

        let shouldActivate = false;

        // Homepage
        if (pageName === "index" && label === "home") {
            shouldActivate = true;
        }

        // Data section
        if (
            pageName.startsWith("data_specs/") &&
            label === "data"
        ) {
            shouldActivate = true;
        }

        // Platforms section
        if (
            pageName.startsWith("platform_tools/") &&
            label === "platforms"
        ) {
            shouldActivate = true;
        }

        // Direct Access section
        if (
            pageName.startsWith("platform_tools/") &&
            pageName.includes("direct_access") &&
            label === "direct access"
        ) {
            shouldActivate = true;
        }

        // Service Status section
        if (
            pageName.startsWith("service_status/") &&
            label === "service status"
        ) {
            shouldActivate = true;
        }

        // About section
        if (
            pageName.startsWith("about/") &&
            label === "about"
        ) {
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