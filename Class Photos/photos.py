def classPhotos(redShirtHeights, blueShirtHeights):

    redShirtHeights.sort()
    blueShirtHeights.sort()

    back_row = "RED" if redShirtHeights[-1] > blueShirtHeights[-1] else "BLUE"

    for i in range(len(redShirtHeights)):
        red_index = redShirtHeights[i]
        blue_index = blueShirtHeights[i]

        if back_row == "RED":
            if red_index <= blue_index:
                return False
        else:
            if blue_index <= red_index:
                return False

    return True
