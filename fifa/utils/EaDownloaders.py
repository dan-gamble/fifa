import requests
from django.utils.text import slugify

from fifa.apps.clubs.models import Club
from fifa.apps.leagues.models import League
from fifa.apps.nations.models import Nation
from fifa.apps.players.models import Player, PLAYER_POSITION_LINES


class Downloader(object):
    def __init__(self):
        self.base_url = 'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item'

    def get_total_pages(self):
        page = requests.get(self.base_url)

        if page.status_code == requests.codes.ok:
            try:
                page_json = page.json()
                return page_json['totalPages']
            except ValueError:
                print("Can't convert page to JSON")
        else:
            raise Exception("Couldn't get total page")

    def get_crawlable_urls(self):
        total_pages = self.get_total_pages()

        return [
            'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item' \
            '?jsonParamObject=%7B%22page%22:{}%7D'.format(
                x
            ) for x in range(1, total_pages + 1)
        ]

    # def get_data(self, mapping, *args, **kwargs):
    #     urls = kwargs.get('failed', self.get_crawlable_urls())
    #     objects = kwargs.get('data', [])
    #     failed = []
    #
    #     for i, url in enumerate(urls):
    #         page = requests.get(url)
    #
    #         if page.status_code == requests.codes.ok:
    #             try:
    #                 print('Got page {}'.format(i))
    #
    #                 page_json = page.json()
    #                 items = page_json['items']
    #
    #                 for item in items:
    #                     ea_item = item[mapping['ea_item']]
    #                     data = {}
    #
    #                     for k, v in mapping['model_mapping'].items():
    #                         data[k] = ea_item[v]
    #
    #                     if mapping['model_images']:
    #                         for k, v in mapping['model_images'].items():
    #                             data[k] = ea_item['imageUrls' if mapping['ea_item'] != 'player' else 'headshot'][v]
    #
    #                     if data not in objects:
    #                         objects.append(data)
    #
    #             except ValueError:
    #                 failed.append(url)
    #
    #                 print("Can't convert page to JSON")
    #         else:
    #             failed.append(url)
    #
    #             print ("Can't convert page {} to JSON".format(i))
    #
    #     print(objects)
    #
    #     if failed:
    #         self.get_data(failed=failed, data=objects)


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
                            'image_sm': nation['imageUrls']['small'],
                            'image_md': nation['imageUrls']['medium'],
                            'image_lg': nation['imageUrls']['large'],
                            'image': nation['imgUrl'],
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

                print('Created Nation: {}'.format(nation))

        print(len(created_nations))

        return


class LeagueDownloader(Downloader):
    def __init__(self):
        super(LeagueDownloader, self).__init__()

        self.leagues_json = 'https://fifa15.content.easports.com/fifa/' \
                            'fltOnlineAssets/' \
                            'B488919F-23B5-497F-9FC0-CACFB38863D0/2016/fut/' \
                            'config/web/teamconfig.json'

    def build_league_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        leagues = kwargs.get('data', [])
        failed_urls = []
        leagues_data = {}

        league_page = requests.get(self.leagues_json)

        if league_page.status_code == requests.codes.ok:
            leagues_json = league_page.json()

            for league in leagues_json['Years']:
                if league['Year'] == '2016':
                    leagues_data = league['Leagues']

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

        self.clubs_json = 'https://fifa15.content.easports.com/fifa/' \
                            'fltOnlineAssets/' \
                            'B488919F-23B5-497F-9FC0-CACFB38863D0/2016/fut/' \
                            'config/web/teamconfig.json'

    def build_club_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        clubs = kwargs.get('data', [])
        failed_urls = []
        clubs_data = {}

        club_page = requests.get(self.clubs_json)

        if club_page.status_code == requests.codes.ok:
            clubs_json = club_page.json()

            for club in clubs_json['Years']:
                if club['Year'] == '2016':
                    clubs_data = club['Teams']

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
                            'image_dark_sm': club['imageUrls']['dark']['small'],
                            'image_dark_md': club['imageUrls']['dark']['medium'],
                            'image_dark_lg': club['imageUrls']['dark']['large'],
                            'image_normal_sm': club['imageUrls']['normal']['small'],
                            'image_normal_md': club['imageUrls']['normal']['medium'],
                            'image_normal_lg': club['imageUrls']['normal']['large'],
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

                        print(player['firstName'])

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

                        player_data = {
                            'first_name': player['firstName'],
                            'last_name': player['lastName'],
                            'common_name': common_name,
                            'club': Club.objects.get(ea_id=player['club']['id']),
                            'league': League.objects.get(ea_id=player['league']['id']),
                            'nation': Nation.objects.get(ea_id=player['nation']['id']),
                            'image': player['headshotImgUrl'],
                            'image_sm': player['headshot']['smallImgUrl'],
                            'image_md': player['headshot']['medImgUrl'],
                            'image_lg': player['headshot']['largeImgUrl'],
                            'image_special_totw_md': player['specialImages']['medTOTWImgUrl'],
                            'image_special_totw_lg': player['specialImages']['largeTOTWImgUrl'],
                            'position': player['position'],
                            'position_full': player['positionFull'],
                            'position_line': position_line,
                            'playstyle': player['playStyle'],
                            'playstyle_id': player['playStyleId'],
                            'height': player['height'],
                            'weight': player['weight'],
                            'date_of_birth': player['birthdate'],
                            'acceleration': player['acceleration'],
                            'aggression': player['aggression'],
                            'agility': player['agility'],
                            'balance': player['balance'],
                            'ballcontrol': player['ballcontrol'],
                            'crossing': player['crossing'],
                            'curve': player['curve'],
                            'dribbling': player['dribbling'],
                            'finishing': player['finishing'],
                            'freekickaccuracy': player['freekickaccuracy'],
                            'gkdiving': player['gkdiving'],
                            'gkhandling': player['gkhandling'],
                            'gkkicking': player['gkkicking'],
                            'gkpositioning': player['gkpositioning'],
                            'gkreflexes': player['gkreflexes'],
                            'headingaccuracy': player['headingaccuracy'],
                            'interceptions': player['interceptions'],
                            'jumping': player['jumping'],
                            'longpassing': player['longpassing'],
                            'longshots': player['longshots'],
                            'marking': player['marking'],
                            'penalties': player['penalties'],
                            'positioning': player['positioning'],
                            'potential': player['potential'],
                            'reactions': player['reactions'],
                            'shortpassing': player['shortpassing'],
                            'shotpower': player['shotpower'],
                            'slidingtackle': player['slidingtackle'],
                            'sprintspeed': player['sprintspeed'],
                            'standingtackle': player['standingtackle'],
                            'stamina': player['stamina'],
                            'strength': player['strength'],
                            'vision': player['vision'],
                            'volleys': player['volleys'],
                            'foot': player['foot'],
                            'skill_moves': player['skillMoves'],
                            'weak_foot': player['weakFoot'],
                            'traits': player['traits'],
                            'specialities': player['specialities'],
                            'workrate_att': player['atkWorkRate'],
                            'workrate_def': player['defWorkRate'],
                            'player_type': player['playerType'],
                            'item_type': player['itemType'],
                            'overall_rating': player['rating'],
                            'card_att_1': player['attributes'][0]['value'],
                            'card_att_2': player['attributes'][1]['value'],
                            'card_att_3': player['attributes'][2]['value'],
                            'card_att_4': player['attributes'][3]['value'],
                            'card_att_5': player['attributes'][4]['value'],
                            'card_att_6': player['attributes'][5]['value'],
                            'quality': player['quality'],
                            'color': player['color'],
                            'is_gk': player['isGK'],
                            'is_special_type': player['isSpecialType'],
                            'is_loan': player['isLoan'],
                            'model_name': player['modelName'],
                            'base_id': player['baseId'],
                            'ea_id': player['baseId']
                        }

                        if player_data not in players:
                            players.append(player_data)

                except ValueError:
                    failed_urls.append(url)

                    print("Can't convert page to JSON")
            else:
                failed_urls.append(url)

                print('Url failed: {}'.format(url))

            print([(n['common_name']) for n in players],
                  'Page {}'.format(i))

        if failed_urls:
            self.build_player_data(failed=failed_urls, data=players)

        return players

    def build_players(self, *args, **kwargs):
        data = self.build_player_data()
        created_players = []

        for obj in data:
            player, created = Player.objects.get_or_create(**obj)

            if created:
                player.slug = slugify(
                    '{}-{}'.format(player.id, player.common_name))
                created_players.append(created)

                print('Created Player: {}'.format(player))

        print(len(created_players))

        return
