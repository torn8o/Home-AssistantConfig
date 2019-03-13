class CustomFanCard extends Polymer.Element {

    static get template() {
        return Polymer.html`
            <style is="custom-style" include="iron-flex iron-flex-alignment"></style>
            <style>
                :host {
                    line-height: 1.5;
                }
                .speed {
                    min-width: 30px;
                    max-width: 30px;
					margin-left: 2px;
                    margin-right: 2px;
    	            //background-color:#546E7A;
					background-color:#759aaa;
	                border: 1px solid lightgrey; 
	                font-size: 10px !important;
	                float: right !important;   
                }
               </style>
            <hui-generic-entity-row hass="[[hass]]" config="[[_config]]">
                <div class='horizontal justified layout' on-click="stopPropagation">
                    <paper-button
                        class='speed'
						style='[[_lowOnColor]]'
                        toggles name="low"
                        on-tap='setSpeed'
                        disabled='[[_isOnLow]]'>LOW</paper-button>
                    <paper-button
                        class='speed'
						style='[[_medOnColor]]'
                        toggles name="medium"
                        on-tap='setSpeed'
                        disabled='[[_isOnMed]]'>MED</paper-button>
                    <paper-button
                        class='speed'
						style='[[_highOnColor]]'
                        toggles name="high"
                        on-tap='setSpeed'
                        disabled='[[_isOnHigh]]'>HIGH</paper-button>
				    <paper-button
                        class='speed'
						style='[[_offColor]]'
                        toggles name="off"
                        on-tap='setSpeed'
                        disabled='[[_isOffState]]'>OFF</paper-button>
                </div>
            </hui-generic-entity-row>
        `;
    }

    static get properties() {
        return {
            hass: {
                type: Object,
                observer: 'hassChanged'
            },
            _config: Object,
            _stateObj: Object,
			_lowOnColor: String,
			_medOnColor: String,
			_highOnColor: String,
			_offColor: String,
            _isOffState: Boolean,
            _isOnState: Boolean,
            _isOnLow: Boolean,
            _isOnMed: Boolean,
            _isOnHigh: Boolean
        }
    }

    setConfig(config) {
        this._config = config;
    }

    hassChanged(hass) {

        const config = this._config;
        const stateObj = hass.states[config.entity];

        let speed;
        if (stateObj && stateObj.attributes) {
            speed = stateObj.attributes.speed || 'off';
        }
		
		let low;
		let med;
		let high;
		let offstate;
		
		if (stateObj && stateObj.attributes) {
		    if (stateObj.state == 'on' && stateObj.attributes.speed == 'low') {
			    low = 'on';
		    } else if (stateObj.state == 'on' && stateObj.attributes.speed == 'medium') {
			    med = 'on';
		    } else if (stateObj.state == 'on' && stateObj.attributes.speed == 'high') {
			    high = 'on';
		    } else {
				offstate = 'on';
			}
		}
		
        let lowcolor;
		let medcolor;
		let hicolor;
		let offcolor;
		
		if (low == 'on') {
			lowcolor = 'background-color: #43A047';
		} else {
			lowcolor = '';
		}
		
		if (med == 'on') {
			medcolor = 'background-color: #43A047';
		} else {
			medcolor = '';
		}
		
		if (high == 'on') {
			hicolor = 'background-color: #43A047';
		} else {
			hicolor = '';
		}
		
		if (offstate == 'on') {
			//offcolor = 'background-color: #43A047';
			offcolor = 'background-color: #f44c09';
		} else {
			offcolor = '';
		}
		
		this.setProperties({
            _stateObj: stateObj,
			_isOffState: stateObj.state == 'off',
            _isOnLow: low === 'on',
			_isOnMed: med === 'on',
			_isOnHigh: high === 'on',
			_lowOnColor: lowcolor,
			_medOnColor: medcolor,
			_highOnColor: hicolor,
			_offColor: offcolor
        });
    }

    stopPropagation(e) {
        e.stopPropagation();
    }

    setSpeed(e) {
        const speed = e.currentTarget.getAttribute('name');
        this.hass.callService('fan', 'set_speed', {
            entity_id: this._config.entity, speed: speed
        });
    }

}

customElements.define('custom-fan-card', CustomFanCard);