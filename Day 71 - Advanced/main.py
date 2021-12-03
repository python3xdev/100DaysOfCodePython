# import pandas as pd

# df = pd.read_csv("salaries_by_college_major.csv")

# print(df.head())  # prints out the first five rows of data
# print(df.shape)  # (51, 6) -> (rows, columns)
# print(df.columns)  # return all the names of the columns
# print(df.isna())  # shows True if a container has a NAN (Not A Number) value, if container is a number then its False
# print(df.tail())  # prints out last five rows of data

# clean_df = df.findna()  # finds the NaN values
# clean_df = df.dropna()  # removes the NaN values
# print(clean_df.tail())

# print(clean_df['Starting Median Salary'])  # returns all values in that column
# print(clean_df['Starting Median Salary'].max())  # returns the highest number from all the results
# print(clean_df['Starting Median Salary'].idxmax())  # get the id of the highest number

# print(clean_df['Undergraduate Major'].loc[43])  # get the name of the major that is on row 43
# OR
# print(clean_df['Undergraduate Major'][43])  # get the name of the major that is on row 43

# print(clean_df.loc[43])  # Not specifying a column will return the whole row


# print(clean_df["Mid-Career Median Salary"].max())
# print(clean_df["Mid-Career Median Salary"].idxmax())
# print(clean_df['Undergraduate Major'].loc[clean_df["Mid-Career Median Salary"].idxmax()])
# print('-' * 10)
# print(clean_df["Starting Median Salary"].min())
# print(clean_df["Starting Median Salary"].idxmax())
# print(clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmin()])
# print('-' * 10)
# print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])  # returns the career with lowest Mid-Career salary



# spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# clean_df.insert(1, "Spread", spread_col)  # .insert(col_position, col_title, col_data_frame)
# # print(clean_df.head())



# low_risk = clean_df.sort_values('Spread')  # by default ascending=True
# print(low_risk[['Undergraduate Major', 'Spread']].head())
#
# print('-' * 10)
# highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
#
# print('-' * 10)
#
# high_spread = clean_df.sort_values('Spread', ascending=False)  # high - > low
# print(high_spread[['Undergraduate Major', 'Spread']].head())

# Grouping
# print(clean_df.groupby('Group').count())

# pd.options.display.float_format = '{:,.2f}'.format  # this will format the numbers into a more readable version
# print(clean_df.groupby('Group').mean())




# - - - Web Scraping Part - - -

import requests
from bs4 import BeautifulSoup
from time import sleep

all_table_data = {
    "Rank": [],
    "Major": [],
    "Degree Type": [],
    "Early Career Pay": [],
    "Mid-Career Pay": [],
    "High Meaning": []
}  # dict with lists
rank = 1


def get_page_table(page_id):
    global rank
    print(page_id)  # To know what page is currently being worked on...
    URL = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_id}"
    soup = BeautifulSoup(
        requests.get(URL).content,
        "html.parser"
    )
    table = soup.select_one("table.data-table tbody")
    sleep(0.5)
    if not table.text:
        return
    list_of_rows = table.select("tr")
    for row in list_of_rows:
        school_name = row.select_one(".csr-col--school-name span.data-table__value").text
        school_type = row.select_one(".csr-col--school-type span.data-table__value").text
        early_career_pay = row.select(".csr-col--right span.data-table__value")[0].text
        mid_career_pay = row.select(".csr-col--right span.data-table__value")[1].text
        high_meaning = row.select(".csr-col--right span.data-table__value")[2].text

        all_table_data["Rank"].append(rank)
        all_table_data["Major"].append(school_name)
        all_table_data["Degree Type"].append(school_type)
        all_table_data["Early Career Pay"].append(early_career_pay)
        all_table_data["Mid-Career Pay"].append(mid_career_pay)
        all_table_data["High Meaning"].append(high_meaning)
        rank += 1
    get_page_table(page_id + 1)


get_page_table(1)  # first page
print(all_table_data)

import pandas as pd

df = pd.DataFrame(all_table_data)
df.to_csv("updated_salaries_by_college_major.csv", index=False)





"""
<tr class="data-table__row"><td class="data-table__cell csr-col--rank"><span class="data-table__title">Rank<!--
 -->:</span><span class="data-table__value">1</span></td><td class="data-table__cell csr-col--school-name">
 <span class="data-table__title">Major<!-- -->:</span><span class="data-table__value">Petroleum Engineering</span></td>
 <td class="data-table__cell csr-col--school-type data-table__cell--hidden-mobile">
 <span class="data-table__title">Degree Type<!-- -->:</span><span class="data-table__value">Bachelors</span>
 </td><td class="data-table__cell csr-col--right"><span class="data-table__title">Early Career Pay<!-- 
 -->:</span><span class="data-table__value">$93,200</span></td><td class="data-table__cell csr-col--right">
 <span class="data-table__title">Mid-Career Pay<!-- -->:</span><span class="data-table__value">$187,300</span></td>
 <td class="data-table__cell csr-col--right"><span class="data-table__title">% High Meaning<!-- 
 -->:</span><span class="data-table__value">67%</span></td></tr>
"""

