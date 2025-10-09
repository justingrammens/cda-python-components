# SenseEmu_Chapter4_AllChallenges.py
from sense_emu import SenseHat
import time

sense = SenseHat()

# --- Configurable thresholds ---
HOT_WARN_C = 40.0
TEMP_COLOR_BREAK_C = 30.0

# Define "optimal" bands (tweak as you like)
OPT_TEMP_RANGE = (20.0, 26.0)     # °C
OPT_HUM_RANGE  = (40.0, 55.0)     # % RH
OPT_PRES_RANGE = (1000.0, 1020.0) # hPa

# Colors
RED   = [255, 0, 0]
BLUE  = [0, 0, 255]
GREEN = [0, 180, 0]
YELL  = [255, 255, 0]
CYAN  = [0, 255, 255]
BLK   = [0, 0, 0]
WHT   = [255, 255, 255]

def temp_text_color(temp_c: float):
    return RED if temp_c > TEMP_COLOR_BREAK_C else BLUE

def is_optimal(temp, hum, pres):
    t_ok = OPT_TEMP_RANGE[0] <= temp <= OPT_TEMP_RANGE[1]
    h_ok = OPT_HUM_RANGE[0]  <= hum  <= OPT_HUM_RANGE[1]
    p_ok = OPT_PRES_RANGE[0] <= pres <= OPT_PRES_RANGE[1]
    return t_ok and h_ok and p_ok

def show_too_hot_warning():
    sense.show_message("TOO HOT!", scroll_speed=0.07, text_colour=RED)

def draw_humidity_bar(humidity: float, color=[0,180,0], bg=[0,0,0], hold_secs=2.0):
    """
    Draw a horizontal bar graph for humidity on the 8x8 LED matrix.
    0% -> 0 rows lit; 100% -> all 8 rows lit.
    """
    # Clamp 0..100, map to 0..8 rows
    h = max(0.0, min(100.0, humidity))
    rows_lit = int(round(h / 12.5))  # 100/8 = 12.5 % per row

    pixels = []
    for y in range(8):
        # bottom rows fill first (y=7 is bottom when we render)
        lit = (7 - y) < rows_lit
        row_color = color if lit else bg
        # append EIGHT triplets, not flattened ints
        pixels.extend([row_color] * 8)

    # pixels now has length 64, each element is a [r,g,b] triplet
    sense.set_pixels(pixels)
    time.sleep(hold_secs)


def show_smiley(hold_secs=2.0):
    """
    Simple white smiley on black background.
    """
    X = WHT; O = BLK
    face = [
        O, O, X, X, X, X, O, O,
        O, X, O, O, O, O, X, O,
        X, O, X, O, O, X, O, X,  # eyes
        X, O, O, O, O, O, O, X,
        X, O, X, O, O, X, O, X,
        X, O, O, X, X, O, O, X,
        O, X, O, O, O, O, X, O,
        O, O, X, X, X, X, O, O,
    ]
    sense.set_pixels(face)
    time.sleep(hold_secs)

def main():
    try:
        while True:
            temp = round(sense.get_temperature(), 2)
            hum  = round(sense.get_humidity(), 2)
            pres = round(sense.get_pressure(), 2)

            print(f"Temp: {temp:.2f} C  Humidity: {hum:.2f}%  Pressure: {pres:.2f} hPa")

            # 1) Scroll T & H with temperature-based color
            msg = f"T:{temp:.1f}C H:{hum:.1f}%"
            sense.show_message(msg, scroll_speed=0.08, text_colour=temp_text_color(temp))

            # 2) TOO HOT warning
            if temp > HOT_WARN_C:
                show_too_hot_warning()

            # 3) Humidity bar graph
            draw_humidity_bar(hum, color=GREEN, bg=BLK, hold_secs=1.8)

            # 4) Smiley if optimal conditions
            if is_optimal(temp, hum, pres):
                show_smiley(hold_secs=1.5)

            time.sleep(0.8)

    except KeyboardInterrupt:
        pass
    finally:
        sense.clear()

if __name__ == "__main__":
    main()
