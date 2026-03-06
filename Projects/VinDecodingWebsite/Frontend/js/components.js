document.addEventListener("DOMContentLoaded", () => {
    const includes = document.querySelectorAll("[data-include]");

    // Loads the navigation bar and footer
    includes.forEach(async (el) => {
        const file = el.getAttribute("data-include");
        try {
            const response = await fetch(file);
            if (!response.ok) throw new Error(`Cannot load ${file}`);
            el.innerHTML = await response.text();
        } catch (err) {
            el.innerHTML = `<p style="color:red;">Error loading ${file}</p>`;
        }
    });

    // Sidebar functions
    window.showSidebar = () => {
        const sidebar = document.querySelector('.sidebar');
        if (sidebar) sidebar.style.display = 'flex';
    };
    window.hideSidebar = () => {
        const sidebar = document.querySelector('.sidebar');
        if (sidebar) sidebar.style.display = 'none';
    };
});

