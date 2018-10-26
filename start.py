import tempfile

temp_location = tempfile.gettempdir()
hots_temp_path = "Heroes of the Storm\\TempWriteReplayP1\\replay.server.battlelobby"
rejoin_file_path = temp_location + "\\" + hots_temp_path

print(temp_location)
print("check")
print(rejoin_file_path)