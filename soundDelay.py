import utils
import streamlit as st

SPEED_OF_SOUND = 343  # m/s
YARDS_PER_METER = 1.09361
SPEED_OF_SOUND_YARDS = SPEED_OF_SOUND * YARDS_PER_METER  # yds/s
SECONDS_PER_MIN = 60

st.title('Sound Delay')

# coordinate scheme: front sideline intersects 50 = (0, 0, 0)

# col0, col1 = st.beta_columns(2)
# # allow user to set height and distance of box
# box_y, box_z = 0, 0
# with col0:

# with col1:


box_y = st.number_input("Box Height (yds)", min_value=0, value=0, step=1)
box_z = st.number_input(
    "Box Distance from front sideline (yds)", min_value=0, value=0, step=1)

# allow user to choose location of drums and hornline
st.write('### Drums Position')
drums_x = st.slider('Drums L/R Position', min_value=-50, max_value=50,
                    value=0, step=1)
drums_y = st.slider('Drums Front/Back Position', min_value=0, max_value=53,
                    value=0, step=1)
st.write('### Horns Position')
horns_x = st.slider('Horns L/R Position', min_value=-50, max_value=50,
                    value=0, step=1)
horns_y = st.slider('Horns Front/Back Position', min_value=0, max_value=53,
                    value=0, step=1)


# allow user to set tempo in beats/min
tempo = st.slider('Tempo (BPM)', min_value=0, max_value=300,
                  value=160, step=1)

# calculate distance of drums & horns to box
drums_to_box = utils.distance_to_box(drums_x, drums_y, box_y, box_z)
horns_to_box = utils.distance_to_box(horns_x, horns_y, box_y, box_z)

# calculate difference in sound arrival
discrepancy_in_seconds = abs(
    drums_to_box - horns_to_box) / SPEED_OF_SOUND_YARDS

# calculate difference as a % of beat
seconds_per_beat = SECONDS_PER_MIN / tempo
discrepancy_percentage_of_beat = discrepancy_in_seconds / seconds_per_beat

# round that to nearest 1/2^n of a beat and display to user
notes = {
    0.5: 'half',
    0.25: 'quarter',
    0.125: 'eighth',
    0.0625: 'sixteenth',
    0.03125: "thirty-second",
    0.015625: 'sixty-fourth'
}
note_keys = list(notes.keys())

# building the adjustment string
adjustment = ''
for i in range(len(note_keys) - 1):
    if discrepancy_percentage_of_beat > note_keys[0]:
        adjustment = "more than a half"
    elif discrepancy_percentage_of_beat <= note_keys[i] and discrepancy_percentage_of_beat > note_keys[i + 1]:
        adjustment = notes[note_keys[i]]
    elif discrepancy_percentage_of_beat < note_keys[-1]:
        adjustment = "less than a sixty-fourth"

ahead_or_behind = 'ahead' if drums_to_box < horns_to_box else 'behind'

# display info to user
st.write('### Discrepancy in seconds')
st.write(discrepancy_in_seconds)

st.write('### Discrepancy as a percentage of the beat')
st.write(discrepancy_percentage_of_beat)

st.write('### Adjustment needed')
st.write(f'{adjustment} note {ahead_or_behind}')
