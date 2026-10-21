import datetime as dt


def post_entry(approval_id: str, actor: str) -> dict:
    return {
        "approval_id": approval_id,
        "posted_by": actor,
        "posted_at": dt.datetime.utcnow().isoformat() + "Z",
        "status": "posted",
    }
