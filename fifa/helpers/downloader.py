from django.utils.text import slugify

from fifa.apps.clubs.models import Club
from fifa.apps.leagues.models import League
from fifa.apps.nations.models import Nation
from fifa.apps.players.models import PLAYER_POSITION_LINES, Player

import requests


class Downloader(object):
    def __init__(self):
        self.base_url = 'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item'

    def get_total_pages(self):
        page = requests.get(self.base_url)

        if page.status_code == requests.codes.ok:
            try:
                page_json = page.json()
                page_count = page_json['totalPages']

                return page_count

            except ValueError:
                print("Can't convert page to JSON")
        else:
            raise Exception("Couldn't get total pages")

    def get_crawlable_urls(self):
        total_pages = self.get_total_pages()
        crawlable_urls = [
            'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{}%7D'.format(
                x
            ) for x in range(1, total_pages + 1)
        ]

        return crawlable_urls


class NationDownloader(Downloader):
    def build_nation_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        nations = kwargs.get('data', [])
        failed_urls = []

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                try:
                    print('Got page {}'.format(i))

                    page_json = page.json()
                    items = page_json['items']

                    for item in items:
                        nation = item['nation']

                        nation_data = {
                            'name': nation['name'],
                            'name_abbr': nation['abbrName'],
                            'ea_id': nation['id'],
                            'image_small': nation['smallImgUrl'],
                            'image_medium': nation['imgUrl'],
                            'slug': slugify(nation['name'])
                        }

                        if nation_data not in nations:
                            nations.append(nation_data)

                except ValueError:
                    failed_urls.append(url)

                    print("Can't convert page to JSON")
            else:
                failed_urls.append(url)

                print('Url failed: {}'.format(url))

            print([n['name'] for n in nations])

        if failed_urls:
            self.build_nation_data(failed=failed_urls, data=nations)

        return nations

    def build_nations(self, *args, **kwargs):
        data = self.build_nation_data()
        created_nations = []

        for obj in data:
            nation, created = Nation.objects.get_or_create(**obj)

            if created:
                created_nations.append(created)

                print('Created League: {}'.format(nation))

        print(len(created_nations))

        return


class LeagueDownloader(Downloader):
    def __init__(self):
        super(LeagueDownloader, self).__init__()

        self.leagues_json = 'https://fifa15.content.easports.com/fifa/fltOnlineAssets/8D941B48-51BB-4B87-960A-06A61A62EBC0/2015/fut/items/web/leagues.json'

    def build_league_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        leagues = kwargs.get('data', [])
        failed_urls = []
        leagues_data = {}

        league_page = requests.get(self.leagues_json)

        if league_page.status_code == requests.codes.ok:
            leagues_json = league_page.json()
            leagues_data = leagues_json['Leagues']['League']

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                try:
                    print('Got page {}'.format(i))

                    page_json = page.json()
                    items = page_json['items']

                    for item in items:
                        league = item['league']

                        league_data = {
                            'name': league['name'],
                            'name_abbr': league['abbrName'],
                            'ea_id': league['id'],
                            'image_medium': league['imgUrl'],
                            'slug': slugify(league['name'])
                        }

                        for data in leagues_data:
                            league_id = int(data['LeagueId'])
                            scraped_id = int(league_data['ea_id'])
                            nation_id = int(data['NationId'])

                            if league_id == scraped_id:
                                league_data['nation'] = Nation.objects.get(
                                    ea_id=nation_id
                                )

                                print(
                                    'Paired League & Nation: {} - {}'.format(
                                        league_data['name'],
                                        league_data['nation']
                                    ))

                                if league_data not in leagues:
                                    leagues.append(league_data)
                            else:
                                print("Can't find Nation for {}".format(
                                    league_data['name']
                                ))

                except ValueError:
                    failed_urls.append(url)

                    print("Can't convert page to JSON")
            else:
                failed_urls.append(url)

                print('Url failed: {}'.format(url))

            print([n['name'] for n in leagues], 'Page {}'.format(i))

        if failed_urls:
            self.build_league_data(failed=failed_urls, data=leagues)

        return leagues

    def build_leagues(self, *args, **kwargs):
        data = self.build_league_data()
        created_leagues = []

        for obj in data:
            league, created = League.objects.get_or_create(**obj)

            if created:
                created_leagues.append(created)

                print('Created Nation: {}'.format(league))

        print(len(created_leagues))

        return


class ClubDownloader(Downloader):
    def __init__(self):
        super(ClubDownloader, self).__init__()

        self.clubs_json = 'https://fifa15.content.easports.com/fifa/fltOnlineAssets/8D941B48-51BB-4B87-960A-06A61A62EBC0/2015/fut/items/web/teams.json'

    def build_club_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        clubs = kwargs.get('data', [])
        failed_urls = []
        clubs_data = {}

        club_page = requests.get(self.clubs_json)

        if club_page.status_code == requests.codes.ok:
            clubs_json = club_page.json()
            clubs_data = clubs_json['Teams']['Team']

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                try:
                    print('Got page {}'.format(i))

                    page_json = page.json()
                    items = page_json['items']

                    for item in items:
                        club = item['club']

                        club_data = {
                            'name': club['name'],
                            'name_abbr': club['abbrName'],
                            'ea_id': club['id'],
                            'image_medium': club['imgUrl'],
                            'image_dark_small': club['imageUrls']['dark']['small'],
                            'image_dark_large': club['imageUrls']['dark']['large'],
                            'image_light_small': club['imageUrls']['light']['small'],
                            'image_light_large': club['imageUrls']['light']['large'],
                            'slug': slugify(club['name'])
                        }

                        for data in clubs_data:
                            club_id = int(data['TeamId'])
                            scraped_id = int(club_data['ea_id'])
                            league_id = int(data['LeagueId'])

                            if club_id == scraped_id:
                                club_data['league'] = League.objects.get(
                                    ea_id=league_id
                                )

                                print(
                                    'Paired Club & League: {} - {}'.format(
                                        club_data['name'],
                                        club_data['league']
                                    ))

                                if club_data not in clubs:
                                    clubs.append(club_data)

                                break
                            else:
                                print("Can't find League for {}".format(
                                    club_data['name']
                                ))

                except ValueError:
                    failed_urls.append(url)

                    print("Can't convert page to JSON")
            else:
                failed_urls.append(url)

                print('Url failed: {}'.format(url))

            print([n['name'] for n in clubs], 'Page {}'.format(i))

        if failed_urls:
            self.build_club_data(failed=failed_urls, data=clubs)

        return clubs

    def build_clubs(self, *args, **kwargs):
        data = self.build_club_data()
        created_clubs = []

        for obj in data:
            club, created = Club.objects.get_or_create(**obj)

            if created:
                created_clubs.append(created)

                print('Created Club: {}'.format(club))

        print(len(created_clubs))

        return


class PlayerDownloader(Downloader):
    def __init__(self):
        super(PlayerDownloader, self).__init__()

        self.players_json = 'https://fifa15.content.easports.com/fifa/fltOnlineAssets/8D941B48-51BB-4B87-960A-06A61A62EBC0/2015/fut/items/web/players.json'

    def build_player_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        players = kwargs.get('data', [])
        failed_urls = []
        players_data = {}

        player_page = requests.get(self.players_json)

        if player_page.status_code == requests.codes.ok:
            players_json = player_page.json()
            players_data_normal = players_json['Players']
            players_data_legends = players_json['LegendsPlayers']
        else:
            raise Exception("Can't get players JSON")

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                try:
                    print('Got page {}'.format(i))

                    page_json = page.json()
                    items = page_json['items']

                    for item in items:
                        player = item

                        if player['commonName']:
                            common_name = player['commonName']
                        elif player['name']:
                            common_name = player['name']
                        else:
                            common_name = '{} {}'.format(
                                player['firstName'],
                                player['lastName']
                            )

                        for k, v in PLAYER_POSITION_LINES.items():
                            if player['position'] in PLAYER_POSITION_LINES[k]:
                                position_line = k

                        if player['traits']:
                            for trait in player['traits']:
                                print(type(trait))

                        if player['specialities']:
                            for specialalitie in player['specialities']:
                                print(type(specialalitie))

                        player_data = {
                            'ea_id': player['baseId'],
                            'slug': slugify(player['name']),
                            'name': player['name'],
                            'first_name': player['firstName'],
                            'last_name': player['lastName'],
                            'common_name': common_name,
                            'club': Club.objects.get(ea_id=player['club']['id']),
                            'league': League.objects.get(ea_id=player['league']['id']),
                            'nation': Nation.objects.get(ea_id=player['nation']['id']),
                            'image_small': player['headshot']['smallImgUrl'],
                            'image_medium': player['headshot']['medImgUrl'],
                            'image_large': player['headshot']['largeImgUrl'],
                            'position': player['position'],
                            'position_line': position_line,
                            'position_full': player['positionFull'],
                            'birthdate': player['birthdate'],
                            'height': player['height'],
                            'weight': player['weight'],
                            'acceleration': player['acceleration'],
                            'aggression': player['aggression'],
                            'agility': player['agility'],
                            'balance': player['balance'],
                            'ball_control': player['ballcontrol'],
                            'weak_foot': player['weakFoot'],
                            'skill': player['skillMoves'],
                            'crossing': player['crossing'],
                            'curve': player['curve'],
                            'dribbling': player['dribbling'],
                            'finishing': player['finishing'],
                            'free_kick_accuracy': player['freekickaccuracy'],
                            'gk_diving': player['gkdiving'],
                            'gk_handling': player['gkhandling'],
                            'gk_kicking': player['gkkicking'],
                            'gk_positioning': player['gkpositioning'],
                            'gk_reflex': player['gkreflexes'],
                            'heading_accuracy': player['headingaccuracy'],
                            'interceptions': player['interceptions'],
                            'jumping': player['jumping'],
                            'long_passing': player['longpassing'],
                            'long_shots': player['longshots'],
                            'marking': player['marking'],
                            'penalties': player['penalties'],
                            'positioning': player['positioning'],
                            'potential': player['potential'],
                            'reactions': player['reactions'],
                            'short_passing': player['shortpassing'],
                            'shot_power': player['shotpower'],
                            'sliding_tackle': player['slidingtackle'],
                            'sprint_speed': player['sprintspeed'],
                            'standing_tackle': player['standingtackle'],
                            'stamina': player['stamina'],
                            'strength': player['strength'],
                            'vision': player['vision'],
                            'volleys': player['volleys'],
                            'preferred_foot': player['foot'],
                            'traits': player['traits'],
                            'specialities': player['specialities'],
                            'workrate_att': player['atkWorkRate'],
                            'workrate_def': player['defWorkRate'],
                            'card_att_1': player['attributes'][0]['value'],
                            'card_att_2': player['attributes'][1]['value'],
                            'card_att_3': player['attributes'][2]['value'],
                            'card_att_4': player['attributes'][3]['value'],
                            'card_att_5': player['attributes'][4]['value'],
                            'card_att_6': player['attributes'][5]['value'],
                            'overall_rating': player['rating'],
                            'ea_id_unique': player['id'],
                            'play_style': player['playStyle'],
                            'item_type': player['itemType'],
                            'player_type': player['playerType'],
                            'quality': player['quality'],
                            'color': player['color'],
                            'is_goalkeeper': player['isGK'],
                            'is_special_type': player['isSpecialType'],
                        }

                        if not player['playerType'] == 'legend':
                            for data in players_data_normal:
                                if data['id'] == player_data['ea_id']:
                                    player_data['is_fut_player'] = True

                                    break

                                player_data['is_fut_player'] = False
                        else:
                            for data in players_data_legends:
                                if data['id'] == player_data['ea_id']:
                                    player_data['is_fut_player'] = True

                                    break

                                player_data['is_fut_player'] = False

                        if player_data not in players:
                            players.append(player_data)

                except ValueError:
                    failed_urls.append(url)

                    print("Can't convert page to JSON")
            else:
                failed_urls.append(url)

                print('Url failed: {}'.format(url))

            break

            print([(n['common_name'], n['is_fut_player']) for n in players], 'Page {}'.format(i))

        if failed_urls:
            self.build_player_data(failed=failed_urls, data=players)

        return players

    def build_players(self, *args, **kwargs):
        data = self.build_player_data()
        created_players = []

        for obj in data:
            try:
                player = Player.objects.get(**obj)
            except Player.DoesNotExist:
                player = Player.objects.create(**obj)

            created_players.append(player)

            print('Created Player: {}'.format(player))

        print(len(created_players))

        return



