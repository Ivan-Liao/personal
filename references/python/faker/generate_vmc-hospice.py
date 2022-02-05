from faker import Faker
import pandas as pd
import random
from datetime import date
from json import dumps

pd.set_option("display.max_columns", 20)
# region faker and random to pandas df
faker = Faker()


def create_rows(num=1):
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
    output = []
    for service in services:
        for cohort in cohorts:
            for month in months:
                if service == 'Hospice':
                    output.extend(
                        [
                            {
                                "service_component": service,
                                "cohort": cohort,
                                "months_before_death": month,
                                "avg_cost": round(random.uniform(1000, 5000), 2) if cohort >= month else 0
                            }
                        ]
                    )
                else:
                    output.extend(

                        [
                            {
                                "service_component": service,
                                "cohort": cohort,
                                "months_before_death": month,
                                "avg_cost": round(random.uniform(1000, 5000), 2) 
                            }
                        ]
                    )
    return output


df = pd.DataFrame(create_rows(10))
print(df)
# endregion
df.to_csv('data.csv', index=False)