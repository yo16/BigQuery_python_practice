"""
サービスアカウントを使った認証
"""

from google.oauth2 import service_account

KEY_PATH = "./credentials/sa-credentials.json"

def authenticate_with_sa()->service_account.Credentials:
    # 参考
    # https://cloud.google.com/bigquery/docs/authentication/service-account-file
    credentials = service_account.Credentials.from_service_account_file(
        KEY_PATH, 
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    
    return credentials
