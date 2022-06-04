import yaml
import tweepy
from yaml import load, dump


class Conf:
    def __init__(self, api_key, bearer, secret_key):
        self.api_key = api_key
        self.bearer = bearer
        self.secret_key = secret_key

def load_conf():
    with open("./conf.yaml") as f_conf:
        data = yaml.load(f_conf, Loader=yaml.CLoader)
        return Conf(data["api_key"], data["bearer_token"], data["api_key_secret"])

def main():
    conf = load_conf()
    auth = tweepy.OAuth2BearerHandler(conf.bearer)
    # api = tweepy.API(auth)
    api2 = tweepy.Client(bearer_token=conf.bearer)
    results = api2.search_recent_tweets("@Pepiit0")
    print(results)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
