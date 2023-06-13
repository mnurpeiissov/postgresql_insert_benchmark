from utils import get_conn

create_table = '''
    CREATE TABLE financial_year (
        Year                        smallint, 
        Industry_aggregation_NZSIOC text, 
        Industry_code_NZSIOC        text, 
        Industry_name_NZSIOC        text, 
        Units                       text, 
        Variable_code               text, 
        Variabel_name               text, 
        Variable_category           text, 
        Value                       text,
        Industry_code_ANZSIC06      text   
    )
'''

if __name__ == '__main__':
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute(create_table)
    conn.commit()
    conn.close()