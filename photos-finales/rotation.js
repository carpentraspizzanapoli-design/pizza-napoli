var state = Object.create(null);

function turn(id, deg) {
  var img  = document.getElementById(id);
  var card = document.getElementById("c" + id);
  var info = document.getElementById("d" + id);
  var cur  = state[id] ? state[id] : 0;
  var next = ((cur + deg) % 360 + 360) % 360;
  state[id] = next;
  img.style.transform = "rotate(" + next + "deg)";
  info.textContent = next + "°";
  card.className = next !== 0 ? "card changed" : "card";
  var n = 0;
  for (var k in state) { if (state[k] !== 0) n++; }
  document.getElementById("nb").textContent = n + " photo(s) modifiée(s)";
}

function save() {
  var lines = [];
  document.querySelectorAll(".card.changed").forEach(function(card) {
    var sid  = card.id.replace(/^c/, "");
    var src  = document.getElementById(sid).getAttribute("src");
    var rot  = state[sid];
    lines.push(src + " => " + rot + "deg");
  });
  var el = document.getElementById("output");
  if (lines.length === 0) {
    el.innerHTML = "Aucune photo à corriger.";
    return;
  }
  var html = "<b>" + lines.length + " rotation(s) à appliquer :</b><br><br>";
  lines.forEach(function(l) { html += l + "<br>"; });
  el.innerHTML = html;
}
