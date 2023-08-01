---
layout: page
title: User Guide for Margin Scraper
---

# 1. Introduction

This user guide will help you effectively utilise the `margin_scraper.exe` application and troubleshoot any minor issues.

As of August 2023, the application downloads the latest margin update documents from the following exchanges:

|     | Exchange     | URL                                                                                                              |
|-----|--------------|------------------------------------------------------------------------------------------------------------------|
| 1   | EUREX        | 'https://www.eurex.com/ec-en/services/risk-parameters/'                                                          |
| 2   | CME          | 'https://www.cmegroup.com/clearing/margins/outright-vol-scans.html#sortField=exchange&sortAsc=true&pageNumber=1' |
| 3   | SGX          | 'https://www2.sgx.com/derivatives/risk-management#Margin%20Schedule'                                             |
| 4   | DGCX         | 'http://www.dgcx.ae/initial-margins'                                                                             |
| 5   | IPE          | 'https://www.theice.com/clear-europe/risk-management#margins-europe'                                             |
| 6   | LIFFE        | 'https://www.theice.com/clear-europe/risk-management#margin-liffe'                                               |
| 7   | TURDEX       | 'https://www.takasbank.com.tr/en/resources/bistech-risk-parameters'                                              |
| 8   | IFSG         | 'https://www.theice.com/clear-singapore/risk-management'                                                         |
| 9   | HKFE         | 'https://www.hkex.com.hk/Services/Clearing/Listed-Derivatives/Risk-Management/Margin/Margin-Tables?sc_lang=en'   |
| 10  | OSE&TSE      | 'https://www.jpx.co.jp/jscc/en/index.html'                                                                       |
| 11  | ICEUS        | 'https://www.theice.com/clear-us/risk-management#margin-rates'                                                   |
| 12  | KSE          | 'http://global.krx.co.kr/contents/GLB/06/0608/0608030700/GLB0608030700.jsp'                                      |
| 13  | SFE          | 'https://www2.asx.com.au/markets/clearing-and-settlement-services/asx-clear-futures'                             |
| 14  | TIFFEE       | 'https://www.tfx.co.jp/en/historical/futures/spparam.html'                                                       |
| 15  | TAIFEX-GOLD  | 'https://www.taifex.com.tw/enl/eng5/goldMargining'                                                               |
| 16  | TAIFEX-INDEX | 'https://www.taifex.com.tw/enl/eng5/indexMargining'                                                              |
| 17  | TAIFEX-FX    | 'https://www.taifex.com.tw/enl/eng5/fXMargining'                                                                 |
| 18  | TIFEX        | 'https://www.set.or.th/en/tch/rules-regulations/regulations'                                                     |
| 19  | LME          | 'https://www.lme.com/en-GB/LME-Clear/Risk-management/Margin-Parameter-files'                                     |
| 20  | ENPAR        | 'https://www.lch.com/risk-management/risk-management-sa/sa-risk-notices'                                         |

* Table of Contents
  {:toc}

--------------------------------------------------------------------------------------------------------------------
<div style="page-break-after: always;"></div>

## 1 User Interface Components

This section highlights the components of the margin_scraper.exe user interface. Refer to the description below for more information.

<img src="images/margin scraper welcome message.png" width="400" />
*Welcome message when the application window is first opened.*


<img src="images/margin scraper folder structure.png" width="400" />
*Folder structure created when the application is run.*

| Component                       | Description                                                                                             |
|---------------------------------|---------------------------------------------------------------------------------------------------------|
| **Application Window**          | The application opens a window that will update you about the progress of the scraping once it starts running.  |
| **"Downloads" Folder**          | The Margin Update documents will be downloaded here. A new subfolder with the `date` and `time` of scraping is created each time you run the application. e.g. `Margins_Downloaded_on_YYYY-MM-DD_HHMMSS` |
|**"temp" folder**                | This folder can be ignored.                                                                             |

--------------------------------------------------------------------------------------------------------------------
<div style="page-break-after: always;"></div>

# 2. Quick Start

1. Ensure you have Microsoft Edge installed in your Computer. It should come pre-installed with every Windows PC. If you don't have it, you can install it from the Microsoft Store.

2. Be logged in to the CME exchange website on your Edge browser - CME currently requires users to be logged in to download the margin updates.

3. Place the application (ie `margin_scraper.exe`) into your desired folder.

4. Double click the application to open the application window.

5. When prompted with `>>> Download EUREX only? Y/N`, type `y` and hit enter if you wish to download just EUREX updates. Type `n` and hit enter if you wish to download margin updates from all the exchanges.

6. The application will open a new Edge browser window and you can leave it to run in the background!

--------------------------------------------------------------------------------------------------------------------
<div style="page-break-after: always;"></div>

# 3. FAQ

**Q**: The application is unable to download particular filess, what should I do? <br>
**A**: Restart your computer and run the application again. If the download still fails, check the respective website where the failed download occurs. If the website has changed or the problem persists, notify the developer to update the source code. If the failed download is on the CME exchange, check that you have logged in and are kept logged in to the CME website on your normal Edge browser.

**Q**: My Edge browser updated to a new version and the application no longer runs. <br>
**A**: Notify the developer about your new browser version so that they can update the MSEdge WebDriver version packaged with the application.

**Q**: I want to add more websites to scrape from. <br>
**A**: Unfortunately, as every website is different, the code logic will need to be written specific for each site. The only way to add or remove websites is to notify the developer and inform them about the changes you require.
