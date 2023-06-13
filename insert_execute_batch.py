from utils import path, profiler, get_conn, read_csv, cols
import psycopg2.extras


@profiler 
def insert_execute_batch(conn, data):
    with conn.cursor() as cursor:
        psycopg2.extras.execute_batch(cursor, '''
                INSERT INTO financial_year (
                    Year                        ,
                    Industry_aggregation_NZSIOC , 
                    Industry_code_NZSIOC        , 
                    Industry_name_NZSIOC        , 
                    Units                       , 
                    Variable_code               , 
                    Variabel_name               , 
                    Variable_category           , 
                    Value                       ,
                    Industry_code_ANZSIC06  )
                SELECT 
                    %(Year)s as Year, 
                    %(Industry_aggregation_NZSIOC)s as Industry_aggregation_NZSIOC,
                    %(Industry_code_NZSIOC)s as Industry_code_NZSIOC,
                    %(Industry_name_NZSIOC)s as Industry_name_NZSIOC,
                    %(Units)s as Units, 
                    %(Variable_code)s as Variable_code,  
                    %(Variable_name)s as Variable_name,
                    %(Variable_category)s as Variable_category,
                    %(Value)s as Value, 
                    %(Industry_code_ANZSIC06)s as Industry_code_ANZSIC06

            ''', data)
    conn.commit()

if __name__ == '__main__':
    conn = get_conn()
    with open(path) as fp:
        rows = read_csv(fp, cols)
        insert_execute_batch(conn, rows)