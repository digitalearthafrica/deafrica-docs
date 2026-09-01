document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".bd-header .navbar-nav a");

    const normalize = (value) =>
        (value || "")
            .trim()
            .toLowerCase()
            .replace(/\s+/g, " ");

    const path = normalize(window.location.pathname);

    /*
     * Prefer an explicit page-id meta tag when available.
     * Fall back to the URL path so the navbar still works when
     * individual pages do not define <meta name="page-id">.
     */
    let pageId = normalize(
        document.querySelector('meta[name="page-id"]')?.content
    );

    if (!pageId) {
        if (
            path === "/" ||
            path.endsWith("/index.html") ||
            path.endsWith("/en/") ||
            path.endsWith("/en/latest/") ||
            path.endsWith("/en/stable/")
        ) {
            pageId = "home";
        } else if (
            path.includes("/data") ||
            path.includes("/datasets") ||
            path.includes("/products")
        ) {
            pageId = "data";
        } else if (path.includes("/platform")) {
            pageId = "platforms";
        } else if (
            path.includes("/direct-access") ||
            path.includes("/direct_access") ||
            path.includes("/accessing-data") ||
            path.includes("/accessing_data")
        ) {
            pageId = "direct-access";
        } else if (
            path.includes("/tech-alert") ||
            path.includes("/tech_alert") ||
            path.includes("/service-status") ||
            path.includes("/service_status") ||
            path.includes("/status")
        ) {
            pageId = "tech-alert";
        } else if (path.includes("/about")) {
            pageId = "about";
        }
    }

    /*
     * Map page identifiers to the visible navbar labels.
     * Aliases are included so older page IDs can still work.
     */
    const pageMap = {
        "home": ["home"],
        "data": ["data"],
        "platforms": ["platforms"],
        "direct-access": ["direct access"],
        "tech-alert": ["tech alert", "service status"],
        "service-status": ["tech alert", "service status"],
        "about": ["about"]
    };

    const activeLabels = pageMap[pageId] || [];

    links.forEach(function (link) {
        const label = normalize(link.textContent);
        const parent = link.closest("li");

        /*
         * Clear Sphinx/PyData active states first so multiple
         * navigation items cannot appear selected at once.
         */
        link.classList.remove(
            "de-nav-active",
            "active",
            "current"
        );

        link.removeAttribute("aria-current");

        if (parent) {
            parent.classList.remove(
                "de-nav-active",
                "active",
                "current"
            );
        }

        /*
         * Apply the active state to the matching navbar item.
         */
        if (activeLabels.includes(label)) {
            link.classList.add("de-nav-active");
            link.setAttribute("aria-current", "page");

            if (parent) {
                parent.classList.add("de-nav-active");
            }
        }
    });
});