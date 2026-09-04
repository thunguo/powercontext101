(function enhanceMintlifyPagination() {
  function titleFromPaginationLabel(label) {
    if (!label) {
      return "";
    }

    const matched = label.match(/^(?:上一页|下一页|Previous|Next):\s*(.+)$/);
    if (matched) {
      return matched[1].trim();
    }

    const index = label.indexOf(": ");
    if (index === -1) {
      return label.trim();
    }

    return label.slice(index + 2).trim();
  }

  function enhancePreviousLink(prev) {
    if (!prev || !prev.getAttribute("aria-label")) {
      return;
    }

    if (prev.querySelector("[data-component-part='pagination-title']")) {
      return;
    }

    if (prev.querySelector("[data-pc-pagination-title]")) {
      return;
    }

    const title = titleFromPaginationLabel(prev.getAttribute("aria-label"));
    if (!title) {
      return;
    }

    const titleNode = document.createElement("span");
    titleNode.setAttribute("data-pc-pagination-title", "");
    titleNode.className = "pagination-title";
    titleNode.textContent = title;
    prev.appendChild(titleNode);
  }

  function enhancePagination() {
    document
      .querySelectorAll("#pagination a[rel='prev']")
      .forEach(enhancePreviousLink);
  }

  function mutationTouchesPagination(mutations) {
    return mutations.some((mutation) => {
      if (mutation.target.closest?.("#pagination")) {
        return true;
      }

      return Array.from(mutation.addedNodes).some((node) => {
        if (node.nodeType !== 1) {
          return false;
        }

        return node.id === "pagination" || Boolean(node.querySelector?.("#pagination"));
      });
    });
  }

  function startPaginationObserver() {
    enhancePagination();

    const observer = new MutationObserver((mutations) => {
      if (mutationTouchesPagination(mutations)) {
        enhancePagination();
      }
    });

    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startPaginationObserver);
  } else {
    startPaginationObserver();
  }
})();
