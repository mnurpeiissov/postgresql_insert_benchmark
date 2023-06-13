import time 
from functools import wraps
from memory_profiler import memory_usage
import psycopg2
import csv
from collections import OrderedDict
from dotenv import load_dotenv
import os

load_dotenv()


path = 'annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
cols = ['Year', 'Industry_aggregation_NZSIOC', 'Industry_code_NZSIOC',
        'Industry_name_NZSIOC', 'Units', 'Variable_code', 'Variable_name',
        'Variable_category', 'Value', 'Industry_code_ANZSIC06']


def get_conn():
    return psycopg2.connect(
        host = os.getenv('host'),
        port = os.getenv('port'),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database = os.getenv('database'),
        )


def profiler(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        fn_kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        print(f'\n{fn.__name__}({fn_kwargs_str})')
        start = time.perf_counter() 
        retval = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'Time {elapsed:0.4}')

        mem, retval = memory_usage((fn, args, kwargs), retval=True, timeout=500, interval=1e-7)
        print(f'Max memory {max(mem)}')
        print(f'Min memory {min(mem)}')
        return retval 
    return inner


def read_csv(fp, columns=None):
    for i, vals in enumerate(csv.reader(fp, dialect=csv.excel)):
        if columns is None:
            columns = vals
            continue
        elif i == 0:
            continue
        yield OrderedDict(zip(columns, vals))