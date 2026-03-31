      // ── Domain toggle
      function toggleDomain(h) {
        var b = h.nextElementSibling;
        var o = b.classList.toggle("open");
        h.classList.toggle("open", o);
      }
      // ── Topic toggle
      function toggleTopic(h) {
        h.classList.toggle("open");
        h.nextElementSibling.classList.toggle("open");
      }
      // ── Filter chips
      function filter(domain, chip) {
        document
          .querySelectorAll(".chip")
          .forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");
        document.querySelectorAll(".domain-section").forEach((s) => {
          s.classList.toggle(
            "hidden",
            domain !== "all" && s.dataset.domain !== domain,
          );
        });
      }

      // ── Build cloud responsibility stack
      (function () {
        var container = document.getElementById("cloud-stack");
        if (!container) return;
        var layers = [
          "Applications",
          "Data",
          "Runtime",
          "Middleware",
          "OS",
          "Virtualization",
          "Servers",
          "Storage",
          "Networking",
        ];
        var resp = [
          [1, 1, 1, 1],
          [1, 1, 1, 0],
          [1, 1, 0, 0],
          [1, 1, 0, 0],
          [1, 1, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
        ];
        var colors = [
          ["rgba(255,77,109,.12)", "#ff4d6d"],
          ["rgba(255,176,32,.09)", "#ffb020"],
          ["rgba(0,212,255,.08)", "#00d4ff"],
          ["rgba(0,255,153,.08)", "#00ff99"],
        ];
        layers.forEach(function (l, i) {
          var row = document.createElement("div");
          row.style.cssText =
            "display:flex;gap:0;margin-bottom:3px;align-items:stretch";
          var lbl = document.createElement("div");
          lbl.style.cssText =
            "width:120px;font-size:11.5px;color:#cdd9f0;padding:5px 4px 5px 0;flex-shrink:0;font-weight:500";
          lbl.textContent = l;
          row.appendChild(lbl);
          resp[i].forEach(function (v, ci) {
            var cell = document.createElement("div");
            cell.style.cssText =
              "flex:1;text-align:center;padding:5px 3px;font-size:11px;font-weight:600;border-radius:3px;margin:0 2px;" +
              (v
                ? "background:" +
                  colors[ci][0] +
                  ";color:" +
                  colors[ci][1] +
                  ";border:1px solid " +
                  colors[ci][0]
                : "background:rgba(255,255,255,.02);color:#3a4a60;border:1px solid rgba(255,255,255,.05)");
            cell.textContent = v ? "Customer" : "Provider";
            row.appendChild(cell);
          });
          container.appendChild(row);
        });
      })();

      // ── Toggle All
      var allExpanded = false;
      function toggleAll(btn) {
        allExpanded = !allExpanded;
        var headers = document.querySelectorAll(".domain-header, .topic-header");
        var bodies = document.querySelectorAll(".domain-body, .topic-body");

        headers.forEach((h) => h.classList.toggle("open", allExpanded));
        bodies.forEach((b) => b.classList.toggle("open", allExpanded));

        btn.textContent = allExpanded ? "↕ COLLAPSE ALL" : "↕ EXPAND ALL";
      }
