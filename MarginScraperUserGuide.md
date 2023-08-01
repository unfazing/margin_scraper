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

<img src="images/margin scraper icon.png" width="400" />

| Component             | Description                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------|
| **Application Window**           | The application opens a window that will update you about the progress of the scraping once it starts running.  |
| **"Downloads" Folder**    | The Margin Update documents will be downloaded here. A new subfolder with the `date` and `time` of scraping is created each time you run the application. e.g. `Margins_Downloaded_on_YYYY-MM-DD_HHMMSS`    |
|**"temp" folder**          | This folder can be ignored. |

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

# 3. Features

## 3.1. Command Components

This section explains some common components you may find in a command.

| Component                 | Example              | Usage                                                                                                                                                                                                                                                                                                                    |
|---------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Parameter**             | `QUESTION`, `ANSWER` | Parameters are placeholders where you have to insert your input.<br/> <br/>Suppose `add q\QUESTION a\ANSWER` is a valid command to add a card. You can simply replace `QUESTION` and `ANSWER` with the question and answer of your choice.                                                                               |  
| **Prefix**                | `q\ `, `a\ `, `t\ `  | Prefixes are used to identify the parameters of a command. <br><br> For example, prefix `q\ ` identifies the parameter `QUESTION` in the command `add q\QUESTION`.                                                                                                                                                       |
| **Optional Component**    | `[t\TAG]`            | Optional components can be **omitted** in certain commands.<br/> <br/>For example, `add q\QUESTION a\QUESTION [t\TAG]` is a valid command to add a card.<br><br>The first two components `q\QUESTION`, `a\ANSWER` are compulsory. The last component `t\TAG` is optional.                                                |
| **Multi-value Parameter** | `KEYWORDS...`        | These are parameters that can appear **multiple times**. <br><br> For example, the command `findCards KEYWORD...` filters all the cards based on the keywords specified.<br><br>This means that the parameter `KEYWORD` can:<br>- Appear one time: `findCards cell`<br>- Appear multiple times: `findCards cell biology` | 
| **Index**                 | `INDEX`              | Index refers to the index of the card/deck you want to target from the list. The index must be a positive integer (1, 2, 3...). <br/> <br/>For example, `deleteDeck 1` deletes the first deck in the deck list.                                                                                                          |
| **Flag**                  | `-e`, `-m`, `-h`     | Flags are used to toggle a particular setting or behavior.<br/><br/> For example, `review 1 -e` lets you review questions in the first deck that are tagged as **easy** only.                                                                                                                                            |

<div markdown="block" class="alert alert-info">

**:information_source: Notes about the command format:**<br>

- If a parameter is expected only once in the command, but you specified it multiple times, only the last occurrence of the parameter will be considered.
  e.g. if you specify `q\What is photosynthesis q\What is a cell`, only `q\What is a cell` will be considered.
- Extraneous parameters succeeding commands that do not take in parameters (such as `help`, `list`, `exit` and `clear`) will be ignored. e.g. if the command specified is `help 123`, it will be interpreted as `help`.

</div>

<div style="page-break-after: always;"></div>

## 3.2. Main Mode

Welcome to the Main Mode of the PowerCards application! This is the default mode you will see when you open the app.

In the Main Mode, you can quickly and easily create new decks, add new cards to your decks, delete and modify existing cards or decks as needed, and more!


| Component         | Description                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **Deck**          | A deck contains a list of cards. The existing decks are displayed in the **left** panel.                                                   |
| **Selected Deck** | The deck currently selected. The cards in this deck are displayed in the **right** panel.                                                  |
| **Card**          | A card contains a question, an answer and an optional difficulty tag.                                                                      |
| **Question**      | The question that you assign to the card.                                                                                                  |
| **Answer**        | The corresponding answer to the question.                                                                                                  |
| **Tag**           | The tag indicating the difficulty level of the card, based on your evaluation. Each card can only be tagged with **at most** 1 difficulty. |

<div style="page-break-after: always;"></div>

## 3.3. Main Mode - Before Selecting a Deck

### 3.3.1. Adding a Deck : `addDeck`

Before you can add any cards, you must first create a deck. Creating a deck is done through the simple command below.

Format: `addDeck DECK_NAME`
- `DECK_NAME` is the name of the deck you want to create.
    - Deck name is case-sensitive and cannot be duplicated, e.g., if you already have a deck named `Science`, you cannot create another deck named `Science`. However, you can create a deck named `SCIENCE` since `SCIENCE` may be an acronym.
    - You do not need any prefix before deck name.

Example:
* `addDeck Science` will create a deck titled Science.

--------------------------------------------------------------------------------------------------------------------

# 4. FAQ

**Q**: How do I transfer my data to another Computer?<br>
**A**: Install the app in the other computer and overwrite the empty data file it creates with the file that contains the data in your previous PC's home folder.

**Q**: Will my data be automatically saved?<br>
**A**: **Yes**, PowerCards automatically saves your data after every command entered.

**Q**: Where is my data saved?<br>
**A**: If you have run PowerCards at least once, there will be a folder named `data` inside the folder you store the application. The save data can be found as `masterdeck.json` in the `data` folder.

**Q**: Can I rename my saved data file?<br>
**A**: **No**, PowerCards currently only supports the use of `masterdeck.json` as the name of the saved data file.

**Q**: How can I verify if my answer is correct?<br>
**A**: PowerCards operates on a self-testing basis. You can check your answer by writing it down before flipping the card to verify if you got it right or wrong.

**Q**: Can I have two cards with the same question?<br>
**A**: **No**, if the two cards are in the same deck. `QUESTION` field of Card is case-sensitive and cannot be duplicated within the same deck. **However**, two cards with the same question can exist **if they belong to different decks**.

**Q**: Can I have two decks with the same name? <br>
**A**: **No**. The name of the deck is case-sensitive and cannot be duplicated, e.g., if you already have a deck named `Science`, you cannot create another deck named `Science`. However, you can create a deck named `SCIENCE` since `SCIENCE` may be an acronym.

**Q**: What if I would like to include the prefix within my card (question or answer) or deck name? (For example `addCard q\What is q\a a\It means q slash a` should add a card with question `What is q\a` instead of `a`)<br>
**A**: At the moment we do not support that. However, we plan to support this feature in the next iteration. We also like to point out that this is the reason why we use backslash &#92; rather than forward slash `/` for this current iteration as backslash is less commonly use than forward slash.
