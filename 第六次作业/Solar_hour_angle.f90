module solar_hour

implicit none

contains

subroutine solar_hour_angle(d, lon, time_zone, lst, hour_angle)

implicit none

  integer, intent(in) :: d
  real(4), intent(in)  :: lon, time_zone, lst
  real(4), intent(out)  :: hour_angle

  real(4)  :: pi, gamma, eot, offset, corr_lst

  pi = 3.14159265359

  !https://solarsena.com/solar-hour-angle-calculator-formula/

  gamma = 2*pi / 365*(d-1+( lst-12 ) / 24)

  eot = 229.18*(0.000075+0.001868*cos(gamma)-0.032077*sin(gamma)-0.014615*cos(2*gamma)-0.040849*sin(2*gamma))

  ! the corrected LST is LST+Offset
  ! Offset = eot+4*(lon-15*time_zone)
  corr_lst = lst+(eot+4*(lon-15*time_zone)) / 60

  hour_angle = 15*(corr_lst-12)

  print*, 'hour angle: ', hour_angle

end subroutine solar_hour_angle

end module

