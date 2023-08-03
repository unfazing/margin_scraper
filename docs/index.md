---
layout: page
title: Margin Scraper
---

## **Acknowledgements**

* This application makes use of [Selenium 4.9.1](https://www.selenium.dev/), an open source library for browser automation.
* This application uses MS Edge WebDriver version 115 as the browser driver.
* This application and related guides are created by Kok Hai, Software Intern at Phillip Nova, in tandem with Xiao Tian, Operations and Settlements Department.

## **Overview**

<img src="images/margin scraper welcome message.png" width="500" /> 

As of August 2023, the application downloads the latest margin update documents from the following exchanges:

|     | Exchange     | URL                                                                                                              |
|-----|--------------|------------------------------------------------------------------------------------------------------------------|
| 1   | EUREX        | https://www.eurex.com/ec-en/services/risk-parameters/                                                          |
| 2   | CME          | https://www.cmegroup.com/clearing/margins/outright-vol-scans.html#sortField=exchange&sortAsc=true&pageNumber=1 |
| 3   | SGX          | https://www2.sgx.com/derivatives/risk-management#Margin%20Schedule                                             |
| 4   | DGCX         | http://www.dgcx.ae/initial-margins                                                                             |
| 5   | IPE          | https://www.theice.com/clear-europe/risk-management#margins-europe                                             |
| 6   | LIFFE        | https://www.theice.com/clear-europe/risk-management#margin-liffe                                               |
| 7   | TURDEX       | https://www.takasbank.com.tr/en/resources/bistech-risk-parameters                                              |
| 8   | IFSG         | https://www.theice.com/clear-singapore/risk-management                                                         |
| 9   | HKFE         | https://www.hkex.com.hk/Services/Clearing/Listed-Derivatives/Risk-Management/Margin/Margin-Tables?sc_lang=en   |
| 10  | OSE&TSE      | https://www.jpx.co.jp/jscc/en/index.html                                                                       |
| 11  | ICEUS        | https://www.theice.com/clear-us/risk-management#margin-rates                                                   |
| 12  | KSE          | http://global.krx.co.kr/contents/GLB/06/0608/0608030700/GLB0608030700.jsp                                      |
| 13  | SFE          | https://www2.asx.com.au/markets/clearing-and-settlement-services/asx-clear-futures                             |
| 14  | TIFFEE       | https://www.tfx.co.jp/en/historical/futures/spparam.html                                                       |
| 15  | TAIFEX-GOLD  | https://www.taifex.com.tw/enl/eng5/goldMargining                                                               |
| 16  | TAIFEX-INDEX | https://www.taifex.com.tw/enl/eng5/indexMargining                                                              |
| 17  | TAIFEX-FX    | https://www.taifex.com.tw/enl/eng5/fXMargining                                                                 |
| 18  | TIFEX        | https://www.set.or.th/en/tch/rules-regulations/regulations                                                     |
| 19  | LME          | https://www.lme.com/en-GB/LME-Clear/Risk-management/Margin-Parameter-files                                     |
| 20  | ENPAR        | https://www.lch.com/risk-management/risk-management-sa/sa-risk-notices                                         |

--------------------------------------------------------------------------------------------------------------------
