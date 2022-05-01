"""
BigQueryから情報を得る
"""

import pandas as pd

from authenticate_with_sa import authenticate_with_sa


def get_from_bigquery():
    """get_from_bigquery
    
    BigQueryから情報を取得
    """
    # 認証
    cred = authenticate_with_sa()
    
    # クエリ
    proj_id = 'tmp-20220501'
    query = "SELECT * FROM `tmp-20220501.test_dataset1.owid-covid-data`"
    df = pd.read_gbq(query, project_id=proj_id, credentials=cred)
    print(df.head())


if __name__=='__main__':
    get_from_bigquery()
    