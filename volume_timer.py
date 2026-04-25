import time
from pycaw.pycaw import AudioUtilities

# Get default speakers
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
# Display current audio info
# print(f"Audio output: {device.FriendlyName}")
# print(f"- Muted: {bool(volume.GetMute())}")
# print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
# print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
# Set master volume to -20 dB
specifiedVolume = 70
end_time = time.time() + 1 * 10

def handleVolume(number):
    volume.SetMasterVolumeLevelScalar(number / 100, None)
    print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")

handleVolume(specifiedVolume)

# while time.time() < end_time:
#     if round(volume.GetMasterVolumeLevelScalar() * 100) != specifiedVolume:
#         print("on remet le volume qu'on a spécifié de base")
#         handleVolume(specifiedVolume)

#     print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
#     time.sleep(1)