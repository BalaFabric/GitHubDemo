# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "387c3f29-405d-4f9c-b7de-077c03d7c2a4",
# META       "default_lakehouse_name": "DWLakehouse",
# META       "default_lakehouse_workspace_id": "aa2a53d5-42a1-4309-adad-060058c42a82",
# META       "known_lakehouses": [
# META         {
# META           "id": "387c3f29-405d-4f9c-b7de-077c03d7c2a4"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

  DataValue = [(101, 'Venkat', 'Male', 343, 'HR Dept'),
            (102, 'Suresh', 'Female', 234, 'HR Dept'),
            (103, 'Pavani', 'Female', 7900, 'IT Dept'),
            (104, 'Rajesh', 'Male', 8767, 'Marketing Dept'),
            (105, 'Rithvik', 'Female', 4545, 'Finance Dept'),
            (106, 'Sravani', 'Male', 3434, 'Sales Dept'),
            (107, 'Bala', 'Male', 34, 'HR Dept'),
            (108, 'Subbu', 'Female', 3434, 'IT Dept'),
            (109, 'Malli', 'Female', 6767, 'Marketing Dept'),
            (110, 'Ravi', 'Female', 4343, 'Finance Dept'),
            (111, 'Anitha', 'Male', 4545, 'Sales Dept'),
            (112, 'Praveen', 'Male', 3334, 'HR Dept'),
            (113, 'Rao', 'Female', 2333, 'IT Dept'),
            (114, 'Hero', 'Female', 343,'Marketing Dept'),
            (115, 'Super', 'Male', 343, 'Finance Dept')]
SchemaValue = ["EmpId","EmpName","EmpGender","EmpSalary","EmpDept"]
df = spark.createDataFrame(data=DataValue,schema=SchemaValue)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format('delta').mode('append').saveAsTable('SalesData')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
