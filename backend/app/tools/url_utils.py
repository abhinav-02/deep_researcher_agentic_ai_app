"""Utility functions for URL handling.

This module currently provides a ``clean_urls`` helper that normalises a list of URLs
by:
1. Keeping only ``http`` and ``https`` schemes.
2. Stripping query strings and fragments.
3. Removing duplicate entries while preserving order.

It is deliberately lightweight and has no external dependencies.
"""

from urllib.parse import urlparse, urlunparse


def clean_urls(urls: list[str]) -> list[str]:
    """Normalize and deduplicate a list of URLs.

    Args:
        urls: Raw URL strings, typically returned by a search function.

    Returns:
        A list of cleaned, unique URLs.
    """
    seen = set()
    cleaned: list[str] = []
    for u in urls:
        parsed = urlparse(u)
        if parsed.scheme not in {"http", "https"}:
            # Skip non‑web URLs such as mailto: or ftp:
            continue
        # Rebuild the URL without query and fragment, and strip trailing slash
        normalized = urlunparse(
            (parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", "")
        )
        if normalized not in seen:
            seen.add(normalized)
            cleaned.append(normalized)
    return cleaned