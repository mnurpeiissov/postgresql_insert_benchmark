from utils import path, profiler, get_conn, read_csv, cols

@profiler
def insert_one_by_one(conn, data):
    with conn.cursor() as cursor:
        for i, row in enumerate(data):
            cursor.execute('''
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

            ''', row)
    conn.commit()

if __name__ == '__main__':
    conn = get_conn()
    conn.autocommit = False
    with open(path) as fp:
        rows = read_csv(fp, cols)
        insert_one_by_one(conn, rows)