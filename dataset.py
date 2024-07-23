import pandas as pd


def get_country_data(dataset_path: str = "facts_countries.csv") -> pd.DataFrame:
    """Ucitava CSV datoteku na dataset_path putanji. Cisti podatke, uklanja NaN celije, transponira podatke u DataFrame-u i vraca formatirani DataFrame

    Args:
        dataset_path (str, optional): Putanja do CSV datoteke. Defaults to "facts_countries.csv".

    Returns:
        pd.DataFrame: DataFrame s pociscenim podacima
    """
    df = pd.read_csv(dataset_path, sep=";", skiprows=[1])

    for column in df.columns:
        df[column].fillna(0, inplace=True)

    df_transposed = df.transpose()  # zamjena redaka sa stupcima
    df_transposed.columns = df_transposed.iloc[0]  # osiguravamo ispravan naziv serija
    # osiguravamo ispravan format stupaca
    df_transposed.columns = map(str.lower, df_transposed.columns)
    df_transposed.columns = map(
        lambda column: column.replace(" ", "_"), df_transposed.columns
    )
    # uklanjamo duplikat
    df_transposed = df_transposed[1:]

    return df_transposed


if __name__ == "__main__":
    df = get_country_data()
    print(df)
