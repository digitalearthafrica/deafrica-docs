document.addEventListener("DOMContentLoaded", () => {
    const normalisePath = (value) => {
        let path = new URL(value, window.location.origin).pathname;

        // Treat /index.html and a trailing slash as the same page.
        path = path.replace(/\/index\.html$/, "/");

        // Ensure directory-style paths end with one slash.
        if (!path.endsWith("/") && !path.split("/").pop().includes(".")) {
            path += "/";
        }

        return path;
    };

    const currentPath = normalisePath(window.location.href);

    const navbarLinks = document.querySelectorAll(
        ".bd-header .navbar-nav a"
    );

    navbarLinks.forEach((link) => {
        const linkPath = normalisePath(link.href);

        // Clear any incorrect active states first.
        link.classList.remove("active", "current");
        link.removeAttribute("aria-current");

        const parent = link.closest("li");

        if (parent) {
            parent.classList.remove("active", "current");
        }

        // Mark the exact matching navbar link as active.
        if (linkPath === currentPath) {
            link.classList.add("active", "current");
            link.setAttribute("aria-current", "page");

            if (parent) {
                parent.classList.add("active", "current");
            }
        }
    });
});