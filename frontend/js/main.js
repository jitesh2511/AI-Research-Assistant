const API_BASE_DEV = "http://127.0.0.1:8000";

const health_check_btn = document.getElementById("health-check-btn");

async function check_health() {
    
    const response = await fetch(API_BASE_DEV + "/health");
    const data = await response.json()

    document.getElementById("health-status").textContent = data.message;

}

health_check_btn.addEventListener("click", check_health);