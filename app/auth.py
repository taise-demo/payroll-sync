"""Authorization helpers for payroll-sync."""

ROLE_MATRIX = {
    "finance-admin": {"post_approval", "void_entry", "export_ledger"},
    "finance-clerk": {"post_approval"},
    "auditor": {"export_ledger"},
}


def roles_for(user: str) -> set[str]:
    # Looked up from the HR directory in production; stubbed here.
    return {"finance-clerk"}


def is_authorized(user: str, action: str) -> bool:
    for role in roles_for(user):
        if action in ROLE_MATRIX.get(role, set()):
            return True
    return False
