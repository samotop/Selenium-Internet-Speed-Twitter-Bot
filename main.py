from InternetTwitterSpeedBot import InternetTwitterSpeedBot

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "WRITE YOUR TWITTER EMAIL HERE "
TWITTER_PASS = "WRITE YOUR TWITTER PASSWORD HERE"
INTERNET_PROVIDER = "WRITE YOUR INTERNET PROVIDERS USERNAME ON TWITTER for example: @Starlink"

bot = InternetTwitterSpeedBot()

bot.get_internet_speed()
if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider(email=TWITTER_EMAIL, password=TWITTER_PASS, promised_down=PROMISED_DOWN,
                          promised_up=PROMISED_UP, provider=INTERNET_PROVIDER)
