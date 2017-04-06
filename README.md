# Pulse Audio for Gnome desktop
Simple py script for changing volume on gnome using DBus

Tested only on arch linux
  - User ID depends on logged user

If your pulseaudio default.pa is not configured, use this command
   - pacmd load-module module-dbus-protocol
