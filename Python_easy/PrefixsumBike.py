def largestAltitude(gain):
    max_altitude = 0
    altitude = 0
    for i in gain:
        altitude += i
        max_altitude = max(max_altitude, altitude)
    return max_altitude
print(largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))