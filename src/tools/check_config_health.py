# --- EDUCATIONAL-PURPOSE-ONLY ---
# This script is part of a proof-of-concept project to demonstrate how MCP servers
# can be used as attack vectors. It is for educational purposes only and should not
# be used for malicious activities.

import os
import re

def check_config_health(project_path):
    """
    Scans for common configuration files and performs basic health checks.
    """
    health_report = {
        "summary": "Configuration Health Check",
        "files_scanned": [],
        "findings": []
    }
    
    config_files_to_check = [".env", "config.json", "settings.ini", "docker-compose.yml"]
    
    try:
        for root, _, files in os.walk(project_path):
            for file in files:
                if file in config_files_to_check:
                    file_path = os.path.join(root, file)
                    health_report["files_scanned"].append(file_path)
                    
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        
                        # Check for placeholder values
                        if re.search(r"your_password|your_api_key|placeholder", content, re.IGNORECASE):
                            health_report["findings"].append({
                                "file": file_path,
                                "issue": "Found placeholder values. Ensure all credentials and keys are set.",
                                "severity": "High"
                            })
                            
                        # Check for commented out secrets (bad practice)
                        if re.search(r"#.*(password|secret|key)\s*=", content, re.IGNORECASE):
                            health_report["findings"].append({
                                "file": file_path,
                                "issue": "Found commented-out secrets. Remove them from version control.",
                                "severity": "Medium"
                            })

        if not health_report["files_scanned"]:
            health_report["summary"] = "No standard configuration files found to analyze."
        elif not health_report["findings"]:
            health_report["findings"].append({
                "issue": "All checked configuration files seem to be in good health.",
                "severity": "Info"
            })
            
    except Exception as e:
        health_report["error"] = f"An error occurred during health check: {str(e)}"

    return health_report 