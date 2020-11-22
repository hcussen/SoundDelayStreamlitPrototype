import utils

SPEED_OF_SOUND = 343  # m/s
YARDS_PER_METER = 1.09361
SPEED_OF_SOUND_YARDS = SPEED_OF_SOUND * YARDS_PER_METER  # yds/s
SECONDS_PER_MIN = 60

# coordinate scheme: front sideline intersects 50 = (0, 0, 0)

# allow user to choose location of drums and hornline
drums_x = 0
drums_y = 0

horns_x = 0
horns_y = 0

# allow user to set height and distance of box
box_y = 0
box_z = 0  # from front sideline

# allow user to set tempo in beats/min
tempo = input("Please enter the tempo in bpm: ")

# calculate distance of drums & horns to box
drums_to_box = utils.distance_to_box(drums_x, drums_y, boxy, box_z)
horns_to_box = utils.distance_to_box(horns_x, horns_y, boxy, box_z)

# calculate difference in sound arrival
discrepancy_in_seconds = abs(
    drums_to_box - horns_to_box) / SPEED_OF_SOUND_YARDS

# calculate difference as a % of beat
seconds_per_beat = SECONDS_PER_MIN / tempo
discrepancy_percentage_of_beat = discrepancy_in_seconds / seconds_per_beat

# round that to nearest 1/2^n of a beat and display to user
print(discrepancy_percentage_of_beat)
