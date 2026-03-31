function toggleCert(header) {
  const body = header.nextElementSibling;
  const isOpen = body.classList.contains('open');
  header.classList.toggle('open', !isOpen);
  body.classList.toggle('open', !isOpen);
}

function toggleTopic(header) {
  const body = header.nextElementSibling;
  header.classList.toggle('open');
  body.classList.toggle('open');
}

function filterCert(cert) {
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
  event.target.classList.add('active');
  document.querySelectorAll('.cert-section').forEach(s => {
    if (cert === 'all' || s.dataset.cert === cert) {
      s.classList.remove('hidden');
    } else {
      s.classList.add('hidden');
    }
  });
}

function renderCloudStack() {
  const container = document.getElementById('cloud-stack-rows');
  if (!container) return;

  // Clear existing content if any
  container.innerHTML = '';

  const layers = ["Applications", "Data", "Runtime", "Middleware", "OS", "Virtualization", "Servers", "Storage", "Networking"];
  const onprem = [1, 1, 1, 1, 1, 1, 1, 1, 1];
  const iaas = [1, 1, 1, 1, 1, 0, 0, 0, 0];
  const paas = [1, 1, 0, 0, 0, 0, 0, 0, 0];
  const saas = [0, 0, 0, 0, 0, 0, 0, 0, 0];

  layers.forEach(function (l, i) {
    const row = document.createElement('div');
    row.style.cssText = 'display:flex;gap:0;margin-bottom:3px;align-items:stretch';

    const label = document.createElement('div');
    label.style.cssText = 'width:130px;font-size:11.5px;color:#cdd9f0;padding:6px 4px 6px 0;flex-shrink:0;font-weight:500';
    label.textContent = l;
    row.appendChild(label);

    const values = [
      [onprem[i], 'rgba(255,77,109,.12)', '#ff4d6d', 'rgba(255,77,109,.25)'],
      [iaas[i], 'rgba(255,176,32,.08)', '#ffb020', 'rgba(255,176,32,.2)'],
      [paas[i], 'rgba(0,212,255,.08)', '#00d4ff', 'rgba(0,212,255,.2)'],
      [saas[i], 'rgba(0,255,153,.08)', '#00ff99', 'rgba(0,255,153,.2)']
    ];

    values.forEach(function (v) {
      const cell = document.createElement('div');
      cell.style.cssText = 'flex:1;text-align:center;padding:5px;font-size:11px;font-weight:600;border-radius:3px;margin:0 2px;background:' + (v[0] ? v[1] : 'rgba(255,255,255,.03)') + ';color:' + (v[0] ? v[2] : '#3a4a60') + ';border:1px solid ' + (v[0] ? v[3] : 'rgba(255,255,255,.06)');
      cell.textContent = v[0] ? 'Customer' : 'Provider';
      row.appendChild(cell);
    });

    container.appendChild(row);
  });
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', function () {
  renderCloudStack();
});
