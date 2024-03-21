# -*- coding: utf-8 -*-
from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
# Tutorial:
  (0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),

# Refresh Merchants
  (0.0, 0, 168.0, [],
  [    
    (call_script, "script_refresh_center_inventories"),
  ]),

# Refresh Armor sellers
  (0.0, 0, 168.0, [],
  [    
    (call_script, "script_refresh_center_armories"),
  ]),

# Refresh Weapon sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_weaponsmiths"),
  ]),

# Refresh Horse sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_stables"),
  ]),
  
  
   #旅行商人物品更新
  (0.0, 0, 120.0, [],
  [
     (try_begin),
     (store_num_parties_of_template, ":num_parties", "pt_travel_merchant"),
     (ge,":num_parties",1),
     (call_script,"script_cf_add_travel_merchant_item_food","trp_npc_traveling_businessmen"),
     (try_end),
  ]),
    
  #秘密之手商人物品更新
  (0.0, 0, 120.0, [],
  [
     #秘密之手军需
     (call_script,"script_cf_add_travel_merchant_item_food","trp_secret_supplies"),
     
     #秘密之手防具
     (reset_item_probabilities, 100),
	 (set_merchandise_modifier_quality, 150),    
     (assign,":cur_merchant","trp_secret_armorer"),#秘密之手防具商人
     (troop_clear_inventory,":cur_merchant"),
     (store_random_in_range, ":cur_faction", "fac_kingdom_1", "fac_kingdom_7"),
	 (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 16),
	 (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 16),
	 (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_foot_armor, 8),
	 (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_hand_armor, 4),
	 (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
	 (troop_sort_inventory, ":cur_merchant"),
	 (store_troop_gold, reg6, ":cur_merchant"),
	 (lt, reg6, 1000),
	 (store_random_in_range, ":new_gold", 1000, 2000),
	 (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
     
      #秘密之手武器
     (reset_item_probabilities, 100),
	 (set_merchandise_modifier_quality, 150),    
     (assign, ":cur_merchant","trp_secret_weaponsmith"),#秘密之手武器商人
	 (troop_clear_inventory, ":cur_merchant"),
     (store_random_in_range, ":cur_faction", "fac_kingdom_1", "fac_kingdom_7"),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 5),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 5),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 5),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 6),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 4),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 3),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 5),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_arrows, 2),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bolts, 2),
	 (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
	 (troop_sort_inventory, ":cur_merchant"),
	 (store_troop_gold, reg6, ":cur_merchant"),
	 (lt, reg6, 1000),
	 (store_random_in_range, ":new_gold", 1000, 2000),
	 (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
     
     
      #秘密之手马匹
     (reset_item_probabilities, 100),
	 (set_merchandise_modifier_quality, 150),    
     (assign, ":cur_merchant","trp_secret_horse_merchant"),#秘密之手马匹商人
	 (troop_clear_inventory, ":cur_merchant"),
     (store_random_in_range, ":cur_faction", "fac_kingdom_1", "fac_kingdom_7"),
     (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 5),
	 (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
	 (troop_sort_inventory, ":cur_merchant"),
	 (store_troop_gold, reg6, ":cur_merchant"),
	 (lt, reg6, 1000),
	 (store_random_in_range, ":new_gold", 1000, 2000),
	 (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
   
   ]),
  

#############

#Captivity:

#  (1.0, 0, 0.0, [],
#   [
#       (ge,"$captivity_mode",1),
#       (store_current_hours,reg(1)),
#       (val_sub,reg(1),"$captivity_end_time"),
#       (ge,reg(1),0),
#       (display_message,"str_nobleman_reached_destination"),
#       (jump_to_menu,"$captivity_end_menu"),
#    ]),


  (5.7, 0, 0.0, 
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),    
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    (store_add, ":p_town_22_plus_one", "p_town_22", 1),
    (store_random_in_range, ":selected_town", "p_town_1", ":p_town_22_plus_one"),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),
  
  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
		
		
		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),
		
		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),
			
			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),
			
			
			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),
			
			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


#Tax Collectors
# Prisoner Trains
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),
#
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),

##Caravans
#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
##               (party_is_in_any_town,reg(2)),
##               ],
##              [(store_faction_of_party, ":faction_no", reg(2)),
##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
##               (party_set_ai_object,reg(2),reg0),
##               (party_set_flags, reg(2), pf_default_behavior, 0),
##            ]),
  
  (4.0, 0, 0.0,
   [
     (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
     (assign, ":continue", 0),
     (try_begin),
       (neg|party_is_active, "$caravan_escort_party_id"),
       (assign, ":continue", 1),
     (else_try),
       (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
       (neq, ":ai_object", "$caravan_escort_destination_town"),
       (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     ],
   [
     (assign, "$caravan_escort_state", 0),
     ]),

#Messengers
#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_swadians"),
#    (assign, "$pin_party_template", "pt_swadian_messenger"),
#    (assign, "$pin_limit", peak_kingdom_messengers),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_vaegirs"),
#    (assign, "$pin_party_template", "pt_vaegir_messenger"),
#    (assign, "$pin_limit", peak_kingdom_caravans),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

  (1.5, 0, 0, [(store_random_party_of_template, reg(2), "pt_messenger_party"),
               (party_is_in_any_town,reg(2)),
               ],
   [(store_faction_of_party, ":faction_no", reg(2)),
    (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
    (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
    (party_set_ai_object,reg(2),reg0),
    (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),
  
  

#Deserters

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
  
#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
##      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##      (try_end),
      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
##      (try_end),
    (try_end),
    ]),


##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),

# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         
         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         
         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
### Raiders quest
##  (0.95, 0.0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##
##  (0.7, 0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##  
##  (0.1, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (neg|party_is_active, ":quest_target_party")
##    ],
##   [
##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
##    ]
##   ),
##  
##  (1.3, 0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", slot_quest_target_center),
##       (party_is_in_town,":quest_target_party",":quest_target_center")
##    ],
##   [
##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
##       (display_message, "str_raiders_reached_base"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (remove_party, ":quest_target_party"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT END

#########################################################################
# Random MERCHANT quest triggers
####################################  
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
# Escort merchant caravan:
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                    (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                    (try_begin),
                      (party_is_active, ":quest_target_party"),
                      (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    (try_end),
                    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                 ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
				  
# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move 

  (0, 0, 24 * 14,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

          (try_for_range, ":unused", 0, 30),
            (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
            (store_random_in_range, ":town", towns_begin, towns_end),
            (store_faction_of_party, ":town_faction", ":town"),
            (store_relation, ":relation", ":town_faction", ":target_faction"),
            (le, ":relation", 0), #fail if nothing qualifies
           
            (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, 4, ":pretender"),
              (str_store_party_name, 5, ":town"),
              (display_message, "@{!}{s4} is in {s5}"),
            (try_end),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
#            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        (try_end), 
       ],
[]
),
#Rebellion changes end

#NPC system changes begin
#Move unemployed NPCs around taverns
   (24 * 15 , 0, 0, 
   [
    (call_script, "script_update_companion_candidates_in_taverns"),
    ],
   []
   ),

#Process morale and determine personality clashes
  (0, 0, 24,
   [],
[

#Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
#Set their relation to the player
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),
        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),
        (assign, reg7, ":grievance_divisor"),

#        (display_message, "@{!}Process NPC changes. GD: {reg7}"),



##Activate personality clash from 24 hours ago
        #(try_begin), #scheduled personality clashes require at least 24hrs together
             #(gt, "$personality_clash_after_24_hrs", 0),
             #(eq, "$disable_npc_complaints", 0),
             #(try_begin),
                  #(troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  #(main_party_has_troop, "$personality_clash_after_24_hrs"),
                  #(main_party_has_troop, ":other_npc"),
                  #(assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             #(try_end),
             #(assign, "$personality_clash_after_24_hrs", 0),
        #(try_end),
#

         
        (try_for_range, ":npc", companions_begin, companions_end),
###Reset meeting variables
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (str_store_troop_name, s31, ":npc"),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (assign, reg4, ":player_renown"),
                (assign, reg5, ":renown_min"),
#                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),


#Check for political issues
			(try_begin), #does npc's opponent pipe up?
				(troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
				(troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

				(troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
				(troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),
				
				(troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),
				
				(str_store_troop_name, s3, ":npc"),
				(str_store_troop_name, s4, ":other_npc"),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
				(try_end),
			(try_end),

			#Check for quitting
            (try_begin),
                (main_party_has_troop, ":npc"),
				
                (call_script, "script_npc_morale", ":npc"),
                (assign, ":npc_morale", reg0),

                (try_begin),
                    (lt, ":npc_morale", 20),
                    (store_random_in_range, ":random", 0, 100),
                    (val_add, ":npc_morale", ":random"),
                    (lt, ":npc_morale", 20),
                    (assign, "$npc_is_quitting", ":npc"),
                (try_end),

				#Reduce grievance over time (or augment, if party is overcrowded
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),


				#Change personality grievance levels
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),


				
#Check for new personality clashes

				#Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

				#Personality clash 2 and personality match is triggered by battles
				(try_begin),
					(eq, "$npc_with_political_grievance", 0),
				
					(troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
					(assign, "$npc_with_political_grievance", ":npc"),
				(try_end),

			#main party does not have troop, and the troop is a companion
			(else_try), 
				(neg|main_party_has_troop, ":npc"),
				(eq, ":occupation", slto_player_companion),

				
				(troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),
				(try_begin),
					(gt, ":days_on_mission", 0),
					(val_sub, ":days_on_mission", 1),
					(troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
				(else_try), 
					(troop_slot_ge, ":npc", slot_troop_current_mission, 1),
					
					#If the hero can join
					(this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
						(hero_can_join, ":npc"),
						
					(assign, "$npc_to_rejoin_party", ":npc"),
				(try_end),
            (try_end),
        (try_end),
    ]),


#NPC system changes end

# Lady of the lake achievement
   (1, 0, 0,
   [
     (troop_get_type, ":is_female", "trp_player"),
     (eq, ":is_female", 1),       
     (try_for_range, ":companion", companions_begin, companions_end),
       (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

       (troop_get_inventory_capacity, ":inv_cap", ":companion"),
       (try_for_range, ":i_slot", 0, ":inv_cap"),
         (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),

		 (ge, ":item_id", 0),

	 	 (this_or_next|eq, ":item_id", "itm_great_sword"),
	 	 (this_or_next|eq, ":item_id", "itm_sword_two_handed_a"),
		 (eq, ":item_id", "itm_strange_great_sword"),
		 		 
		 (unlock_achievement, ACHIEVEMENT_LADY_OF_THE_LAKE),
		 (assign, ":inv_cap", 0),
	   (try_end),
	 (try_end),
    ],
   []
   ),
   ##################################################################33
   #矫正AI士兵4种属性点随机得太离谱的代码 rubik
    (1, 0, ti_once, [],
  [
    (try_for_range, ":troop_no", "trp_tutorial_maceman", "trp_kingdom_heroes_including_player_begin"),
      (store_attribute_level, ":str", ":troop_no", ca_strength),
      (store_attribute_level, ":agi", ":troop_no", ca_agility),
      (store_attribute_level, ":int", ":troop_no", ca_intelligence),
      (store_attribute_level, ":cha", ":troop_no", ca_charisma),
      (store_add, ":total_points", ":str", ":agi"),
      (val_add, ":total_points", ":int"),
      (val_add, ":total_points", ":cha"),
      # dest_cha
      (store_div, ":dest_cha", ":total_points", 6),
      (store_random_in_range, ":rand_cha", -1, 2),
      (val_add, ":dest_cha", ":rand_cha"),
      # dest_int
      (store_div, ":dest_int", ":total_points", 6),
      (store_sub, ":rand_int", 0, ":rand_cha"),
      (val_add, ":dest_int", ":rand_int"),
      # dest_agi
      (val_sub, ":total_points", ":dest_int"),
      (val_sub, ":total_points", ":dest_cha"),
      (assign, ":agi_ratio", 40), # default, for infantry
      (try_begin),
        (troop_is_guarantee_horse, ":troop_no"),
        (assign, ":agi_ratio", 50), # for cavalry
      (else_try),
        (troop_is_guarantee_ranged, ":troop_no"),
        (assign, ":agi_ratio", 60), # for archer
      (try_end),
      (store_mul, ":dest_agi", ":total_points", ":agi_ratio"),
      (val_div, ":dest_agi", 100),
      (store_random_in_range, ":rand_agi", -1, 2),
      (val_add, ":dest_agi", ":rand_agi"),
      # dest_str
      (store_sub, ":dest_str", ":total_points", ":dest_agi"),
      
      # set_troop_attribute_level
      (call_script, "script_set_troop_attribute_level", ":troop_no", ca_strength, ":dest_str"),
      (call_script, "script_set_troop_attribute_level", ":troop_no", ca_agility, ":dest_agi"),
      (call_script, "script_set_troop_attribute_level", ":troop_no", ca_intelligence, ":dest_int"),
      (call_script, "script_set_troop_attribute_level", ":troop_no", ca_charisma, ":dest_cha"),
    (try_end),
  ]),
  
  ######################################################################################################
   
   (1,0,24*10,
   [],
   [
    (call_script,"script_cf_add_explore_elder_item","trp_explore_elder"),
   ],
   ),
   
    # Spawn travel merchant.
   (1, 24*20, 1,
   [
    (store_num_parties_of_template, ":num_parties", "pt_travel_merchant"),
    (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 3),
     (spawn_around_party,"p_town_16","pt_travel_merchant"),
     (assign,":party_id",reg0),
     (party_set_slot, ":party_id", slot_party_type, spt_travel_merchant),
     (party_add_leader, reg0, "trp_npc_traveling_businessmen"),
     (troop_set_slot, "trp_npc_traveling_businessmen", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_traveling_businessmen",100),
     (party_set_ai_behavior,":party_id",ai_bhvr_patrol_location),
     (party_get_position, pos0, "p_town_16"), 
     (party_set_ai_patrol_radius, ":party_id", 50),
     (party_set_ai_target_position, ":party_id", pos0), 
     (display_message, "str_traveling_businessmen_appear"),
     
     (call_script,"script_cf_add_travel_merchant_item_food","trp_npc_traveling_businessmen"),
    
   ],
   ),
   
   # Spawn sea raiders army.
  (1, 24*14, 1,
   [
     (store_num_parties_of_template, ":num_parties", "pt_sea_raiders_army"),
     (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 10),
     (spawn_around_party,"p_town_13","pt_sea_raiders_army"),
     (assign,":party_id",reg(0)),
     (assign, "$g_sea_raider_army_party", reg(0)),
     (party_set_slot, ":party_id", slot_party_type, spt_kingdom_hero_party),
     (party_add_leader, reg0, "trp_npc_sea_raiders_army_leader"),
     (troop_set_slot, "trp_npc_sea_raiders_army_leader", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_sea_raiders_army_leader",100),
     (call_script, "script_party_set_ai_state_andit", "$g_sea_raider_army_party", spai_patrolling_around_center, "p_town_13"),
     (display_message, "str_sea_raiders_army_appear",0xFF0000FF),
   ],
   ),
   
  (72, 0, 0,
   [
     (store_num_parties_of_template, ":num_parties", "pt_sea_raiders_army"),
     (ge,":num_parties",1),
     (store_faction_of_party, ":faction","$g_sea_raider_army_party"),
     (eq,":faction","fac_sea_raider"),
   ],
   [
     (display_message, "str_sea_raiders_army_appear",0xFF0000FF),
   ],
   ),
   
  # Spawn desert bandit army.#########################################################################33
  (1, 24*14, 1,
   [
     (store_num_parties_of_template, ":num_parties", "pt_desert_bandits_army"),
     (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 10),
     (spawn_around_party,"p_town_21","pt_desert_bandits_army"),
     (assign,":party_id",reg(0)),
     (assign, "$g_desert_bandit_army_party", reg(0)),
     (party_set_slot, ":party_id", slot_party_type, spt_kingdom_hero_party),
     (party_add_leader, reg0, "trp_npc_desert_bandit_army_leader"),
     (troop_set_slot, "trp_npc_desert_bandit_army_leader", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_desert_bandit_army_leader",100),
     (call_script, "script_party_set_ai_state_andit", "$g_desert_bandit_army_party", spai_patrolling_around_center, "p_town_21"),
     (display_message, "str_desert_bandits_army_appear",0xFFFF00),
   ],
   ),
   
  (72, 0, 0,
   [
     (store_num_parties_of_template, ":num_parties", "pt_desert_bandits_army"),
     (ge,":num_parties",1),
     (store_faction_of_party, ":faction","$g_desert_bandit_army_party"),
     (eq,":faction","fac_desert_bandit"),
   ],
   [
     (display_message, "str_desert_bandits_army_appear",0xFFFF00),
   ],
   ),
   
   # Spawn forest bandits army.#####################################################################
  (1, 24*7, 1,
   [
     (store_num_parties_of_template, ":num_parties", "pt_forest_bandits_army"),
     (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 10),
     (spawn_around_party,"p_town_4","pt_forest_bandits_army"),
     (assign,":party_id",reg(0)),
     (assign, "$g_forest_bandits_army_party", reg(0)),
     (party_set_slot, ":party_id", slot_party_type, spt_kingdom_hero_party),
     (party_add_leader, reg0, "trp_npc_forest_bandit_army_leader"),
     (troop_set_slot, "trp_npc_forest_bandit_army_leader", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_forest_bandit_army_leader",100),
     (call_script, "script_party_set_ai_state_andit", "$g_forest_bandits_army_party", spai_patrolling_around_center, "p_town_4"),
     (display_message, "str_forest_bandits_army_appear",0x00FF00),
   ],
   ),
   
  (24, 0, 0,
   [
     (store_num_parties_of_template, ":num_parties", "pt_forest_bandits_army"),
     (ge,":num_parties",1),
     (store_faction_of_party, ":faction","$g_forest_bandits_army_party"),
     (eq,":faction","fac_forest_bandits"),
   ],
   [
     (display_message, "str_forest_bandits_army_appear",0x00FF00),
   ],
   ),
   
   # Spawn steppe bandit army leader ######################################################
  (1, 24*21, 1,
   [
     (store_num_parties_of_template, ":num_parties", "pt_steppe_bandits_army"),
     (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 10),
     (spawn_around_party,"p_town_10","pt_steppe_bandits_army"),
     (assign,":party_id",reg(0)),
     (assign, "$g_steppe_bandit_army_party", reg(0)),
     (party_set_slot, ":party_id", slot_party_type, spt_kingdom_hero_party),
     (party_add_leader, reg0, "trp_npc_steppe_bandit_army_leader"),
     (troop_set_slot, "trp_npc_steppe_bandit_army_leader", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_steppe_bandit_army_leader",100),
     (call_script, "script_party_set_ai_state_andit", "$g_steppe_bandit_army_party", spai_patrolling_around_center, "p_town_10"),
     (display_message, "str_steppe_bandits_army_appear",0xDEB887),
   ],
   ),
   
  (72, 0, 0,
   [
     (store_num_parties_of_template, ":num_parties", "pt_steppe_bandits_army"),
     (ge,":num_parties",1),
     (store_faction_of_party, ":faction","$g_steppe_bandit_army_party"),
     (eq,":faction","fac_steppe_bandit"),
   ],
   [
     (display_message, "str_steppe_bandits_army_appear",0xDEB887),
   ],
   ),
   
   # Spawn taiga bandit army leader ##########################################################3
  (1, 24*7, 1,
   [
     (store_num_parties_of_template, ":num_parties", "pt_taiga_bandits_army"),
     (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 10),
     (spawn_around_party,"p_town_9","pt_taiga_bandits_army"),
     (assign,":party_id",reg(0)),
     (assign, "$g_taiga_bandit_army_party", reg(0)),
     (party_set_slot, ":party_id", slot_party_type, spt_kingdom_hero_party),
     (party_add_leader, reg0, "trp_npc_taiga_bandit_army_leader"),
     (troop_set_slot, "trp_npc_taiga_bandit_army_leader", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_taiga_bandit_army_leader",100),
     (call_script, "script_party_set_ai_state_andit", "$g_taiga_bandit_army_party", spai_patrolling_around_center, "p_town_9"),
     (display_message, "str_taiga_bandits_army_appear",0x556B2F),
   ],
   ),
   
  (24, 0, 0,
   [
    (store_num_parties_of_template, ":num_parties", "pt_taiga_bandits_army"),
    (ge,":num_parties",1),
    (store_faction_of_party, ":faction","$g_taiga_bandit_army_party"),
    (eq,":faction","fac_taiga_bandit"),
   ],
   [
     (display_message, "str_taiga_bandits_army_appear",0x556B2F),
   ],
   ),
   
  # Spawn mountain bandit army leader ##############################################################
  (1, 24*12, 1,
   [
     (store_num_parties_of_template, ":num_parties", "pt_mountain_bandits_army"),
     (lt,":num_parties",1),
   ],
   [
     (set_spawn_radius, 10),
     (spawn_around_party,"p_town_3","pt_mountain_bandits_army"),
     (assign,":party_id",reg(0)),
     (assign, "$g_mountain_bandit_army_party", reg(0)),
     (party_set_slot, ":party_id", slot_party_type, spt_kingdom_hero_party),
     (party_add_leader, reg0, "trp_npc_mountain_bandits_army_leader"),
     (troop_set_slot, "trp_npc_mountain_bandits_army_leader", slot_troop_leaded_party, ":party_id"),
     (troop_set_health,"trp_npc_mountain_bandits_army_leader",100),
     (call_script, "script_party_set_ai_state_andit", "$g_mountain_bandit_army_party", spai_patrolling_around_center, "p_town_3"),
     (display_message, "str_mountain_bandits_army_appear",0x2E8B57),
   ],
   ),
  
  (48, 0, 0,
   [
     (store_num_parties_of_template, ":num_parties", "pt_mountain_bandits_army"),
     (ge,":num_parties",1),
     (store_faction_of_party, ":faction","$g_mountain_bandit_army_party"),
     (eq,":faction","fac_mountain_bandits"),
   ],
   [
     (display_message, "str_mountain_bandits_army_appear",0x2E8B57),
   ],
   ),
   
   (24, 24*1, 0,
   [
     (eq,"$rodrigo_de_rraganca_special_time_cnt",1),
   ],
   [
     (assign,"$rodrigo_de_rraganca_special_time_cnt",0),
   ],
   ),
   #############################################################################################################3
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_sea_raider",1),
   ],
   [
     (assign,"$recruit_bandit_flag_sea_raider",0),
   ],
   ),
   
  (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_desert_bandit",1),
   ],
   [
     (assign,"$recruit_bandit_flag_desert_bandit",0),
   ],
   ),
   
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_steppe_bandit",1),
   ],
   [
     (assign,"$recruit_bandit_flag_steppe_bandit",0),
   ],
   ),
   
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_steppe_bandit_1",1),
   ],
   [
     (assign,"$recruit_bandit_flag_steppe_bandit_1",0),
   ],
   ),
   
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_forest_bandit",1),
   ],
   [
     (assign,"$recruit_bandit_flag_forest_bandit",0),
   ],
   ),
   
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_mountain_bandit",1),
   ],
   [
     (assign,"$recruit_bandit_flag_mountain_bandit",0),
   ],
   ),
   
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_taiga_bandit",1),
   ],
   [
     (assign,"$recruit_bandit_flag_taiga_bandit",0),
   ],
   ),
   
   (24, 24*5, 0,
   [
     (eq,"$recruit_bandit_flag_heresy_missionary",1),
   ],
   [
     (assign,"$recruit_bandit_flag_heresy_missionary",0),
   ],
   ),
   
   (1, 24, 0,
   [
    (eq,"$sacrifice_act_ok",0),
   ],
   [
    (assign,"$sacrifice_act_ok",1),
   ],
   ),
   
   
   ## g_magic_cnt updata 
   (24, 0, 0,
   [
    #(faction_get_slot,":culture","fac_player_supporters_faction",slot_faction_culture),
    #(eq,":culture","fac_culture_undead"),
   ],
   [
        (store_skill_level,":riding_level","skl_riding","trp_player"),
        (val_div,":riding_level",2),
        (store_add,"$g_mount_magic_cnt",1,":riding_level"),
        (assign,reg53,"$g_mount_magic_cnt"),
        (display_message,"@mount magic {reg53} cnt"),
        
        (store_attribute_level, ":int", "trp_player", ca_intelligence),
        (assign,reg51,":int"),
        (val_add,"$g_magic_cnt",":int"),
        
        (try_begin),
            (val_mul,":int",3),
            (gt,"$g_magic_cnt",":int"),
            (assign,"$g_magic_cnt",":int"),
        (try_end),
        
        (assign,reg52,"$g_magic_cnt"),
        (assign, "$g_resurrect_the_corpse",0),
            
        (display_message, "@Dead cnt count of {reg52}, add {reg51} ", 0xFF4B0082), 
   ],
   ),
   
   (24*1, 0, 0,
   [
    (faction_get_slot,":culture","fac_player_supporters_faction",slot_faction_culture),
    (eq,":culture","fac_culture_undead"),
    (store_skill_level, ":level", "skl_persuasion", "trp_player"),
    (ge,":level",1),
    
    (eq,"$g_missionary_work",1),
   ],
   [
        (assign,reg41,0),#献祭点 reg41
        (assign,reg42,0),#经验值 reg42
        
        (store_skill_level, ":level", "skl_persuasion", "trp_player"),
        (assign,":morale",":level"),
            
            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
            (try_for_range, ":stack_no", 0, ":num_stacks"),              ###循环全部   
                (gt,":level",0),
                (party_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"), ###获取队伍单位id  
                (troop_get_type,":type",":stack_troop"), 
                (store_troop_faction, ":faction", ":stack_troop"),               
                (neg|troop_is_hero, ":stack_troop"), ##id不是英雄 
                (eq|this_or_next,":type",tf_male),
                (eq,":type",tf_female),
                (neq,":faction","fac_kingdom_undead"),
                (party_stack_get_size, ":stack_size","p_main_party",":stack_no"), ###获取兵种ID数量多少
                (party_stack_get_num_wounded, ":stack_wounded_size","p_main_party",":stack_no"), ###获取兵种ID受伤数量多少
                (val_sub, ":stack_size",":stack_wounded_size"),###获取兵种非受伤数量
                (ge, ":stack_size",1),
                
                (try_begin),
                    (ge,":stack_size",":level"),
                    (assign,":stack_size",":level"),
                (try_end),
                
                (assign,":troop_level",0),
                (store_character_level,":troop_level", ":stack_troop"),
                (call_script, "script_members_to_undead",":stack_troop",), 	 #####同伴黑化
                (party_add_members,"p_main_party",reg8,":stack_size"),           ##同伴黑化加到队伍
                (party_remove_members,"p_main_party",":stack_troop",":stack_size"),      ## 移除兵种及数量
                    
                (store_mul,":value",":stack_size",2),
                (val_add,reg41,":value"),
                (val_mul,":troop_level",":stack_size"),
                (val_mul,":troop_level",4),
                (val_add,reg42,":troop_level"),
                
                (val_sub,":level",":stack_size"),
                (assign,reg39,":stack_size"),
                (str_store_troop_name_link,s8,reg8),
                (str_store_troop_name_link,s9,":stack_troop"),
                (display_message, "@persuasion {reg39} the number of {s9} changes to  {s8} joins the troops ", 0xFF4B0082), 
            (try_end),  
            
        (try_begin),
            (gt,reg41,0),
            (val_mul,reg42,xp_mul_value),
            (assign,":add_xp",reg42),
            (display_message, "@Get total of {reg41} sacrifice cnt", 0xFF9400D3),    
            (display_message, "@Undead god give you xp {reg42}", 0xFF9400D3),  
            (add_xp_to_troop,":add_xp","trp_player"),
            (val_add,"$g_necromancer_act_cnt",reg41),
            (val_div,":morale",2),
            (call_script, "script_change_player_party_morale",":morale"),
            
            #增加和玩家同文化的英雄经验 玩家和同伴同时加xp
            (call_script,"script_increase_the_hero_and_plyer_xp_same_culture",":add_xp",fac_culture_undead),
        (try_end),
  
   ],
   ),
   
  (24*1, 0, 0,
   [
    (faction_get_slot,":culture","fac_player_supporters_faction",slot_faction_culture),
    (eq,":culture","fac_culture_sept"),
    (store_skill_level, ":level", "skl_persuasion", "trp_player"),
    (ge,":level",1),
   ],
   [
        (assign,reg41,0),#献祭点 reg41
        (assign,reg42,0),#经验值 reg42
        
        (store_skill_level, ":level", "skl_persuasion", "trp_player"),
        (assign,":morale",":level"),
            
            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
            (try_for_range, ":stack_no", 0, ":num_stacks"),              ###循环全部   
                (gt,":level",0),
                (party_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"), ###获取队伍单位id  
                (troop_get_type,":type",":stack_troop"), 
                (store_troop_faction, ":faction", ":stack_troop"),               
                (neg|troop_is_hero, ":stack_troop"), ##id不是英雄 
                (neq,":type",tf_undead),	  ##不等于亡灵  
                (neq,":type",tf_undead_giant),	  ##不等于亡灵巨人      
                (neq,":type",tf_undead_giant_pluse),	  ##不等于亡灵巨人                  
                (neq,":faction","fac_kingdom_sept"),	
                (party_stack_get_size, ":stack_size","p_main_party",":stack_no"), ###获取兵种ID数量多少
                (party_stack_get_num_wounded, ":stack_wounded_size","p_main_party",":stack_no"), ###获取兵种ID受伤数量多少
                (val_sub, ":stack_size",":stack_wounded_size"),###获取兵种非受伤数量
                (ge, ":stack_size",1),
                
                (try_begin),
                    (ge,":stack_size",":level"),
                    (assign,":stack_size",":level"),
                (try_end),
                
                (assign,":troop_level",0),
                (store_character_level,":troop_level", ":stack_troop"),
                (call_script, "script_troop_to_sept_troop",":stack_troop",0), 	 #####同伴黑化
                (party_add_members,"p_main_party",reg8,":stack_size"),           ##同伴黑化加到队伍
                (party_remove_members,"p_main_party",":stack_troop",":stack_size"),      ## 移除兵种及数量
                    
                (val_add,reg41,":stack_size"),
                (val_mul,":troop_level",":stack_size"),
                (val_mul,":troop_level",2),
                (val_add,reg42,":troop_level"),
                
                (val_sub,":level",":stack_size"),
                (assign,reg39,":stack_size"),
                (str_store_troop_name_link,s8,reg8),
                (str_store_troop_name_link,s9,":stack_troop"),
                (display_message, "@persuasion {reg39} the number of {s9} changes to  {s8} joins the troops ", color_code_hot), 
            (try_end),  
            
        (try_begin),
            (gt,reg41,0),
            (display_message, "@Sept Get total of {reg41} sacrifice cnt", 0xFF9400D3),    
            (display_message, "@Sept god give you xp {reg42}", color_code_hot), 
            (val_mul,reg42,3),
            (add_xp_to_troop,reg42,"trp_player"),
            (val_add,"$g_necromancer_act_cnt",reg41),
            (val_div,":morale",2),
            (call_script, "script_change_player_party_morale",":morale"),

        (try_end),
  
   ],
   ),
   
   ##########################################死灵邪教入侵-开始#############################################
   
    (1, 24*70, ti_once,
    [
         (eq,"$my_debug",1),
    ],
    [
       (jump_to_menu,"mnu_faction_kingdom_undead_invasion"),
       (faction_set_slot,"fac_kingdom_undead",slot_faction_state,sfs_active),

       (call_script, "script_appoint_faction_marshall", "fac_kingdom_undead", "trp_kingdom_undead_lord"),
       
       (call_script, "script_create_kingdom_hero_party", "trp_kingdom_undead_lord", "p_town_6"),#国王NPC
       (try_for_range,":party_template","pt_kingdom_undead_reinforcements_inite_a","pt_kingdom_undead_reinforcements_inite_d"),
           (party_add_template, "$pout_party", ":party_template"), 
       (try_end),
       (party_add_members,"$pout_party","trp_undead_knight_a",40),
       (party_add_members,"$pout_party","trp_undead_ogre",10),
       (assign,"$pout_party_kingom", "$pout_party"),
       
       (spawn_around_party, "p_town_6", "pt_living_dead_army"),#创造不死大军 
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
           (party_add_template, reg0, ":party_template"), 
       (try_end),
       (party_set_ai_behavior,reg0,ai_bhvr_escort_party),
       (party_set_ai_object,reg0,"$pout_party"),
       (party_set_flags, reg0, pf_default_behavior, 0),
       (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
           
       (try_for_range,":kingdom_hero","trp_knight_undead_1",lords_end),#领主NPC
           (call_script, "script_troop_change_relation_with_troop", "trp_kingdom_undead_lord", ":kingdom_hero", 100),
       (try_end),
       
       (try_for_range,":kingdom_hero","trp_knight_undead_1","trp_knight_undead_5"),#领主NPC),
           (call_script, "script_create_kingdom_hero_party", ":kingdom_hero", "p_town_6"),
           (call_script, "script_party_set_ai_state","$pout_party", spai_accompanying_army, "$pout_party_kingom"),
           (try_begin),
               (eq,":kingdom_hero","trp_knight_undead_4"),  
               (party_add_members,"$pout_party","trp_undead_knight_a",120),
           (else_try),
              (try_for_range,":party_template","pt_kingdom_undead_reinforcements_inite_a","pt_kingdom_undead_reinforcements_inite_d"),
                (party_add_template, "$pout_party", ":party_template"), 
              (try_end),
           (try_end),
           
           (spawn_around_party, "p_town_6", "pt_living_dead_army"),#创造不死大军 
           (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
            (party_add_template, reg0, ":party_template"), 
           (try_end),
           (party_set_ai_behavior,reg0,ai_bhvr_escort_party),
           (party_set_ai_object,reg0,"$pout_party"),
           (party_set_flags, reg0, pf_default_behavior, 0),
           (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
       (try_end), 

       (try_for_range,":kingdom_hero","trp_knight_undead_5","trp_knight_undead_14"),#领主NPC),
           (call_script, "script_create_kingdom_hero_party", ":kingdom_hero", "p_town_13"),
           (call_script, "script_party_set_ai_state","$pout_party", spai_accompanying_army, "$pout_party_kingom"),
           (try_for_range,":party_template","pt_kingdom_undead_reinforcements_inite_a","pt_kingdom_undead_reinforcements_inite_d"),
            (party_add_template, "$pout_party", ":party_template"), 
           (try_end),
       
           
           (spawn_around_party, "p_town_13", "pt_living_dead_army"),#创造不死大军 
           (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
            (party_add_template, reg0, ":party_template"), 
           (try_end),
           (party_set_ai_behavior,reg0,ai_bhvr_escort_party),
           (party_set_ai_object,reg0,"$pout_party"),
           (party_set_flags, reg0, pf_default_behavior, 0),
           (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
       (try_end),


       (try_for_range,":kingdom_hero","trp_knight_undead_14","trp_kingdom_1_pretender"),#领主NPC),
           (call_script, "script_create_kingdom_hero_party", ":kingdom_hero", "p_town_2"),
           (call_script, "script_party_set_ai_state","$pout_party", spai_accompanying_army, "$pout_party_kingom"),
           (try_for_range,":party_template","pt_kingdom_undead_reinforcements_inite_a","pt_kingdom_undead_reinforcements_inite_d"),
            (party_add_template, "$pout_party", ":party_template"), 
           (try_end),
       
           
           (spawn_around_party, "p_town_2", "pt_living_dead_army"),#创造不死大军 
           (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
            (party_add_template, reg0, ":party_template"), 
           (try_end),
           (party_set_ai_behavior,reg0,ai_bhvr_escort_party),
           (party_set_ai_object,reg0,"$pout_party"),
           (party_set_flags, reg0, pf_default_behavior, 0),
           (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
       (try_end),        
           
      
     #(call_script, "script_create_kingdom_hero_party", "trp_knight_undead_10", "p_town_6"),
     #(call_script, "script_party_set_ai_state","$pout_party", spai_accompanying_army, "$pout_party_kingom"),
     #(party_add_members,"$pout_party","trp_undead_ogre",50),
     
     
     (party_set_flags, "p_castle_51", pf_disabled, 0),
 	 (call_script, "script_give_center_to_lord", "p_castle_51",  "trp_kingdom_undead_lord", 0),
     (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, "p_castle_51", ":party_template"), 
     (try_end),
     
    (party_set_flags, "p_castle_52", pf_disabled, 0),
 	 (call_script, "script_give_center_to_lord", "p_castle_52",  "trp_kingdom_undead_lord", 0),
     (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, "p_castle_52", ":party_template"), 
     (try_end),
        
     ##玩家快速加入死灵邪教
     (try_begin),
        (faction_get_slot,":culture","fac_player_supporters_faction",slot_faction_culture),
        (eq,":culture","fac_culture_undead"),
        (call_script,"script_player_quick_to_join_faction","fac_kingdom_undead"),
        (call_script, "script_troop_change_relation_with_troop", "trp_kingdom_undead_lord", "trp_player", 100),
     (try_end),
     ##
     
     #创建攻城大军队
       (store_faction_of_party,":faction","p_town_6"),
       (try_begin),
        (neq,":faction","fac_kingdom_undead"),
        (call_script, "script_diplomacy_start_war_between_kingdoms",  "fac_kingdom_undead", ":faction", 1),
       (try_end),
       
       (store_faction_of_party,":faction","p_town_13"),
       (try_begin),
        (neq,":faction","fac_kingdom_undead"),
        (call_script, "script_diplomacy_start_war_between_kingdoms",  "fac_kingdom_undead", ":faction", 1),
       (try_end),
       
       (store_faction_of_party,":faction","p_town_2"),
       (try_begin),
        (neq,":faction","fac_kingdom_undead"),
        (call_script, "script_diplomacy_start_war_between_kingdoms",  "fac_kingdom_undead", ":faction", 1),
       (try_end),

       (assign,":party", "p_town_6"),
       (spawn_around_party, ":party", "pt_living_dead_besiege"),#创造不死大军
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       
       (try_begin),
        (neq,":faction","fac_kingdom_undead"),
        (party_set_ai_behavior,reg0,ai_bhvr_attack_party),
       (else_try),
        (party_set_ai_behavior,reg0,ai_bhvr_travel_to_party),
       (try_end),
       
       (party_set_ai_object,reg0,":party"),
       (party_set_flags, reg0, pf_default_behavior, 1),
       (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
       
       
       (assign,":party", "p_town_2"),
       (spawn_around_party, ":party", "pt_living_dead_besiege"),#创造不死大军
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       
       (try_begin),
        (neq,":faction","fac_kingdom_undead"),
        (party_set_ai_behavior,reg0,ai_bhvr_attack_party),
       (else_try),
        (party_set_ai_behavior,reg0,ai_bhvr_travel_to_party),
       (try_end),
       
       (party_set_ai_object,reg0,":party"),
       (party_set_flags, reg0, pf_default_behavior, 1),
       (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
       
       
       (assign,":party", "p_town_13"),
       (spawn_around_party, ":party", "pt_living_dead_besiege"),#创造不死大军
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       (try_for_range,":party_template","pt_living_dead_army_reinforcements_a","pt_living_dead_army_reinforcements_d"),
        (party_add_template, reg0, ":party_template"), 
       (try_end),
       
       (try_begin),
        (neq,":faction","fac_kingdom_undead"),
        (party_set_ai_behavior,reg0,ai_bhvr_attack_party),
       (else_try),
        (party_set_ai_behavior,reg0,ai_bhvr_travel_to_party),
       (try_end),
       
       (party_set_ai_object,reg0,":party"),
       (party_set_flags, reg0, pf_default_behavior, 1),
       (party_set_slot, reg0, slot_party_type, spt_kingdom_hero_party),
    ],
    ),
    

    (1, 0, 0,
    [
       (store_num_parties_of_template,":num","pt_living_dead_besiege"),
       (gt,":num",0),
    ],
    [
        (store_random_party_of_template,reg3,"pt_living_dead_besiege"),
        (get_party_ai_current_object,":ai_object",reg3),
        (try_begin),
            (is_between,":ai_object",towns_begin,towns_end),
            (store_faction_of_party,":party_faction",reg3),
            (store_faction_of_party,":object_faction",":ai_object"),
            (store_relation, ":relation", ":object_faction", ":party_faction"),
            (try_begin),
                (eq,":object_faction","fac_kingdom_undead"),       
                (party_set_ai_behavior,reg3,ai_bhvr_travel_to_party),
                (party_set_ai_object,reg3,":ai_object"),
                (call_script, "script_party_add_party", ":ai_object", reg3),
                (party_detach, reg3),
                (remove_party, reg3),
            (else_try),
                 (lt,":relation",0),
                 (party_set_ai_behavior,reg3,ai_bhvr_attack_party),
                 (party_set_ai_object,reg3,":ai_object"),
           (else_try),
                (troop_get_slot, ":party_no", "trp_kingdom_undead_lord", slot_troop_leaded_party),
                (party_set_ai_behavior,reg3,ai_bhvr_escort_party),
                (party_set_ai_object,reg3,":party_no"),
                (party_set_flags, reg3, pf_default_behavior, 0),
        (try_end),
    ],
    ),
    
   #开局特殊初始化
   (0, 0, ti_once,
   [],
   [
     (call_script,"script_cf_add_travel_merchant_item_food","trp_secret_supplies"),
     
     (store_attribute_level, ":int", "trp_player", ca_intelligence),
     (val_mul,":int",3),
     (assign,"$g_magic_cnt",":int"),
   ],
   ),
    
   
    
    
    
    
    
   ##########################################死灵邪教入侵-结束#############################################
   
   
 
  ##########################################圣堂触发器-开始#############################################
  (0, 0, 4,
   [
   (eq,"$game_mod",1),
   (store_num_parties_of_template,":template_num","pt_holy_knight_team"),
   (lt,":template_num",60),
   ],
   [
    (set_spawn_radius, 100),
    (store_random_in_range,":p_town",towns_begin,towns_end),
    (spawn_around_party,":p_town","pt_holy_knight_team"),
    (assign,":party_id",reg0),
    (call_script, "script_party_set_ai_state_andit", ":party_id", spai_patrolling_around_center, ":p_town"),
    
    (store_character_level, ":troop_level", "trp_player"),
    (try_begin),
        (val_div,":troop_level",10),
        (val_min, ":troop_level", 3),
        (gt,":troop_level",0),
        (party_add_members,":party_id","trp_angel_b",":troop_level"),
        #(try_for_range,":range",0,":troop_level"),
            #(party_add_template,":party_id","pt_holy_knight_team"),
        #(try_end),
    (try_end),
    
   ],
   ),


  ##########################################圣堂触发器-开始#############################################


 
]
