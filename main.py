import init_django_orm # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for player in players:
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )

        guild = None
        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"]["description"]}
            )

        for skill_data in player["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        Player.objects.create(
            nickname=player["nickname"],
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
