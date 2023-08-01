from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import datetime
import os
import time
import shutil
import sys
import logging
import traceback
import subprocess
def print_welcome():
    welcome_string =  "\
 ___  _    _  _  _  _        _ _                                  \n\
| . \| |_ <_>| || |<_> ___  | \ | ___  _ _  ___                   \n\
|  _/| . || || || || || . \ |   |/ . \| | |<_> |                  \n\
|_|  |_|_||_||_||_||_||  _/ |_\_|\___/|__/ <___|                  \n\
                      |_|                                         \n\
 __ __                 _        ___                               \n\
|  \  \ ___  _ _  ___ <_>._ _  / __> ___  _ _  ___  ___  ___  _ _ \n\
|     |<_> || '_>/ . || || ' | \__ \/ | '| '_><_> || . \/ ._>| '_>\n\
|_|_|_|<___||_|  \_. ||_||_|_| <___/\_|_.|_|  <___||  _/\___.|_|  \n\
                 <___'                             |_|            \n\
__________________________________________________________________\n"

    introduction_string = \
"This application uses Python, Selenium and MS Edge WebDriver to scrape Margin Update documents. \n\
Check the accompanying User and Developer Guide for help. \n\
== Application Last Updated: August 2023 == \n\
__________________________________________________________________"
    
    print(welcome_string + introduction_string)
    # logging.info(welcome_string)
    
def init_logger(LOGS_DIRECTORY="", today="", save_logs=False):
    if save_logs:
        # store logs locally instead of just printing to stdout. 
        # Check if the logs directory already exists before creating it
        if not os.path.exists(LOGS_DIRECTORY):
            os.makedirs(LOGS_DIRECTORY)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(f"Logs\\{today}_debug.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )

    else:
        # Initialize logger that only prints to stdout
        logging.basicConfig(
            level=logging.INFO,
            format="> %(message)s",
            handlers=[
                logging.StreamHandler(sys.stdout)
            ]
        )

def copy_directory_with_xcopy(source, destination):
    try:
        # Form the xcopy command with appropriate options
        command = f'xcopy "{source}" "{destination}" /E /I /H /K /Y'

        # Run the xcopy command using subprocess
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logging.info("Directory copied successfully.")
    except subprocess.CalledProcessError as e:
        logging.info(f"Error occurred while copying directory: {e}")

def download_wait(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    time.sleep(3)
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload') or fname.endswith('.tmp'):
                dl_wait = True

        seconds += 1
    logging.info("%d sec waited to download", seconds)
    return seconds

def initialise_driver(webdriver_path, download_directory, temp_directory, eurex_only):   
    # Set Edge options to specify preferences
    edge_options = Options()
    edge_options.use_chromium = True
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging']) # exclude logs in terminal 
    edge_options.add_experimental_option("detach", True)
    edge_options.add_experimental_option("prefs", {"download.default_directory": download_directory,
                                                   "plugins.always_open_pdf_externally": True,})
    # edge_options.add_argument('--ignore-certificate-errors')
    # edge_options.add_argument("--headless")
    # edge_options.add_argument('--disable-dev-shm-usage')
    # edge_options.add_argument(f'--download.default_directory={download_directory}')
    # edge_options.add_argument("--remote-debugging-port=9222") # to fix MS Edge driver error: DevToolsActivePort file doesn't exist
    
    ### Make a copy of existing edge profile and use it instead of selenium creating a new profile at each launch
    ### Retains log in status so sites that require log in to download (e.g. CME) can function.
    if not eurex_only:
        source_dir = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Microsoft\\Edge\\User Data"
        logging.info("Copying over Edge Profile from '%s' to temp directory.", source_dir)
        try:
            # shutil.copytree(source_dir, temp_directory)
            copy_directory_with_xcopy(source_dir, temp_directory) # to overcome permission issues that shutil.copytree has
        except shutil.Error as err:
            logging.error(traceback.format_exc())
            
        # set the path to the profile directory
        edge_options.add_argument(f"user-data-dir=" + temp_directory)
        # specify the actual profile folder name
        edge_options.add_argument("profile-directory=Default")
    
    # Initialize the Edge WebDriver with the specified options
    ser = Service(webdriver_path)
    driver = webdriver.Edge(service = ser, options=edge_options)

    # Wait for the file to be downloaded (you may need to adjust the wait time based on the file size)
    # In this example, we wait for 10 seconds for the download to complete
    driver.implicitly_wait(10)
    
    # Settings - set NOT to open office files in browser
    driver.get('edge://settings/downloads')
    toggle = driver.execute_script('''
            return document.querySelector(' input[aria-label="Open Office files in the browser"]');
    ''')
    toggle.click()

    return driver

def rename_latest(download_directory, exchange_name):
    filepath = max([download_directory + "\\" + f for f in os.listdir(download_directory)], key=os.path.getctime)
    filename = filepath.split("\\")[-1]
    # logging.info(filename)
    new_filepath = os.path.join(download_directory, f"{exchange_name}_{filename}")
    shutil.move(filepath, new_filepath)
    return filename
    
def download_files(driver, download_directory, url, css_element, exchange_name, index=0):
    # Navigate to the URL where the download icon is located
    driver.get(url)

    ######### special cases ##########
    if url == "https://www.set.or.th/en/tch/rules-regulations/regulations":
        elements = driver.find_elements(By.CSS_SELECTOR, 'div[data-item-id="ef605c8e-a089-46b2-898b-d66812f966d4"]')
        driver.execute_script("arguments[0].click();", elements[0])
        elements = driver.find_elements(By.CSS_SELECTOR, 'div[data-item-id="a1e92b1b-ce8d-4dbb-89b0-a93d96d08df9"]')
        driver.execute_script("arguments[0].click();", elements[0])
        
    elif url == 'https://www.cmegroup.com/clearing/margins/outright-vol-scans.html#sortField=exchange&sortAsc=true&pageNumber=1':
        elements = driver.find_elements(By.CSS_SELECTOR, 'button.span1-button')
        driver.execute_script("arguments[0].click();", elements[0])
        
    elif url == "http://global.krx.co.kr/contents/GLB/06/0608/0608030700/GLB0608030700.jsp":
        file_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Listed Derivatives Margin Rate.xls")
        elements = driver.find_elements(By.XPATH, '//button[text()="File"]')
        i = 0
        while len(file_link) == 0 :
            if i >= len(elements):
                logging.info("Could not find KSE margin document.")
                break
            driver.execute_script("arguments[0].click();", elements[i])
            file_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Listed Derivatives Margin Rate.xls")
            i += 1
        logging.info("clicking link: %s", file_link[0].get_attribute('href'))
        driver.execute_script("arguments[0].click();", file_link[0])
        download_wait(download_directory, 20)
    ######### special cases END ##########
    
    if len(css_element) != 0:
        # Find all download links on the webpage
        download_links = driver.find_elements(By.CSS_SELECTOR, css_element)
        # logging.info("download links found: %s", str(map(download_links, lambda x : x.get_attribute('href'))))

        i = 3 # try to find the link a maximum of 3 times
        while len(download_links) == 0:
            if i == 0:
                logging.info("Could not find a download link for %s", exchange_name)
                return ""
            download_links = driver.find_elements(By.CSS_SELECTOR, css_element)
            i -= 1
                 
        link = download_links[index] # for ENPAR, there is a special case where we want only the second link (index = 1) 
        driver.execute_script("arguments[0].scrollIntoView();", link)

        if "TAIFEX" in exchange_name: # for logging purposes: since TAIFEX is a button, not link.
            logging.info("clicking link: %s", link.get_attribute('title'))
        else:
            logging.info("clicking link: %s", link.get_attribute('href'))
        
        ############# ENPAR special case again - to overcome download is not secure error ##############
        if url == 'https://www.lch.com/risk-management/risk-management-sa/sa-risk-notices':
            driver.get(link.get_attribute('href'))
        else: # general case
            driver.execute_script("arguments[0].click();", link)
        
        download_wait(download_directory, 20)

        # Rename the latest downloaded file to the desired filename
        downloaded_files = [download_directory + "\\" + f for f in os.listdir(download_directory)]
        sleep_counter = 5  # wait for 5 sec max before giving up on rename
        while len(downloaded_files) == 0:
            if sleep_counter == 0:
                logging.info("Could not rename file for %s", exchange_name)
                return ""
            time.sleep(1)
            downloaded_files = [download_directory + "\\" + f for f in os.listdir(download_directory)]
            sleep_counter -= 1

    
    filename = rename_latest(download_directory, exchange_name)
    return filename
    
def close_driver(driver):
    # Close the WebDriver
    driver.quit()    
    
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

################################################

def generateDict(eurex_only = False):
    my_dict = dict() # KEY is [exchange name], VALUE is tuple of ([url], [css_element])

    # COMPLETED
    # 1
    my_dict['EUREX'] = ('https://www.eurex.com/ec-en/services/risk-parameters/', 
                    'a[href$="IndicativePrismaMarginRequirements.xls"]', 0)
    
    if eurex_only == False:
        # 2 
        my_dict['CME'] = ('https://www.cmegroup.com/clearing/margins/outright-vol-scans.html#sortField=exchange&sortAsc=true&pageNumber=1',
                        'a.btn.download-margins', 0)
        # 3
        my_dict['SGX'] = ('https://www2.sgx.com/derivatives/risk-management#Margin%20Schedule',
                        'a[href$=".xlsx"]', 0)
        # 4
        my_dict['DGCX'] = ('http://www.dgcx.ae/initial-margins',
                        'a[href$=".xlsx"]', 0)
        # 5
        my_dict['IPE'] = ('https://www.theice.com/clear-europe/risk-management#margins-europe', 
                        'a[href*="ENERGY_MARGIN_SCANNING"]', 0)    
        # 6
        my_dict['LIFFE'] = ('https://www.theice.com/clear-europe/risk-management#margin-liffe', 
                        'a[href*="LIFFE_MARGIN_SCANNING"]', 0)      
        # 7                 
        my_dict['TURDEX'] = ('https://www.takasbank.com.tr/en/resources/bistech-risk-parameters', 
                        'a[href$=".xlsx"]', 0)    
        # 8
        my_dict['IFSG'] = ('https://www.theice.com/clear-singapore/risk-management', 
                        'a[href*="ICSG_MARGIN_SCANNING"]', 0)   
        # 9 
        my_dict['HKFE'] = ('https://www.hkex.com.hk/Services/Clearing/Listed-Derivatives/Risk-Management/Margin/Margin-Tables?sc_lang=en', 
                        'a[href*="HKCC_Margin_Levels_Eng.xlsx"]', 0) 
        # 10
        my_dict['OSE&TSE'] = ('https://www.jpx.co.jp/jscc/en/index.html', 
                            'a[href$=".xls"]', 0)
        # 11
        my_dict['ICEUS'] = ('https://www.theice.com/clear-us/risk-management#margin-rates', 
                        'a[href*="ICUS_MARGIN_SCANNING"]', 0)   
        # 12
        my_dict['KSE'] = ('http://global.krx.co.kr/contents/GLB/06/0608/0608030700/GLB0608030700.jsp', '', 0)   
        
        # 13
        my_dict['SFE'] = ('https://www2.asx.com.au/markets/clearing-and-settlement-services/asx-clear-futures', 
                        'a[href*="/margin-rates.pdf"]', 0)   
        # 14
        my_dict['TIFFEE'] = ('https://www.tfx.co.jp/en/historical/futures/spparam.html', 
                            'a[href$=".pdf"]', 0)  
        # 15.1
        my_dict['TAIFEX - GOLD'] = ('https://www.taifex.com.tw/enl/eng5/goldMargining', 
                                    'input[value="Download"]', 0)
        # 15.2
        my_dict['TAIFEX - INDEX'] = ('https://www.taifex.com.tw/enl/eng5/indexMargining',
                                    'input[value="Download"]', 0)
        # 15.3
        my_dict['TAIFEX - FX'] = ('https://www.taifex.com.tw/enl/eng5/fXMargining',
                                'input[value="Download"]', 0)                    
        # 16 
        my_dict['TIFEX'] = ('https://www.set.or.th/en/tch/rules-regulations/regulations', 
                        'a[href*="Margin_Announcement"]', 0)                
        # 17
        my_dict['LME'] = ('https://www.lme.com/en-GB/LME-Clear/Risk-management/Margin-Parameter-files', 
                        'a[href*="LME-Clear-Margin-Parameters"]', 0)                          
        # 18
        my_dict['ENPAR'] = ('https://www.lch.com/risk-management/risk-management-sa/sa-risk-notices', 
                        'a[href*="noticecash_derives"]', 1)                          
    return my_dict

##########################################
# Initialise variables
today = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S') # Today's date in YYYY-MM-DD_HHMMSS format - used for file naming
WEBDRIVER_PATH = resource_path('./driver/msedgedriver.exe') # Set the path to the Edge WebDriver executable
DOWNLOAD_DIRECTORY = os.path.join(os.getcwd(), f"Downloads\\Margins_Downloaded_on_{today}") # Set the path to download dir
TEMP_DIRECTORY = os.path.join(os.getcwd(), "temp") # Set the path to temp dir
LOGS_DIRECTORY = os.path.join(os.getcwd(), f"Logs") # Set the path to logs dir


def main():
    # Initialise logger
    init_logger(LOGS_DIRECTORY=LOGS_DIRECTORY, today=today, save_logs=False)

    # Check if user wants to download eurex only
    user_input = input(">>> Download EUREX only? Y/N  ")
    eurex_only = "y" in str.lower(user_input)

    # Check if the download directory already exists before creating it
    if not os.path.exists(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)
        logging.info("Download Directory '%s' created successfully.", DOWNLOAD_DIRECTORY)
    else:
        logging.info("Download Directory '%s' already exists.", DOWNLOAD_DIRECTORY)

    # remove temp directory
    if os.path.exists(TEMP_DIRECTORY):
        logging.info("Removing leftover temp directory.")
        remove_temp_dir()
    driver = initialise_driver(WEBDRIVER_PATH, DOWNLOAD_DIRECTORY, TEMP_DIRECTORY, eurex_only)

    # Generate the dictionary data structure
    if eurex_only:
        my_dict = generateDict(eurex_only=True)
        logging.info("Downloading from EUREX only.")
    else:
        my_dict = generateDict()
        list_of_brokers = my_dict.keys()
        logging.info("Downloading from all brokers: %s", str(list(list_of_brokers)))

    logging.info("Saving documents into: %s", DOWNLOAD_DIRECTORY)

    # Loop through dictionary and download the files
    list_of_files = []
    for exchange in my_dict:
        url = my_dict[exchange][0]
        css_element = my_dict[exchange][1]
        index = my_dict[exchange][2]
        
        try:
            downloaded_file = download_files(driver, DOWNLOAD_DIRECTORY, url, css_element, exchange, index=index)
        except Exception as err:
            logging.info(traceback.format_exc())
        
        list_of_files.append(downloaded_file)

    logging.info("List of files downloaded: %s", str(list_of_files))
    logging.info("Documents saved into: %s", DOWNLOAD_DIRECTORY)
    close_driver(driver)
    remove_temp_dir()

def remove_temp_dir():
    # delete temp profile
    try:
        if os.path.exists(TEMP_DIRECTORY):
            shutil.rmtree(TEMP_DIRECTORY)
            logging.info(f"Directory '{TEMP_DIRECTORY}' deleted successfully.")
    except Exception as e:
        logging.info(f"Error occurred while deleting temp directory: {e}")
        
####################################################################
# MAIN
try:
    print_welcome()
    main()
finally:
    remove_temp_dir() 