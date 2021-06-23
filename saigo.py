import sqlite3
import csv

conn = sqlite3.connect('testdb')
curs = conn.cursor()

with open('./saigo.csv','w',encoding='utf-8-sig',newline='') as csv_file:
    sql ="select trv.ID, emp.EMP_NAME, trv.YEAR, trv.MONTH, sum(MONEYY) from  travel AS trv left join Employee2 as emp on trv.ID = emp.EMPLOYEE_NO group by trv.ID, trv.YEAR, trv.MONTH order by trv.ID ASC, trv.YEAR ASC, trv.MONTH ASC;"
    curs.execute(sql)


    writer = csv.writer(csv_file)
    writer.writerow(['ID','EMP_NAME','YEAR','MONTH','MONEY'])
    writer.writerows(curs.fetchall())
    conn.close()





