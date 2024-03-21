from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_player_kingdom_relations = [("player_faction",1.00),("outlaws",-0.15),("sea_raider",-0.15),("steppe_bandit",-0.15),("taiga_bandit",-0.15),("mountain_bandits", -0.15),("forest_bandits", -0.15),("desert_bandit",-0.15),("embers_flame",-0.15),("peasant_rebels", -0.1),("deserters", -0.05),("heresy_missionary",-0.05),("living_dead", -0.05)]
default_kingdom_relations = [("outlaws",-0.05),("sea_raider",-0.05),("steppe_bandit",-0.05),("taiga_bandit",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("desert_bandit",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("heresy_missionary",-1),("living_dead", -1)]
default_Nords_kingdom_relations = [("outlaws",-0.05),("sea_raider",+0.01),("steppe_bandit",-0.05),("taiga_bandit",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("desert_bandit",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("heresy_missionary",-1),("living_dead", -1)]
default_kingdom_relations_undead = [("outlaws",-0.05),("sea_raider",-0.05),("steppe_bandit",-0.05),("taiga_bandit",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("desert_bandit",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("heresy_missionary",1),("living_dead", 1)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [],0x778899),
  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
   
  ("sea_raider","SeaRaider", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x6495ED),
  ("steppe_bandit","Steppebandit", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0xADFF2F),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x2E8B57),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x228B22),
  ("taiga_bandit","Taigabandit", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [],  0x556B2F),
  ("desert_bandit","Desertbandit", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x808000),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.15)], [], 0x888888),
  ("skolderbrotva","Skolderbrotva", 0, 0.5,[], [],0x4682B4),
  ("embers_flame","Nethor of the Embers", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.15)], [], 0xBA55D3),
  
  
  ("holy_missionary",  "HolyMissionary", 0, 0.5,[("player_faction",0),("heresy_missionary",-1),("kingdom_undead",-1),("commoners",0),("outlaws",-0.05),("sea_raider",-0.05),("steppe_bandit",-0.05),("taiga_bandit",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("desert_bandit",-0.05),("peasant_rebels", -0.1),("deserters", -0.05)], [], 0xFFFFFF00),
  ("heresy_missionary",  "HeresyMissionary", 0, 0.5,[("player_faction",-0.30),("holy_missionary",-1),("kingdom_sept",-1),("commoners",-0.6),("outlaws",-0.05),("sea_raider",-0.05),("steppe_bandit",-0.05),("taiga_bandit",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("desert_bandit",-0.05),("peasant_rebels", -0.1),("deserters", -0.05)], [], 0xFFBA55D3),
  ("living_dead",  "LivingDead", 0, 0.5,[("player_faction",0),("commoners",-0.6),("player_faction",-0.15),("outlaws",-0.05),("sea_raider",-0.05),("steppe_bandit",-0.05),("taiga_bandit",-0.05),("mountain_bandits", -0.05),("forest_bandits", -0.05),("desert_bandit",-0.05),("peasant_rebels", -0.1),("deserters", -0.05)], [], 0xFF4B0082),
  
 

# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  ("culture_7",  "{!}culture_7", 0, 0.9, [], []),
  ("culture_undead",  "{!}culture_undead", 0, 0.9, [], []),
  ("culture_sept",  "{!}culture_sept", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, default_player_kingdom_relations, [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Kingdom of Swadia", 0, 0.9, default_kingdom_relations, [], 0xEE7744),
  ("kingdom_2",  "Kingdom of Vaegirs",    0, 0.9, default_kingdom_relations, [], 0xCCBB99),
  ("kingdom_3",  "Khergit Khanate", 0, 0.9, default_kingdom_relations, [], 0xCC99FF),
  ("kingdom_4",  "Kingdom of Nords",    0, 0.9, default_Nords_kingdom_relations, [], 0x33DDDD),
  ("kingdom_5",  "Kingdom of Rhodoks",  0, 0.9, default_kingdom_relations, [], 0x33DD33),
  ("kingdom_6",  "Sarranid Sultanate",  0, 0.9, default_kingdom_relations, [], 0xDDDD33),
  ("kingdom_undead",  "Kingdom of Undead",    0, 0.9, default_kingdom_relations_undead, [], 0xFF9400D3),
  ("kingdom_sept",  "Kingdom of Sept",    0, 0.9, default_kingdom_relations, [], 0xF0FFFF),
  	
  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], [],0xF0FFF0),
  ("travelingmerchants","Travelingmerchants", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], [],  0xFFFFF0),

  ("kingdom_7",  "City state of Zendar",    0, 0.9, default_kingdom_relations, [], 0xF0FFFF), 
 
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  ("invalid_camp","{!}Invalid_camp", 0, 0.5,[], []),
#INVASION MODE START
  ("ccoop_all_stars","All Stars", 0, 0.5,[], []),
#INVASION MODE END
]
