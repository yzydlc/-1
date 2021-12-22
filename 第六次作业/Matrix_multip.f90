module procedures
  implicit none

contains
subroutine matrix_multip(a, b, c)

implicit none

 real(4), dimension(:,:), intent(in) :: a, b
 real(4), dimension(:,:), intent(out) :: c

integer :: i, j, n, m,k
real(4) :: tmp

i = size(a(:,1))
j = size(a(1,:))

do n=1,i

  do m=1,i
    !print*,a(n,m)
    tmp = 0.0
    do k=1,j
     !  print *, n
      ! print *, k
       tmp = tmp + a(n,k) * b(k,n)
    enddo
    !print *, n,m
    !print *,tmp
    c(n,m) = tmp
  enddo

enddo

end subroutine matrix_multip
end module
