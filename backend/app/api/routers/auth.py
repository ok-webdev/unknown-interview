from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse

from app.config import settings
from app.db.models.user import User

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.get("/htmlpage")
async def htmlpage(request: Request):
    user = request.session.get("user")

    if user is not None:
        email = user["email"]
        html = (
            f"<pre>Email: {email}</pre><br>"
            '<a href="http://localhost:2080/api/docs">documentation</a><br>'
            '<a href="http://localhost:2080/api/v1/auth/logout">logout</a>'
        )
        return HTMLResponse(html)

    return HTMLResponse(
        '<a href="http://localhost:2080/api/v1/auth/login/google">login</a>'
    )


oauth = OAuth()

oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    client_kwargs={"scope": "openid email profile"},
)


@auth_router.get("/login/google")
async def google_login(request: Request):
    # Redirect Google OAuth back to our application
    redirect_uri = "http://localhost:2080/api/v1/auth/google"

    return await oauth.google.authorize_redirect(request, redirect_uri)


@auth_router.get("/user_info")
async def user_info(request: Request):
    user = request.session.get("user")

    if user is not None:
        email = user["email"]
        return JSONResponse({"email": email})

    return JSONResponse({"email": None})


@auth_router.get("/google")
async def google_auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    request_user = token.get("userinfo")

    # get a user from db if it exists, otherwise create it
    user_in_db = await User.find_one(User.email == request_user["email"])

    if not user_in_db:
        user_in_db = User(email=request_user["email"], name=request_user["name"])
        await user_in_db.create()

    request.session["user"] = request_user

    return RedirectResponse(url="/")


@auth_router.get("/logout")
async def logout(request: Request, response: Response):
    if "user" in request.session:
        del request.session["user"]
        return RedirectResponse(url="/")

    return RedirectResponse(url="/")
