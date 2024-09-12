from math import sin, cos, pi
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def main():
    initial_height = int(input('Start height, m: '))
    initial_velocity = int(input('Start velocity, m/s: '))
    initial_angle = int(input('Start angle, degrees: '))

    if initial_height < 0:
        raise Exception('Initial height cannot be negative')
    if initial_velocity < 0:
        raise Exception('Initial velocity cannot be negative')

    g = 9.81
    initial_angle_radians = initial_angle * pi / 180
    initial_vertical_velocity = initial_velocity * sin(initial_angle_radians)
    initial_horizontal_velocity = initial_velocity * cos(initial_angle_radians)

    # overall_time = 2 * (start_speed * sin(start_angle * pi / 180)) / g
    horizontal_coords = [0]
    vertical_coords = [initial_height]
    time = [0]
    vertical_velocity = [initial_vertical_velocity]

    t = 0.2
    while True:
        x = initial_horizontal_velocity * t
        y = initial_height + initial_vertical_velocity * t - (1 / 2) * g * t ** 2
        velocity_y = initial_vertical_velocity - g * t

        if y < 0:
            break

        horizontal_coords.append(x)
        vertical_coords.append(y)
        vertical_velocity.append(velocity_y)
        time.append(t)
            
        t += 0.2

    fig = plt.figure()
    gs = GridSpec(nrows=2, ncols=2, figure=fig)
    
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(time, vertical_coords, color='red')
    ax1.set_title("Trajectory")
    ax1.set_xlabel("time, s")
    ax1.set_ylabel("height, m")

    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(time, vertical_velocity)
    ax2.set_title("Dependence of vertical velocity on time")
    ax2.set_xlabel("time, s")
    ax2.set_ylabel("velocity, m/s")

    ax3 = fig.add_subplot(gs[1, 1])
    ax3.plot(time, horizontal_coords)
    ax3.set_title("Dependence of distance traveled on time")
    ax3.set_xlabel("time, s")
    ax3.set_ylabel("distance, m")
    
    plt.show()


if __name__ == '__main__':
    main()