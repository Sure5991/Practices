from sqlalchemy import create_engine
import pandas as pd

'''
dialect+driver://username:password@host:port/database
'''

user_data = {
    'host':'localhost',
    'user':'root',
    'password':'Data100%40',
    'database':'datasets'
}

query = 'select * from loan_train'

def read_sql_to_df(user:dict,sql:str):
    engine = create_engine(f'mysql+pymysql://{user_data["user"]}:{user_data["password"]}@{user_data["host"]}:3306/{user_data["database"]}')
    df = pd.read_sql(query,engine)
    return df

def write_df_to_sql(user:dict,df,exist:str):
    engine = create_engine(f'mysql+pymysql://{user_data["user"]}:{user_data["password"]}@{user_data["host"]}:3306/{user_data["database"]}')
    df.to_sql('loan_train',con=engine,if_exists = exist, index = False)
    print('writing completed')
    return 0

if __name__ == '__main__':
    df = pd.read_csv('train.csv')
    write_df_to_sql(user_data,df,'replace')