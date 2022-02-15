import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list')
print(data[0])
