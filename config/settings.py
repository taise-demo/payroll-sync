import os

LEDGER_URL = os.environ.get("LEDGER_URL", "https://ledger.internal.example.com")
HR_DIRECTORY_URL = os.environ.get("HR_DIRECTORY_URL", "https://hr.internal.example.com")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
