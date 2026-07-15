(() => {
  const tabRoot = document.querySelector("[data-tabs]");

  if (tabRoot) {
    const tabs = Array.from(tabRoot.querySelectorAll("[role='tab']"));
    const panels = Array.from(tabRoot.querySelectorAll("[role='tabpanel']"));

    const activateTab = (tab, moveFocus = false) => {
      const selected = tab.dataset.tab;

      tabs.forEach((candidate) => {
        const active = candidate === tab;
        candidate.setAttribute("aria-selected", String(active));
        candidate.tabIndex = active ? 0 : -1;
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset.panel !== selected;
      });

      if (moveFocus) tab.focus();
      window.history.replaceState(null, "", `#${selected}`);
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => activateTab(tab));
      tab.addEventListener("keydown", (event) => {
        let targetIndex = null;
        if (event.key === "ArrowRight") targetIndex = (index + 1) % tabs.length;
        if (event.key === "ArrowLeft") targetIndex = (index - 1 + tabs.length) % tabs.length;
        if (event.key === "Home") targetIndex = 0;
        if (event.key === "End") targetIndex = tabs.length - 1;
        if (targetIndex === null) return;
        event.preventDefault();
        activateTab(tabs[targetIndex], true);
      });
    });

    const requested = window.location.hash.slice(1);
    const requestedTab = tabs.find((tab) => tab.dataset.tab === requested);
    if (requestedTab) activateTab(requestedTab);
  }

  const copyText = async (value) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(value);
      return true;
    }

    const helper = document.createElement("textarea");
    helper.value = value;
    helper.setAttribute("readonly", "");
    helper.style.position = "fixed";
    helper.style.opacity = "0";
    document.body.appendChild(helper);
    helper.select();
    const copied = document.execCommand("copy");
    helper.remove();
    return copied;
  };

  document.querySelectorAll("[data-copy]").forEach((button) => {
    const label = button.querySelector("span:last-child");
    const original = label ? label.textContent : "Copy prompt";

    button.addEventListener("click", async () => {
      try {
        const copied = await copyText(button.dataset.copy || "");
        if (label) label.textContent = copied ? "Copied" : "Copy unavailable";
      } catch {
        if (label) label.textContent = "Copy unavailable";
      }

      window.setTimeout(() => {
        if (label) label.textContent = original;
      }, 1800);
    });
  });
})();
