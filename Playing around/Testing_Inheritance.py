Units_list=[]
class Barracks:
    def __init__(self,id,Upgrade_level=0,Units_Counter=0):
        self.id = id
        self.Building_HP=1500
        self.Upgrade_Level=Upgrade_level
        self.Units_Counter=Units_Counter
        self.Units=[
            {
                "Sword":"Men at Arms",
                "Spear": "Pickman"
                }
        ]

    def Upgrades(self):
        if self.Upgrade_Level >= 3:
            print(f"The Upgrade Level reached its maximum ({self.Upgrade_Level})")
            return self
        else:
            self.Upgrade_Level +=1
            for i in Units_list:
                i.Upgrade_Level = self.Upgrade_Level
            return self
        
    def Units_numbers(self):
        print(f"The number of units = {self.Units_Counter}")
        return self

    def Add_Unit(self):
        Building.Units_Counter+=1
        return self


class Man_at_Arms(Barracks):
    def __init__(self,id,Upgrade_level,Units_Counter,MATid,Unit_HP,Attack_dmg,Armor):
        
        super().__init__(id,Upgrade_level,Units_Counter)
        self.Unit_id=MATid
        self.Unit_HP=Unit_HP
        self.Unit_upgrade_level=0
        self.Attack_dmg=5
        self.Armor=2
        self.Add_Unit()
        

    def unit_info(self):
        print(f"\nUnit_id = {self.Unit_id}\
            \nUnit_HP = {self.Unit_HP}\
            \nUnit_Attack = {self.Attack_dmg}\
            \nUnit_Armor = {self.Armor}\
            \nUnite_Upgrade_Level = {self.Unit_upgrade_level}\
            \nUnit Barracks_id= {self.id} \
            \nBarracks_Upgrade_Level = {self.Upgrade_Level}")
        return self


Building=Barracks(1)
Building.Upgrades().Upgrades()
for i in range(10):
    #Building.Add_Unit()
    Units_list.append(Man_at_Arms(Building.id,Building.Upgrade_Level,Building.Units_Counter,1,80,0,0)) 

Building.Units_numbers()