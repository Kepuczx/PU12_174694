import pandas as pd
import openpyxl

# s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s)
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# print(s['c'])
# print(s.c)
#
# print(df[0:2])
# print("")
#
# print(df['Populacja'])
# print(df.iloc[0, 0])
# print(df.loc[0, "Kraj"])
# print(df.at[0, "Kraj"])
# print(df.loc[0])
# print("")
#
# #wyswietli wszystkie wiersze z nazwa kraju z dopiskiem 'kraj: '
# print('kraj: ' + df.Kraj)
# #wyswietla losowy wiersz
# print(df.sample())
# print("")
# print(df.sample(2))
# print("")
# #frac wynik procentowy
# print(df.sample(frac=0.5))
# print("")
# #10 losowych, replace ustawiony na true oznacza powtarzalnosc
# print(df.sample(n=10, replace=True))
# print("")
# #pobiera pierwsze 5 wierszy
# print(df.head())
# print("")
# #pobiera ostatnie 5 wierszy
# print(df.tail())
# print("")
# print(df.describe())
# print("")
# print(df.T)
# print("")
#
# print(s[s>9])
#
# print(s.where(s > 10))
#
# print(s.where(s > 10, 'za duże'))
#
# seria = s.copy()
# #seria.where(seria > 10,'za duze',inplace=True)
# print('############')
# print(seria)
#
# print(s[~(s > 10)])
#
# print(s[(s < 13) & (s > 8)])
# print("")
# print("")
# print("")
# #
# # print(df[df['Populacja'] > 1200000000])
# # print("")
# # print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])
# #
# # print("########")
# # szukaj = ['Belgia', 'Brasilia']
# # print(df.isin(szukaj))
#
# s['e'] = 15
# print(s.e)
# s['f'] = 16
# print(s)
#
# df.loc[3] = 'dodane'
# print(df)
# print("")
# df.loc[4] = ['Polska','Warszawa', 38675467]
# print(df)
# print("")
# new_df = df.drop([3])
# print(new_df)
# print("")
#
# df.drop([3], inplace=True)
# print(df)
# print("")
# #axis ustawiony na 1 usuwa kolumny, domyslnie jest na 0 dlatego wywala wiersze
# #df.drop('Kraj', axis=1, inplace=True)
#
# print("")
#
# df['Kontynent'] = ['Europa','Azja','Ameryka Połudioniowa','Europa']
# print(df)
# print("")
# print(df.sort_values('Kraj'))
# print("")
# grouped = df.groupby(['Kontynent'])
# print(grouped.get_group('Europa'))
# print("")
# print(grouped.agg({'Populacja':['sum']}))


# df2 = pd.read_csv('iris.data', header=0)
#
# print(df2)

df = pd.read_excel(io='iris.xlsx')
print(df)



