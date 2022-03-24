import requests
import json

# ------------------------
# This python script searches among the top wallets listed in DeBank
# according to tokens held in a specific blockchain (e.g. ETH, CRO, BSC, etc...)
# ------------------------

# ---------------
#  Input Variables
# ----------------
# Wallet counts is the maximum top wallet IDs to look into (e.g. 100)
walletsCount = 100
# ChainId indicates which wallet id contains tokens from the specific chain
# For the chainId valid values please refer to 'https://openapi.debank.com/docs'
chainId = 'cro'

"""
Retrieve all wallest addresses available
"""
def GetTopWalletAddresses(count):
    counter = 1
    walletIds = []
    while True:
        response = requests.get("https://api.debank.com/social_ranking/list?page_num=%d" % counter)
        counter += 1
        parsed = json.loads(response.text)
        if ("error_msg" in parsed):
            # All wallets retrieved
            # Exit from while cycle
            break
        # Wallets addresses retrieved
        for socialProfile in parsed['data']['social_ranking_list']:
            walletIds.append(socialProfile['id'])
        print("[{}/{}] ...".format(len(walletIds), count))
        if (len(walletIds) >= count):
            # Retrieved enough wallet ids
            break
    return walletIds

"""
Get Simple Protocol List
"""
def GetSimpleProtocolList(walletId, chainId):
        response = requests.get("https://openapi.debank.com/v1/user/simple_protocol_list?id={}&chain_id={}".format(walletId, chainId))        
        parsed = json.loads(response.text)
        return parsed


print("Begin retrieving %d top wallet ids..." % walletsCount)
walletIds = GetTopWalletAddresses(walletsCount)
walletIdsWithTokens = []

print("Begin retrieving which wallet contains tokens from chain %s..." % chainId)
for walletId in walletIds:
    tokens = GetSimpleProtocolList(walletId, chainId)
    if (len(tokens) <= 0):
        continue
    print("[{}/{}] Scanning...".format(walletIds.index(walletId) + 1, walletsCount))
    walletIdsWithTokens.append(walletId)

print("Scan completed! The following wallets contains tokens from %s blockchain" % chainId)
for walletId in walletIdsWithTokens:
    print("https://debank.com/profile/%s" % walletId)