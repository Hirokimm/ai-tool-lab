import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "owned_publisher.py"
spec = importlib.util.spec_from_file_location("owned_publisher", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def sample_item():
    return {
        "id": "owned-test-001",
        "status": "READY",
        "site": "ai-tool-lab",
        "slug": "safe-test",
        "title": "<Test> AI visibility",
        "description": "A & B",
        "published_at": "2026-10-24",
        "venture": "#002",
        "campaign": "owned_test",
        "content_id": "owned-test-001",
        "cta_target": "ai-search-audit",
        "cta_label": "Check",
        "sections": [{"heading": "H2", "paragraphs": ["<script>alert(1)</script>"]}],
        "sources": [{"label": "Source", "url": "https://example.com/source"}],
    }


class OwnedPublisherTests(unittest.TestCase):
    def test_publish_is_idempotent_and_escapes_html(self):
        manifest = {"schema_version": 1, "items": [sample_item()]}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            count1, changed1 = mod.publish(manifest, root)
            count2, changed2 = mod.publish(manifest, root)
            self.assertEqual((count1, changed1), (1, ["owned-test-001"]))
            self.assertEqual((count2, changed2), (0, []))
            page = (root / "insights" / "safe-test" / "index.html").read_text(encoding="utf-8")
            self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", page)
            self.assertNotIn("<script>alert(1)</script>", page)
            self.assertIn("t=ai-search-audit", page)
            receipts = json.loads((root / "data" / "owned_publish_receipts.json").read_text(encoding="utf-8"))
            self.assertIn("owned-test-001", receipts["items"])

    def test_rejects_unallowlisted_cta(self):
        item = sample_item()
        item["cta_target"] = "https://evil.example"
        with self.assertRaises(ValueError):
            mod._render_page(item)

    def test_rejects_unsafe_slug(self):
        item = sample_item()
        item["slug"] = "../escape"
        with self.assertRaises(ValueError):
            mod._render_page(item)


if __name__ == "__main__":
    unittest.main()
