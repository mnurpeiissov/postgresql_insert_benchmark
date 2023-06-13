import psycopg2
from utils import get_conn, profiler, path


@profiler
def cur_expert(conn, fp):
    with conn.cursor() as cursor:
        cursor.copy_expert('''
        COPY financial_year (
            Year                        ,
            Industry_aggregation_NZSIOC , 
            Industry_code_NZSIOC        , 
            Industry_name_NZSIOC        , 
            Units                       , 
            Variable_code               , 
            Variabel_name               , 
            Variable_category           , 
            Value                       ,
            Industry_code_ANZSIC06         
        ) FROM STDIN delimiter ',' csv header;''', fp)
    conn.commit()

if __name__ == '__main__':
    conn = get_conn() 
    with open(path, 'r') as fp:
        cur_expert(conn, fp)