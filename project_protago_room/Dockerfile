# docker内の環境と実行プロセスを構築(設計図)
# dockerコンテナの設計図

# Python3.12が入ったDockerイメージを使う
FROM python:3.12 

# docker内の作業フォルダの指定( /app や /home などがある)
WORKDIR /code

# MySQLのC言語ライブラリとコンパイラ環境を作っている(mysqlclientの方が早いため、採用)
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc pkg-config

# WORKDIRにコピーする
COPY requirements.txt .

# docker内でRUN以降のコマンドを実行
RUN pip install -r requirements.txt

# pcのコードを全てdockerにコピー
COPY . .

# dockerを起動する時に自動で実行されるコマンド
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]