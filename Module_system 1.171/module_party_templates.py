from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Hidden hand",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_rioter,1,10),(trp_looter,2,20),(trp_rogue,3,20)]),
  ("looters_a","Hidden hand",icon_axeman|carries_goods(20),0,fac_outlaws,bandit_personality,[(trp_rioter,5,20),(trp_bandit,8,20),(trp_brigand,8,20),(trp_looter,10,30),(trp_rogue,10,30)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_slaver_chief,1,1),(trp_slave_crusher,2,4),(trp_slave_hunter,4,8),(trp_slave_driver,6,20),(trp_manhunter,10,50)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_steppe_bandit,bandit_personality,[(trp_steppe_bandit_2,1,3),(trp_steppe_bandit_1,2,12),(trp_steppe_bandit,5,50)]),
  ("steppe_bandits_a","Steppe Bandits",icon_khergit|carries_goods(6),0,fac_steppe_bandit,bandit_personality,[(trp_steppe_bandit_2,3,9),(trp_steppe_bandit_1,6,30),(trp_steppe_bandit,20,50)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_taiga_bandit,bandit_personality,[(trp_taiga_bandit_3,1,3),(trp_taiga_bandit_2,2,10),(trp_taiga_bandit_1,2,10),(trp_taiga_bandit,5,50)]),
  ("taiga_bandits_a","Tundra Bandits",icon_axeman|carries_goods(6),0,fac_taiga_bandit,bandit_personality,[(trp_taiga_bandit_3,3,9),(trp_taiga_bandit_2,6,20),(trp_taiga_bandit_1,6,20),(trp_taiga_bandit,25,50)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_desert_bandit,bandit_personality,[(trp_desert_bandit_2,1,10),(trp_desert_bandit_1,1,20),(trp_desert_bandit,5,50)]),
  ("desert_bandits_a","Desert Bandits",icon_vaegir_knight|carries_goods(6),0,fac_desert_bandit,bandit_personality,[(trp_desert_bandit_2,3,10),(trp_desert_bandit_1,6,30),(trp_desert_bandit,20,50)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_2,1,8),(trp_forest_bandit_1,1,20),(trp_forest_bandit,5,50)]),
  ("forest_bandits_a","Forest Bandits",icon_axeman|carries_goods(6),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_2,4,16),(trp_forest_bandit_1,5,30),(trp_forest_bandit,25,50)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit_2,1,3),(trp_mountain_bandit_1,2,20),(trp_mountain_bandit,5,30)]),
  ("mountain_bandits_a","Mountain Bandits",icon_axeman|carries_goods(6),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit_2,3,9),(trp_mountain_bandit_1,8,30),(trp_mountain_bandit,30,60)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_sea_raider,bandit_personality,[(trp_sea_raider_captain,1,3),(trp_sea_raider_senior,2,10),(trp_sea_raider,5,50)]),
  ("sea_raiders_a","Sea Raiders",icon_axeman|carries_goods(6),0,fac_sea_raider,bandit_personality,[(trp_sea_raider_captain,3,9),(trp_sea_raider_senior,10,30),(trp_sea_raider,20,50)]),
    
  ("heresy_missionary_steppe","Heresy Missionary Steppe",icon_axeman|carries_goods(2),0,fac_heresy_missionary,bandit_personality,[(trp_undead_shoot_c,3,10),(trp_undead_believer,10,20)]),
  ("heresy_missionary_taiga","Heresy Missionary Taiga",icon_axeman|carries_goods(2),0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard_c,1,2),(trp_undead_guard_b,2,4),(trp_undead_guard_a,3,6),(trp_undead_guard,5,10),(trp_undead_believer,10,20)]),
  ("heresy_missionary_desert","Heresy Missionary Desert",icon_axeman|carries_goods(2),0,fac_heresy_missionary,bandit_personality,[(trp_undead_knight,1,2),(trp_undead_horse,2,6),(trp_undead_believer,10,20)]),
  ("heresy_missionary_forest","Heresy Missionary Forest",icon_axeman|carries_goods(2),0,fac_heresy_missionary,bandit_personality,[(trp_undead_shoot_d,1,3),(trp_undead_shoot_b,2,6),(trp_undead_shoot_a,4,12),(trp_undead_believer,10,20)]),
  ("heresy_missionary_mountain","Heresy Missionary Mountain",icon_axeman|carries_goods(2),0,fac_heresy_missionary,bandit_personality,[(trp_undead_shoot_a,3,8),(trp_undead_footman_d,1,2),(trp_undead_footman_c,2,4),(trp_undead_footman_b,3,6),(trp_undead_footman_a,5,10)]),
  ("heresy_missionary_sea","Heresy Missionary Sea",icon_axeman|carries_goods(2),0,fac_heresy_missionary,bandit_personality,[(trp_undead_shoot_b,3,8),(trp_undead_footman_d,1,2),(trp_undead_footman_c,2,4),(trp_undead_footman_b,3,6),(trp_undead_footman_a,5,10)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
  ("sea_raiders_army","Sea Raiders Army",icon_axeman|carries_goods(180),0,fac_sea_raider,bandit_personality,[(trp_sea_raider_captain,15,30),(trp_sea_raider_senior,30,80),(trp_sea_raider,150,250)]),
  ("desert_bandits_army","Desert Banditss Army",icon_vaegir_knight|carries_goods(150),0,fac_desert_bandit,bandit_personality,[(trp_desert_bandit_2,15,30),(trp_desert_bandit_1,30,60),(trp_desert_bandit,100,200)]),
  ("forest_bandits_army","Forest Bandit Army",icon_axeman|carries_goods(70),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit_2,10,30),(trp_forest_bandit_1,40,100),(trp_forest_bandit,80,200)]),
  ("steppe_bandits_army","Steppe Bandit Army",icon_khergit|carries_goods(200),0,fac_steppe_bandit,bandit_personality,[(trp_black_khergit_horseman,30,60),(trp_steppe_bandit_2,30,60),(trp_steppe_bandit_1,60,120),(trp_steppe_bandit,120,200)]),
  ("taiga_bandits_army","Taiga Bandit Army",icon_axeman|carries_goods(50),0,fac_taiga_bandit,bandit_personality,[(trp_taiga_bandit_3,15,30),(trp_taiga_bandit_2,15,45),(trp_taiga_bandit_1,20,60),(trp_taiga_bandit,100,200)]),
  ("mountain_bandits_army","Mountain Bandit Army",icon_axeman|carries_goods(120),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit_2,20,60),(trp_mountain_bandit_1,50,120),(trp_mountain_bandit,150,300)]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,
  [
  (trp_caravan_master,1,1),(trp_caravan_guard,10,50)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,6,16)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),

  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(100)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_mercenary_swordsman,4,12),(trp_caravan_guard,12,40),(trp_mercenary_horseman,2,6),(trp_mercenary_crossbowman,4,12),]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,10),(trp_swadian_militia,2,4)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_infantry,2,4),(trp_swadian_skirmisher,2,4)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,1,2),(trp_swadian_knight,1,1)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight_1,1,2)]),

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,10),(trp_vaegir_footman,2,4)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_infantry,2,4),(trp_vaegir_marksman,2,4)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,1,1),(trp_vaegir_marksman_pluse,1,1)]),
  ("kingdom_2_reinforcements_d", "{!}kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_vaegir_knight_a,1,1)]),
  
  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,1,2),(trp_khergit_horse_archer,2,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_3_reinforcements_d", "{!}kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_khergit_lancer_1,1,1),(trp_khergit_veteran_horse_archer,1,1)]), #
 
  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,2,4)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_archer,2,4),(trp_nord_warrior,2,4)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,1),(trp_nord_champion_1,1,1),(trp_nord_veteran_archer_pluse,1,1)]),
  ("kingdom_4_reinforcements_d", "{!}kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_nord_dragon_rider,1,1)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_crossbowman,2,4),(trp_rhodok_veteran_spearman,2,4)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant_1,1,1),(trp_rhodok_sharpshooter_1,1,1)]), 
  ("kingdom_5_reinforcements_d", "{!}kingdom_5_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_rhodok_rider_sergeant_a,1,1)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_veteran_footman,2,4),(trp_sarranid_archer,2,2)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,1,1),(trp_sarranid_mamluke,1,1)]),
  ("kingdom_6_reinforcements_d", "{!}kingdom_6_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_sarranid_mamluke_dragon,1,1)]),
  
  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_zendar_soldier,2,4),(trp_zendar_soldier_1,2,3)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_zendar_senior_soldier,2,4),(trp_zendar_senior_soldier_1,2,3)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_zendar_sergeant,1,2),(trp_zendar_sergeant_1,1,1),(trp_zendar_sergeant_horseman,1,1)]),
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_zendar_sergeant,1,2),(trp_zendar_sergeant_1,1,1),(trp_zendar_sergeant_horseman,1,1)]),
  
  ("kingdom_1_reinforcements_kingdom", "{!}kingdom_1_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_swadian_queen_guard,4,6),(trp_swadian_queen_knight,2,3),(trp_swadian_queen_knight_a,1,1),(trp_angel_c,1,1)]),
  ("kingdom_2_reinforcements_kingdom", "{!}kingdom_2_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_vaegir_marksman_women,8,16),(trp_vaegir_marksman_women_pluse,4,6)]),
  ("kingdom_3_reinforcements_kingdom", "{!}kingdom_3_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_khergit_woman_horse,8,16),(trp_khergit_woman_horse_pluse,4,6)]),
  ("kingdom_4_reinforcements_kingdom", "{!}kingdom_4_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_nord_women_veteran,1,2),(trp_nord_women_champion,1,1),(trp_nord_women_rider_dragon,1,1),(trp_nord_valkyries,1,1)]),
  ("kingdom_5_reinforcements_kingdom", "{!}kingdom_5_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_rhodok_sister,8,1),(trp_rhodok_sister_sergeant,3,6),(trp_rhodok_sister_sergeant_a,1,2)]),
  ("kingdom_6_reinforcements_kingdom", "{!}kingdom_6_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_sarranid_horsewomen,4,6),(trp_sarranid_mamlukewomen,2,3),(trp_sarranid_mamlukewomen_dragon,1,1)]),
  ("kingdom_7_reinforcements_kingdom", "{!}kingdom_7_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_zendar_combat_maid,2,5)]),
  ("kingdom_undead_reinforcements_kingdom", "{!}kingdom_undead_reinforcements_kingdom", 0, 0, fac_commoners, 0, [(trp_undead_knight_b,2,4),(trp_angel_a,1,1)]),
  
  ("kingdom_undead_reinforcements_a", "{!}kingdom_undead_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_undead_farmer,4,8),(trp_skeleton,4,8),(trp_undead_believer,3,6)]),
  ("kingdom_undead_reinforcements_b", "{!}kingdom_undead_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_undead_shooter,4,8),(trp_undead_shoot_a,4,8),(trp_skeleton_shooter,4,8)]),
  ("kingdom_undead_reinforcements_c", "{!}kingdom_undead_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_undead_infantry_horse,1,2),(trp_undead_infantry_horse_a,1,1),(trp_undead_guard_b,1,1),(trp_undead_knight,1,1),(trp_undead_knight_pluse,1,1)]),
  ("kingdom_undead_reinforcements_d", "{!}kingdom_undead_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_undead_knight_b,2,4),(trp_angel_a,1,1)]),
  
  ("kingdom_undead_reinforcements_inite_a", "{!}kingdom_undead_reinforcements_inite", 0, 0, fac_commoners, 0, [(trp_undead_believer,100,150),(trp_undead_guard_a,20,30),(trp_undead_guard_b,10,25),(trp_undead_guard_c,10,25),(trp_undead_horse,10,20),(trp_undead_knight,10,10)]),
  ("kingdom_undead_reinforcements_inite_b", "{!}kingdom_undead_reinforcements_inite", 0, 0, fac_commoners, 0, [(trp_undead_footman,20,40),(trp_undead_footman_a,20,30),(trp_undead_footman_b,10,25),(trp_undead_footman_c,10,25),(trp_undead_footman_c,15,20),(trp_undead_footman_d,10,10)]),
  ("kingdom_undead_reinforcements_inite_c", "{!}kingdom_undead_reinforcements_inite", 0, 0, fac_commoners, 0, [(trp_undead_shoot_a,20,40),(trp_undead_shoot_b,20,30),(trp_undead_shoot_c,10,25),(trp_undead_footman_c,10,25),(trp_undead_footman_d,15,20)]),
  ("kingdom_undead_reinforcements_inite_d", "{!}kingdom_undead_reinforcements_inite", 0, 0, fac_commoners, 0, [(trp_undead_believer,50,60),(trp_undead_guard_a,10,25),(trp_undead_guard_b,10,25),(trp_undead_guard_c,10,25),(trp_undead_horse,15,20),(trp_undead_knight,10,10)]),

#("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_steppe_bandit,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_steppe_bandit,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_taiga_bandit,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_desert_bandit,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_sea_raider,bandit_personality,[(trp_sea_raider,15,50),(trp_sea_raider_senior,3,15),(trp_sea_raider_captain,1,3)]),
  ("looter_lair","Kidnappers Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_outlaws,bandit_personality,[(trp_looter,15,25)]),
  
 
  ("heresy_church_fores_lair","heresy church",icon_bandit_lair|carries_goods(8)|pf_is_static|pf_hide_defenders,0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard,15,25),(trp_undead_guard_a,10,20)]),
  ("heresy_church_steppe_lair","heresy church",icon_bandit_lair|carries_goods(8)|pf_is_static|pf_hide_defenders,0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard,15,25),(trp_undead_guard_a,10,20)]),
  ("heresy_church_taiga_lair","heresy church",icon_bandit_lair|carries_goods(8)|pf_is_static|pf_hide_defenders,0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard,15,25),(trp_undead_guard_a,10,20)]),
  ("heresy_church_desert_lair","heresy church",icon_bandit_lair|carries_goods(8)|pf_is_static|pf_hide_defenders,0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard,15,25),(trp_undead_guard_a,10,20)]),
  ("heresy_church_mountain_lair","heresy church",icon_bandit_lair|carries_goods(8)|pf_is_static|pf_hide_defenders,0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard,15,25),(trp_undead_guard_a,10,20)]),
  ("heresy_church_sea_lair","heresy church",icon_bandit_lair|carries_goods(8)|pf_is_static|pf_hide_defenders,0,fac_heresy_missionary,bandit_personality,[(trp_undead_guard,15,25),(trp_undead_guard_a,10,20)]),
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2),0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  
 
  
  ("travel_merchant","Traveling merchant",icon_mule|carries_goods(500)|pf_show_faction,0,fac_travelingmerchants,merchant_personality,
      [
          (trp_caravan_master,5,10),(trp_slaver_chief,15,30),
          (trp_follower_woman,50,100),(trp_manhunter,50,150),
          (trp_slave_crusher,30,60),(trp_slave_driver,50,150),
      ]
  ),
 
  ("skolderbrotva_team","Skolderbrotva team",icon_axeman|carries_goods(2),0,fac_skolderbrotva,soldier_personality,[(trp_skolder_veteran_brotva,5,8),(trp_skolder_warrior_brotva,10,20),(trp_skolder_recruit,25,50)]),
  ("embers_flame_team","Embers Flame team",icon_vaegir_knight|carries_goods(2),0,fac_embers_flame,soldier_personality,[(trp_embers_flame_knight,1,20),(trp_embers_flame_recruit,5,60)]),
  ("living_dead_team","Living Dead team",icon_axeman|carries_goods(0),0,fac_living_dead,soldier_personality,[(trp_undead_farmer,1,1)]),
  ("living_dead_besiege","Living Dead Besiege",icon_axeman|carries_goods(0),0,fac_kingdom_undead,soldier_personality,[(trp_undead_ogre,5,10)]),
  ("living_dead_army","Living Dead Army",icon_axeman|carries_goods(0),0,fac_kingdom_undead,soldier_personality,[(trp_undead_farmer,1,1)]),
  ("living_dead_army_reinforcements_a","Living Dead Army",icon_axeman|carries_goods(0),0,fac_kingdom_undead,soldier_personality,[(trp_skeleton,25,80),(trp_skeleton_soldier,20,60),(trp_skeleton_soldier_a,20,60),(trp_skeleton_soldier_b,10,50),(trp_skeleton_soldier_c,10,20),(trp_skeleton_horse,10,20)]),
  ("living_dead_army_reinforcements_b","Living Dead Army",icon_axeman|carries_goods(0),0,fac_kingdom_undead,soldier_personality,[(trp_skeleton_shooter,20,30),(trp_skeleton_shooter_a,10,30),(trp_skeleton_shooter_b,10,20),(trp_skeleton_shooter_c,10,30),(trp_skeleton_soldier_d,10,20),(trp_skeleton_horse_a,10,20)]),
  ("living_dead_army_reinforcements_c","Living Dead Army",icon_axeman|carries_goods(0),0,fac_kingdom_undead,soldier_personality,[(trp_undead_farmer,20,50),(trp_undead_infantry,10,50),(trp_undead_infantry_a,10,30),(trp_undead_shooter,20,60),(trp_undead_shooter_a,10,50),(trp_undead_shooter_c,10,30)]),
  ("living_dead_army_reinforcements_d","Living Dead Army",icon_axeman|carries_goods(0),0,fac_kingdom_undead,soldier_personality,[(trp_skeleton,30,60)]),

  ("test_team","Test Army",icon_axeman|carries_goods(0),0,fac_outlaws,soldier_personality,[(trp_nord_valkyries,10,10)]),
  
  ("holy_knight_team","holy knight team",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_man_at_arms,6,12),(trp_sept_knight,2,5),(trp_sept_priest,1,1)]),
  ("holy_knight_unit","holy knight unit",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_man_at_arms,20,40),(trp_sept_knight,10,20),(trp_sept_priest,2,2)]),
  ("holy_knight_regiment","holy knight regiment",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_man_at_arms,20,40),(trp_sept_knight,10,20),(trp_sept_god_officer,2,4),(trp_sept_knight_pluse,2,4)]),
  ("holy_knight_army","holy knight army",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_sharpshooter_pluse,40,80),(trp_sept_sergeant_pluse_a,40,80),(trp_sept_knight,10,20),(trp_sept_man_at_arms,20,30),(trp_sept_knight_pluse,8,15),(trp_sept_god_officer_pluse,8,15)]),
  
  ("holy_missionary_team","holy missionary team",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_friar,6,18),(trp_sept_deacon,4,6),(trp_sept_priest,1,2)]),
  ("holy_missionary_unit","holy missionary unit",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_friar,12,30),(trp_sept_deacon,10,18),(trp_sept_priest,4,6),(trp_sept_god_officer,1,2)]),
  ("holy_missionary_regiment","holy missionary regiment",icon_gray_knight|carries_goods(20),0,fac_holy_missionary,soldier_personality,[(trp_sept_friar,24,50),(trp_sept_deacon,16,36),(trp_sept_priest,8,15),(trp_sept_god_officer,4,6),(trp_sept_god_officer_pluse,2,4)]),

  
]
