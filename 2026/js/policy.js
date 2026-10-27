document.getElementById("accept-cookies").addEventListener("click", function() {
    // Hide the cookie consent banner
    document.getElementById("cookie-consent").style.display = "none";
    
    // Set a cookie to remember consent
    document.cookie = "cookieConsent=true; max-age=31536000; path=/"; // Expires in 1 year
});

// Check if the consent cookie exists
if (document.cookie.split(';').some((item) => item.trim().startsWith('cookieConsent='))) {
    document.getElementById("cookie-consent").style.display = "none";
}
