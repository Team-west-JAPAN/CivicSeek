# 開発者向けのREADME

上から目線の文言で大変恐縮ですが,メンバーの中には横文字ばかり使うと内容を把握できない人もいるのかなと思いできるだけ避けて書いたつもりです.<br>
横文字慣れている人には少し冗長だと思います.悪しからず.<br>
> P.S. dockerじゃなくてごめんよ！
> P.S. 今後docker使うかもだし、どうせデプロイの時bash使うだろうからコマンド系はbashを標準で書いときますね.
> どころころpowershell script書いてるけど別段消す必要もなかったから入れてるだけです。悪しからず.

## 開発環境構築

### 想定環境
|         OS         |                            Shell                             |
| :----------------: | :----------------------------------------------------------: |
| Ubuntu 22.04.3 LTS | GNU bash, バージョン 5.1.16(1)-release (x86_64-pc-linux-gnu) |

### リポジトリをcloneしたら以下を実行
```bash

timeout_max=15

# install required system packages
sudo apt update && sudo apt upgrade -y # update your system
sudo apt install python3 git python3-venv python3-pip # install required packages
# download git repository
timeout $timeout_max git clone https://github.com/Team-west-JAPAN/CivicSeek.git \
    || timeout $timeout_max git clone git@github.com:Team-west-JAPAN/CivicSeek.git \
    || echo "Maybe you're messing with your proxy settings...(._.)b"

# configure your environment
cd CivicSeek # move to Backend dir
python -m venv venv # create virtual environment for python
source ./venv/bin/activate # activate venv
pip install -r requirements.txt # install required packages
python regenerateSecretKey.py
python manage.py migrate

echo "done(._.)b!..." # print end message
```
