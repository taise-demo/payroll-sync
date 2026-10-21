from app.auth import is_authorized


def test_clerk_can_post():
    assert is_authorized("clerk@example.com", "post_approval")


def test_clerk_cannot_export():
    assert not is_authorized("clerk@example.com", "export_ledger")
