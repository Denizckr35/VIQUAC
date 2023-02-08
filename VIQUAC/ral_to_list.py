import pandas as pd
def ral_dict(file_name):
    try:
        df=pd.read_csv(file_name)
        new_name_column=[]
        for col in df.columns:
            a=col.replace(" ","")
            df[a]=df[col]
            new_name_column.append(a)
        RAL={}
        ral_numbers=[]
        len_asagı_yon=len(df["RGB"])
        liste=[]
        for column in df:
            liste.append(df[column].values)
        for i in range(len_asagı_yon):
            rgb=[int(n) for n in liste[1][i].split("-")]
            #avg=np.average(rgb)
            ral_numbers.append((liste[0][i].split(" "))[1])
            RAL[(liste[0][i].split(" "))[1]]=[liste[4][i],rgb]
        return ral_numbers,RAL

    except Exception as e:
        print(e)