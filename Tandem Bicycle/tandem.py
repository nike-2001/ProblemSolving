def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse = True)

    result = 0
    for i in range(len(blueShirtSpeeds)):
        if fastest == True:
            tandem_speed = max(redShirtSpeeds[i], blueShirtSpeeds[i])
            result += tandem_speed
        else:
            tandem_speed = max(redShirtSpeeds[i], blueShirtSpeeds[len(blueShirtSpeeds) - i - 1])
            result += tandem_speed

    return result
        
