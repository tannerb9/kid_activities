def run(*names):
    for kid in names:
        print(f"{kid} ran like a fool!")


def swing(*names):
    for kid in names:
        print(f"{kid} enjoyed playing on the swings.")


def slide(*names):
    for kid in names:
        print(f"{kid} raced down the slides.")


def hide_and_seek(*names):
    for kid in names:
        print(f"{kid} played hide and seek.")


run("Pam", "Sam", "Andres", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")
