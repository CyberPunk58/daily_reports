import pandas as pd
import openpyxl

#Путь к файлу
file_path  = 'table.xls'
df_dailytable = pd.read_excel(file_path)
#org = ['ООО "Клинико-диагностический центр МЕДИКЛИНИК"']
#Номера касс для Стасова
medi_kassi = [54276,92222,78036,617,41240,28775,28777,28776,17741,8014,27261]

#Фильтруем по номрам касс оставляя только нужные
filter_df = df_dailytable.loc[df_dailytable['Unnamed: 16'].isin(medi_kassi)]
#Создаем итоговый ДатаФрейм
new_df = pd.DataFrame(columns = ['Группировка', 'Итого'])

#Временная строка, для просмотра отфильтрованного списка
filter_df.to_excel('filter.xlsx', index = False)

#Группируем по первому столбцу и суммируем по столбцу оплата и прочим
grouped_df = filter_df.groupby('Итоговый отчет кассира по дням').agg({'Unnamed: 2': 'sum'}).reset_index()



#new_df = pd.concat([new_df, pd.DataFrame([new_row])])
org_file_path = 'medi.xlsx'

#print(new_df)

#итоговый файл
grouped_df.to_excel(org_file_path, index = False)


