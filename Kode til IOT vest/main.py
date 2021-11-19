# Importere library til at forbinde til adafruit.io
import umqtt_robust2
from machine import Pin
from led_ring import set_color
from time import sleep_ms, sleep, ticks_ms
import buzzer
import GPSfunk

lib = umqtt_robust2
tilt_sensor = Pin(33, Pin.IN)

# opret en ny feed kaldet map_gps indo på io.adafruit
mapFeed = bytes('{:s}/feeds/{:s}'.format(b'Jesper123', b'mapfeed/csv'), 'utf-8')
# opret en ny feed kaldet speed_gps indo på io.adafruit
speedFeed = bytes('{:s}/feeds/{:s}'.format(b'Jesper123', b'speedfeed/csv'), 'utf-8')
tiltsensor = bytes('{:s}/feeds/{:s}'.format(b'Jesper123', b'tiltsensor/csv'), 'utf-8')

previousTime = 0
interval = 7000
previousTime2 = 0
interval2 = 7000

while True:
    currentTime = ticks_ms()
    besked = lib.besked
    
    # haandtere fejl i forbindelsen og hvor ofte den skal forbinde igen
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        # Det er primært herinde at i skal tilfoeje kode
        if currentTime - previousTime2 > interval2:
            previousTime2 = currentTime
            lib.c.publish(topic=tiltsensor, msg=str(tilt_sensor.value()))
        
        if currentTime - previousTime > interval:
            previousTime = currentTime
            lib.c.publish(topic=mapFeed, msg=GPSfunk.main())
            speed = GPSfunk.main()
            speed = speed[:4]
            print("speed: ",speed)
            lib.c.publish(topic=speedFeed, msg=speed)
            
        if besked == "1 rød":
            print("modtaget")
            buzzer.set_buzzer()
            set_color(255, 0, 0)
            #lib.c.publish(topic=lib.mqtt_pub_feedname, msg="1 er nu rød")
            sleep(2)
            buzzer.clear_buzzer()
            sleep(3)
            set_color(0, 0, 0)
            lib.besked = ""
        if besked == "1 grøn":
            print("modtaget")
            buzzer.set_buzzer()
            set_color(0, 255, 0)
            #lib.c.publish(topic=lib.mqtt_pub_feedname, msg="1 er nu grøn")
            sleep(2)
            buzzer.clear_buzzer()
            sleep(3)
            set_color(0, 0, 0)
            lib.besked = ""    
        if besked == "1 blå":
            print("modtaget")
            buzzer.set_buzzer()
            set_color(0, 0, 255)
            #lib.c.publish(topic=lib.mqtt_pub_feedname, msg="1 er nu blå")
            sleep(2)
            buzzer.clear_buzzer()
            sleep(3)
            set_color(0, 0, 0)
            lib.besked = ""
        if besked == "1 lilla":
            print("modtaget")
            buzzer.set_buzzer()
            set_color(128,0,128)
            #lib.c.publish(topic=lib.mqtt_pub_feedname, msg="1 er nu lilla")
            sleep(2)
            buzzer.clear_buzzer()
            sleep(3)
            set_color(0, 0, 0)
            lib.besked = ""
        if besked == "1 gul":
            print("modtaget")
            buzzer.set_buzzer()
            set_color(255, 255, 0)
            #lib.c.publish(topic=lib.mqtt_pub_feedname, msg="1 er nu gul")
            sleep(2)
            buzzer.clear_buzzer()
            sleep(3)
            set_color(0, 0, 0)
            lib.besked = ""
            
        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    lib.c.check_msg() # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages
lib.c.disconnect()


