if __name__ == "__main__":
    import argparse as agp
    parser = agp.ArgumentParser(
        prog="Sudden Flash Card Event",
        description="Nagware to get the user to do their damn flash card studying.",
    )
    parser.add_argument('-cfg', '--config', '-c', type=str, help="Directory to the config file.", required=True)
    args = parser.parse_args()

    import desktop.TrayMenu
    tray = desktop.TrayMenu.TrayMenu(args.config)
    pass