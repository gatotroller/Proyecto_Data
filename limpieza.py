import pandas as pd
import numpy as np

data = pd.read_csv("jobs_data.csv")

# Cambio de nombre de columnas y agarrar esenciales
data.columns = ['id', 'salary', 'jobexperience', 'skills', 'industry', 'role']
data = data.iloc[:, 0:6]

# Limpieza del salario
data['salary'] = data['salary'].str.strip()
data['salary'] = data['salary'].replace('Not Disclosed by Recruiter', np.nan)
data['salary'] = data['salary'].apply(lambda x: x.rstrip('.') + '.' if isinstance(x, str) else x)

lb = []
ub = []

for index, salary in enumerate(data['salary']):
    numero = ''
    if isinstance(salary, str):
        for letter in salary:
            if letter.isnumeric():
                numero += letter
            elif letter == '-' or letter == '.':
                lb.append(int(numero))
                break
    else:
        lb.append(salary)

for index, salary in enumerate(data['salary']):
    agarrar = False
    numero = ''
    if isinstance(salary, str):
        for letter in salary:
            if agarrar:
                if letter.isnumeric():
                    numero += letter
                elif letter == 'P' or letter == '.':
                    ub.append(int(numero))
                    break
            elif letter == '-':
                agarrar = True
            elif letter == '.' and agarrar is False:
                for letter in salary:
                    if letter.isnumeric():
                        numero += letter
                ub.append(int(numero))
    else:
        ub.append(salary)

data['salary_lb'] = lb
data['salary_ub'] = ub
data.drop('salary', axis=1, inplace=True)

# Limpieza de la experiencia laboral
data['jobexperience'] = data['jobexperience'].str.strip()

experience = []

for exp in data['jobexperience']:
    yrs = ''
    for letter in exp:
        if letter.isnumeric():
            yrs += letter
        elif letter == '-':
            experience.append(int(yrs))

data['min_yrs'] = experience
data.drop('jobexperience', axis=1, inplace=True)

# Limpieza de skills
skills = data[['id', 'skills']].copy()
skills['skills'] = skills['skills'].apply(lambda x: [item.strip() for item in x.split('|')])
skills = skills.explode('skills', ignore_index=True)
data.drop('skills', axis=1, inplace=True)

# Limpieza final
data['industry'] = data['industry'].str.strip()
data['industry'] = data['industry'].str.replace('&', 'and')
data['industry'] = data['industry'].str.replace('/', ',')
data['industry'] = data['industry'].str.replace('   ', ' ')
data['industry'] = data['industry'].str.replace('  ', ' ')
data['industry'] = data['industry'].str.replace(' ,', ',')
data['role'] = data['role'].str.strip()
data['role'] = data['role'].str.replace('&', 'and')
data['role'] = data['role'].str.replace('/', ',')
data['role'] = data['role'].str.replace('   ', ' ')
data['role'] = data['role'].str.replace('  ', ' ')
data['role'] = data['role'].str.replace(' ,', ',')

# Guardado de datos
data.to_csv('data.txt', sep='@', index=False)
skills.to_csv('skills.txt', sep='@', index=False)
