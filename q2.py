    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime, timedelta
    import json
    import pandas as pd
    from sqlalchemy import create_engine   

    def sql_create_table():  
        engine = create_engine('postgresql://localhost/macbookpro15')
        product_table = """
            CREATE TABLE IF NOT EXISTS products_table (
                    id char(50) NOT NULL,
                    type char(100) NOT NULL,
                    name char(100) NOT NULL,
                    ppu DECIMAL,                
                    batters json,
                    topping json)    
            PARTITION BY LIST(name);    
            
            TRUNCATE TABLE products_table;
        """
        engine.execute(product_table)

    def etl_and_insert():
        f = open('source_json.json')
        data = json.load(f)
        df = pd.DataFrame(data)
        df['batters'] = [d.get('batter') for d in df['batters']]
        df['batters'] = list(map(lambda x: json.dumps(x), df['batters']))
        df['topping'] = list(map(lambda x: json.dumps(x), df['topping']))

        sql_create_table()
        engine = create_engine('postgresql://localhost/macbookpro15')
        df.to_sql('products_table', engine,if_exists='append    ',index=False)
        
    default_args = {
        "owner": "airflow",
        "start_date": datetime.today() - timedelta(days=1)
                }
    with DAG(
        "kitabisa_q2",
        default_args=default_args,
        schedule_interval = "0 1 * * *",
        ) as dag:
            etl_and_insert = PythonOperator(
            task_id="etl_and_insert",
            python_callable=etl_and_insert
        )
    etl_and_insert