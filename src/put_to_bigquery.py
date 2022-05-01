"""
BigQueryへInsert
"""

import os
import pandas as pd

from authenticate_with_sa import authenticate_with_sa

DATA_DIR = './data'

def put_to_bigquery():
    """put_to_bigquery
    
    BigQueryへinsert
    ※ テーブルは存在している前提
    """
    # 認証
    cred = authenticate_with_sa()
    
    # 元データ
    # 型: 整数, 文字列, Float, 日時(タイムスタンプ)
    df = pd.read_csv(f'{DATA_DIR}/test_table1_data.csv', encoding='utf-8')
    # 日時は明示的にdatetimeにしないと、to_gbq()の内部でintにしようとして、下記のエラーになる
    #   pyarrow.lib.ArrowTypeError: object of type <class 'str'> cannot be converted to int
    df['col4'] = pd.to_datetime(df['col4'])
    #print(df.dtypes)
    #print(df.head())
    
    # Insert
    dest_table = 'test_dataset1.test_table1'
    tab_schema = [
        {'name': 'col1', 'type': 'INTEGER'},
        {'name': 'col2', 'type': 'STRING'},
        {'name': 'col3', 'type': 'FLOAT'},
        {'name': 'col4', 'type': 'TIMESTAMP'},
    ]
    proj_id = 'tmp-20220501'
    df.to_gbq(
        destination_table=dest_table,
        if_exists='append',
        table_schema=tab_schema,
        project_id=proj_id,
        credentials=cred
    )


if __name__=='__main__':
    put_to_bigquery()
    