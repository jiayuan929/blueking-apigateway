ENCRYPT_KEY="dGVzdDMzNDA4YWJlNDMyNGJmYzE4Mjk4NGM3ZXRlc3Q="
BK_APP_SECRET="egrKq5TnJvlFiPLIrtquv3Mow792xVgTzqTiSrVkUIk="

DASHBOARD_CSRF_COOKIE_DOMAIN=".example.com"
DASHBOARD_CSRF_COOKIE_NAME="bk_apigateway_csrftoken"
BK_PAAS_LOGIN_URL="http://paas.example.com/login"

BK_APIGW_DATABASE_HOST="localhost"

BK_APIGW_DATABASE_NAME="bk_apigateway"
BK_APIGW_DATABASE_HOST="localhost"
BK_APIGW_DATABASE_PORT=3306
BK_APIGW_DATABASE_USER="root"
BK_APIGW_DATABASE_PASSWORD_UNENCRYPTED=""

BK_ESB_DATABASE_NAME="bk_esb"
BK_ESB_DATABASE_HOST="localhost"
BK_ESB_DATABASE_PORT=3306
BK_ESB_DATABASE_USER="root"
BK_ESB_DATABASE_PASSWORD_UNENCRYPTED=""

# FIXME: can't only set unencrypted to empty,
# in default.py env.str("BK_APIGW_REDIS_PASSWORD_UNENCRYPTED", "") or sec_env.str("BK_APIGW_REDIS_PASSWORD") will check the password
BK_APIGW_REDIS_PASSWORD=""
BK_APIGW_REDIS_PASSWORD_UNENCRYPTED=""

# add the frontend domain, will add to CORS_ORIGIN_REGEX_WHITELIST
DASHBOARD_FE_URL="http://apigw.example.com"