program Main
use procedures  
Implicit none
integer                            :: u, i, l
!real(4) :: n
real(4), allocatable :: M(:,:)
real(4), allocatable :: N(:,:)
real(4), allocatable :: RES(:,:)

u = 50

open(unit=u, file='fortran_demo1/M.dat', status='old')

! lines of file
l = 5

allocate( M(l,3))

do i = 1,l
  read(u, *) M(i,1), M(i,2), M(i,3)
enddo

! print*,M(1,1)
! lines of file N
l = 3
close(u)
open(unit=u, file='fortran_demo1/N.dat', status='old')

allocate(N(l,5))

do i = 1,l
  read(u, *) N(i,1), N(i,2), N(i,3), N(i,4),N(i,5)
enddo

close(u)
!problem 1.3
allocate(RES(5,5))
call matrix_multip(M,N,RES)

open(unit=u, file='MN.dat')

do i = 1,5
  write(u, '(f9.2,f9.2,f9.2,f9.2,f9.2)') RES(i,1), RES(i,2), RES(i,3), RES(i,4), RES(i,5)
enddo

deallocate(M,N,RES)
close(u)
end program Main
