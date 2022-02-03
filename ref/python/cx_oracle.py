import cx_Oracle as cx
import pandas as pd

def get_mrn():
    conn = cx.connect(dsn = 'CLARITY_PRD')

    print("Successfully connected to CLARITY_PRD")

    cursor = conn.cursor()

    row_list = cursor.execute(
        """
        SELECT DISTINCT order_disp_info.rx_num_unfmtted_hx AS "Prescription Number",
            patient.pat_mrn_id AS MRN
        FROM clarity.order_disp_info
            INNER JOIN clarity.order_med ON order_med.order_med_id = order_disp_info.order_med_id
            INNER JOIN clarity.patient ON patient.pat_id = order_med.pat_id
        WHERE ROWNUM < 50
        """)
        
    df = pd.DataFrame([row_list])
    return df

df = get_mrn()
df.head(5)