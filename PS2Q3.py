# ## Question 3

# #### a)

# +
url1 = "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT"
url2 = "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT"
url3 = "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT"
url4 = "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT"

NHANES_1112 = pd.read_sas(url1)
NHANES_1314 = pd.read_sas(url2)
NHANES_1516 = pd.read_sas(url3)
NHANES_1718 = pd.read_sas(url4)

NHANES_1112 = NHANES_1112.drop_duplicates(subset='SEQN')
NHANES_1314 = NHANES_1314.drop_duplicates(subset='SEQN')
NHANES_1516 = NHANES_1516.drop_duplicates(subset='SEQN')
NHANES_1718 = NHANES_1718.drop_duplicates(subset='SEQN')

NHANES_1112["cohort"] = "11-12"
NHANES_1314["cohort"] = "13-14"
NHANES_1516["cohort"] = "15-16"
NHANES_1718["cohort"] = "17-18"

NHANES_all = NHANES_1112.append(NHANES_1314, ignore_index = True)
NHANES_all = NHANES_all.append(NHANES_1516, ignore_index = True)
NHANES_all = NHANES_all.append(NHANES_1718, ignore_index = True)
# -

NHANES_all = NHANES_all[["cohort", "SEQN", "RIDAGEYR",
                         "RIDRETH3", "DMDEDUC2", "DMDMARTL",
                         "RIDSTATR", "SDMVPSU", "SDMVSTRA",
                         "WTMEC2YR", "WTINT2YR"]]

NHANES_all = NHANES_all.astype({"SEQN": pd.Int64Dtype(),
                                "RIDAGEYR": pd.CategoricalDtype(),
                                "RIDRETH3": pd.CategoricalDtype(),
                                "DMDEDUC2": pd.CategoricalDtype(),
                                "DMDMARTL": pd.CategoricalDtype(),
                                "RIDSTATR": pd.CategoricalDtype(),
                                "SDMVPSU": pd.CategoricalDtype(),
                                "SDMVSTRA": pd.CategoricalDtype()}) 
variable_list = ["SEQN", "RIDAGEYR", "RIDRETH3", "DMDEDUC2", "DMDMARTL",
                 "RIDSTATR", "SDMVPSU", "SDMVSTRA", "WTMEC2YR", "WTINT2YR"]
rename_list = ["unique_id", "age", "race_and_ethnicity", "education",
               "marital_status","intervew_and_exam_status", "pseudo-PSU",
               "pseudo-stratum","MEC_exam_weight", "interview weight"]
dic = dict(zip(variable_list, rename_list))
NHANES_all.rename(columns=dic)

NHANES_all.to_pickle("demographic.pickle")

# #### b)

# +
url5 = "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT"
url6 = "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT"
url7 = "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT"
url8 = "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT"

OHD_1112 = pd.read_sas(url5)
OHD_1314 = pd.read_sas(url6)
OHD_1516 = pd.read_sas(url7)
OHD_1718 = pd.read_sas(url8)

OHD_1112 = OHD_1112.drop_duplicates(subset='SEQN')
OHD_1314 = OHD_1314.drop_duplicates(subset='SEQN')
OHD_1516 = OHD_1516.drop_duplicates(subset='SEQN')
OHD_1718 = OHD_1718.drop_duplicates(subset='SEQN')

OHD_1112["cohort"] = "11-12"
OHD_1314["cohort"] = "13-14"
OHD_1516["cohort"] = "15-16"
OHD_1718["cohort"] = "17-18"

OHD_all = OHD_1112.append(OHD_1314, ignore_index = True)
OHD_all = OHD_all.append(OHD_1516, ignore_index = True)
OHD_all = OHD_all.append(OHD_1718, ignore_index = True)
# -

# Select targeted columns
lst = OHD_all.columns
variable_list_OHD = ["cohort", "SEQN", "OHDDESTS"]
temp_list = []
for item in lst:
    if re.match(r'OHX\d+\d+TC', item) or re.match(r'OHX\d+\d+CTC', item):
        variable_list_OHD.append(item)
        temp_list.append(item)
OHD_all = OHD_all[variable_list_OHD]

# Change Category
dic2 = {}
for item in variable_list_OHD:
    if item == "cohort":
        dic2[item] = pd.StringDtype()
    elif item == "SEQN":
        dic2[item] = pd.Int64Dtype()
    else:
        dic2[item] = pd.CategoricalDtype()
OHD_all = OHD_all.astype(dic2) 

# Rename
rename_list2 = []
for item in temp_list:
    if len(item) == 7:
        rename_list2.append("tooth count: " + item[3:5])
    else:
        rename_list2.append("coronal cavities tooth count: " + item[3:5])
dic3 = dict(zip(temp_list, rename_list2))
dic3["SEQN"] = "unique id"
dic3["OHDDESTS"] = "overall oral health status"
OHD_all.rename(columns=dic3)

OHD_all.to_pickle("oral_health.pickle")

# #### c)

# The number of case in the demographic datasets is:

NHANES_all.shape[0]

# The number of case in the oral health and dentition data is:

OHD_all.shape[0]