from social_core.backends.monzo import MonzoOAuth2


class Monzo(MonzoOAuth2):
    ID_KEY = 'user_id'
