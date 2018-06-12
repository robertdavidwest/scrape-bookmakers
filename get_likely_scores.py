import json
import pandas as pd


def get_score_url(game_name):
    return "https://www.oddschecker.com/" \
            "football/world-cup/%s/correct-score" % game_name


def get_score_table(game_name):
    url = get_score_url(game_name)
    dfs = pd.read_html(url)
    score_table = dfs[1]
    score_table = score_table.iloc[:, :2]
    score_table.columns = ['winner_and_score', 'odds']
    return score_table


def get_likely_score(score_table):
    likely_result = score_table.iloc[0, 0]
    odds = score_table.iloc[0, 1]
    return likely_result, odds


def main():
    game_names = json.load(open("group-game-names.json", 'r'))
    for game_name in game_names:
        #game_name = "russia-v-saudi-arabia"
        score_table = get_score_table(game_name)
        likely_score, odds = get_likely_score(score_table)
        print(game_name, likely_score, odds)


if __name__ == '__main__':
    main()
