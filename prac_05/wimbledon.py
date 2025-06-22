"""
Wimbledon Winners Report
Estimate: 60 minutes
Actual:   123 minutes
"""

DATA_FILE = "wimbledon.csv"


def run():
    match_data = load_data(DATA_FILE)
    winner_counts = tally_winners(match_data)
    winner_countries = extract_countries(match_data)

    print("Wimbledon Champions:")
    show_winners(winner_counts)

    print(f"\nThese {len(winner_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winner_countries)))


def load_data(file_path):
    """Load match data from the CSV file and return as a list of lists."""
    with open(file_path, "r", encoding="utf-8-sig") as file:
        next(file)  # skip header
        return [line.strip().split(',') for line in file]


def tally_winners(data):
    """Create a dictionary with each champion and how many times they've won."""
    win_dict = {}
    for entry in data:
        player = entry[2]
        if player in win_dict:
            win_dict[player] += 1
        else:
            win_dict[player] = 1
    return win_dict


def extract_countries(data):
    """Extract a set of unique countries from the data."""
    return {entry[1] for entry in data}


def show_winners(winner_data):
    """Print out each winner and their total wins."""
    for player, total in winner_data.items():
        print(f"{player} {total}")


run()
