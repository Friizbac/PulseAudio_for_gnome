import dbus
user = str(input('Insert user(default 0): '))
srv_addr = 'unix:path=/run/user/' + user + '/pulse/dbus-socket'
bus=dbus.connection.Connection(srv_addr)
location = input('Insert sink name(default: sink0): ')
location = ('/org/pulseaudio/core1/' + location)
sink = ( dbus.Interface( bus.get_object(object_path=location),
          dbus_interface='org.freedesktop.DBus.Properties' ))

volume = int(input('Volume (0-65537): '))

sink.Set( 'org.PulseAudio.Core1.Device', 'Volume', [dbus.UInt32(volume)],
          dbus_interface='org.freedesktop.DBus.Properties' )
volume = str(volume)
print('\nSuccessfully changed to:' + volume)
