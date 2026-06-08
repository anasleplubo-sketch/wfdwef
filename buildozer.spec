[app]

# ---------------------------------------------------------
# MINOS SIGINT // UFO Scanner - Buildozer spec
# ---------------------------------------------------------

# (str) Title of your application
title = MINOS SIGINT

# (str) Package name (lowercase, no spaces)
package.name = minossigint

# (str) Package domain
package.domain = org.kruixart

# (str) Source code directory (where main.py lives)
source.dir = .

# (list) Extensions to include when packaging source
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,onnx

# Include YOLO model if placed locally in a models/ folder
source.include_patterns = models/*.onnx

# (str) Application version
version = 1.0.0

# ---------------------------------------------------------
# Requirements
# - kivy        : UI framework (Android-compatible)
# - opencv      : p4a recipe, compiles OpenCV with DNN for Android
# - numpy       : required by OpenCV and the app
# - python3     : base Python runtime
# ---------------------------------------------------------
requirements = python3,kivy==2.3.0,numpy,opencv

# (str) Application icon (optional - place icon.png in source dir)
# icon.filename = %(source.dir)s/data/icon.png

# ---------------------------------------------------------
# Android permissions
# CAMERA              : live camera feed (mandatory)
# READ/WRITE_EXTERNAL : access /storage/emulated/0/Python Projects/models/
# MANAGE_EXTERNAL     : full external storage access for model path
# ---------------------------------------------------------
android.permissions =
    android.permission.CAMERA,
    android.permission.READ_EXTERNAL_STORAGE,
    android.permission.WRITE_EXTERNAL_STORAGE,
    android.permission.MANAGE_EXTERNAL_STORAGE

# Declare camera hardware feature (required for CAMERA permission)
android.features = android.hardware.camera

# ---------------------------------------------------------
# Android API targets
# - api 33  : Android 13 (good modern target)
# - minapi 21: Android 5.0+ (broad device support)
# ---------------------------------------------------------
android.api = 33
android.minapi = 21

# (str) Android NDK version to use (25b is stable with p4a + OpenCV)
android.ndk = 25b

# (list) Target ABIs - arm64-v8a for modern phones, armeabi-v7a for older ones
android.archs = arm64-v8a, armeabi-v7a

# (str) Orientation
# The app has a portrait layout with button rows at the bottom
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (bool) Allow backup (can be False for a scanner app)
android.allow_backup = False

# (bool) Set to true to indicate that your app requires internet access.
# Not needed for local camera+CV processing.
# android.internet = False

# ---------------------------------------------------------
# p4a (python-for-android) options
# ---------------------------------------------------------

# Request the MANAGE_EXTERNAL_STORAGE dialog on first launch
# (Android 11+ needs this to access arbitrary paths)
android.meta_data = android.content.Intent.CATEGORY_LAUNCHER=True

# ---------------------------------------------------------
# Buildozer options
# ---------------------------------------------------------
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
