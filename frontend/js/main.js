const API_BASE_DEV = "http://127.0.0.1:8000";
// TODO: Change the Development API to Production API

// Health Check

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

// PDF Upload

const pdf_upload_input = document.getElementById("pdf-upload-input");

pdf_upload_input.addEventListener("change", async (event) => {
    
    const files = event.target.files;
    if (files.length === 0) return;

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append("files", files[i]);
    }

    try {
        const response = await fetch(API_BASE_DEV + "/upload", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        display_pdf_metadata(data);
        console.log(data);
        // TODO : remove the console log
    } catch (error) {
        alert("Error uploading files");
        console.error("Error uploading files:", error);
    }   
});

const pdf_list = document.getElementById("pdf-upload-list")

function display_pdf_metadata(data) {
    
    for (let i = 0; i < data.files.length; i++){
        meta = data.files[i].meta
        size = meta.size / (1024*1024);
        unit = "MB";
        if (size < 1) {
            size = size * 1024;
            unit = "KB";
        }
        size = Number(size.toFixed(2));
        status = meta.upload_status;
        
        pdf_list.innerHTML += "<p>Filename : " + meta.filename + " <br> Size : " + size + " " + unit + " <br> No. of Pages : " + meta.pages + " <br> Upload Status : " + status + " <br> Text Extraction Status : " + meta.text_extraction_status +"</p>";

        if (status=="failed") {
            reason = meta.reason;
            pdf_list.innerHTML += "<p>Reason : "+reason+"</p>";
        }
    }

}


// Delete PDFs on leaving page

window.addEventListener("pagehide", () => { 
    navigator.sendBeacon(API_BASE_DEV + "/cleanup");
});