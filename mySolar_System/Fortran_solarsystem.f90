program solar_system
    real :: g, t, ti, T1
    real, dimension(0:8) :: ax, ay, x, y, m, vx, vy
    real, dimension(0:8,0:8) :: r

    open(11, file ='Sun.dat', status ='unknown')
    open(12, file ='Mercury.dat', status ='unknown')
    open(13, file ='venus.dat', status ='unknown')
    open(14, file ='Earth.dat', status ='unknown')
    open(15, file ='Mars.dat', status ='unknown')
    open(16, file ='Jupiter.dat', status ='unknown')
    open(17, file ='Saturn.dat', status ='unknown')
    open(18, file ='Uranus.dat', status ='unknown')
    open(19, file ='Neptune.dat', status ='unknown')

    ! Initial conditions
    y = 0
    vx = 0
    x(0) = 0
    x(1) = 4.7e10
    x(2) = -4.6e10
    x(3) = 1.471e11
    x(4) = -2.06e11
    x(5) = 7.41e11
    x(6) = -1.4e12
    x(7) = 2.5e12
    x(8) = -4.46e12

    vy(0) = 0
    vy(1) = 43870
    vy(2) = -54000
    vy(3) = 30290
    vy(4) = -26500
    vy(5) = 13720
    vy(6) = -10140
    vy(7) = 7130
    vy(8) = -5470

    m(0) = 1.9891e30
    m(1) = 3.285e23
    m(2) = 4.867e24
    m(3) = 5.972e24
    m(4) = 6.39e23
    m(5) = 1.898e27
    m(6) = 5.683e26
    m(7) = 8.681e25
    m(8) = 1.024e26

    g = 6.67e-11
    T1 = 60190*24*3600*15
    ti = 0
    t = 86400

    do while (ti <= T1)
        ax = 0
        ay = 0

        do i = 0, 8
            do j = 0, 8
                r(i, j) = sqrt((x(i) - x(j))**2 + (y(i) - y(j))**2)
            enddo
        enddo

        do i = 0, 8
            do j = 0, 8
                if (j .eq. i) then
                    ax(i) = ax(i)
                    ay(i) = ay(i)
                else
                    ax(i) = ax(i) + (-g * m(j) * (x(i) - x(j))) / r(i, j)**3
                    ay(i) = ay(i) + (-g * m(j) * (y(i) - y(j))) / r(i, j)**3
                endif
            enddo
        enddo

        do i = 0, 8
            vx(i) = vx(i) + ax(i) * t
            vy(i) = vy(i) + ay(i) * t
            x(i) = x(i) + vx(i) * t
            y(i) = y(i) + vy(i) * t
        enddo

        ti = ti + t

        do i = 0, 2
            write(11+i,*) x(i)/10e8*2.2, y(i)/10e8*2.2
        enddo

        do i = 3, 4
            write(11+i,*) x(i)/10e9*9, y(i)/10e9*9
        enddo

        do i = 5, 6
            write(11+5,*) (x(5)/10e9)*3.5, (y(5)/10e9)*3.5
            write(11+6,*) (x(6)/10e9)*2.64, (y(6)/10e9)*2.15
        enddo

        write(11+7,*) (x(7)/10e9)*2, (y(7)/10e9)*1.25
        write(11+8,*) (x(8)/10e9)*1.3, y(8)/(10e9)*0.83
    enddo

end program solar_system
