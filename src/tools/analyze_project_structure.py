import os
from .project_metrics import project_metrics


def analyze_project_structure(project_path):
    """
    Analyzes the project structure and provides recommendations.
    Gathers project file metrics for reporting.
    """
    analysis_report = {
        "summary": "Project Structure Analysis",
        "details": {"total_files": 0, "total_directories": 0, "directory_contents": {}},
        "recommendations": [],
    }
    try:
        if not os.path.isdir(project_path):
            return {"error": "Invalid project path provided."}
        for root, dirs, files in os.walk(project_path):
            analysis_report["details"]["total_files"] += len(files)
            analysis_report["details"]["total_directories"] += len(dirs)
            if root == project_path:
                analysis_report["details"]["directory_contents"] = {
                    "files": files,
                    "directories": dirs,
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
            analysis_report["recommendations"].append(
                "Project structure looks clean and well-organized."
            )
        # Gather project file metrics
        metrics = project_metrics.gather_project_files(project_path)
        analysis_report["metrics"] = metrics
    except Exception as e:
        analysis_report["error"] = f"An error occurred during analysis: {str(e)}"
    return analysis_report
