const API_BASE_DEV = "http://127.0.0.1:8000";

const health_check_btn = document.getElementById("health-check-btn");

async function check_health() {

    try { 
        const response = await fetch(API_BASE_DEV + "/health");
        const data = await response.json()

        document.getElementById("health-status").textContent = data.message;
        document.getElementById("health-status").style.color = "green";

    } catch (error) {
        document.getElementById("health-status").textContent = "Backend is not running";
        document.getElementById("health-status").style.color = "red";
    }

}

health_check_btn.addEventListener("click", check_health);