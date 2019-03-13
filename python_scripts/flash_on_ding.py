
outdoor_yard_light = hass.states.get('light.door_motion')
upstairs_hallway_ceiling_light = hass.states.get('light.tv_room_light_level')

yard_light_original_state = outdoor_yard_light.state
hallway_light_original_state = upstairs_hallway_ceiling_light.state

if yard_light_original_state is 'on':
    yard_light_brightness = outdoor_yard_light.attributes.get('brightness') or 0
if hallway_light_original_state is 'on':
    hallway_light_brightness = upstairs_hallway_ceiling_light.attributes.get('brightness') or 0

if yard_light_original_state is 'off':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.door_motion'})
if hallway_light_original_state is 'off':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.tv_room_light_level'})
time.sleep(1)
hass.services.call('light', 'turn_off', {'entity_id': 'light.door_motion'})
hass.services.call('light', 'turn_off', {'entity_id': 'light.tv_room_light_level'})
time.sleep(1)
hass.services.call('light', 'turn_on', {'entity_id': 'light.door_motion'})
hass.services.call('light', 'turn_on', {'entity_id': 'light.tv_room_light_level'})
time.sleep(1)

hass.services.call('light', 'turn_off', {'entity_id': 'light.door_motion'})
hass.services.call('light', 'turn_off', {'entity_id': 'light.tv_room_light_level'})
time.sleep(1)

if yard_light_original_state is 'on':
    hass.services.call('light', 'turn_off', {'entity_id': 'light.door_motion', 'brightness': yard_light_brightness})
if hallway_light_original_state is 'on':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.tv_room_light_level', 'brightness': hallway_light_brightness})