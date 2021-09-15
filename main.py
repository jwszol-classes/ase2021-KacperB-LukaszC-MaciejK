
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import matplotlib.pyplot as plt
import numpy as np


spark = SparkSession.builder.appName('spark_test').getOrCreate()

entry_green_taxi_df_2019_5 = spark.read.csv("data/green_tripdata_2019-05.csv", header=True, inferSchema=True)
entry_yellow_taxi_df_2019_5 = spark.read.csv("data/yellow_tripdata_2019-05.csv", header=True, inferSchema=True)
entry_green_taxi_df_2020_5 = spark.read.csv("data/green_tripdata_2020-05.csv", header=True, inferSchema=True)
entry_yellow_taxi_df_2020_5 = spark.read.csv("data/yellow_tripdata_2020-05.csv", header=True, inferSchema=True)

# we need to extract passenger_count and payment_type
green_2019  = entry_green_taxi_df_2019_5.select(["passenger_count", "payment_type"])
yellow_2019  = entry_yellow_taxi_df_2019_5.select(["passenger_count", "payment_type"])
green_2020  = entry_green_taxi_df_2020_5.select(["passenger_count", "payment_type"])
yellow_2020  = entry_yellow_taxi_df_2020_5.select(["passenger_count", "payment_type"])

data_2020 = green_2020.union(yellow_2020)
data_temp = data_2020.union(green_2019)
data = data_temp.union(yellow_2019)

data_1_pass = data.filter("passenger_count == 1")
data_2_pass = data.filter("passenger_count == 2")
data_3_pass = data.filter("passenger_count == 3")
data_4_pass = data.filter("passenger_count == 4")
data_5andMore_pass = data.filter("passenger_count > 4")
our_frames = [data_1_pass,data_2_pass,data_3_pass,data_4_pass,data_5andMore_pass]


labels = ["Card","Cash","No charge","Dispute","Unknown"]
x = np.arange(len(labels))
width = 0.7
fig, ax = plt.subplots()

percentages_for_each_nr_of_pass = []
for passenger_count in our_frames:
    data_grouped_by_payment_type = passenger_count.groupBy("payment_type").count().sort("payment_type")
    total_num_of_payments = data_grouped_by_payment_type.agg(F.sum("count")).collect()[0][0]

    print(total_num_of_payments)
    data_with_percentage_column = data_grouped_by_payment_type.withColumn('Percentage', (100*data_grouped_by_payment_type['count'] / float(total_num_of_payments)))
    only_percentage_data = data_with_percentage_column.select(["Percentage"])
    zmienna = only_percentage_data.select('Percentage').rdd.flatMap(lambda x: x).collect()
    if len(zmienna)<5:
        zmienna.append(0)
    percentages_for_each_nr_of_pass.append(zmienna)
rects1 = ax.bar(x-width/5, percentages_for_each_nr_of_pass[0], width/5, label="1 passenger")
rects2 = ax.bar(x-2*width/5, percentages_for_each_nr_of_pass[1], width/5, label="2 passengers")
rects3 = ax.bar(x, percentages_for_each_nr_of_pass[2], width/5, label="3 passengers")
rects4 = ax.bar(x+width/5, percentages_for_each_nr_of_pass[3], width/5, label="4 passengers")
rects5 = ax.bar(x+2*width/5, percentages_for_each_nr_of_pass[4], width/5, label="5 or more")

ax.set_ylabel("Percentage of transactions")
ax.set_title("Percentages of transactions by number of passengers")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.show()
