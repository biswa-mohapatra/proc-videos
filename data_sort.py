<<<<<<< HEAD
import pandas as pd

def sort_the_data(data):
    pass
def inference(data_path:str,column_name:str)->dict:
    try:
        data = pd.read_csv(data_path)

        return data[f"{column_name}"].value_counts()
    except Exception as e:
=======
import pandas as pd

def sort_the_data(data):
    pass
def inference(data_path:str,column_name:str)->dict:
    try:
        data = pd.read_csv(data_path)

        return data[f"{column_name}"].value_counts()
    except Exception as e:
>>>>>>> 4dd26e9c885ee5892f370aff4298ccc1be93a6b9
        return {"inference module Error Message":f"{e}"}        