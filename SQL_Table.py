from abc import ABC, abstractmethod

class SQL_Table(ABC):
    obj_file_path = None
    sql_file_path = None
    sql_table = None

    def __init__(self): pass

    @abstractmethod
    def to_sql_insert(): pass

