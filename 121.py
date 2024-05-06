import pandas as pd

# df = pd.read_excel('imiona.xlsx')
#
# print(df)
#
#
# print('#####################')
# #zad2.1
# print(df[df['Liczba']>1000])
# print('#####################')
# #zad2.2
#
# print(df[df['Imie'] == 'DOMINIK'])
# print('#####################')
# #zad2.3
#
# print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
# print('#####################')
# #zad2.4
#
# print(df[df.Rok < 2006].agg({'Liczba':['sum']}))
# print('#####################')
# #zad2.5
#
# print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
# print('#####################')
# #zad2.6
#
#
# popular_names = df.loc[df.groupby(['Rok', 'Plec'])['Liczba'].idxmax()]
#
# print(popular_names)
#
#
#
# print('#####################')
# #zad2.7
#
# print(df.loc[df.groupby(['Plec'])['Liczba'].idxmax()])
#



#zad3.1

#df = pd.read_excel('zamowienia.csv')


