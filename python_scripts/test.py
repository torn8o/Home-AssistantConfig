
outdoor_yard_light = hass.states.get('light.outdoor_yard_light')


yard_light_original_state = outdoor_yard_light.state


if yard_light_original_state is 'on':
    yard_light_brightness = outdoor_yard_light.attributes.get('brightness') or 0


if yard_light_original_state is 'off':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.outdoor_yard_light'})
time.sleep(1)
hass.services.call('light', 'turn_off', {'entity_id': 'light.outdoor_yard_light'})
time.sleep(1)
hass.services.call('light', 'turn_on', {'entity_id': 'light.outdoor_yard_light'})
time.sleep(1)

hass.services.call('light', 'turn_off', {'entity_id': 'light.outdoor_yard_light'})
time.sleep(1)

if yard_light_original_state is 'on':
    hass.services.call('light', 'turn_on', {'entity_id': 'light.outdoor_yard_light', 'brightness': yard_light_brightness})
