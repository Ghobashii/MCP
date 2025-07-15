# --- EDUCATIONAL-PURPOSE-ONLY ---
# This script is part of a proof-of-concept project to demonstrate how MCP servers
# can be used as attack vectors. It is for educational purposes only and should not
# be used for malicious activities.

import os

def analyze_project_structure(project_path):
    """
    Analyzes the project structure and provides recommendations.
    In this simulation, it just counts files and directories.
    """
    analysis_report = {
        "summary": "Project Structure Analysis",
        "details": {
            "total_files": 0,
            "total_directories": 0,
            "directory_contents": {}
        },
        "recommendations": []
    }

    try:
        if not os.path.isdir(project_path):
            return {"error": "Invalid project path provided."}

        for root, dirs, files in os.walk(project_path):
            analysis_report["details"]["total_files"] += len(files)
            analysis_report["details"]["total_directories"] += len(dirs)
            
            # To keep it simple, we'll just list the contents of the root.
            if root == project_path:
                analysis_report["details"]["directory_contents"] = {
                    "files": files,
                    "directories": dirs
                }

        if analysis_report["details"]["total_files"] > 100:
            analysis_report["recommendations"].append(
                "Consider modularizing your project to reduce the number of files in the root directory."
            )
        
        if analysis_report["details"]["total_directories"] > 20:
            analysis_report["recommendations"].append(
                "Your project has a large number of directories. Ensure a clear and consistent naming convention is used."
            )
            
        if not analysis_report["recommendations"]:
            analysis_report["recommendations"].append("Project structure looks clean and well-organized.")

    except Exception as e:
        analysis_report["error"] = f"An error occurred during analysis: {str(e)}"

    return analysis_report 