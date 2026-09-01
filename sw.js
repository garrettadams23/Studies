/**
 * sw.js — Service worker for the Tech & Life Reference.
 * Precaches the whole (tiny, self-contained) site so it installs as an offline
 * PWA. Cache-first with a network fallback; bump CACHE_VERSION on each release
 * to invalidate old caches. Only runs on the deployed https:// site — the
 * file:// path never registers it (guarded in script.js).
 */
// Written by build.py from a hash of the precached assets — see stamp_sw_version().
// Deriving it means a release can never ship with a stale cache because someone
// forgot to bump a number, and an unchanged build never invalidates a cache for
// no reason.
const CACHE_VERSION = "techref-b001c0979dd3";

const PRECACHE = [
  "/",
  "/index.html",
  "/style.css",
  "/script.js",
  "/Img/fonts.css",
  "/Img/fonts/QGYvz_MVcBeNP4NJtEtq.woff2",
  "/Img/fonts/QGYvz_MVcBeNP4NJuktqQ4E.woff2",
  "/Img/fonts/J7aHnp1uDWRBEqV98dVQztYldFcLowEF.woff2",
  "/Img/Studying-Tips.png",
  "/Img/favicon/favicon-96x96.png",
  "/Img/favicon/favicon.ico",
  "/Img/favicon/apple-touch-icon.png",
  "/Img/favicon/site.webmanifest",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    // No skipWaiting() here on purpose. Taking over immediately swaps the
    // assets under a page that is already open, which is how a reader ends up
    // with a new script.js talking to an old index.html. The new worker waits,
    // the page offers a reload, and skipWaiting() happens below when the reader
    // accepts it.
    caches.open(CACHE_VERSION).then((cache) => cache.addAll(PRECACHE))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_VERSION).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// The page asks for the swap once the reader has agreed to it.
self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "skip-waiting") self.skipWaiting();
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req)
        .then((res) => {
          // Cache same-origin successful responses for next time.
          if (res && res.ok && new URL(req.url).origin === self.location.origin) {
            const copy = res.clone();
            caches.open(CACHE_VERSION).then((cache) => cache.put(req, copy));
          }
          return res;
        })
        .catch(() => {
          // Offline & uncached: fall back to the app shell for navigations.
          if (req.mode === "navigate") return caches.match("/index.html");
          return new Response("", { status: 504, statusText: "Offline" });
        });
    })
  );
});
