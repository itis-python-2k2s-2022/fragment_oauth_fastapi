# редирект пользователя на ссылку для авторизации
@router.get('/oauth')
async def oauth(request: Request, db: Session = Depends(get_db)):
    return responses.RedirectResponse(f'https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile&include_granted_scopes=true&response_type=token&redirect_uri=http://localhost:8000/auth/token&client_id={settings.CLIENT_ID}')


# работа с access токен
@router.get('/token')
async def access_token(request: Request, db: Session = Depends(get_db)):
    token = request.query_params.get("token")

    if token:
        print(token)
        response = requests.get(f'https://www.googleapis.com/oauth2/v3/userinfo?access_token={token}')
        userinfo = response.json()
        print(userinfo.get('name'))
        print(userinfo.get('email'))
        return {'message': 'ok'}
    return templates.TemplateResponse("get_this_fucking_token.html", {"request": request})
