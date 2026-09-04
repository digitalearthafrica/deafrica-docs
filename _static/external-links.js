document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a[href^='http']").forEach(function (link) {
    const url = new URL(link.href, window.location.href);

    if (url.hostname !== window.location.hostname) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  });
});