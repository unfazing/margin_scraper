---
layout: page
title: Developer Guide for Margin Scraper
---
* Table of Contents
{:toc}

--------------------------------------------------------------------------------------------------------------------
<div style="page-break-after: always;"></div>

## **Acknowledgements**

* This application makes use of [Selenium 4.9.1](https://www.selenium.dev/), an open source library for browser automation.
* This application uses MS Edge WebDriver version 115 as the browser driver.
* This application and related guides are created by Kok Hai, Software Intern at Phillip Nova, in tandem with Xiao Tian, Operations and Settlements Department.

--------------------------------------------------------------------------------------------------------------------

## **Setting up, getting started**
For Windows:
1. Download the latest version of [Python 3 for Windows](https://www.python.org/downloads/).
2. Check that the Python installation is successful by running the following command in terminal:
    
    `python --version`

3. Install the latest version of Selenium with the following command: 

    `pip install selenium`

   You may consider installing the packages into a [venv](https://docs.python.org/3/library/venv.html) to prevent cluttering your base installation of Python.
4. Edge should be installed on your Windows PC. Otherwise, install it from the Microsoft Store
5. Check the version of your Edge browser. Type (or copy and paste) `edge://version` into the Edge browser address bar and press Enter.
6. If it is no longer version 115, download a new [MS Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place the driver in the `./driver` directory.
--------------------------------------------------------------------------------------------------------------------
<div style="page-break-after: always;"></div>

## **
