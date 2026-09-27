// Shared behaviour for every node dashboard.
// Each index.html sets: <body data-password="....">

document.addEventListener('DOMContentLoaded', function () {
  var root = document.documentElement;
  root.setAttribute('data-lang', 'bn');

  // ---- Language toggle ----
  var langBtn = document.getElementById('langToggle');
  if (langBtn) {
    langBtn.addEventListener('click', function () {
      var current = root.getAttribute('data-lang');
      var next = current === 'bn' ? 'en' : 'bn';
      root.setAttribute('data-lang', next);
      langBtn.textContent = next === 'bn' ? 'English' : 'বাংলা';
    });
  }

  // ---- Live Bangladesh time clock (UTC+6) ----
  var clockEl = document.getElementById('clock');
  function updateClock() {
    if (!clockEl) return;
    var now = new Date();
    var utc = now.getTime() + now.getTimezoneOffset() * 60000;
    var bd = new Date(utc + 6 * 3600000);
    var h = bd.getHours(), m = bd.getMinutes(), s = bd.getSeconds();
    var ampm = h >= 12 ? 'PM' : 'AM';
    var h12 = h % 12 === 0 ? 12 : h % 12;
    function pad(n) { return n < 10 ? '0' + n : n; }
    clockEl.textContent = pad(h12) + ':' + pad(m) + ':' + pad(s) + ' ' + ampm + ' (BD)';
  }
  updateClock();
  setInterval(updateClock, 1000);

  // ---- Lock screen ----
  var lock = document.getElementById('lock');
  var body = document.body;
  var expected = body.getAttribute('data-password');
  var input = document.getElementById('lockInput');
  var btn = document.getElementById('lockSubmit');
  var err = document.getElementById('lockError');

  function tryUnlock() {
    if (!input) return;
    if (input.value === expected) {
      lock.style.display = 'none';
    } else {
      err.textContent = 'ভুল পাসওয়ার্ড / Incorrect password';
      input.value = '';
      input.focus();
    }
  }
  if (btn) btn.addEventListener('click', tryUnlock);
  if (input) input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') tryUnlock();
  });
});
