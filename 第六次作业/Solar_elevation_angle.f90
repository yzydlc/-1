Program Solar_elevation_angle

use declination
use solar_hour
Implicit none

! lst is local solar time
integer  :: d
real(4) :: lat, lon, time_zone, lst, hour_angle, dt, SEA, pi

pi = 3.14159265
lat = 22.542883
lon = 114.062996
time_zone = 8
lst = 10.533
d = 364

call declination_angle(d, dt)

call solar_hour_angle(d, lon, time_zone, lst, hour_angle)

! calculate SEA

SEA = asin(sin(lat*pi/180)*sin(dt)+cos(lat*pi/180)*cos(dt)*cos(hour_angle*pi/180))*180/pi

print*, 'SEA: ', SEA

End Program Solar_elevation_angle
