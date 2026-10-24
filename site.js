/* Subtle only. The artwork is the spectacle; the website is the frame. */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Fade in on scroll.
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // Very gentle parallax: elements with data-parallax="0.08" drift at a different speed.
  var px = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
  if (px.length && !reduce) {
    var ticking = false;
    var update = function () {
      var vh = window.innerHeight;
      px.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var mid = r.top + r.height / 2 - vh / 2;
        var k = parseFloat(el.getAttribute("data-parallax")) || 0.06;
        el.style.transform = "translate3d(0," + (-mid * k).toFixed(1) + "px,0)";
      });
      ticking = false;
    };
    var onScroll = function () { if (!ticking) { requestAnimationFrame(update); ticking = true; } };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    update();
  }

  // Mobile menu.
  var nav = document.querySelector(".nav");
  var btn = nav && nav.querySelector(".menu-btn");
  if (btn) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? "Close" : "Menu";
    });
  }

  // Lightbox for the artwork page.
  var lb = document.querySelector(".lightbox");
  if (lb) {
    var lbImg = lb.querySelector("img");
    document.querySelectorAll("[data-zoom]").forEach(function (a) {
      a.addEventListener("click", function (ev) {
        ev.preventDefault();
        lbImg.src = a.getAttribute("data-zoom");
        lb.classList.add("open");
      });
    });
    var close = function () { lb.classList.remove("open"); };
    lb.addEventListener("click", close);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
  }

  // Enquiry form: post if an action is configured, otherwise open a mail draft.
  var form = document.querySelector("form.form");
  if (form) {
    form.addEventListener("submit", function (ev) {
      if (form.querySelector(".hp input").value) { ev.preventDefault(); return; }
      if (form.getAttribute("action")) return; // normal POST to the configured endpoint
      ev.preventDefault();
      var fd = new FormData(form);
      var lines = [];
      ["name", "email", "idea", "size", "timeline"].forEach(function (k) {
        var v = (fd.get(k) || "").toString().trim();
        if (v) lines.push(k.toUpperCase() + ": " + v);
      });
      var to = form.getAttribute("data-mailto");
      var subject = encodeURIComponent("An enquiry from " + (fd.get("name") || "someone with an idea"));
      window.location.href = "mailto:" + to + "?subject=" + subject + "&body=" + encodeURIComponent(lines.join("\n\n"));
      form.classList.add("done");
    });
  }
})();
