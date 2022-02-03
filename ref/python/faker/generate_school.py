#region imports
from faker import Faker
import pandas as pd
import random
from datetime import date
from json import dumps
#endregion


#region config
#region examples
'''
services = [
    "Hospice",
    "SNF",
    "Professional",
    "Outpatient",
    "Inpatient",
    "HHA",
    "DME",
]
cohorts = [0, 1, 2, 3, 4, 5, 6]
months = [1, 2, 3, 4, 5, 6]
{
    "service_component": service,
    "cohort": cohort,
    "months_before_death": month,
    "avg_cost": round(random.uniform(1000, 5000), 2) if cohort >= month else 0,
    "name": faker.name(),
    "address": faker.address(),
    "name": faker.name(),
    "email": faker.email(),
    "bs": faker.bs(),
    "address": faker.address(),
    "city": faker.city(),
    "state": faker.state(),
    "date_time": faker.date_between(date(2021, 8, 1), date(2021, 12, 1)),
    "paragraph": faker.paragraph(),
    "Conrad": faker.catch_phrase(),
    "randomdata": random.randint(1000, 2000),
    "randomfloat": round(random.uniform(10.1, 15.2), 2),
}
'''
#endregion
CREATE_PREDEFINED_LISTS_CODE = '''
gender_list = ['Male', 'Female', 'Unknown']
'''
CREATE_ROW_CODE = '''
{
    "name": faker.name(),
    "address": faker.address(),
    "city": faker.city(),
    "state": faker.state(),
    "birth_date": faker.date_between(date(2007, 8, 1), date(2012, 12, 1)),
    "gender": faker.words(1, gender_list, False)[0],
    "GPA": round(min(max(random.gauss(2.6, 2), 0), 4), 2),
}
'''
#endregion


#region functions
def create_rows(num_rows=1):
    faker = Faker()
    output = []
    exec(CREATE_PREDEFINED_LISTS_CODE)
    for _ in range(num_rows):
        row = eval(CREATE_ROW_CODE)
        output.append(row)
    return output

def main():
    df = pd.DataFrame(create_rows(100))
    df.to_csv('./python/faker/data.csv', index=False)
    


if __name__ =='__main__':
    main()

#end region


#region reference

#endregion