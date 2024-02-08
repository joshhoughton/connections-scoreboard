window.onload = function() {
    var darkColors = [
        "#000000", // Black
        "#1A1A1A", // Very Dark Gray
        "#333333", // Dark Charcoal
        "#4F4F4F", // Gray
        "#660000", // Dark Red
        "#006600", // Dark Green
        "#000066", // Dark Blue
        "#660066", // Dark Purple
        "#006666", // Dark Cyan
        "#663300", // Dark Brown
        "#003366", // Dark Azure
        "#330066", // Dark Indigo
        "#336600", // Dark Lime
        "#660033"  // Dark Maroon
    ];    
    var randomColor = darkColors[Math.floor(Math.random() * darkColors.length)];
    document.body.style.backgroundColor = randomColor;
};