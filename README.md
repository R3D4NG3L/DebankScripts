**Table of contents**
- [💰 Debank Scripts](#-debank-scripts)
- [🔎 Python Scripts details](#-python-scripts-details)
  - [scripts/WalletsWithTokensFromSpecificBlockchain.py](#scriptswalletswithtokensfromspecificblockchainpy)
    - [How to use it](#how-to-use-it)
      - [Configure walletsCount](#configure-walletscount)
      - [Configure chainId](#configure-chainid)
    - [🏃 Run pre-made examples online](#-run-pre-made-examples-online)
- [✅ Do you like it? Buy me a beer!](#-do-you-like-it-buy-me-a-beer)

# 💰 Debank Scripts
Python scripts to scrape data from [Debank](https://debank.com/).

> The purpose of these scripts is to scrape data in order to find the **strategies used by whales by looking at their belongings and transactions**.

**🤝 Feel free to contribute by fork, and making pull-request**

# 🔎 Python Scripts details
Here below a description of python scripts details.
## scripts/WalletsWithTokensFromSpecificBlockchain.py
> This python script **searches among the top wallets** listed in DeBank according to tokens **held in a specific blockchain** (e.g. ETH, CRO, BSC, etc...)

### How to use it
**Configure Input Variables** located on top of the script, and then run it

#### Configure walletsCount
``` python
# Wallet counts is the maximum top wallet IDs to look into (e.g. 100)
walletsCount = 100
```

#### Configure chainId
For possible chainId values, **please refer to [Debank OpenAPI](https://openapi.debank.com/docs) website**
``` python
# ChainId indicates which wallet id contains tokens from the specific chain
# For the chainId valid values please refer to 'https://openapi.debank.com/docs'
chainId = 'cro'
```

### 🏃 Run pre-made examples online


* Run [Top 1000 Wallets with tokens from Ethereum blockchain](https://replit.com/@R3D4NG3L/DeBank-Top-wallets-containing-tokens-in-Eth-blockchain)
* Run [Top 1000 Wallets with tokens from BSC blockchain](
https://replit.com/@R3D4NG3L/DeBank-Top-wallets-containing-tokens-in-BSC-blockchain)
* Run [Top 1000 Wallets with tokens from Cronos blockchain](https://replit.com/@R3D4NG3L/DeBank-Top-wallets-containing-tokens-in-Cronos-blockchain)

**Output example:**
```
Begin retrieving 1000 top wallet ids...
[50/1000] ...
[100/1000] ...
....
[950/1000] ...
[1000/1000] ...
----
Begin retrieving which wallet contains tokens from chain cro...
[6/1000] Scanning...
[7/1000] Scanning...
[15/1000] Scanning...
...
[995/1000] Scanning...
[1000/1000] Scanning...
----
Scan completed! The following wallets contains tokens from cro blockchain
https://debank.com/profile/0x3ec6732676db7996c1b34e64b0503f941025cb63
https://debank.com/profile/0x108a8b7200d044bbbe95bef6f671baec5473e05f
....
https://debank.com/profile/0x438bbff80252c9c959797d0180a5c868e1a86c91
```

# ✅ Do you like it? Buy me a beer!
**ETH / CRO / BSC Wallet Address:**

👉 0x542AD209341d2944CDa9b9e1eB098E6A7Cb35366