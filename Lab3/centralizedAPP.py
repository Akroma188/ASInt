import dbUI


def main():
    interface = dbUI.dbUI()

    while not interface.user_input() :
        pass
    interface.db.file.close()

if __name__ == "__main__":
    main()