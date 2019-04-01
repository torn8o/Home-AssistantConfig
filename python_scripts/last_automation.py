##############################################################################
# Last automation, to create a sensor for the last automation. It takes as data the trigger.event  form the automation.automation_ran
# Take note: an automation's attribute last_triggered is only set when the action part is executed (and not when the trigger gets triggered....)
# @Mariusthvdb
##############################################################################
# Get params
event = data.get('event')
#logger.error("LAST AUTOMATION: " + str(event))
# Sample: <Event call_service[L]: domain=automation, service=trigger, service_data=entity_id=automation.call_service_event_automation, service_call_id=1972124944-486>

# Find the automation name
#** pos_start = event.find('entity_id=')+10
pos_start = event.find('entity_id=')+21
pos_end = event.find(',', pos_start)

# Get the entity_id
#** entity_id = event[pos_start:pos_end]
entity_id = 'automation.' + event[pos_start:pos_end]

# get the state object
state = hass.states.get(entity_id)

# Make a time string in 24 hour format
#time_string = datetime.datetime.now().strftime('%I:%M')
dt = datetime.datetime.now() #state.attributes.get('last_triggered') #
time = "%02d:%02d:%02d" % (dt.hour, dt.minute, dt.second)
# try to get the automation friendly name
msg = []

try:
    msg = state.name
except:
    msg = None

if msg:
   if not msg.startswith('Set '):
       # Sensor update
       hass.states.set('sensor.last_automation', msg, {
#            'custom_ui_state_card': 'state-card-value_only',
#            'text': sensor_message,
            'unit_of_measurement': 'Aut',
            'friendly_name': time,
            'entity_picture': '/local/buttons/play-mode-repeat.png' })
