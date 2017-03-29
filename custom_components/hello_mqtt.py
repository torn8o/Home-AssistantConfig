import homeassistant.loader as loader

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "hello_mqtt"

# List of component names (string) your component depends upon.
DEPENDENCIES = ['mqtt']


CONF_TOPIC = 'topic'
DEFAULT_TOPIC = 'home-assistant/hello_mqtt'


def setup(hass, config):
    """Setup the Hello MQTT component."""
    mqtt = loader.get_component('mqtt')
    topic = config[DOMAIN].get('topic', DEFAULT_TOPIC)
    entity_id = 'hello_mqtt.last_message'

    # Listener to be called when we receive a message.
    def message_received(topic, payload, qos):
        """A new MQTT message has been received."""
        hass.states.set(entity_id, payload)

    # Subscribe our listener to a topic.
    mqtt.subscribe(hass, topic, message_received)

    # Set the intial state
    hass.states.set(entity_id, 'No messages')

    # Service to publish a message on MQTT.
    def set_state_service(call):
        """Service to send a message."""
        mqtt.publish(hass, topic, call.data.get('new_state'))

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'set_state', set_state_service)

    # Return boolean to indicate that initialization was successfully.
    return True
