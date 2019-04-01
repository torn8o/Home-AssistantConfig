
outdoor_yard_light = hass.states.get('light.hair_area_level')
upstairs_hallway_ceiling_light = hass.states.get('switch.washer_lights')

yard_light_original_state = outdoor_yard_light.state
hallway_light_original_state = upstairs_hallway_ceiling_light.state

if yard_light_original_state is 'on':
    yard_light_brightness = outdoor_yard_light.attributes.get('brightness') or 0
if hallway_light_original_state is 'on':
    hallway_light_brightness = upstairs_hallway_ceiling_light.attributes.get('brightness') or 0

if yard_light_original_state is 'off':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.hair_area_level'})
if hallway_light_original_state is 'off':
    hass.services.call('switch', 'turn_on', {'entity_id': 'switch.washer_lights'})
time.sleep(3)
hass.services.call('light', 'turn_off', {'entity_id': 'light.hair_area_level'})
hass.services.call('switch', 'turn_off', {'entity_id': 'switch.washer_lights'})
time.sleep(3)
hass.services.call('light', 'turn_on', {'entity_id': 'light.hair_area_level'})
hass.services.call('switch', 'turn_on', {'entity_id': 'switch.washer_lights'})
time.sleep(3)

hass.services.call('light', 'turn_off', {'entity_id': 'light.hair_area_level'})
hass.services.call('switch', 'turn_off', {'entity_id': 'switch.washer_lights'})
time.sleep(3)

if yard_light_original_state is 'on':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.hair_area_level', 'brightness': yard_light_brightness})
if hallway_light_original_state is 'on':
    hass.services.call('switch', 'turn_on', {'entity_id': 'switch.washer_lights', 'brightness': hallway_light_brightness})
