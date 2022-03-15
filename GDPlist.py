#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('GDPlist.csv')
df.info()
#%%
df_2 = df.loc[:,['Continent','GDP (millions of US$)']]
df_2

# %%
plt.plot(df_2['Continent'] == 'South America')
plt.xlabel('GDP', fontsize = 14)
plt.show()

# %%
df['Country']= df['Country'].map(lambda x:x.lstrip('�'))
df

# %%
df_vn = df.loc[df['Country'] =='Vietnam']
df_vn

# %%
df_asia = df.loc[df['Country'].isin(['Vietnam',  'Indonesia', 'Cambodia', 'Thailand', 'Malaysia'])]
df_asia


# %%
df_asia = pd.concat([pd.DataFrame([['5 Country','Asia',df_asia['GDP (millions of US$)'].sum()]], columns=df_asia.columns),df_asia]).reset_index(drop=True)

# %%
plt.plot(df_asia['Country'], df_asia['GDP (millions of US$)'])
plt.show()

# %%
vn = df_asia['GDP (millions of US$)'][5]
asia = df_asia['GDP (millions of US$)'][0]
print('Tỉ lệ đóng góp GDP của VN so với 5 nước Asia là: ',(vn/asia)*100,'%')

# %%
