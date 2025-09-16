(async function() {
  const mount = document.getElementById('pubs');
  if (!mount) return;
  try {
    const res = await fetch('{{ "/assets/data/publications.json" | relative_url }}', {cache: "no-store"});
    if (!res.ok) throw new Error("Failed to load publications.json");
    const items = await res.json();
    if (!Array.isArray(items) || items.length === 0) {
      mount.innerHTML = '<p>No publications found yet.</p>';
      return;
    }
    // Render list
    const ul = document.createElement('ul');
    ul.className = 'pub-list';
    items.forEach(p => {
      const li = document.createElement('li');
      const title = p.title || "Untitled";
      const authors = p.authors ? `<span class="authors">${p.authors}</span>` : "";
      const venue = p.publication || p.journal || p.conference || "";
      const year = p.year ? ` (${p.year})` : "";
      const link = p.link || p.citation_url || null;
      const titleHtml = link ? `<a href="${link}" target="_blank" rel="noopener">${title}</a>` : title;
      li.innerHTML = `
        <div class="pub-item">
          <div class="pub-title">${titleHtml}${year}</div>
          <div class="pub-meta">${authors}${authors && (venue ? " · " : "")}${venue}</div>
        </div>`;
      ul.appendChild(li);
    });
    mount.appendChild(ul);
  } catch (e) {
    mount.innerHTML = '<p>Unable to load publications right now.</p>';
    console.error(e);
  }
})();