# FastAPI Practice

FastAPI と PostgrSQL を用いて、API サーバーを構築する方法を学習した時のメモです。
基本的には FastAPI の [チュートリアル](https://fastapi.tiangolo.com/ja/tutorial/sql-databases/) のソースコードを流用しています。

# Usage

## PostgrSQL の起動

`sample.env` を `.env` という名前でコピーして、Dockerで PostgreSQL を起動します。
```
cp sample.env .env
docker compose up -d
```

## Python 仮想環境の構築

`pipenv` を用いて、Python の仮想環境を構築します。
```
cd backend
pipenv install --dev
pipenv shell
```

## データベースのマイグレーション

`alembic revision ––autogenerate` コマンドを実行すると、マイグレーションファイルが生成されます。
```
$ alembic revision --autogenerate -m "Initial"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_users_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_users_id' on '['id']'
INFO  [alembic.autogenerate.compare] Detected added table 'items'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_items_description' on '['description']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_items_id' on '['id']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_items_title' on '['title']'
  Generating /home/shasegawa/works/practice-fastapi/backend/migrations/versions/7d6d12066dcf_initial.py ...  done
```

マイグレーションを適用します。
```
$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 7d6d12066dcf, Initial
```

## アプリの起動

`uvicorn` でアプリを起動します。

```
pipenv run start
```

[http://127.0.0.1:8000/docs] にアクセスすると、APIをたたくことができます。


## References
* https://fastapi.tiangolo.com/tutorial/
* https://nmomos.com/tips/2021/01/23/fastapi-docker-2/
* https://zenn.dev/shimakaze_soft/scraps/bfa75df3e51258
