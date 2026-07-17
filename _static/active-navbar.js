document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
    const links = document.querySelectorAll(
        ".bd-header .navbar-nav a.nav-link, " +
        ".bd-header .navbar-nav li > a"
    );

    links.forEach(function (link) {
        const linkPath = new URL(link.href, window.location.origin)
            .pathname
            .replace(/\/index\.html$/, "/");

        const isHomepage =
            currentPath.endsWith("/") &&
            (link.textContent.trim().toLowerCase() === "home");

        const isCurrentPage = currentPath === linkPath;

        if (isHomepage || isCurrentPage) {
            link.classList.add("active");
            link.setAttribute("aria-current", "page");

            const parent = link.closest("li");
            if (parent) {
                parent.classList.add("current", "active");
            }
        }
    });
});