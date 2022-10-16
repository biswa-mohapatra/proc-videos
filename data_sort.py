import pandas as pd

def sort_the_data(data):
    pass
def inference(data_path:str,column_name:str)->dict:
    try:
        data = pd.read_csv(data_path)

        return data[f"{column_name}"].value_counts()
    except Exception as e:
        return {"inference module Error Message":f"{e}"}        