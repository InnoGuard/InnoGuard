from ..config import Config
import pandas as pd
import browserhistory as bh # Used to extract Browsing History
from pysafebrowsing import SafeBrowsing # Uses Google's safe browsing API to test if websites are safe
from google.cloud import vision


API_KEY = Config.API_KEY
print(API_KEY)


def get_history():
    '''
    Gets all Browsing History from a Local Computer and inputs
    into a pandas array for analysis.

    :param sites: Accepts a list of sites from a pandas array
    :return: A pandas array of sites from Browsing History   
    '''
    dict_obj = bh.get_browserhistory()
    dict_obj.keys()
    # dict_keys(['safari', 'chrome', 'firefox'])
    # dict_obj['safari'][0]
    # Example Output: ('https://mail.google.com', 'Mail', '2018-08-14 08:27:26')
    # So for now, we would only need the first in the array
    bh.write_browserhistory_csv() # Writes history to a csv
    
    # Put history into Pandas Dataframe
    # df = pd.DataFrame(data=dict_obj)


def check_site(): # input websites
    '''
    Uses Google's Safe Browsing API to test if sites are safe
    A flag is raised if a site is malicious or inaproppriate for children

    :param sites: Accepts a list of sites from a pandas array
    :return: A flag is raised if a site is malicious and added to the pandas array       
    '''
    s = SafeBrowsing(API_KEY)
    r = s.lookup_urls(['http://malware.testing.google.test/testing/malware/'])
    print(r)


def main():
    # get_history()
    check_site()


if __name__ == '__main__':
    main()