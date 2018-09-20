def load_power(Class, data):
    powerlist = list()
    powers = data.split("%")
    for power in powers:
        delimiter = power.find("*")
        power_name = power[0:delimiter]
        power_strength = power[delimiter+1:]
        power_to_add = Class(power_name, power_strength)
        powerlist.append(power_to_add)

    return powerlist

#Previous version to load powers for heroes from file
abilities = data[3].split("%")
for ability in abilities:
    delimiter = ability.find("*")
    ability_name = ability[0:delimiter]
    ability_power = ability[delimiter+1:]
    ability = Ability(ability_name,ability_power)
    hero.add_ability(ability)

weapons = data[4].split("%")
for weapon in weapons:
    delimiter = weapon.find("*")
    weapon_name = weapon[0:delimiter]
    weapon_power = weapon[delimiter+1:]
    weapon = Weapon(weapon_name,weapon_power)
    hero.add_ability(ability)

armors = data[5].split("%")
for armor in armors

#test code for main
'''#if __name__ == "__main__":
hero = Hero("Wonder Woman")
#print(hero.attack())
ability = Ability("Divine Speed", 300)
hero.add_ability(ability)
#print(hero.attack())
hero2 = Hero("Batman")
#print(hero2.attack())
new_ability = Ability("Rich", 800)
weapon = Weapon("Batmobile", 1600)
armor2 = Armor("Batsuit", 1500)
hero2.add_ability(new_ability)
hero2.add_ability(weapon)
hero2.add_armor(armor2)
#print(hero2.attack())

team = Team("Justice League")
team2 = Team("Injustice League")
hero3 = Hero("Superman", 2000)
ability3 = Ability ("Heat Vision", 1000)
armor = Armor("Iron Skin", 1000)
hero3.add_armor(armor)
hero3.add_ability(ability3)
team2.add_hero(hero)
team.add_hero(hero2)
team2.add_hero(hero3)
team.view_all_heroes()
team2.view_all_heroes()

team.stats()
team2.stats()

team.attack(team2)

team.stats()
team2.stats()

team2.attack(team)

team.stats()
team2.stats()

team.attack(team2)

team.stats()
team2.stats()

team2.attack(team)

team.stats()
team2.stats()
'''

#Allows user to build team 1 from the terminal
'''def build_team_one(self):
    #This method should allow a user to build team one.

    team_name = self.get_and_validate_input_string("Please enter name for team 1: ")
    self.teams[0] = Team(team_name)
    want_to_add_more = True
    while(want_to_add_more):
        name = self.get_and_validate_input_string("Enter name of hero: ")
        health = self.get_and_validate_input_int("Enter max health of hero: ")
        priority = self.get_and_validate_input_int("Enter damage priority of hero (standard is 10, higher means they take a greater portion of damage): ")
        hero = Hero(name,health,priority)
        want_to_add_more_attributes = True
        while(want_to_add_more_attributes):
            choice = self.get_and_validate_input_string("Would you like to add an ability, weapon or armor? (Enter type to add or something else to skip: ")
            if(choice.lower() == "ability"):
                ability_name = self.get_and_validate_input_string("Please enter ability name: ")
                ability_strength = self.get_and_validate_input_int("Please enter abilty strength: ")
                ability = Ability(ability_name,ability_strength)
                hero.add_ability(ability)

            elif(choice.lower() == "weapon"):
                weapon_name = self.get_and_validate_input_string("Please enter weapon name: ")
                weapon_strength = self.get_and_validate_input_int("Please enter weapon strength: ")
                weapon = Weapon(weapon_name,weapon_strength)
                hero.add_ability(weapon)

            elif(choice.lower() == "armor"):
                armor_name = self.get_and_validate_input_string("Please enter armor name: ")
                armor_strength = self.get_and_validate_input_int("Please enter armor strength: ")
                armor = Armor(armor_name,armor_strength)
                hero.add_armor(armor)

            else:
                choice = self.get_and_validate_input_string("Stop adding abilities, weapons and armor? (S to stop, anything else to continue):")
                if(choice.lower() == "s"):
                    want_to_add_more_attributes = False

        self.teams[0].add_hero(hero)

        #Checks if user wants to keep adding heroes
        choice = self.get_and_validate_input_string("Stop adding heroes? (S to stop, anything else to continue): ")
        if(choice.lower() == "s"):
            want_to_add_more = False
'''
