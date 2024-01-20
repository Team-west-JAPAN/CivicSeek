# Dockerfile
FROM python:3

# ログ出力をリアルタイムに行う (バッファリングしない)
ENV PYTHONUNBUFFERED 1 

# 作業ディレクトリを指定
WORKDIR /usr/src/app

# requirements.txtをコピーしてpip install
COPY . .
# --no-cache-dir: キャッシュを使わない -> イメージサイズを小さくする & 最新のパッケージをインストールできる
# RUN apt-get update \
    # --no-install-recommends: 推奨パッケージをインストールしない
    # && apt-get upgrade -y\
    # && apt-get clean \
    # Dockerイメージのサイズを小さくするためにキャッシュを削除
    # && rm -rf /var/lib/apt/lists/*\
RUN pip install  -r requirements.txt\
	python manage.py migrate\
