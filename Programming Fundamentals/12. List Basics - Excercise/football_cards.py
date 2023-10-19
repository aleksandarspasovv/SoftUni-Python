team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

is_game_terminated = False

terminated_players = input().split()

for players in terminated_players:
    if players in team_a:
        team_a.remove(players)
    elif players in team_b:
        team_b.remove(players)

    if len(team_a) < 7 or len(team_b) < 7:
        is_game_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if is_game_terminated:
    print(f'Game was terminated')
