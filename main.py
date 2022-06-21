import pandas as pd
import function as fc

df1 = pd.read_csv('only_wood_customer_us_1 (3).csv')
df2 = pd.read_csv('only_wood_customer_us_2.csv', sep=';')
df3 = pd.read_csv('only_wood_customer_us_3.csv', sep="\t|,", engine='python')
df2.columns = ['Age', 'City', 'Gender', 'Name', 'Email']

# TABLE 1
df1.drop(['UserName'], inplace=True, axis=1)
df1['FirstName'] = df1['FirstName'].apply(fc.replace_str)
df1['LastName'] = df1['LastName'].apply(fc.replace_str)
df1['Gender'] = df1['Gender'].apply(fc.sort_gender)
df1['City'] = df1['City'].apply(fc.replace_str2)
df1['Email'] = df1['Email'].str.lower()
df1['Country'] = 'USA'

# TABLE 2
df2['Age'] = df2['Age'].apply(fc.cut_age)
df2['City'] = df2['City'].apply(fc.replace_str2)
df2['Gender'] = df2['Gender'].apply(fc.sort_gender)
df2[['FirstName', 'LastName']] = df2.Name.str.split(pat=' ', expand=True)
df2.drop(['Name'], inplace=True, axis=1)
df2['FirstName'] = df2['FirstName'].apply(fc.replace_str)
df2['LastName'] = df2['LastName'].apply(fc.replace_str)
df2['Email'] = df2['Email'].str.lower()
df2['Country'] = 'USA'

# TABLE 3
df3['Gender'] = df3['Gender'].apply(fc.cut_gender)
df3[['FirstName', 'LastName']] = df3['Name'].str.split(pat=' ', expand=True)
df3['FirstName'] = df3['FirstName'].apply(fc.cut_str)
df3['LastName'] = df3['LastName'].apply(fc.replace_str)
df3.drop(['Name'], inplace=True, axis=1)
df3['Email'] = df3['Email'].apply(lambda x: str(x).replace('string_', '').lower())
df3['Age'] = df3['Age'].apply(lambda x: x.replace('integer_', '').replace('"', '')).apply(fc.cut_age)
df3['City'] = df3['City'].apply(fc.cut_str).apply(fc.replace_str2)
df3['Country'] = 'USA'

all_df = pd.concat([df1, df2, df3])
fc.csv_to_sql(all_df)