import pandas as pd


def xlsx_file():
    data = {'Product': ['Cell Phone'],
            'Quantity': [10]}
    df = pd.DataFrame(data)

    df.to_excel('sells.xlsx', index=False)
    df = pd.read_excel("sells.xlsx")
    print(df)


xlsx_file()
