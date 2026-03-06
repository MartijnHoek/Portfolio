const container = document.getElementById("vehicleContainer");
const searchInput = document.getElementById("modelSearchInput");

let vehicleData = [];

// Fetch the JSON data
fetch('/data/vehicles.json')
    .then(response => {
        if (!response.ok) throw new Error("Failed to load vehicle data");
        return response.json();
    })
    .then(data => {
        vehicleData = data;
        renderVehicles(); // initial render
    })
    .catch(err => console.error(err));

// Helper function to sanitize names for URLs/file paths
function sanitizeName(name) {
    return name
        .replace(/[\/\\:*?"<>|&]/g, '') // remove invalid characters
        .replace(/\s+/g, '-')           // replace spaces with hyphens
        .toLowerCase();
}

// Render vehicles
function renderVehicles(filterText = "") {
    const text = filterText.toLowerCase();
    container.innerHTML = "";

    // Sort brands alphabetically
    const sortedBrands = vehicleData.slice().sort((a, b) =>
        a.name.toLowerCase().localeCompare(b.name.toLowerCase())
    );

    sortedBrands.forEach(brand => {
        const brandMatches = brand.name.toLowerCase().includes(text);
        const filteredModels = brand.models.filter(model =>
            model.name.toLowerCase().includes(text)
        );

        if (!brandMatches && filteredModels.length === 0 && filterText !== "") return;

        const brandBox = document.createElement("div");
        brandBox.className = "box";

        const brandHeader = document.createElement("h2");
        brandHeader.className = "box-header";
        brandHeader.textContent = brand.name;
        brandBox.appendChild(brandHeader);

        if (brand.description) {
            const desc = document.createElement("p");
            desc.textContent = brand.description;
            brandBox.appendChild(desc);
        }

        const modelsToShow = brandMatches ? brand.models : filteredModels;

        if (modelsToShow.length > 0) {
            // Sort models alphabetically
            const sortedModels = modelsToShow.slice().sort((a, b) =>
                a.name.toLowerCase().localeCompare(b.name.toLowerCase())
            );

            const ul = document.createElement("ul");
            ul.style.listStyleType = "square";
            ul.style.marginLeft = "20px";

            sortedModels.forEach(model => {
                const brandSafe = sanitizeName(brand.name);
                const modelSafe = sanitizeName(model.name);

                const li = document.createElement("li");
                li.innerHTML = `<a href="/pages/model/${brandSafe}/${brandSafe}-${modelSafe}.html">${model.name}</a>`;
                ul.appendChild(li);
            });

            brandBox.appendChild(ul);
        } else {
            const noModels = document.createElement("p");
            noModels.textContent = "No models match your search.";
            noModels.style.fontStyle = "italic";
            brandBox.appendChild(noModels);
        }

        container.appendChild(brandBox);
    });

    if (!container.hasChildNodes()) {
        const noResults = document.createElement("div");
        noResults.textContent = "No vehicles found for your search.";
        noResults.style.fontStyle = "italic";
        container.appendChild(noResults);
    }
}

// Search listener
searchInput.addEventListener("input", e => {
    renderVehicles(e.target.value);
});
