import random

#Attack using magical damage
class Ability:

    def __init__(self, name, attack_strength, crit_strength = 1, crit_chance = 0):
        self.name = name
        self.attack_strength = attack_strength
        self.crit_strength = crit_strength
        self.crit_chance = crit_chance

    def attack(self):
    # Return attack value. Value is a random integer between half the attack_strength and the attack_strength
        damage = random.randint(self.attack_strength//2,self.attack_strength)
        print(self.name + " deals " + str(damage) + " magical damage!")
        return damage

    def update_attack(self, attack_strength):
    # Update attack value
        self.attack_strength = attack_strength

#Attack with physical damage
class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        The waepon can also land a critical hit for extra damage
        Hint: The attack power is inherited.
        """
        crit_modifier = 1
        if(random.randint(1,100) < self.crit_chance):
            crit_modifier = self.crit_strength
            print(self.name + " deals a critical Hit!")
        damage = random.randint(0,self.attack_strength)*crit_modifier
        print(self.name + " deals " + str(damage) + " physical damage!")
        return damage

#Blocks physical damage
class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        defended_amount = random.randint(0,self.defense)
        print(self.name + " blocks " +str(defended_amount) + " physical damage")
        return defended_amount

#Blocks magical damage
class Relic(Armor):
    def defend(self):
        defended_amount = random.randint(self.defense//4,self.defense*3//4)
        print(self.name + " blocks " +str(defended_amount) + " magical damage")
        return defended_amount

class Hero:
    def __init__(self, name, health=1000, damage_priority = 10, speed = 10):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.damage_priority = damage_priority
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
        self.is_alive = True
        self.speed = speed

    def add_ability(self, ability):
    # Add ability to abilities list
        self.abilities.append(ability)

    def add_armor(self, armor):
    # Add ability to abilities list
        self.armors.append(armor)

    def attack(self):
    # Run attack() on every ability hero has
        print(self.name + " begins attacking!")
        physical_attack_total = 0
        magical_attack_total = 0

        for ability in self.abilities:
            if(type(ability).__name__ == "Weapon"):
                physical_attack_total += ability.attack()
            else:
                magical_attack_total += ability.attack()

        print(self.name + " deals " + str(physical_attack_total) + " physical damage and " + str(magical_attack_total) + " magic damage!")
        attack_total = list()
        attack_total.append(physical_attack_total)
        attack_total.append(magical_attack_total)
        return attack_total

    def defend(self):
    # Run defend() on every armor hero has
        armor_defend_total = 0
        relic_defend_total = 0

        for armor in self.armors:

            if(type(armor).__name__ == "Armor"):
                armor_defend_total += armor.defend()
            else:
                relic_defend_total += armor.defend()


        defend_total = list()
        defend_total.append(armor_defend_total)
        defend_total.append(relic_defend_total)
        return defend_total

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        self.health -= damage_amt
        if(self.health <= 0 and self.is_alive):
            print(self.name + " has died!")
            self.is_alive = False
            self.deaths += 1
            self.health = 0
            return 1

        return 0

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

    def modify_hero(self):
        want_to_add_more_attributes = True
        while(want_to_add_more_attributes):
            choice = get_and_validate_input_string("Would you like to add an ability, weapon, armor or relic? (Enter type to add or something else to skip: ")
            if(choice.lower() == "ability"):
                # ability_name = self.get_and_validate_input_string("Please enter ability name: ")
                # ability_strength = self.get_and_validate_input_int("Please enter abilty strength: ")
                # ability = Ability(ability_name,ability_strength)
                ability = create_ability_object(Ability)
                self.add_ability(ability)

            elif(choice.lower() == "weapon"):
                #weapon_name = self.get_and_validate_input_string("Please enter weapon name: ")
                #weapon_strength = self.get_and_validate_input_int("Please enter weapon strength: ")
                #weapon = Weapon(weapon_name,weapon_strength)
                weapon = create_ability_object(Weapon)
                self.add_ability(weapon)

            elif(choice.lower() == "armor"):
                #armor_name = self.get_and_validate_input_string("Please enter armor name: ")
                #armor_strength = self.get_and_validate_input_int("Please enter armor strength: ")
                #armor = Armor(armor_name,armor_strength)
                armor = create_object(Armor)
                self.add_armor(armor)

            elif(choice.lower() == "relic"):
                relic = create_object(Relic)
                self.add_armor(relic)

            else:
                choice = get_and_validate_input_string("Stop adding abilities, weapons and armor? (S to stop, anything else to continue): ")
                if(choice.lower() == "s"):
                    want_to_add_more_attributes = False

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()
        self.living_heroes = 0

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)
        self.living_heroes += 1

    def load_hero(self, file_name):
        data = list()
        try:
            f = open(file_name, 'r')
        except FileNotFoundError:
            print("Error, file not found.")
            return 0

        data = f.readlines()
        f.close()

        name = data[0].rstrip()
        health = int(data[1])
        priority = int(data[2])
        hero = Hero(name, health, priority)

        abilities = load_power(Ability, data[3])
        weapons = load_power(Weapon, data[4])
        armors = load_defense(Armor, data[5])
        relics = load_defense(Relic, data[6])

        for ability in abilities:
            hero.add_ability(ability)

        for weapon in weapons:
            hero.add_ability(weapon)

        for armor in armors:
            hero.add_armor(armor)

        for relic in relics:
            hero.add_armor(relic)

        self.add_hero(hero)

    def build_hero(self):
        #Allows user to build a hero and add it to this team
        name = get_and_validate_input_string("Enter name of hero: ")
        health = get_and_validate_input_int("Enter max health of hero: ")
        priority = get_and_validate_input_int("Enter damage priority of hero (standard is 10, higher means they take a greater portion of damage): ")
        hero = Hero(name,health)
        want_to_add_more_attributes = True
        hero.modify_hero()
        self.add_hero(hero)

    def get_hero(self, index):
        #returns hero from index, helper function for find and remove_hero
        if(int(index) == -999):
            print("Error, hero not found")
            return "Error"
        elif(int(index) >= len(self.heroes)):
            print("Error, index out of range")
            return "Error"
        else:
            return self.heroes[index]

    def find_hero(self, name):
        """
        Find and return hero index from heroes list.
        If Hero isn't found return -999.
        """
        for index in range(0,len(self.heroes)):
            if(self.heroes[index].name == name):
                return index

        return -999

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return -999.
        """
        hero_index = self.find_hero(name)
        if(hero_index == -999):
            return -999

        if(self.heroes[hero_index].is_alive):
            self.living_heroes -= 1
        self.heroes.pop(hero_index)

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)
            for ability in hero.abilities:
                print(ability.name + ": " + str(ability.attack_strength).rstrip() + " " + str(ability.crit_strength).rstrip() + " " + str(ability.crit_chance).rstrip())
            for armor in hero.armors:
                print(armor.name + ": " + str(armor.defense).rstrip())

    def update_kills(self, num_kills):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            hero.add_kill(num_kills)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        print(self.name + " attacks " + other_team.name +"!")
        physical_attack_total = 0
        magical_attack_total= 0
        for hero in self.heroes:
            if(hero.is_alive):
                attack_total = hero.attack()
                physical_attack_total += attack_total[0]
                magical_attack_total += attack_total[1]

        attack_total = list()
        attack_total.append(physical_attack_total)
        attack_total.append(magical_attack_total)
        #print(attack_total)
        kills = other_team.defend(attack_total)
        print(self.name + " has killed " + str(kills) + " opponent(s)")
        self.update_kills(kills)

    def deal_damage(self, damage, priority_total):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        print(self.name + " takes " + str(damage) + " damage!")
        kills = 0
        for hero in self.heroes:
            if(hero.is_alive):
                #kills += hero.take_damage(damage)
                damage_portion = damage * hero.damage_priority//priority_total
                print(hero.name + " takes " + str(damage_portion) + " damage!")
                kill = hero.take_damage(damage_portion)
                self.living_heroes -= kill
                kills += kill

        return kills

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        print(self.name + " prepares their defense!")
        physical_defend_total = 0
        magical_defend_total = 0
        priority_total = 0
        for hero in self.heroes:
            if(hero.is_alive):
                defend_total = hero.defend()
                physical_defend_total += defend_total[0]
                magical_defend_total += defend_total[1]
                priority_total += hero.damage_priority

        #print(defend_total)

        physical_damage = damage_amt[0]
        magical_damage = damage_amt[1]

        if(physical_defend_total >= physical_damage):
            print("Physical damage was completely blocked!")
            physical_damage = 0

        else:
            physical_damage -= physical_defend_total

        if(magical_defend_total >= magical_damage):
            print("Magical damage was completely blocked!")
            magical_damage = 0

        else:
            magical_damage -= magical_defend_total

        remain_damage = physical_damage + magical_damage

        kills = self.deal_damage(remain_damage,priority_total)

        return kills

    def revive_heroes(self, health=1000):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health
            if(not hero.is_alive):
                hero.is_alive = True
                self.living_heroes += 1

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        print("Team name: " + self.name)
        print("Heroes remaining: " + str(self.living_heroes))
        for hero in self.heroes:
            print("Name: " + hero.name)
            print("Is alive: " + str(hero.is_alive))
            print("Health: " + str(hero.health) + "/"+ str(hero.start_health))
            print("Kills: " + str(hero.kills))
            print("Deaths: " + str(hero.deaths))

    def build_or_load_hero_to_team(self):
        want_to_add_more = True
        while(want_to_add_more):
            choice = get_and_validate_input_string("Would you like to build a hero? (B to build one, L to load hero, S to stop): ")
            if(choice.lower() == "b"):
                self.build_hero()

            elif(choice.lower() =="l"):
                file = get_and_validate_input_string("Input file to load hero data from: ")
                self.load_hero(file)
            #Checks if user wants to keep adding heroes
            elif(choice.lower() == "s"):
                if(self.living_heroes < 1):
                    print("Error, need at least 1 hero on each team")
                else:
                    want_to_add_more = False
            else:
                print("Error, invalid input")


class Arena:
    def __init__(self):
        self.teams = [None, None]
        self.teams[0] = None
        self.teams[1] = None

    def load_team(self,team_name,team_number):
        data = list()
        team_file = team_name
        try:
            f = open(team_file, 'r')
        except FileNotFoundError:
            return 0

        data = f.readlines()
        f.close()

        print("File found")
        name = get_and_validate_input_string("What would you like to rename this team for the upcoming battle: ")
        self.teams[team_number-1] = Team(name)

        hero_names = data[0].split("*")
        for name in hero_names:
            hero = self.teams[team_number-1].load_hero(name.rstrip())
            if(hero == 0):
                print("Error, " + name + " file was not found.")

    def build_team(self, team_number):
        """
        This method should allow user to build team two.
        """
        team_name = get_and_validate_input_string("Please enter name for team "+ str(team_number)+" (Enter file name to load a team, include .txt): ")
        file_found = self.load_team(team_name,team_number)
        if(file_found == 0):
            print("No file found, creating team")
            self.teams[team_number-1] = Team(team_name)

        self.teams[team_number-1].build_or_load_hero_to_team()

    #Allows you to modify a team by adding a hero, removing a hero or adding a power to a hero
    def modify_team(self, team_number):
        print("Modifying " + arena.teams[team_number].name)
        arena.teams[team_number].view_all_heroes()
        want_to_add_more = True
        while(want_to_add_more):
            choice = get_and_validate_input_string("A to add hero, R to remove hero, P to add power to hero, S to stop: ")
            if(choice.lower() == "a"):
                self.teams[team_number].build_or_load_hero_to_team()

            elif(choice.lower() =="r"):
                choice = get_and_validate_input_string("Input name of hero to remove: ")
                code = self.teams[team_number].remove_hero(choice)
                if(code == -999):
                    print("Error, hero not found")

            #Checks if user wants to keep adding heroes
            elif(choice.lower() == "p"):
                choice = get_and_validate_input_string("Input name of hero to add powers to: ")
                code = self.teams[team_number].find_hero(choice)
                if(code == -999):
                    print("Error, hero not found")
                else:
                    hero = self.teams[team_number].get_hero(code)
                    want_to_add_more_attributes = True
                    hero.modify_hero()

                    choice = get_and_validate_input_string("Would you like to save this hero for future battles? (Y to save, anything else to skip): ")
                    if(choice.lower() == "y"):
                        save_hero(hero)

            elif(choice.lower() == "s"):
                if(self.teams[team_number].living_heroes < 1):
                    print("Error, need at least 1 hero on team")
                else:
                    want_to_add_more = False

            else:
                print("Error, invalid input")


    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        attacking_team = 0
        while(self.teams[0].living_heroes > 0 and self.teams[1].living_heroes > 0):
            self.show_stats()
            self.teams[attacking_team].attack(self.teams[1-attacking_team])
            if(attacking_team == 0):
                attacking_team = 1
            else:
                attacking_team = 0

        print(self.teams[attacking_team].name + " has won the battle!")

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        self.teams[0].stats()
        self.teams[1].stats()

#User creates object based on their input
def create_object(Class):
    class_name = Class.__name__.lower()
    name = get_and_validate_input_string("Please enter {} name: ".format(class_name))
    strength = get_and_validate_input_int("Please enter {} strength: ".format(class_name))
    object = Class(name, strength)
    return object

def create_ability_object(Class):
    class_name = Class.__name__.lower()
    name = name = get_and_validate_input_string("Please enter {} name: ".format(class_name))
    strength = get_and_validate_input_int("Please enter {} strength: ".format(class_name))
    crit = get_and_validate_input_int("Please enter {} critical power: ".format(class_name),0)
    chance = get_and_validate_input_int("Please enter {} critical chance: ".format(class_name),0)
    object = Class(name, strength, crit, chance)
    return object


def load_power(Class, data):
    powerlist = list()
    if(data.rstrip() == "%"):
        return powerlist
    powers = data.rstrip().split("%")
    powers.pop(0)
    for power in powers:
        delimiter = power.find("*")
        delimiter2 = power.find("*", delimiter+1)
        delimiter3 = power.find("*", delimiter2+1)
        power_name = power[0:delimiter]
        power_strength = int(power[delimiter+1:delimiter2])
        power_crit = int(power[delimiter2+1:delimiter3])
        power_chance = int(power[delimiter3+1:])
        power_to_add = Class(power_name, power_strength, power_crit, power_chance)
        powerlist.append(power_to_add)

    return powerlist

def load_defense(Class, data):
    powerlist = list()
    if(data.rstrip() == "%"):
        return powerlist
    powers = data.rstrip().split("%")
    powers.pop(0)
    for power in powers:
        delimiter = power.find("*")
        power_name = power[0:delimiter]
        power_strength = int(power[delimiter+1:])
        power_to_add = Class(power_name, power_strength)
        powerlist.append(power_to_add)

    return powerlist


def get_and_validate_input_string(prompt):
    try:
        string_to_return = input(prompt)
    except EOFError:
        print("Please do not try to crash the program Alan.")
        string_to_return = get_and_validate_input_string(prompt)
    finally:
        if(len(string_to_return)<1):
            print("Error, nothing in string!")
            string_to_return = get_and_validate_input_string(prompt)
        return string_to_return


def get_and_validate_input_int(prompt, minimum=1):
    try:
        int_to_return = input(prompt)
    except EOFError:
        print("Please do not try to crash the program Alan.")
        int_to_return = get_and_validate_input_int(prompt, minimum)
    finally:
        try:
            int_to_return = int(int_to_return)
        except ValueError:
            print("Error, input is not a number")
            int_to_return = get_and_validate_input_int(prompt, minimum)
        finally:
            if(int_to_return < minimum):
                print("Error, value must be at least " + str(minimum))
                int_to_return = get_and_validate_input_int(prompt, minimum)
            else:
                return int_to_return


def save_hero(hero):

    choice = get_and_validate_input_string("Please enter filename to save to (include .txt at the end): ")
    hero_abilities = "%"
    hero_weapons = "%"
    hero_armors = "%"
    hero_relics = "%"

    for ability in hero.abilities:
        if(type(ability).__name__ == "Weapon"):
            hero_weapons += ability.name + "*"
            hero_weapons += str(ability.attack_strength) + "*"
            hero_weapons += str(ability.crit_strength) + "*"
            hero_weapons += str(ability.crit_chance) + "%"
        else:
            hero_abilities += ability.name + "*"
            hero_abilities += str(ability.attack_strength) + "*"
            hero_abilities += str(ability.crit_strength) + "*"
            hero_abilities += str(ability.crit_chance) + "%"

    for armor in hero.armors:
        if(type(armor).__name__ == "Armor"):
            hero_armors += armor.name + "*"
            hero_armors += str(armor.defense) + "%"
        else:
            hero_relics += armor.name + "*"
            hero_relics += str(armor.defense) + "%"


    hero_abilities = hero_abilities[0:len(hero_abilities)-1]
    hero_weapons = hero_weapons[0:len(hero_weapons)-1]
    hero_armors = hero_armors[0:len(hero_armors)-1]
    hero_relics = hero_relics[0:len(hero_relics)-1]

    file = open(choice,"w")

    file.write(hero.name+"\n")
    file.write(str(hero.start_health)+"\n")
    file.write(str(hero.damage_priority)+"\n")
    file.write(hero_abilities + "\n")
    file.write(hero_weapons + "\n")
    file.write(hero_armors + "\n")
    file.write(hero_relics + "\n")

    file.close()


arena = Arena()
arena.build_team(1)
arena.build_team(2)
running = True
while(running):
    arena.teams[0].view_all_heroes()
    arena.teams[1].view_all_heroes()
    arena.team_battle()
    arena.show_stats()

    choice = get_and_validate_input_string("Would you like to stage another battle? (S to stop, anything else to continue): ")

    if(choice.lower() == 's'):
        running = False

    else:
        arena.teams[0].revive_heroes()
        arena.teams[1].revive_heroes()
        choice = get_and_validate_input_string("Would you like to add or remove a hero, or add a power to a hero? (S to skip): ")
        if(choice.lower() != 's'):
            arena.modify_team(0)
            arena.modify_team(1)
