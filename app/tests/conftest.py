import pytest
from datetime import datetime
import os
import requests

API_BASE_URL = "http://localhost:8000"  # adjust to your service URL

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only process results for the 'call' phase (actual test execution)
    if rep.when != "call":
        return

    status = "passed" if rep.passed else "failed" if rep.failed else "skipped"
    test_name = item.name
    nodeid = item.nodeid
    execution_time = datetime.now().isoformat()

    screenshot_path = None
    if rep.failed:  # only capture screenshot on failure
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screens", exist_ok=True)
            screenshot_path = f"reports/screens/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            try:
                import allure
                allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass

    # Send result to API (only once per test execution)
    try:
        payload = {
            "test_name": test_name,
            "nodeid": nodeid,
            "status": status,
            "execution_time": execution_time,
            "screenshot": screenshot_path if screenshot_path else None,
            "error_message": str(rep.longrepr) if rep.failed else None
        }
        requests.post(f"{API_BASE_URL}/results", json=payload, timeout=5)
    except Exception as e:
        print(f"⚠️ Could not store test result: {e}")
