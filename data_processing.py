import json
from pathlib import Path
from pandas import read_csv
import numpy as np

base_path = Path(__file__).parent


##Useful data
#Convert country name to ISO3
file_path = (base_path / "harmonizing/name2iso3.json").resolve() #relative paths within script
with open(file_path,"r") as f:
    name2iso3 = json.loads(f.read())
#     name2iso3["Curaçao and Sint Maarten"] = "ANT" 
    name2iso3["Africa, other countries"] = "IRS_Other_Africa" 
    name2iso3["Americas, other countries"] = "IRS_Other_America" 
    name2iso3["Asia & Oceania, other countries"] = "IRS_Other_Asia_Oceania" 
    name2iso3["Europe, other countries"] = "IRS_Other_Europe" 
    name2iso3["Bolivia (Plurin. State of)"] = name2iso3["Bolivia"]
    name2iso3["Micronesia (Fed. States of)"] = name2iso3["Micronesia"] 
    name2iso3["Netherlands Antilles [former]"] = "ANT" 
    name2iso3["Sudan [former]"] = name2iso3["Sudan"] 
    name2iso3["Venezuela (Boliv. Rep. of)"] = name2iso3["Venezuela"] 
    name2iso3["Bonaire, St. Eustatius & Saba"] = "BES" 
    name2iso3["Côte d`Ivoire"] = name2iso3["Côte d'Ivoire"] 
    name2iso3["China, Taiwan"] = name2iso3["Taiwan"] 
    name2iso3["China, People`s Republic of"] = "CHN" 
    name2iso3["Columbia"] = name2iso3["Colombia"] #german spelling?


# import json
# with open(file_path, 'w') as fp:
#     json.dump(name2iso3, fp)

    
file_path = (base_path / "harmonizing/iso3_iso2_name.csv").resolve() #relative paths within script
iso32name = read_csv(file_path,sep="\t").set_index("iso3").to_dict()["name"]
iso32iso2 = read_csv(file_path,sep="\t").set_index("iso3").to_dict()["iso2"]
    
    
def iso3_to_name(iso3):
    """
    Returns ISO3 code of a country name
    """
    
    if iso32name.get(iso3) is None:
        print("{} not matched to any file".format(iso3))
        return iso3
    else:
        return iso32name[iso3]
    
def iso3_to_iso2(iso3):
    """
    Returns ISO3 code of a country name
    """
    
    if iso32iso2.get(iso3) is None:
        print("{} not matched to any file".format(iso3))
        return iso3
    else:
        return iso32iso2[iso3]
    

##Useful functions
def get_iso3(country_name,print_failure=True):
    """
    Returns ISO3 code of a country name
    """
    
    if name2iso3.get(country_name) is None:
        if print_failure == True:
            print("{} not matched to any file".format(country_name))
        return np.NaN#country_name
    else:
        return name2iso3[country_name]
    
    
def save_comps(filename,comment=None,sheet_name="Sheet1"):
    from openpyxl import load_workbook
    with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
        if comment is not None:
            startrow = 1
            w.write_string(0,1,comment)
        else:
            startrow = 0

        x.to_excel(writer,sheet_name=cf,startrow=startrow ,index=False,startcol=0)
        w = writer.sheets[cf]


    writer.save()
    writer.close()
