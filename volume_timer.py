from pycaw.pycaw import AudioUtilities
# Get default speakers
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
specifiedVolume = 30
# Display current audio info
# print(f"Audio output: {device.FriendlyName}")
# print(f"- Muted: {bool(volume.GetMute())}")
# print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
# print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
# Set master volume to -20 dB

def handleVolume(number):
    volume.SetMasterVolumeLevelScalar(number / 100, None)
    print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")

handleVolume(specifiedVolume)