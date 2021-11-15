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
    STRING_SESSION = "1BJWap1wBuz_w0jVTNv2VkblGNxUbKZ56X50y_06BuKv4lW8C0CznFmobS30YtdRSJTkpwPtOWJoYgOo-_4DI_9heCvVg3PkpOuPWU3hpwFjtGrpHuqmAJVZS1TCS5DoiF240WEMUPRHjd0lLtBnG7HUzfwnHJnAj67pKd7MJlGrArvCjY9bCXjWFqL-Wt9EeZFiFksoAhxvySw3OLQn-_h2OUkWpBm7N-JGOiGK5pLQf0AZGRqKMKvTbKyQvdNgoA9WwJUC3l9hls4EvY9TerEywzAqH1fd7qnhznbxAM9a9Myuz131vWgibS0hZdVmafzvHseYawJgCWGnpznQeLRVE4ixLyQM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "2129679575:AAG858HBozM-Wz-yCIJWv5ZQarFrJ7vESrk"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001645021060
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
