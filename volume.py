import dbus
bus = dbus.SessionBus()

remote_object = bus.get_object(
    "org.PulseAudio1",
    "/org/pulseaudio/server_lookup1"
)
print ("Introspection data:\n")
print (remote_object.Introspect())
