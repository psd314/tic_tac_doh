"""Console script for tic_tac_doh."""
import argparse
from .game_menu import menu

def main():
    """Console script for tic_tac_doh."""
    parser = argparse.ArgumentParser()

    parser.add_argument('game', choices=['tic', 'connect'], help='Select game.')
    parser.add_argument('action', choices=['play', 'train'], help='Play or train the AI.')
    parser.add_argument('-p', '--policy', default='default data included with package',
                        help='File path to policy for agent to play with.')
    parser.add_argument('-e', '--episodes', default=10000, help='Number of episodes for AI to train.')
    args = parser.parse_args()

    print("Arguments: " + str(args))
    if args.game == 'tic' and args.action == 'play':
        menu()
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
