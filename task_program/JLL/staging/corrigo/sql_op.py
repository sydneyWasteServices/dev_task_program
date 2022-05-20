import textwrap as tw
class Sql_op:
    def __init__(self):
        return
    
    def truncateTable(
        self,
        curs : object,
        TB_name : str):

        sqlStatement = f"TRUNCATE TABLE [JLL].[dbo].[{TB_name}]"
        curs.execute(sqlStatement)


    def get_insert_statement(
        self,
        curs : object,
        sqlStatement : str,
        TB_name : str):

        cols_name = []
        q_marks = []

        curs.execute(sqlStatement)

        for row in curs.fetchall():
            cols_name.append(row[0])
        
        cols_name = [str(tw.wrap(name)).replace("'", "") for name in cols_name]

        cols_name_str = ",".join(cols_name)

        for value in range(len(cols_name)):
            q_marks.append("?")
        
        q_marks_str = ",".join(q_marks)

        statement = f"INSERT INTO [JLL].[dbo].[{TB_name}] ({cols_name_str}) VALUES ({q_marks_str})"
        print(statement)
        return statement


    def insert_data(
        self,
        curs : object,
        insert_statement : str,
        df : object ):
        
        print(df['BU Number'].dtype)
        for index, row in df.iterrows():
            id = index + 1
            print(row[1])
            
            curs.execute(insert_statement,
            id, row[0], row[1],row[2],row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10],
            row[11], row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])