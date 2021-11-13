from matplotlib import pyplot as plt
import math
import numpy as np

def vec_size(v):
    v1, v2 = v
    return ((v2-v1)**2 + (v2-v1)**2) ** 0.5

class Star:
    n = 3
    star_lst = []
    MAX_V = 30
    # G = 6.67 * 10 ** (-11)
    G = 1
    def __init__(self, m: float, v: tuple, pos: tuple):
        self.mass = m
        self.velocity = v
        self.pos = pos
        self.xs = [pos[0]]
        self.ys = [pos[1]]
        # print0(self.pos)
        Star.star_lst.append(self)

    def distance(self, other):
        x1, y1 = self.pos
        x2, y2 = other.pos
        # print(self.pos, other.pos)
        # print(x1, y1)
        # print(x2, y2)
        return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    
    def net_force(self):
        force_vec = (0, 0)
        # print(Star.star_lst)
        for star in Star.star_lst:
            if self is star: continue
            x1, y1 = self.pos
            x2, y2 = star.pos
            force_num = Star.G * self.mass * star.mass / ((self.distance(star)) ** 2)
            f1, f2 = force_vec
            
            force_vec = (f1 + force_num * (x2 - x1)/self.distance(star), f2 + force_num * (y2 - y1)/self.distance(star))
        return force_vec

    def move(self, t = 0.001):
        sx, sy = self.pos
        vx, vy = self.velocity
        fx, fy = self.net_force()
        ax, ay = fx / self.mass, fy / self.mass
        self.pos = (sx + vx*t + 0.5 * ax * t**2, sy + vy*t + 0.5 * ay * t**2)
        self.velocity = (vx*t + ax * t, vy*t + ay * t)
        # print(vec_size(self.velocity), Star.MAX_V)
        # if vec_size(self.velocity) > Star.MAX_V: 
        #     self.velocity = (vx, vy)
        return self.pos
    
    def collide(self, star, r):
        if self.distance(star) < r:
            print(self.distance(star))
            v1_x, v1_y = self.velocity
            v2_x, v2_y = star.velocity
            m1, m2 = self.mass, star.mass
            self.velocity = (((m1-m2) * v1_x + 2*m2*v2_x) / (m1+m2), ((m1-m2) * v1_y + 2*m2*v2_y))
            star.velocity = (((m2-m1) * v2_x + 2*m1*v1_x) / (m1+m2), ((m2-m1) * v2_y + 2*m1*v1_y) / (m1+m2))


    def __repr__(self): return f'Star({self.pos})'


def move_star(stars, t):
    plt.ion()
    observation_max = 100
    for i in range(t):
        for star in stars:
            x, y = star.xs, star.ys
            new_pos = star.move()
            for other in stars:
                if other is star: continue
                # print(1)
                star.collide(other, 0.1)
            x.append(new_pos[0])
            y.append(new_pos[1])
            
            plt.plot(x[-1], y[-1], 'og', markersize=star.mass/1000)
            plt.plot(x, y, '-g', markersize=star.mass/10000)
        axis_x = 0
        axis_y = 0
        for star in stars: 
            axis_x += star.xs[-1]
            axis_y += star.ys[-1]
        axis_x /= len(stars)
        axis_y /= len(stars)
        # plt.axis([axis_x-observation_max, axis_x+observation_max, axis_y-observation_max,  axis_y+observation_max])
        plt.show()
            
            # draw_star(x[-1], y[-1])
        plt.pause(1) 


if __name__ == '__main__':
    s1 = Star(500, (1, 1), (0, 0))
    s2 = Star(600, (0, 0), (1, 0))
    # s3 = Star(200, (0, 0), (0, 1))
    # for i in range(10000):
    #     print(s1.pos)
    #     s1.move()
    move_star([s1, s2], 1000)


# def printPattern():
#     x=[]
#     y=[]
#     plt
#     def 