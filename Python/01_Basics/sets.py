# Frequencies detected across two different antenna channels (in MHz)
channel_A = {100, 200, 300, 400}
channel_B = {300, 400, 500, 600}

# Find unique frequencies common to BOTH channels (Intersection)
common_freqs = channel_A.intersection(channel_B)
print("Common Frequencies:", common_freqs)  # {300, 400}

# Combine all unique detected frequencies (Union)
all_freqs = channel_A.union(channel_B)
print("All Unique Frequencies:", all_freqs)  # {100, 200, 300, 400, 500, 600}