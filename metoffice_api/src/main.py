import traceback

import lumen

import requests
import xarray as xr
from datetime import datetime

try:
    current_day = str(datetime.now().day)
    current_month = str(datetime.now().month)
    current_year = str(datetime.now().year)
    order_id = "o154455352910"
    file_id = f"ground_diffuse-short-wave-radiation-flux_{current_year}{current_month}{current_day}00"

    url = f"https://api-metoffice.apiconnect.ibmcloud.com/1.0.0/orders/{order_id}/latest/{file_id}/data"

    payload={}
    headers = {
        'Accept': 'application/json',
        "Content-Type": "application/json",
        'X-IBM-Client-Id': '652ff1bac6e2554ced2230bdfa04fcc8',
        'X-IBM-Client-Secret': '83a47458c8f1ca3e284cf22065f47a99',
        'accept': 'application/x-grib'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    content = response.content
    f = open('data.grb', 'wb')
    f.write(content)
    f.close()

    ds = xr.open_dataset("data.grb", engine='cfgrib')
    print(ds.load())

    df = ds.to_dataframe()

    diffuse_results_dict = {}
    times = []
    irradiance = []
    indx = 0
    for index in df.index:
        if index[1] == 360 and index[2] == 243:
            diffuse_results_dict[str(df["valid_time"][indx])] = df.iloc[indx, 5]

        indx+=1

    output_dict = {}
    output_dict["diffuse_irradiance"] = diffuse_results_dict

    file_id = f"ground_direct-short-wave-radiation-flux_{current_year}{current_month}{current_day}00"
    url = f"https://api-metoffice.apiconnect.ibmcloud.com/1.0.0/orders/{order_id}/latest/{file_id}/data"
    response = requests.request("GET", url, headers=headers, data=payload)

    content = response.content
    f = open('data.grb1', 'wb')
    f.write(content)
    f.close()

    ds = xr.open_dataset("data.grb1", engine='cfgrib')
    print(ds.load())

    df = ds.to_dataframe()

    direct_results_dict = {}
    times = []
    irradiance = []
    indx = 0
    for index in df.index:
        if index[1] == 360 and index[2] == 243:
            direct_results_dict[str(df["valid_time"][indx])] = df.iloc[indx, 5]

        indx+=1
    
    output_dict["direct_irradiance"] = direct_results_dict
    lumen.save(output_dict)

except Exception as e:
    lumen.save_exception(traceback.format_exc())