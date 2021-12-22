module declination
  implicit none

contains
subroutine declination_angle(d,dt)

implicit none

 integer, intent(in) :: d
 real(4), intent(out) :: dt

real(4) :: pi

pi = 3.14159265359

dt = sin(-23.44*pi/180)*cos(pi/180*(360/365.24*(d+10)+360/pi*0.0167*sin(pi/180*360/365.24*(d-2))))
dt = asin(dt)

print *, 'Delta: ', dt * 180 / pi

end subroutine declination_angle
end module
