import os

LEDGER_URL = os.environ.get("LEDGER_URL", "https://ledger.internal.example.com")
HR_DIRECTORY_URL = os.environ.get("HR_DIRECTORY_URL", "https://hr.internal.example.com")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

# Local development shortcut so the ledger export works without SSO.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
