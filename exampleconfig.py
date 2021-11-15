from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 14027438
    API_HASH = "9c9527c9c3e59853818ba0b0e2486737"
    # the name to display in your alive message
    ALIVE_NAME = "tan over cos"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://byauqhox:VfRRzasR6GG998_6RV-kdcdv8T13F3Hc@fanny.db.elephantsql.com/byauqhox"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1wBuz2mrvFm5zWTCMzk0kovIT0duir7uVSBZ0dkfXCU2jp_LF2SLqpjpc3x72WXnrLIb7ZKt_mq7rZP7YuQFCGtD8EDaPiAiqsncEMaGZ7rZm6y5EsxvVhBLg17ORN_nDOrv9aNEDQLnqInlASwlnJLWfHrCuMfLXEWasfdP9e7FoCQtuVc7rCsuvZSXWo0HB0Q424j-p9N4lhZG8WxOLRA0rsH_I6L-br_Bu2iPvaEDrUZXS4sEM4F3PRiRe4UvTx6LvS0t8WUTF4qMe-w0JOhQypjgr2W5Sgiqn2fnTVE6sRjR5dJsZLjxznU9N7Ac2y62MDv2BfAxRjv7RPlIn3z59o="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "2129679575:AAG858HBozM-Wz-yCIJWv5ZQarFrJ7vESrk"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001645021060
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
