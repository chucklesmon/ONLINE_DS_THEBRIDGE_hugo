import pandas as pd
import requests
import variables as v

from bs4 import BeautifulSoup

def tournaments(tournaments_url):
    columns = ['Deck', 'Placement', 'Tournament', 'Players', 'Tier']
    df_tournaments = pd.DataFrame(columns = columns)

    tournaments = requests.get(tournaments_url)
    soup_tournaments = BeautifulSoup(tournaments.text, "lxml")

    table = soup_tournaments.find('table')
    rows = table.find_all('tr')

    for tournament in rows:
        t_name = tournament.get('data-name') if tournament.get('data-name') else None
        t_players = int(tournament.get('data-players')) if tournament.get('data-players') else None

        '''df_tournaments.loc[len(df_tournaments)] = {
            'Tournament': t_name,
            'Players': t_players
        }'''

        link_tag = tournament.find('a')
        link = link_tag.get('href') if link_tag else None

        if t_players:
            if t_players > 128:
                tier = 1
            elif t_players > 64:
                tier = 2
            else:
                tier = 3


        if link:
            top16(df_tournaments = df_tournaments, url = v.BASE_URL + link, t_name = t_name, t_players = t_players, tier = tier)

    return df_tournaments

def top16(df_tournaments, url, t_name, t_players, tier):
    tournament = requests.get(url)
    soup_tournament = BeautifulSoup(tournament.text, "lxml")

    table = soup_tournament.find('table')
    rows = table.find_all('tr')

    player_rows = rows[1:17]

    for player in player_rows:
        p_placement = player.get('data-placing') if player.get('data-placing') else None

        locate_deck = player.find('span', attrs = {'data-tooltip':True})
        p_deck = locate_deck.get('data-tooltip') if locate_deck else None

        df_tournaments.loc[len(df_tournaments)] = {
            'Deck': p_deck,
            'Placement': p_placement,
            'Tournament': t_name,
            'Players': t_players,
            'Tier': tier
        }

    return df_tournaments


