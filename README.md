# Provably Rare Gem Miner Go (for Rarity)
Original https://github.com/TkzcM/GemMiner-Go

### Pull Request is strongly welcome as I don't know anything about Golang/Python/Web3.

# Usage
- Install Python 3.x if you don't have it.
- Get Visual Studio Build Tools from [here](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16).
- Install it with "C++ Desktop Development" marked and restart your PC.
- Win+R, input "cmd", click Run, input "cd /dirname/of/path/to/file" and hit "Enter".
```
$ cd /dirname/of/path/to/folder
```
- input "pip install -r requirements.txt" and hit "Enter".
```
$ pip install -r requirements.txt
```
- Edit .env, fill your address, private key, line notify token and gems kind in it.
  - GET [Line notify token](https://notify-bot.line.me/en/)
  - GET [Wallet Address](https://metamask.zendesk.com/hc/en-us/articles/360015289512-How-to-copy-your-MetaMask-account-public-address-)
  - GET [Private Key](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key)
```
.env

WALLET_ADDRESS=0xA8sFe39sdfDIFJQO8A3dAB
TARGET_GEM=2
NOTIFY_AUTH_TOKEN=6WDcdaIDUROLB908DBJKS
PRIVATE_KEY=jg8fg9lsksmlaabbbcsefaksjdfpq023lfks
DIFFICULTY=50000000
THREAD_NUM=3
```
- Double click loop.py and mining started (check status in Line) :+1.


# Update
- line notify [Provably-Rare-Gem-Miner](https://github.com/yoyoismee/Provably-Rare-Gem-Miner?fbclid=IwAR1OPzzuoDxHGWdilWADvwNBYF7-9yZLCOLp-a6gj6FFLQxqKPHFWulpG-g)
- random salt
- mining pool

# Remark
- 25k Iterations/sec/core on my environment (i5-9300H)
- go env -w GOOS=linux # for colab
- go env -w GOOS=windows # for windows
