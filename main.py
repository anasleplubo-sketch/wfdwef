# MINOS SIGINT - Entrypoint for Buildozer APK build
# Buildozer requires a file named main.py as the Android entry point.
# This simply delegates to the actual application in UFOscanner.py.

from UFOscanner import MinosSigintUFOApp

if __name__ == "__main__":
    MinosSigintUFOApp().run()
