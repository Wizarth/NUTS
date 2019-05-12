import math

def generate_above_switches(args):
  print('wtf')

def generate_draw_switches_short_alternating(args):
  veh_name = args[0]
  veh_id   = args[1]
  outcome_front   = args[2]
  outcome_back    = args[3]
  outcome_wagon   = args[4]

  outcome_switch_front = veh_name + '_switch_outcome_switch_front'
  outcome_switch_back  = veh_name + '_switch_outcome_switch_end'
  outcome_switch_wagon = veh_name + '_switch_outcome_switch_wagon'

  output_file = '../src-includes/' + veh_name + '_graphics.nml'
  with open(output_file, 'w') as output_nml:
    # drawing results & layers
    # front outcome switch
    output_nml.write('// front')
    output_nml.write('\nswitch (FEAT_TRAINS,SELF, ' + outcome_switch_front + '_layers' + ', [')
    output_nml.write('\nSTORE_TEMP((getbits(extra_callback_info1, 8, 8) < 4 ? CB_FLAG_MORE_SPRITES  : 0) + PALETTE_USE_DEFAULT, 0x100),')
    output_nml.write('\ngetbits(extra_callback_info1, 8, 8)')
    output_nml.write('\n]){')
    output_nml.write('\n0: ' + outcome_wagon + ';')
    output_nml.write('\n1: ' + outcome_front + ';')
    output_nml.write('\n2: ' + outcome_wagon + ';')
    output_nml.write('\n}')
    output_nml.write('\nswitch(FEAT_TRAINS, PARENT, ' + outcome_switch_front + ', vehicle_is_stopped + vehicle_is_in_depot){')
    output_nml.write('\n2: ' + outcome_switch_front + '_layers' + ';')
    output_nml.write('\n'+ outcome_front + ';')
    output_nml.write('\n}')
  


    # separator
    output_nml.write('\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')
    output_nml.write('//' + '-'*128 + '\n')



    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # the many drawing switches ---------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    for i in range(1, 65):

      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # dual headed drawing ---------------------------------------------------------------------------------------------------------------------------
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # write _end version
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      if i>1:
        # write switch header
        output_nml.write('switch(FEAT_TRAINS, SELF, switch_mglv_freight_short_graphics_both_draw' + str(i) + '_end, position_in_consist_from_end){\n')
        # do stuff with i
        i_half = float(i)/2
        i_test = math.floor(i_half)#floor for _end
        i_range = int(i_test-1)
        # define i_text, change it if i == 0
        i_text = '..' + str(i_range)
        if i_range == 0:
          i_text = ''
        
        # define which spritesheet is to be used
        spritesheet = outcome_switch_back + ';\n'
        default_spritesheet = '  ' + outcome_switch_wagon + ';\n'
        
        for n in range(0, int(i_test*2)):
          if (n%4)==0:
            spritesheet = 'sprite_INVISIBLE;\n'
          elif (n%4)==1:
            spritesheet = outcome_switch_back + ';\n'
          elif (n%4)==2:
            spritesheet = outcome_switch_front + ';\n'
          elif (n%4)==3:
            spritesheet = 'sprite_INVISIBLE;\n'
          output_nml.write('  ' + str(n) + ': ' + spritesheet)
        output_nml.write(default_spritesheet)
        output_nml.write('}\n')
        
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # write no _end version
      # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      # write switch header
      output_nml.write('switch(FEAT_TRAINS, SELF, switch_mglv_freight_short_graphics_both_draw' + str(i) + ', position_in_consist){\n')
      # do stuff with i
      i_half = float(i)/2
      i_test = math.ceil(i_half)#floor for _end
      i_range = int(i_test-1)
      # define i_text, change it if i == 0
      i_text = '..' + str(i_range)
      if i_range == 0:
        i_text = ''
      
      spritesheet = outcome_switch_front + ';\n'
      default_spritesheet = '  switch_mglv_freight_short_graphics_both_draw' + str(i) + '_end;\n'
      if i == 1:
        default_spritesheet = outcome_switch_wagon +';\n'

      for n in range(0, int(i_test*2)):
        if (n%4)==0:
          spritesheet = 'sprite_INVISIBLE;\n'
        elif (n%4)==1:
          spritesheet = outcome_switch_front + ';\n'
        elif (n%4)==2:
          spritesheet = outcome_switch_back + ';\n'
        elif (n%4)==3:
          spritesheet = 'sprite_INVISIBLE;\n'
        output_nml.write('  ' + str(n) + ': ' + spritesheet)

      output_nml.write(default_spritesheet)
      output_nml.write('}\n')

      # -----------------------------------------------------------------------------------------------------------------------------------------------
      # front drawing ---------------------------------------------------------------------------------------------------------------------------------
      output_nml.write('switch(FEAT_TRAINS, SELF, switch_mglv_freight_short_graphics_front_draw' + str(i) + ', position_in_consist){\n')
      for n in range(0, i*2):
        default_spritesheet = '  ' + outcome_switch_wagon + ';\n'
        if (n%4)==0:
          spritesheet = 'sprite_INVISIBLE;\n'
        elif (n%4)==1:
          spritesheet = outcome_switch_front + ';\n'
        elif (n%4)==2:
          spritesheet = outcome_switch_back + ';\n'
        elif (n%4)==3:
          spritesheet = 'sprite_INVISIBLE;\n'
        output_nml.write('  ' + str(n) + ': ' + spritesheet)
      output_nml.write(default_spritesheet)
      output_nml.write('}\n')

      # -----------------------------------------------------------------------------------------------------------------------------------------------
      # draw method switch
      output_nml.write('switch(FEAT_TRAINS, PARENT, switch_mglv_freight_short_graphics_draw' + str(i) + ', [')
      output_nml.write('\n  STORE_TEMP(position_in_consist_from_end, 0x10F), var[0x61, 0, 0xFFFF, 0xC6]')
      output_nml.write('\n  ]){')
      output_nml.write('\n  ' + str(veh_id) + ': ' + 'switch_mglv_freight_short_graphics_both_draw' + str(i) + ';')
      output_nml.write('\n  ' + 'switch_mglv_freight_short_graphics_front_draw' + str(i) + ';')
      output_nml.write('\n  }\n')
      
      # separator
      output_nml.write('//' + '-'*128 + '\n')
      output_nml.write('//' + '-'*128 + '\n')
      output_nml.write('//' + '-'*128 + '\n')


    





freight_short_normal_list = [
  # veh_name      veh_id     output      output_end       wagon output
  ('rail_early1', 7),
  ('rail_early2', 8),
  ('rail_early3', 9),

  ('rail_strong1', 11),
  ('rail_strong2', 13),
  ('rail_strong3', 15),
  
  ('rail_medium1', 31),
  ('rail_medium2', 33),
  ('rail_medium3', 35),
  
  ('rail_fast1', 51),
  ('rail_fast2', 53),
  ('rail_fast3', 55)
]
freight_short_alternating_list = [
  # veh_name      veh_id
  ('mglv_medium1', 211, 'spriteset_train_magstrong1', 'spriteset_train_magstrong1_end', 'maglevuniversal_switch'),
  ('mglv_medium2', 213, 'spriteset_train_magstrong2', 'spriteset_train_magstrong2_end', 'maglevuniversal_switch'),
  ('mglv_medium3', 215, 'spriteset_train_magstrong3', 'spriteset_train_magstrong3_end', 'maglevuniversal_switch'),
  ('mglv_medium4', 217, 'spriteset_train_magstrong4', 'spriteset_train_magstrong4_end', 'maglevuniversal_switch'),

  ('mglv_fast1', 251, 'spriteset_train_magfast1', 'spriteset_train_magfast1_end', 'maglevuniversal_switch'),
  ('mglv_fast2', 253, 'spriteset_train_magfast2', 'spriteset_train_magfast2_end', 'maglevuniversal_switch'),
  ('mglv_fast3', 255, 'spriteset_train_magfast3', 'spriteset_train_magfast3_end', 'maglevuniversal_switch'),
  ('mglv_fast4', 257, 'spriteset_train_magfast4', 'spriteset_train_magfast4_end', 'maglevuniversal_switch')
]
freight_long_normal_list = [
  'rail_strong4',
  'rail_strong5',
  'rail_strong6',
  'rail_strong7',
  'rail_strong8',
  'rail_strong9',

  'rail_medium4',
  'rail_medium5',
  'rail_medium6',
  'rail_medium7',
  'rail_medium8',
  'rail_medium9',

  'rail_fast4',
  'rail_fast5',
  'rail_fast6',
  'rail_fast7',
  'rail_fast8',
  'rail_fast9',
]
freight_long_alternating_list = [
  'mono_wtf1',
  'mono_wtf2',
  'mono_wtf3',
  'mono_wtf4',
  
  'mono_medium1',
  'mono_medium2',
  'mono_medium3',
  'mono_medium4',
  
  'mono_fast1',
  'mono_fast2',
  'mono_fast3',
  'mono_fast4',
]

y = 0
generate_draw_switches_short_alternating(
    [
      freight_short_alternating_list[y][0],
      freight_short_alternating_list[y][1],
      freight_short_alternating_list[y][2],
      freight_short_alternating_list[y][3],
      freight_short_alternating_list[y][4]
    ]
  )