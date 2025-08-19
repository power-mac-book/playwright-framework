from playwright.sync_api import Page, TimeoutError

def smart_click(page: Page, selector: str, hint_text: str | None = None, timeout=3000):
    try:
        page.click(selector, timeout=timeout)
        return
    except TimeoutError:
        pass
    # basic fallbacks: text-based and role-based
    if hint_text:
        try:
            page.get_by_text(hint_text, exact=True).click(timeout=timeout)
            return
        except TimeoutError:
            pass
    # heuristic: try button with text substring
    if hint_text:
        try:
            page.get_by_role("button", name=hint_text).click(timeout=timeout)
            return
        except TimeoutError:
            pass
    # last resort: visible button
    try:
        page.locator("button:visible").first.click(timeout=timeout)
    except TimeoutError as e:
        raise AssertionError(f"smart_click failed for '{selector}' (hint='{hint_text}')") from e

def smart_fill(page: Page, selector: str, value: str, hint_label: str | None = None, timeout=3000):
    try:
        page.fill(selector, value, timeout=timeout)
        return
    except TimeoutError:
        pass
    # fallback: label locator
    if hint_label:
        try:
            page.get_by_label(hint_label).fill(value, timeout=timeout)
            return
        except TimeoutError:
            pass
    # fallback: placeholder heuristic
    if hint_label:
        try:
            page.get_by_placeholder(hint_label).fill(value, timeout=timeout)
            return
        except TimeoutError:
            pass
    raise AssertionError(f"smart_fill failed for '{selector}' (label='{hint_label}')")
