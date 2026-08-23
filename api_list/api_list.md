POST /api/login

用途
IDをを記入してアクセス

Request:

{
    "username": str
    "password": str
}

もうユーザーファイルがありパスワードがあっていた場合
Responce (200 OK):
{
    "username": str
}

ファイルがなかった場合
Responce (201 Created)
{
    "username": str
}

ファイルがあってパスワードが違う場合
Responce (401 Bat Request)
{
    "username": str
}

形式が違う場合
Responce (400 Bat Request)
{
    "username": str
}
