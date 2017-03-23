import dbus
bus = dbus.SessionBus()
proxy = bus.get_object("org.PulseAudio1", "/org/pulseaudio/core1/sinkX")
interface = dbus.Interface(proxy, "org.PulseAudio.Core1.Device")
